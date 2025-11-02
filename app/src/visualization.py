"""
Visualization functions for the DataOps Platform Comparison Tool.
Creates interactive charts using Plotly.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import streamlit as st
from typing import Dict, List


def create_radar_chart(dimension_scores: pd.DataFrame, 
                      platform_colors: Dict[str, str],
                      title: str = "Srovnání platforem podle dimenzí") -> go.Figure:
    """
    Create an interactive radar chart showing platform scores across dimensions.
    
    Args:
        dimension_scores: DataFrame with dimensions as rows, platforms as columns
        platform_colors: Dictionary mapping platform names to colors
        title: Chart title
    
    Returns:
        Plotly Figure object
    """
    fig = go.Figure()
    
    # Get dimension names for the radar chart
    dimensions = dimension_scores.index.tolist()
    
    # Format dimension names for display
    formatted_dimensions = [dim.replace('_', ' ') for dim in dimensions]
    
    # Add a trace for each platform
    for platform in dimension_scores.columns:
        values = dimension_scores[platform].tolist()
        # Close the radar chart by appending the first value
        values_closed = values + [values[0]]
        dimensions_closed = formatted_dimensions + [formatted_dimensions[0]]
        
        fig.add_trace(go.Scatterpolar(
            r=values_closed,
            theta=dimensions_closed,
            fill='none',
            name=platform.replace('_', ' '),
            line=dict(color=platform_colors.get(platform, '#666666'), width=3),
            marker=dict(size=8, color=platform_colors.get(platform, '#666666'))
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5],
                tickmode='linear',
                tick0=0,
                dtick=1
            )
        ),
        showlegend=True,
        title=dict(
            text=title,
            x=0.5,
            xanchor='center',
            font=dict(size=20)
        ),
        height=600,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.15,
            xanchor="center",
            x=0.5
        )
    )
    
    return fig


def create_topsis_bar_chart(topsis_scores: pd.Series,
                            platform_colors: Dict[str, str],
                            title: str = "Finální TOPSIS skóre") -> go.Figure:
    """
    Create a horizontal bar chart showing final TOPSIS scores.
    
    Args:
        topsis_scores: Series with platform names as index and TOPSIS scores as values
        platform_colors: Dictionary mapping platform names to colors
        title: Chart title
    
    Returns:
        Plotly Figure object
    """
    # Sort by score (descending)
    sorted_scores = topsis_scores.sort_values(ascending=True)
    
    # Format platform names
    platforms = [p.replace('_', ' ') for p in sorted_scores.index]
    scores = sorted_scores.values
    
    # Get colors for each platform
    colors = [platform_colors.get(p, '#666666') for p in sorted_scores.index]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=platforms,
        x=scores,
        orientation='h',
        marker=dict(color=colors),
        text=[f'{score:.3f}' for score in scores],
        textposition='auto',
        textfont=dict(size=14, color='white'),
        hovertemplate='<b>%{y}</b><br>TOPSIS Score: %{x:.4f}<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(
            text=title,
            x=0.5,
            xanchor='center',
            font=dict(size=20)
        ),
        xaxis=dict(
            title='TOPSIS skóre',
            range=[0, 1],
            tickformat='.2f'
        ),
        yaxis=dict(
            title='',
            tickfont=dict(size=14)
        ),
        height=400,
        showlegend=False,
        margin=dict(l=150, r=50, t=80, b=50)
    )
    
    return fig


def create_weights_heatmap(weights_df: pd.DataFrame,
                          title: str = "Váhy metrik podle dimenzí") -> go.Figure:
    """
    Create a heatmap showing metric weights organized by dimension.
    
    Args:
        weights_df: DataFrame with dimensions as rows, metrics as columns
        title: Chart title
    
    Returns:
        Plotly Figure object
    """
    fig = px.imshow(
        weights_df,
        labels=dict(x="Metric", y="Dimension", color="Weight"),
        x=weights_df.columns,
        y=weights_df.index,
        color_continuous_scale='Blues',
        aspect='auto'
    )
    
    fig.update_layout(
        title=dict(
            text=title,
            x=0.5,
            xanchor='center',
            font=dict(size=20)
        ),
        height=500
    )
    
    return fig


def create_dimension_weights_pie(dimension_weights: Dict[str, float],
                                title: str = "Rozložení vah dimenzí") -> go.Figure:
    """
    Create a pie chart showing the distribution of dimension weights.
    
    Args:
        dimension_weights: Dictionary mapping dimension names to weights
        title: Chart title
    
    Returns:
        Plotly Figure object
    """
    # Format dimension names
    dimensions = [d.replace('_', ' ') for d in dimension_weights.keys()]
    weights = list(dimension_weights.values())
    
    fig = go.Figure(data=[go.Pie(
        labels=dimensions,
        values=weights,
        textinfo='label+percent',
        textposition='auto',
        hovertemplate='<b>%{label}</b><br>Weight: %{value:.3f}<br>Percentage: %{percent}<extra></extra>',
        marker=dict(line=dict(color='white', width=2))
    )])
    
    fig.update_layout(
        title=dict(
            text=title,
            x=0.5,
            xanchor='center',
            font=dict(size=20)
        ),
        height=500,
        showlegend=True
    )
    
    return fig


def create_detailed_scores_table(scores_df: pd.DataFrame,
                                 dimension_col: str = 'Dimension') -> pd.DataFrame:
    """
    Format platform scores for display as a styled table.
    
    Args:
        scores_df: Platform scores DataFrame
        dimension_col: Name of dimension column
    
    Returns:
        Formatted DataFrame
    """
    # Create a copy and format column names
    display_df = scores_df.copy()
    
    # Replace underscores with spaces in dimension and metric names
    if 'Dimension' in display_df.columns:
        display_df['Dimension'] = display_df['Dimension'].str.replace('_', ' ')
    if 'Metric' in display_df.columns:
        display_df['Metric'] = display_df['Metric'].str.replace('_', ' ')
    
    # Format platform column names
    for col in display_df.columns:
        if col not in ['Dimension', 'Metric', 'Metric_Type']:
            new_col = col.replace('_', ' ')
            display_df = display_df.rename(columns={col: new_col})
    
    # Remove Metric_Type column if it exists
    if 'Metric_Type' in display_df.columns:
        display_df = display_df.drop(columns=['Metric_Type'])
    
    return display_df


def create_comparison_scatter(topsis_results: Dict,
                             x_metric: str,
                             y_metric: str,
                             platform_colors: Dict[str, str]) -> go.Figure:
    """
    Create a scatter plot comparing two metrics across platforms.
    
    Args:
        topsis_results: Results from TOPSIS analysis
        x_metric: Metric name for x-axis
        y_metric: Metric name for y-axis
        platform_colors: Dictionary mapping platform names to colors
    
    Returns:
        Plotly Figure object
    """
    normalized_scores = topsis_results['normalized_scores']
    
    platforms = normalized_scores.columns.tolist()
    x_values = normalized_scores.loc[x_metric].values
    y_values = normalized_scores.loc[y_metric].values
    
    colors = [platform_colors.get(p, '#666666') for p in platforms]
    platform_names = [p.replace('_', ' ') for p in platforms]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=x_values,
        y=y_values,
        mode='markers+text',
        marker=dict(
            size=20,
            color=colors,
            line=dict(width=2, color='white')
        ),
        text=platform_names,
        textposition='top center',
        textfont=dict(size=12),
        hovertemplate='<b>%{text}</b><br>' +
                     f'{x_metric}: %{{x:.3f}}<br>' +
                     f'{y_metric}: %{{y:.3f}}<extra></extra>'
    ))
    
    fig.update_layout(
        title=f'{x_metric.replace("_", " ")} vs {y_metric.replace("_", " ")}',
        xaxis=dict(
            title=x_metric.replace('_', ' '),
            range=[0, 1]
        ),
        yaxis=dict(
            title=y_metric.replace('_', ' '),
            range=[0, 1]
        ),
        height=500,
        showlegend=False
    )
    
    return fig


def create_ranking_table(topsis_scores: pd.Series,
                        d_plus: pd.Series,
                        d_minus: pd.Series) -> pd.DataFrame:
    """
    Create a formatted ranking table with TOPSIS details.
    
    Args:
        topsis_scores: Final TOPSIS scores
        d_plus: Distances to positive ideal solution
        d_minus: Distances to negative ideal solution
    
    Returns:
        Formatted DataFrame with rankings
    """
    # Sort by TOPSIS score (descending)
    sorted_platforms = topsis_scores.sort_values(ascending=False).index
    
    ranking_data = {
        'Rank': range(1, len(sorted_platforms) + 1),
        'Platform': [p.replace('_', ' ') for p in sorted_platforms],
        'D+ (Distance to PIS)': [f'{d_plus[p]:.4f}' for p in sorted_platforms],
        'D- (Distance to NIS)': [f'{d_minus[p]:.4f}' for p in sorted_platforms],
        'TOPSIS Score': [f'{topsis_scores[p]:.4f}' for p in sorted_platforms]
    }
    
    return pd.DataFrame(ranking_data)


def style_dataframe(df: pd.DataFrame, 
                   highlight_cols: List[str] = None,
                   precision: int = 3) -> pd.DataFrame:
    """
    Apply styling to a DataFrame for better display in Streamlit.
    
    Args:
        df: DataFrame to style
        highlight_cols: Columns to highlight
        precision: Number of decimal places for numeric columns
    
    Returns:
        Styled DataFrame
    """
    # This function returns a regular DataFrame since Streamlit handles styling
    # We just ensure numeric formatting is consistent
    styled_df = df.copy()
    
    for col in styled_df.columns:
        if styled_df[col].dtype in ['float64', 'float32']:
            styled_df[col] = styled_df[col].round(precision)
    
    return styled_df

