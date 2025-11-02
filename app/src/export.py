"""
Export functionality for the DataOps Platform Comparison Tool.
Handles PDF and CSV report generation.
"""

import pandas as pd
import io
from datetime import datetime
from typing import Dict
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT


def export_to_csv(topsis_results: Dict,
                 dimension_scores: pd.DataFrame,
                 platform_scores: pd.DataFrame) -> str:
    """
    Export TOPSIS results to CSV format.
    
    Args:
        topsis_results: Dictionary containing TOPSIS analysis results
        dimension_scores: DataFrame with dimension-level scores
        platform_scores: DataFrame with detailed metric scores
    
    Returns:
        CSV string
    """
    # Extract relevant data
    topsis_scores = topsis_results['topsis_scores'].sort_values(ascending=False)
    d_plus = topsis_results['d_plus']
    d_minus = topsis_results['d_minus']
    
    # Create main results dataframe
    results_data = []
    for rank, platform in enumerate(topsis_scores.index, 1):
        row_data = {
            'Rank': rank,
            'Platform': platform.replace('_', ' ')
        }
        
        # Add dimension scores
        for dimension in dimension_scores.index:
            dim_name = dimension.replace('_', ' ')
            row_data[dim_name] = dimension_scores.loc[dimension, platform]
        
        # Add TOPSIS metrics
        row_data['D+ (Distance to PIS)'] = d_plus[platform]
        row_data['D- (Distance to NIS)'] = d_minus[platform]
        row_data['TOPSIS Score'] = topsis_scores[platform]
        
        results_data.append(row_data)
    
    results_df = pd.DataFrame(results_data)
    
    # Convert to CSV
    csv_buffer = io.StringIO()
    results_df.to_csv(csv_buffer, index=False, float_format='%.4f')
    
    return csv_buffer.getvalue()


def export_detailed_csv(topsis_results: Dict,
                       platform_scores: pd.DataFrame,
                       weights: Dict[str, float]) -> str:
    """
    Export detailed analysis including all metrics to CSV.
    
    Args:
        topsis_results: Dictionary containing TOPSIS analysis results
        platform_scores: DataFrame with all metric scores
        weights: Dictionary of metric weights
    
    Returns:
        CSV string
    """
    # Create detailed export with metrics
    export_df = platform_scores.copy()
    
    # Add weight column
    export_df['Weight'] = export_df['Metric'].map(weights)
    
    # Reorder columns
    cols = ['Dimension', 'Metric', 'Weight'] + [col for col in export_df.columns 
                                                  if col not in ['Dimension', 'Metric', 'Weight', 'Metric_Type']]
    export_df = export_df[cols]
    
    # Format names
    export_df['Dimension'] = export_df['Dimension'].str.replace('_', ' ')
    export_df['Metric'] = export_df['Metric'].str.replace('_', ' ')
    
    # Rename platform columns
    for col in export_df.columns:
        if '_' in col and col not in ['Dimension', 'Metric', 'Weight']:
            export_df = export_df.rename(columns={col: col.replace('_', ' ')})
    
    csv_buffer = io.StringIO()
    export_df.to_csv(csv_buffer, index=False, float_format='%.4f')
    
    return csv_buffer.getvalue()


def generate_pdf_report(topsis_results: Dict,
                       dimension_scores: pd.DataFrame,
                       platform_scores: pd.DataFrame,
                       weights: Dict[str, float],
                       dimension_weights: Dict[str, float],
                       mode: str = "average") -> bytes:
    """
    Generate a comprehensive PDF report of the analysis.
    
    Args:
        topsis_results: Dictionary containing TOPSIS analysis results
        dimension_scores: DataFrame with dimension-level scores
        platform_scores: DataFrame with detailed metric scores
        weights: Dictionary of hierarchical weights
        dimension_weights: Dictionary of dimension weights
        mode: Either "average" or "custom"
    
    Returns:
        PDF content as bytes
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                           rightMargin=0.75*inch, leftMargin=0.75*inch,
                           topMargin=1*inch, bottomMargin=0.75*inch)
    
    # Container for PDF elements
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#0066CC'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#0066CC'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    # Page 1: Cover Page
    elements.append(Spacer(1, 2*inch))
    elements.append(Paragraph("DataOps Platform Comparison Report", title_style))
    elements.append(Spacer(1, 0.3*inch))
    
    date_str = datetime.now().strftime("%B %d, %Y")
    elements.append(Paragraph(f"Generated: {date_str}", styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    mode_text = "Average Weights (from Thesis Research)" if mode == "average" else "Custom Weight Configuration"
    elements.append(Paragraph(f"Analysis Mode: {mode_text}", styles['Normal']))
    elements.append(PageBreak())
    
    # Page 2: Executive Summary
    elements.append(Paragraph("Executive Summary", heading_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Final Rankings
    topsis_scores = topsis_results['topsis_scores'].sort_values(ascending=False)
    ranking_text = "Final Platform Rankings (TOPSIS Method):"
    elements.append(Paragraph(ranking_text, styles['Heading3']))
    elements.append(Spacer(1, 0.1*inch))
    
    for rank, (platform, score) in enumerate(topsis_scores.items(), 1):
        platform_name = platform.replace('_', ' ')
        rank_text = f"{rank}. {platform_name}: {score:.4f}"
        elements.append(Paragraph(rank_text, styles['Normal']))
    
    elements.append(Spacer(1, 0.3*inch))
    
    # TOPSIS Results Table
    elements.append(Paragraph("Detailed TOPSIS Metrics", styles['Heading3']))
    elements.append(Spacer(1, 0.1*inch))
    
    d_plus = topsis_results['d_plus']
    d_minus = topsis_results['d_minus']
    
    table_data = [['Rank', 'Platform', 'D+', 'D-', 'TOPSIS Score']]
    for rank, platform in enumerate(topsis_scores.index, 1):
        table_data.append([
            str(rank),
            platform.replace('_', ' '),
            f"{d_plus[platform]:.4f}",
            f"{d_minus[platform]:.4f}",
            f"{topsis_scores[platform]:.4f}"
        ])
    
    table = Table(table_data, colWidths=[0.7*inch, 2*inch, 1*inch, 1*inch, 1.3*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0066CC')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
    ]))
    
    elements.append(table)
    elements.append(PageBreak())
    
    # Page 3: Dimension Analysis
    elements.append(Paragraph("Dimension-Level Analysis", heading_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Dimension scores table
    dim_table_data = [['Dimension'] + [p.replace('_', ' ') for p in dimension_scores.columns]]
    for dimension in dimension_scores.index:
        row = [dimension.replace('_', ' ')]
        for platform in dimension_scores.columns:
            row.append(f"{dimension_scores.loc[dimension, platform]:.2f}")
        dim_table_data.append(row)
    
    dim_table = Table(dim_table_data, colWidths=[2.5*inch, 1.5*inch, 1.5*inch, 1.5*inch])
    dim_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#107C10')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
    ]))
    
    elements.append(dim_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Dimension weights
    elements.append(Paragraph("Dimension Weights", styles['Heading3']))
    elements.append(Spacer(1, 0.1*inch))
    
    weight_table_data = [['Dimension', 'Weight', 'Percentage']]
    for dimension, weight in dimension_weights.items():
        weight_table_data.append([
            dimension.replace('_', ' '),
            f"{weight:.4f}",
            f"{weight*100:.1f}%"
        ])
    
    weight_table = Table(weight_table_data, colWidths=[3*inch, 1.5*inch, 1.5*inch])
    weight_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FF6B00')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    elements.append(weight_table)
    elements.append(PageBreak())
    
    # Page 4: Detailed Metric Breakdown
    elements.append(Paragraph("Detailed Metric Scores", heading_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Group metrics by dimension
    for dimension in platform_scores['Dimension'].unique():
        dim_metrics = platform_scores[platform_scores['Dimension'] == dimension]
        
        elements.append(Paragraph(dimension.replace('_', ' '), styles['Heading3']))
        elements.append(Spacer(1, 0.1*inch))
        
        # Create table for this dimension
        metric_table_data = [['Metric'] + [p.replace('_', ' ') for p in 
                                            [col for col in dim_metrics.columns 
                                             if col not in ['Dimension', 'Metric', 'Metric_Type']]]]
        
        for _, row in dim_metrics.iterrows():
            metric_row = [row['Metric'].replace('_', ' ')]
            for col in dim_metrics.columns:
                if col not in ['Dimension', 'Metric', 'Metric_Type']:
                    metric_row.append(str(row[col]))
            metric_table_data.append(metric_row)
        
        metric_table = Table(metric_table_data, colWidths=[2.5*inch, 1.5*inch, 1.5*inch, 1.5*inch])
        metric_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
        ]))
        
        elements.append(metric_table)
        elements.append(Spacer(1, 0.2*inch))
    
    elements.append(PageBreak())
    
    # Page 5: Methodology Reference
    elements.append(Paragraph("Methodology Reference", heading_style))
    elements.append(Spacer(1, 0.2*inch))
    
    methodology_text = """
    <b>TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)</b><br/><br/>
    
    TOPSIS is a multi-criteria decision analysis method that ranks alternatives based on their 
    geometric distance from the ideal solution. The method involves:<br/>
    <br/>
    1. <b>Normalization</b>: Converting all metrics to a comparable scale (0-1)<br/>
    2. <b>Weighting</b>: Applying hierarchical weights to reflect importance<br/>
    3. <b>Ideal Solutions</b>: Identifying the best (PIS) and worst (NIS) possible scores<br/>
    4. <b>Distance Calculation</b>: Computing Euclidean distances to PIS and NIS<br/>
    5. <b>Scoring</b>: Calculating relative closeness to the ideal solution<br/>
    <br/>
    The platform with the highest TOPSIS score (closest to 1.0) is considered the best 
    overall choice given the specified weights and evaluation criteria.<br/>
    <br/>
    <b>Data Sources:</b><br/>
    - Platform evaluations based on hands-on testing and documentation review<br/>
    - Weights derived from expert interviews and calibration exercises<br/>
    - Methodology validated through academic research<br/>
    <br/>
    <b>For more information:</b><br/>
    Full thesis available at: [GitHub Repository]<br/>
    Contact: [Author Information]<br/>
    """
    
    elements.append(Paragraph(methodology_text, styles['Normal']))
    
    # Build PDF
    doc.build(elements)
    
    buffer.seek(0)
    return buffer.getvalue()


def create_download_filename(prefix: str, extension: str) -> str:
    """
    Generate a timestamped filename for downloads.
    
    Args:
        prefix: Filename prefix (e.g., "topsis_results")
        extension: File extension (e.g., "csv", "pdf")
    
    Returns:
        Formatted filename with timestamp
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.{extension}"

