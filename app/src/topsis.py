"""
TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) Implementation
This module calculates multi-criteria decision analysis scores for DataOps platforms.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple


def normalize_metrics(df: pd.DataFrame, metric_types: Dict[str, str]) -> pd.DataFrame:
    """
    Normalize platform scores using min-max normalization.
    
    Args:
        df: DataFrame with platform scores (rows=metrics, columns=platforms)
        metric_types: Dictionary mapping metric names to 'benefit' or 'cost'
    
    Returns:
        Normalized DataFrame with values between 0 and 1
    """
    normalized_df = df.copy()
    
    for metric in df.index:
        values = df.loc[metric].values
        min_val = values.min()
        max_val = values.max()
        
        if max_val == min_val:
            # If all values are the same, set to 0.5
            normalized_df.loc[metric] = 0.5
        else:
            if metric_types.get(metric, 'benefit') == 'benefit':
                # For benefit metrics: higher is better
                normalized_df.loc[metric] = (values - min_val) / (max_val - min_val)
            else:
                # For cost metrics: lower is better (invert normalization)
                normalized_df.loc[metric] = (max_val - values) / (max_val - min_val)
    
    return normalized_df


def calculate_weighted_matrix(normalized_df: pd.DataFrame, weights: Dict[str, float]) -> pd.DataFrame:
    """
    Apply hierarchical weights to normalized scores.
    
    Args:
        normalized_df: Normalized platform scores
        weights: Dictionary mapping metric names to their final hierarchical weights
    
    Returns:
        Weighted normalized matrix
    """
    weighted_df = normalized_df.copy()
    
    for metric in weighted_df.index:
        weight = weights.get(metric, 0)
        weighted_df.loc[metric] = weighted_df.loc[metric] * weight
    
    return weighted_df


def find_ideal_solutions(weighted_df: pd.DataFrame) -> Tuple[pd.Series, pd.Series]:
    """
    Identify Positive Ideal Solution (PIS) and Negative Ideal Solution (NIS).
    
    Args:
        weighted_df: Weighted normalized matrix
    
    Returns:
        Tuple of (PIS, NIS) as pandas Series
    """
    # PIS: Maximum value for each metric across all platforms
    pis = weighted_df.max(axis=1)
    
    # NIS: Minimum value for each metric across all platforms
    nis = weighted_df.min(axis=1)
    
    return pis, nis


def calculate_distances(weighted_df: pd.DataFrame, pis: pd.Series, nis: pd.Series) -> Tuple[pd.Series, pd.Series]:
    """
    Calculate Euclidean distances from each platform to PIS and NIS.
    
    Args:
        weighted_df: Weighted normalized matrix
        pis: Positive Ideal Solution
        nis: Negative Ideal Solution
    
    Returns:
        Tuple of (distances_to_pis, distances_to_nis)
    """
    distances_to_pis = {}
    distances_to_nis = {}
    
    for platform in weighted_df.columns:
        # Calculate Euclidean distance to PIS
        d_plus = np.sqrt(np.sum((weighted_df[platform] - pis) ** 2))
        distances_to_pis[platform] = d_plus
        
        # Calculate Euclidean distance to NIS
        d_minus = np.sqrt(np.sum((weighted_df[platform] - nis) ** 2))
        distances_to_nis[platform] = d_minus
    
    return pd.Series(distances_to_pis), pd.Series(distances_to_nis)


def calculate_topsis_scores(d_plus: pd.Series, d_minus: pd.Series) -> pd.Series:
    """
    Calculate final TOPSIS scores (relative closeness to ideal solution).
    
    Args:
        d_plus: Distances to Positive Ideal Solution
        d_minus: Distances to Negative Ideal Solution
    
    Returns:
        TOPSIS scores (0 to 1, higher is better)
    """
    topsis_scores = d_minus / (d_plus + d_minus)
    return topsis_scores


def run_topsis_analysis(platform_scores: pd.DataFrame, 
                        weights: Dict[str, float],
                        metric_types: Dict[str, str]) -> Dict:
    """
    Execute complete TOPSIS analysis pipeline.
    
    Args:
        platform_scores: DataFrame with dimensions as rows, platforms as columns
        weights: Dictionary of hierarchical weights for each metric
        metric_types: Dictionary mapping metrics to 'benefit' or 'cost'
    
    Returns:
        Dictionary containing:
            - normalized_scores: Normalized platform scores
            - weighted_scores: Weighted normalized scores
            - pis: Positive Ideal Solution
            - nis: Negative Ideal Solution
            - d_plus: Distances to PIS
            - d_minus: Distances to NIS
            - topsis_scores: Final TOPSIS scores
            - ranking: Platforms ranked by TOPSIS score
    """
    # Step 1: Normalize metrics
    normalized = normalize_metrics(platform_scores, metric_types)
    
    # Step 2: Apply weights
    weighted = calculate_weighted_matrix(normalized, weights)
    
    # Step 3: Find ideal solutions
    pis, nis = find_ideal_solutions(weighted)
    
    # Step 4: Calculate distances
    d_plus, d_minus = calculate_distances(weighted, pis, nis)
    
    # Step 5: Calculate TOPSIS scores
    topsis_scores = calculate_topsis_scores(d_plus, d_minus)
    
    # Step 6: Rank platforms
    ranking = topsis_scores.sort_values(ascending=False)
    
    return {
        'normalized_scores': normalized,
        'weighted_scores': weighted,
        'pis': pis,
        'nis': nis,
        'd_plus': d_plus,
        'd_minus': d_minus,
        'topsis_scores': topsis_scores,
        'ranking': ranking
    }


def calculate_dimension_scores(platform_scores_df: pd.DataFrame,
                               dimension_col: str = 'Dimension') -> pd.DataFrame:
    """
    Calculate aggregated scores for each dimension by averaging metric scores.
    
    Args:
        platform_scores_df: DataFrame with Dimension, Metric, and platform columns
        dimension_col: Name of the dimension column
    
    Returns:
        DataFrame with dimensions as rows and platforms as columns
    """
    # Get platform columns (exclude Dimension, Metric, Metric_Type)
    platform_cols = [col for col in platform_scores_df.columns 
                    if col not in [dimension_col, 'Metric', 'Metric_Type']]
    
    # Group by dimension and calculate mean for each platform
    dimension_scores = platform_scores_df.groupby(dimension_col)[platform_cols].mean()
    
    return dimension_scores


def calculate_hierarchical_weights(dimension_weights: Dict[str, float],
                                   metric_weights: Dict[str, Dict[str, float]]) -> Dict[str, float]:
    """
    Calculate final hierarchical weights by multiplying dimension and metric weights.
    
    Args:
        dimension_weights: Dictionary of dimension weights (must sum to 1.0)
        metric_weights: Dictionary of dictionaries - dimension -> metric -> weight
                       (metric weights within each dimension must sum to 1.0)
    
    Returns:
        Dictionary mapping each metric to its final hierarchical weight
    """
    hierarchical_weights = {}
    
    for dimension, dim_weight in dimension_weights.items():
        if dimension in metric_weights:
            for metric, metric_weight in metric_weights[dimension].items():
                # Final weight = dimension weight × metric weight
                hierarchical_weights[metric] = dim_weight * metric_weight
    
    return hierarchical_weights


def normalize_weights(weights: Dict[str, float]) -> Dict[str, float]:
    """
    Normalize weights to sum to 1.0.
    
    Args:
        weights: Dictionary of weights
    
    Returns:
        Normalized weights dictionary
    """
    total = sum(weights.values())
    if total == 0:
        return weights
    return {k: v / total for k, v in weights.items()}


def validate_weights(weights: Dict[str, float], tolerance: float = 0.01) -> bool:
    """
    Validate that weights sum to approximately 1.0.
    
    Args:
        weights: Dictionary of weights
        tolerance: Acceptable deviation from 1.0
    
    Returns:
        True if weights are valid, False otherwise
    """
    total = sum(weights.values())
    return abs(total - 1.0) < tolerance

