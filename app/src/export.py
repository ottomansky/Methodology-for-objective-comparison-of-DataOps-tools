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
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, KeepTogether
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
        fontSize=28,
        textColor=colors.HexColor('#0066CC'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#333333'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor('#0066CC'),
        spaceAfter=14,
        spaceBefore=18,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubheading',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=colors.HexColor('#333333'),
        spaceAfter=10,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#333333'),
        spaceAfter=8,
        leading=14,
        fontName='Helvetica'
    )
    
    link_style = ParagraphStyle(
        'LinkStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#0066CC'),
        spaceAfter=8,
        fontName='Helvetica',
        underline=True
    )
    
    # Page 1: Cover Page
    elements.append(Spacer(1, 1.8*inch))
    elements.append(Paragraph("DataOps Platform Comparison Report", title_style))
    elements.append(Spacer(1, 0.5*inch))
    
    # Subtitle
    subtitle_text = "Multi-Criteria Decision Analysis using TOPSIS Methodology"
    elements.append(Paragraph(subtitle_text, subtitle_style))
    elements.append(Spacer(1, 0.4*inch))
    
    # Analysis details
    date_str = datetime.now().strftime("%B %d, %Y")
    elements.append(Paragraph(f"<b>Generated:</b> {date_str}", body_style))
    elements.append(Spacer(1, 0.15*inch))
    
    mode_text = "Average Weights (from Thesis Research)" if mode == "average" else "Custom Weight Configuration"
    elements.append(Paragraph(f"<b>Analysis Mode:</b> {mode_text}", body_style))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("<b>Evaluated Platforms:</b> Keboola, Microsoft Fabric, Databricks", body_style))
    elements.append(Spacer(1, 1*inch))
    
    # Footer with thesis link
    thesis_info = """
    <para alignment="center">
    <b>Based on Research Methodology:</b><br/>
    <link href="https://github.com/ottomansky/Methodology-for-objective-comparison-of-DataOps-tools" color="blue">
    Methodology for Objective Comparison of DataOps Tools
    </link><br/>
    <font color="#666666" size="9">https://github.com/ottomansky/Methodology-for-objective-comparison-of-DataOps-tools</font>
    </para>
    """
    elements.append(Paragraph(thesis_info, body_style))
    
    elements.append(PageBreak())
    
    # Page 2: Executive Summary
    elements.append(Paragraph("Executive Summary", heading_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # Summary description
    summary_intro = """
    This report presents a comprehensive evaluation of three leading DataOps platforms using the TOPSIS 
    (Technique for Order of Preference by Similarity to Ideal Solution) methodology. The analysis evaluates 
    platforms across five key dimensions with 20 specific metrics, providing an objective, data-driven 
    comparison to support platform selection decisions.
    """
    elements.append(Paragraph(summary_intro, body_style))
    elements.append(Spacer(1, 0.25*inch))
    
    # Final Rankings
    topsis_scores = topsis_results['topsis_scores'].sort_values(ascending=False)
    ranking_text = "<b>Final Platform Rankings</b>"
    elements.append(Paragraph(ranking_text, subheading_style))
    elements.append(Spacer(1, 0.1*inch))
    
    for rank, (platform, score) in enumerate(topsis_scores.items(), 1):
        platform_name = platform.replace('_', ' ')
        rank_text = f"<b>{rank}. {platform_name}</b> — TOPSIS Score: {score:.4f}"
        elements.append(Paragraph(rank_text, body_style))
    
    elements.append(Spacer(1, 0.3*inch))
    
    # TOPSIS Results Table - Keep together with title
    topsis_table_elements = []
    topsis_table_elements.append(Paragraph("<b>Detailed TOPSIS Metrics</b>", subheading_style))
    topsis_table_elements.append(Spacer(1, 0.1*inch))
    
    # Explanation of metrics
    metrics_explanation = """
    <b>D+</b> represents the distance to the Positive Ideal Solution (lower is better), 
    <b>D-</b> represents the distance to the Negative Ideal Solution (higher is better). 
    The TOPSIS score is calculated as D-/(D+ + D-), where scores closer to 1.0 indicate better overall performance.
    """
    topsis_table_elements.append(Paragraph(metrics_explanation, body_style))
    topsis_table_elements.append(Spacer(1, 0.15*inch))
    
    d_plus = topsis_results['d_plus']
    d_minus = topsis_results['d_minus']
    
    table_data = [['Rank', 'Platform', 'D+ (to PIS)', 'D- (to NIS)', 'TOPSIS Score']]
    for rank, platform in enumerate(topsis_scores.index, 1):
        table_data.append([
            str(rank),
            platform.replace('_', ' '),
            f"{d_plus[platform]:.4f}",
            f"{d_minus[platform]:.4f}",
            f"{topsis_scores[platform]:.4f}"
        ])
    
    table = Table(table_data, colWidths=[0.7*inch, 2*inch, 1.2*inch, 1.2*inch, 1.3*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0066CC')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F5F5F5')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CCCCCC')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))
    
    topsis_table_elements.append(table)
    elements.append(KeepTogether(topsis_table_elements))
    elements.append(PageBreak())
    
    # Page 3: Dimension Analysis
    elements.append(Paragraph("Dimension-Level Analysis", heading_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # Dimension intro
    dim_intro = """
    The following table presents average scores for each platform across the five evaluation dimensions. 
    Scores range from 0-5, where higher values indicate better performance in that dimension.
    """
    elements.append(Paragraph(dim_intro, body_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Dimension scores table - Keep together
    dim_table_elements = []
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
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CCCCCC')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))
    
    dim_table_elements.append(dim_table)
    elements.append(KeepTogether(dim_table_elements))
    elements.append(Spacer(1, 0.3*inch))
    
    # Dimension weights - Keep together with title
    weight_table_elements = []
    weight_table_elements.append(Paragraph("<b>Dimension Weights</b>", subheading_style))
    weight_table_elements.append(Spacer(1, 0.1*inch))
    
    weights_intro = """
    The following weights represent the relative importance assigned to each dimension in the final analysis. 
    These hierarchical weights are combined with individual metric weights to calculate the final TOPSIS scores.
    """
    weight_table_elements.append(Paragraph(weights_intro, body_style))
    weight_table_elements.append(Spacer(1, 0.15*inch))
    
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
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#FFF0E5')]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CCCCCC')),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))
    
    weight_table_elements.append(weight_table)
    elements.append(KeepTogether(weight_table_elements))
    elements.append(PageBreak())
    
    # Page 4: Detailed Metric Breakdown
    elements.append(Paragraph("Detailed Metric Scores", heading_style))
    elements.append(Spacer(1, 0.15*inch))
    
    metrics_intro = """
    This section provides a detailed breakdown of individual metric scores for each platform, organized by dimension. 
    Scores reflect platform capabilities assessed through documentation review, hands-on testing, and expert evaluation.
    """
    elements.append(Paragraph(metrics_intro, body_style))
    elements.append(Spacer(1, 0.25*inch))
    
    # Group metrics by dimension - Keep each table with its title
    for dimension in platform_scores['Dimension'].unique():
        dim_metrics = platform_scores[platform_scores['Dimension'] == dimension]
        
        # Create elements for this dimension table
        dimension_table_elements = []
        dimension_table_elements.append(Paragraph(f"<b>{dimension.replace('_', ' ')}</b>", subheading_style))
        dimension_table_elements.append(Spacer(1, 0.1*inch))
        
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
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#666666')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('TOPPADDING', (0, 0), (-1, 0), 8),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F9F9F9')]),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CCCCCC')),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('TOPPADDING', (0, 1), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ]))
        
        dimension_table_elements.append(metric_table)
        
        # Add the table with its title as a single unit
        elements.append(KeepTogether(dimension_table_elements))
        elements.append(Spacer(1, 0.2*inch))
    
    elements.append(PageBreak())
    
    # Page 5: Methodology Reference
    elements.append(Paragraph("Methodology Reference", heading_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # TOPSIS Overview
    elements.append(Paragraph("<b>TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)</b>", subheading_style))
    elements.append(Spacer(1, 0.1*inch))
    
    topsis_overview = """
    TOPSIS is a multi-criteria decision analysis (MCDA) method that ranks alternatives based on their 
    geometric distance from the ideal solution. This methodology provides an objective, quantitative approach 
    to complex decision-making scenarios where multiple conflicting criteria must be considered simultaneously.
    """
    elements.append(Paragraph(topsis_overview, body_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Methodology Steps
    elements.append(Paragraph("<b>Analysis Process</b>", subheading_style))
    elements.append(Spacer(1, 0.1*inch))
    
    methodology_steps = """
    The TOPSIS methodology follows a structured five-step process:<br/>
    <br/>
    <b>1. Normalization:</b> All metrics are converted to a comparable scale (0-1) using vector normalization, 
    ensuring that differences in measurement units and scales do not bias the analysis.<br/>
    <br/>
    <b>2. Weighting:</b> Hierarchical weights are applied to reflect the relative importance of each metric 
    and dimension. Weights can be derived from expert interviews, analytical hierarchy process (AHP), or custom priorities.<br/>
    <br/>
    <b>3. Ideal Solutions:</b> The Positive Ideal Solution (PIS) and Negative Ideal Solution (NIS) are identified, 
    representing the best and worst possible performance across all metrics.<br/>
    <br/>
    <b>4. Distance Calculation:</b> Euclidean distances from each platform to both the PIS (D+) and NIS (D-) 
    are computed, quantifying how close each alternative is to optimal and worst-case scenarios.<br/>
    <br/>
    <b>5. Relative Closeness Scoring:</b> The final TOPSIS score is calculated as D-/(D+ + D-), where scores 
    closer to 1.0 indicate better overall performance. The platform with the highest score represents the optimal choice.<br/>
    """
    elements.append(Paragraph(methodology_steps, body_style))
    elements.append(Spacer(1, 0.25*inch))
    
    # Data Sources
    elements.append(Paragraph("<b>Data Sources and Validation</b>", subheading_style))
    elements.append(Spacer(1, 0.1*inch))
    
    data_sources = """
    <b>Platform Evaluations:</b> Scores are based on comprehensive hands-on testing, official documentation review, 
    vendor specifications, and feature analysis conducted across all three platforms.<br/>
    <br/>
    <b>Weight Derivation:</b> Weights were derived from structured expert interviews with DataOps practitioners, 
    data engineers, and platform architects, ensuring the priorities reflect real-world organizational needs.<br/>
    <br/>
    <b>Methodology Validation:</b> The approach has been validated through academic research and peer review, 
    ensuring methodological rigor and reproducibility of results.<br/>
    """
    elements.append(Paragraph(data_sources, body_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # Thesis Reference with clickable link
    elements.append(Paragraph("<b>Research Thesis</b>", subheading_style))
    elements.append(Spacer(1, 0.1*inch))
    
    thesis_reference = """
    This analysis is based on comprehensive research methodology documented in the thesis:<br/>
    <br/>
    <b>"Methodology for Objective Comparison of DataOps Tools"</b><br/>
    <br/>
    <link href="https://github.com/ottomansky/Methodology-for-objective-comparison-of-DataOps-tools" color="blue">
    <u>https://github.com/ottomansky/Methodology-for-objective-comparison-of-DataOps-tools</u>
    </link><br/>
    <br/>
    The thesis provides detailed documentation of the evaluation framework, metric definitions, 
    scoring methodology, weight calibration process, and validation procedures. The complete research 
    materials, including raw data, interview transcripts, and analysis scripts, are available in the repository.
    """
    elements.append(Paragraph(thesis_reference, body_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # Disclaimer
    disclaimer = """
    <i><font color="#666666">
    <b>Disclaimer:</b> This report provides an analytical framework for platform comparison based on defined criteria 
    and weights. Final platform selection should consider organization-specific requirements, existing infrastructure, 
    budget constraints, and strategic objectives. Platform capabilities are subject to change as vendors release updates 
    and new features.
    </font></i>
    """
    elements.append(Paragraph(disclaimer, body_style))
    
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

