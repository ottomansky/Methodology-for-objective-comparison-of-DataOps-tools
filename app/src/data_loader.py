"""
Data loading utilities for the DataOps Platform Comparison Tool.
Handles loading and caching of platform scores, weights, and metric definitions.
"""

import pandas as pd
import json
import streamlit as st
from pathlib import Path
from typing import Dict, Tuple


# Get the base directory (DataApp folder)
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"


@st.cache_data
def load_platform_scores() -> Tuple[pd.DataFrame, Dict[str, str]]:
    """
    Load platform evaluation scores from CSV file.
    
    Returns:
        Tuple of (DataFrame, metric_types_dict)
        - DataFrame: Contains Dimension, Metric, and platform scores
        - Dict: Maps metric names to 'benefit' or 'cost'
    """
    file_path = DATA_DIR / "platform_scores.csv"
    df = pd.read_csv(file_path)
    
    # Create metric types dictionary
    metric_types = dict(zip(df['Metric'], df['Metric_Type']))
    
    return df, metric_types


@st.cache_data
def load_default_weights() -> Tuple[Dict[str, float], Dict[str, Dict[str, float]], Dict[str, float]]:
    """
    Load pre-calculated average weights from the thesis research.
    
    Returns:
        Tuple of (dimension_weights, metric_weights, hierarchical_weights)
        - dimension_weights: Dict mapping dimension names to normalized weights
        - metric_weights: Nested dict - dimension -> metric -> normalized weight
        - hierarchical_weights: Dict mapping metric names to final hierarchical weights
    """
    file_path = DATA_DIR / "weights.csv"
    df = pd.read_csv(file_path)
    
    # Extract dimension weights
    dimension_df = df[df['Level'] == 'dimension']
    dimension_weights = dict(zip(dimension_df['Item'], dimension_df['Normalized_Weight']))
    
    # Extract metric weights (organized by dimension)
    metric_df = df[df['Level'] == 'metric']
    metric_weights = {}
    
    for _, row in metric_df.iterrows():
        dimension = row['Category']
        metric = row['Item']
        weight = row['Normalized_Weight']
        
        if dimension not in metric_weights:
            metric_weights[dimension] = {}
        metric_weights[dimension][metric] = weight
    
    # Calculate hierarchical weights (dimension weight × metric weight)
    hierarchical_weights = {}
    for dimension, dim_weight in dimension_weights.items():
        if dimension in metric_weights:
            for metric, metric_weight in metric_weights[dimension].items():
                hierarchical_weights[metric] = dim_weight * metric_weight
    
    return dimension_weights, metric_weights, hierarchical_weights


@st.cache_data
def load_metric_definitions() -> Dict:
    """
    Load metric definitions including names, descriptions, and importance.
    
    Returns:
        Dictionary organized by dimension -> metric -> details
    """
    file_path = DATA_DIR / "metrics.json"
    with open(file_path, 'r', encoding='utf-8') as f:
        definitions = json.load(f)
    
    return definitions


def get_platform_columns(df: pd.DataFrame) -> list:
    """
    Extract platform column names from the scores DataFrame.
    
    Args:
        df: Platform scores DataFrame
    
    Returns:
        List of platform column names
    """
    # Exclude metadata columns
    metadata_cols = ['Dimension', 'Metric', 'Metric_Type']
    return [col for col in df.columns if col not in metadata_cols]


def prepare_topsis_input(scores_df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert the scores DataFrame to the format needed for TOPSIS calculation.
    
    Args:
        scores_df: DataFrame with Dimension, Metric, and platform columns
    
    Returns:
        DataFrame with metrics as rows and platforms as columns
    """
    platform_cols = get_platform_columns(scores_df)
    
    # Create a new DataFrame with Metric as index
    topsis_df = scores_df.set_index('Metric')[platform_cols].copy()
    
    return topsis_df


def get_dimension_mapping(scores_df: pd.DataFrame) -> Dict[str, str]:
    """
    Create a mapping from metric names to their dimensions.
    
    Args:
        scores_df: Platform scores DataFrame
    
    Returns:
        Dictionary mapping metric names to dimension names
    """
    return dict(zip(scores_df['Metric'], scores_df['Dimension']))


def format_platform_name(platform_name: str) -> str:
    """
    Format platform names for display (convert underscores to spaces).
    
    Args:
        platform_name: Raw platform name from data
    
    Returns:
        Formatted platform name
    """
    return platform_name.replace('_', ' ')


def get_dimension_order() -> list:
    """
    Return the standard order of dimensions for consistent display.
    
    Returns:
        List of dimension names in standard order
    """
    return [
        'Technical_Efficiency',
        'Data_Quality',
        'CI_CD',
        'User_Experience',
        'Business_Impact'
    ]


def get_platform_colors() -> Dict[str, str]:
    """
    Return the standard color scheme for platforms.
    
    Returns:
        Dictionary mapping platform names to hex color codes
    """
    return {
        'Keboola': '#228DFF',
        'Microsoft_Fabric': '#7AD5B1',
        'Databricks': '#FF3D2A'
    }


def validate_data_files() -> Dict[str, bool]:
    """
    Validate that all required data files exist and are readable.
    
    Returns:
        Dictionary mapping file names to existence status
    """
    required_files = {
        'platform_scores.csv': DATA_DIR / "platform_scores.csv",
        'default_weights.csv': DATA_DIR / "default_weights.csv",
        'metric_definitions.json': DATA_DIR / "metric_definitions.json"
    }
    
    status = {}
    for name, path in required_files.items():
        status[name] = path.exists() and path.is_file()
    
    return status


def get_summary_statistics(scores_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate summary statistics for platform scores.
    
    Args:
        scores_df: Platform scores DataFrame
    
    Returns:
        DataFrame with summary statistics
    """
    platform_cols = get_platform_columns(scores_df)
    
    stats = pd.DataFrame({
        'Platform': platform_cols,
        'Mean': [scores_df[col].mean() for col in platform_cols],
        'Std': [scores_df[col].std() for col in platform_cols],
        'Min': [scores_df[col].min() for col in platform_cols],
        'Max': [scores_df[col].max() for col in platform_cols]
    })
    
    return stats

