"""
Srovnání DataOps platforem - Diplomová práce
Implementace metodiky TOPSIS pro hodnocení platforem.
"""

import streamlit as st
import pandas as pd
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'src'))

from data_loader import (
    load_platform_scores, load_default_weights, load_metric_definitions,
    prepare_topsis_input, get_dimension_order, get_platform_colors
)
from topsis import (
    run_topsis_analysis, calculate_dimension_scores, 
    calculate_hierarchical_weights, normalize_weights
)
from visualization import (
    create_radar_chart, create_topsis_bar_chart, 
    create_dimension_weights_pie, create_ranking_table
)
from export import (
    export_to_csv, export_detailed_csv, 
    generate_pdf_report, create_download_filename
)


st.set_page_config(
    page_title="Srovnání DataOps platforem",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .main { padding-top: 2rem; }
    .stTabs [data-baseweb="tab-list"] { gap: 2rem; }
    .stTabs [data-baseweb="tab"] { padding: 0.5rem 1rem; }
    h1 { margin-bottom: 0.5rem; }
    h2 { margin-top: 2rem; margin-bottom: 1rem; }
    h3 { margin-top: 1.5rem; margin-bottom: 0.5rem; }
    
    
    /* Card Styles */
    .card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    .card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border-color: #0066cc;
    }
    .card-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
    }
    .card-description {
        font-size: 0.9rem;
        color: #666;
        line-height: 1.5;
    }
    
    /* Result Cards */
    .result-card {
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        height: 100%;
    }
    .result-rank {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        opacity: 0.95;
    }
    .result-platform {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .result-score {
        font-size: 2.5rem;
        font-weight: 700;
        margin-top: 1rem;
    }
    .result-label {
        font-size: 0.9rem;
        opacity: 0.85;
        margin-bottom: 0.3rem;
    }
    
    /* Points Counter */
    .points-counter {
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    .points-counter.valid {
        border-color: #28a745;
        background: #f0fff4;
    }
    .points-counter.over {
        border-color: #dc3545;
        background: #fff5f5;
    }
    .points-counter.under {
        border-color: #ffc107;
        background: #fffbf0;
    }
    .points-number {
        font-size: 3rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    .points-number.valid { color: #28a745; }
    .points-number.over { color: #dc3545; }
    .points-number.under { color: #ffc107; }
    .points-label {
        font-size: 0.9rem;
        color: #666;
        margin-bottom: 0.5rem;
    }
    .points-message {
        font-size: 1rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    
    /* Weight Table */
    .weight-table {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .weight-row {
        display: flex;
        justify-content: space-between;
        padding: 0.5rem 0;
        border-bottom: 1px solid #f0f0f0;
    }
    .weight-row:last-child {
        border-bottom: none;
    }
    .weight-name {
        font-weight: 500;
    }
    .weight-value {
        color: #0066cc;
        font-weight: 600;
    }
    .metric-weight {
        padding-left: 1.5rem;
        font-size: 0.9rem;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)


def init_session():
    if 'mode' not in st.session_state:
        st.session_state.mode = None
    if 'metric_weights' not in st.session_state:
        st.session_state.metric_weights = {}
    if 'dim_weights' not in st.session_state:
        st.session_state.dim_weights = {}
    if 'results' not in st.session_state:
        st.session_state.results = None


def reset_session():
    st.session_state.mode = None
    st.session_state.metric_weights = {}
    st.session_state.dim_weights = {}
    st.session_state.results = None


def show_landing():
    st.title("Srovnání DataOps platforem")
    st.caption("Metodika TOPSIS pro hodnocení Keboola, Microsoft Fabric a Databricks")
    
    st.markdown("##")
    
    col1, col2, col3 = st.columns([1, 8, 1])
    
    with col2:
        st.markdown("### Vyberte režim hodnocení")
        st.markdown("")
        
        # Mode cards
        col_left, col_right = st.columns(2)
        
        with col_left:
            st.markdown("""
            <div class="card">
                <div class="card-title">Průměrné váhy z výzkumu</div>
                <div class="card-description">
                    Použití vah z expertních rozhovorů. Reprodukuje výsledky diplomové práce.
                    <br><br>
                    <strong>Vhodné pro:</strong> Rychlé hodnocení, porovnání s výzkumem
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Spustit s průměrnými váhami", use_container_width=True, type="primary"):
                st.session_state.mode = "average"
                st.rerun()
        
        with col_right:
            st.markdown("""
            <div class="card">
                <div class="card-title">Vlastní kalibrace</div>
                <div class="card-description">
                    Definujte vlastní priority a váhy podle potřeb vaší organizace.
                    <br><br>
                    <strong>Vhodné pro:</strong> Specifické požadavky, organizační kontext
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Spustit vlastní kalibraci", use_container_width=True):
                st.session_state.mode = "custom"
                st.rerun()
        
        st.markdown("##")
        
        # Methodology info
        with st.expander("ℹ️ O metodice TOPSIS"):
            col_info1, col_info2 = st.columns(2)
            
            with col_info1:
                st.markdown("""
                **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution)
                
                Metoda vícekriteriálního rozhodování pro objektivní srovnání alternativ.
                
                **Hodnocené platformy:**
                - Keboola
                - Microsoft Fabric  
                - Databricks
                """)
            
            with col_info2:
                st.markdown("""
                **Struktura hodnocení:**
                - 5 dimenzí
                - 20 metrik (4 na dimenzi)
                - Hierarchické váhy
                
                **Proces:**
                1. Normalizace metrik
                2. Aplikace vah
                3. Výpočet vzdáleností
                4. Finální skóre
                """)


def get_platform_color(platform_name):
    """Get the color for a specific platform."""
    colors = get_platform_colors()
    return colors.get(platform_name, '#667eea')


def display_result_cards(ranking, scores):
    """Display results as professional cards with platform colors."""
    platforms = list(ranking.index)
    
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    
    for i, (col, platform) in enumerate(zip(cols, platforms)):
        with col:
            platform_name = platform.replace('_', ' ')
            score = scores.get(platform, 0)
            rank = i + 1
            color = get_platform_color(platform)
            
            st.markdown(f"""
            <div class="result-card" style="background: {color};">
                <div class="result-rank">{rank}.</div>
                <div class="result-label">místo</div>
                <div class="result-platform">{platform_name}</div>
                <div class="result-score">{score:.3f}</div>
            </div>
            """, unsafe_allow_html=True)


def display_detailed_weights(dim_weights, metric_weights):
    """Display detailed breakdown of dimension and metric weights."""
    st.markdown("### Rozložení vah dimenzí")
    
    # Create simple bar chart
    dim_data = pd.DataFrame({
        'Dimenze': [d.replace('_', ' ') for d in dim_weights.keys()],
        'Váha (%)': [v * 100 for v in dim_weights.values()]
    })
    
    import plotly.graph_objects as go
    
    fig = go.Figure(data=[
        go.Bar(
            x=dim_data['Váha (%)'],
            y=dim_data['Dimenze'],
            orientation='h',
            marker=dict(
                color=['#667eea', '#764ba2', '#f093fb', '#4facfe', '#43e97b'],
                line=dict(color='rgba(0,0,0,0.2)', width=1)
            ),
            text=dim_data['Váha (%)'].apply(lambda x: f'{x:.1f}%'),
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis_title="Váha (%)",
        yaxis_title="",
        showlegend=False,
        xaxis=dict(range=[0, max(dim_data['Váha (%)']) * 1.1])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### Detailní breakdown metrik")
    
    scores_df, _ = load_platform_scores()
    
    for dimension in get_dimension_order():
        dim_name = dimension.replace('_', ' ')
        dim_weight = dim_weights.get(dimension, 0)
        
        with st.expander(f"**{dim_name}** — {dim_weight*100:.1f}%", expanded=False):
            # Get metrics for this dimension
            dim_metrics = scores_df[scores_df['Dimension'] == dimension]['Metric'].tolist()
            
            # Create table
            for metric in dim_metrics:
                metric_name = metric.replace('_', ' ')
                if dimension in metric_weights and metric in metric_weights[dimension]:
                    metric_weight = metric_weights[dimension][metric]
                    hierarchical = dim_weight * metric_weight
                    
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col1:
                        st.markdown(f"**{metric_name}**")
                    with col2:
                        st.caption(f"{metric_weight*100:.1f}%")
                    with col3:
                        st.caption(f"→ {hierarchical*100:.1f}%")
            
            st.caption("Levý sloupec: relativní váha v rámci dimenze | Pravý sloupec: finální hierarchická váha")


def show_average_mode():
    st.title("Hodnocení s průměrnými váhami")
    
    if st.button("← Zpět na výběr režimu"):
        reset_session()
        st.rerun()
    
    scores_df, metric_types = load_platform_scores()
    dim_weights, metric_weights, hierarchical_weights = load_default_weights()
    
    with st.expander("Zobrazit použité váhy"):
        # Display detailed weights
        display_detailed_weights(dim_weights, metric_weights)
    
    topsis_input = prepare_topsis_input(scores_df)
    topsis_results = run_topsis_analysis(topsis_input, hierarchical_weights, metric_types)
    dimension_scores = calculate_dimension_scores(scores_df)
    
    st.markdown("---")
    st.markdown("## Výsledky")
    st.markdown("")
    
    # Display result cards
    display_result_cards(topsis_results['ranking'], topsis_results['topsis_scores'])
    
    st.markdown("##")
    st.markdown("---")
    
    tab1, tab2 = st.tabs(["TOPSIS skóre", "Srovnání podle dimenzí"])
    
    with tab1:
        st.markdown("### Finální skóre")
        platform_colors = get_platform_colors()
        fig_bar = create_topsis_bar_chart(topsis_results['topsis_scores'], platform_colors)
        st.plotly_chart(fig_bar, use_container_width=True)
        
        st.markdown("### Pořadí")
        ranking_table = create_ranking_table(
            topsis_results['topsis_scores'],
            topsis_results['d_plus'],
            topsis_results['d_minus']
        )
        st.dataframe(ranking_table, hide_index=True, use_container_width=True)
    
    with tab2:
        st.markdown("### Srovnání podle dimenzí")
        fig_radar = create_radar_chart(dimension_scores, platform_colors)
        st.plotly_chart(fig_radar, use_container_width=True)
        
        st.markdown("### Skóre podle dimenzí")
        display_scores = dimension_scores.copy()
        display_scores.index = [idx.replace('_', ' ') for idx in display_scores.index]
        display_scores.columns = [col.replace('_', ' ') for col in display_scores.columns]
        st.dataframe(display_scores.T, use_container_width=True)
    
    st.markdown("---")
    st.markdown("## Export")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        csv_data = export_to_csv(topsis_results, dimension_scores, scores_df)
        st.download_button(
            "Stáhnout CSV (souhrn)",
            csv_data,
            create_download_filename("topsis_souhrn", "csv"),
            "text/csv",
            use_container_width=True
        )
    
    with col2:
        detailed_csv = export_detailed_csv(topsis_results, scores_df, hierarchical_weights)
        st.download_button(
            "Stáhnout CSV (detail)",
            detailed_csv,
            create_download_filename("topsis_detail", "csv"),
            "text/csv",
            use_container_width=True
        )
    
    with col3:
        pdf_data = generate_pdf_report(
            topsis_results, dimension_scores, scores_df, 
            hierarchical_weights, dim_weights, mode="average"
        )
        st.download_button(
            "Stáhnout PDF zprávu",
            pdf_data,
            create_download_filename("topsis_zprava", "pdf"),
            "application/pdf",
            use_container_width=True
        )


def show_custom_mode():
    st.title("Vlastní kalibrace")
    
    col1, col2 = st.columns([4, 1])
    with col1:
        if st.button("← Zpět na výběr režimu"):
            reset_session()
            st.rerun()
    with col2:
        if st.button("↻ Reset kalibrace"):
            # Reset all slider values to 3 (default)
            for key in list(st.session_state.keys()):
                if key.startswith('m_'):
                    st.session_state[key] = 3
                elif key.startswith('d_'):
                    st.session_state[key] = 20.0
            
            # Clear tracking dictionaries
            st.session_state.metric_weights = {}
            st.session_state.dim_weights = {}
            st.session_state.results = None
            st.rerun()
    
    scores_df, metric_types = load_platform_scores()
    metric_defs = load_metric_definitions()
    dimensions = get_dimension_order()
    
    total_metrics = len(scores_df)
    completed = len(st.session_state.metric_weights)
    
    st.markdown(f"### Krok 1: Ohodnoťte metriky ({completed}/{total_metrics})")
    
    # Add rating scale explanation
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f0f8ff 0%, #e6f2ff 100%); 
                padding: 1.25rem; border-radius: 10px; margin-bottom: 1.5rem; 
                border-left: 5px solid #0066cc; box-shadow: 0 2px 4px rgba(0,102,204,0.1);">
        <strong style="font-size: 1.05rem; color: #0066cc;">📊 Škála hodnocení (1-5):</strong><br>
        <div style="margin-top: 0.75rem; line-height: 1.8;">
            <strong>1</strong> = Nepodstatné <span style="color: #666;">(minimální vliv na rozhodování)</span><br>
            <strong>2</strong> = Málo důležité <span style="color: #666;">(malý vliv)</span><br>
            <strong>3</strong> = Středně důležité <span style="color: #666;">(průměrný vliv)</span><br>
            <strong>4</strong> = Velmi důležité <span style="color: #666;">(velký vliv)</span><br>
            <strong>5</strong> = Kritické <span style="color: #666;">(rozhodující vliv na výběr platformy)</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    for dimension in dimensions:
        # Always keep expanders open for better UX
        with st.expander(f"📊 {dimension.replace('_', ' ')}", expanded=True):
            dim_metrics = scores_df[scores_df['Dimension'] == dimension]['Metric'].tolist()
            
            for metric in dim_metrics:
                col1, col2 = st.columns([2, 3])
                
                with col1:
                    if dimension in metric_defs and metric in metric_defs[dimension]:
                        info = metric_defs[dimension][metric]
                        st.markdown(f"**{info['name']}**")
                        with st.popover("ℹ️ Co to znamená?"):
                            st.caption(info['description'])
                
                with col2:
                    current = st.session_state.metric_weights.get(metric, 3)
                    rating = st.slider(
                        f"_{metric}",
                        min_value=1,
                        max_value=5,
                        value=current,
                        step=1,
                        key=f"m_{metric}",
                        label_visibility="collapsed"
                    )
                    st.session_state.metric_weights[metric] = rating
                
                st.markdown("")  # Add spacing between metrics
    
    all_rated = len(st.session_state.metric_weights) == total_metrics
    
    if all_rated:
        st.success("Všechny metriky ohodnoceny.")
        
        st.markdown("---")
        st.markdown("### Krok 2: Rozdělte 100 bodů mezi dimenze")
        st.caption("Alokujte body podle důležitosti jednotlivých dimenzí.")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            for dimension in dimensions:
                current = st.session_state.dim_weights.get(dimension, 20.0)
                weight = st.number_input(
                    dimension.replace('_', ' '),
                    0.0, 100.0, float(current), 1.0,
                    key=f"d_{dimension}"
                )
                st.session_state.dim_weights[dimension] = weight
        
        with col2:
            total = sum(st.session_state.dim_weights.values())
            remaining = 100 - total
            
            # Determine status
            valid = abs(total - 100) < 0.01
            status = "valid" if valid else ("over" if total > 100 else "under")
            
            # Display points counter
            st.markdown(f"""
            <div class="points-counter {status}">
                <div class="points-label">Zbývá bodů</div>
                <div class="points-number {status}">{abs(remaining):.0f}</div>
                <div class="points-message">
                    {'Můžete pokračovat!' if valid else 
                     f'Překročeno o {total - 100:.0f}' if total > 100 else 
                     f'Přidejte ještě {remaining:.0f}'}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if valid:
                fig_pie = create_dimension_weights_pie(
                    normalize_weights(st.session_state.dim_weights)
                )
                st.plotly_chart(fig_pie, use_container_width=True)
        
        st.markdown("---")
        
        if valid and st.button("Vypočítat TOPSIS skóre", type="primary", use_container_width=True):
            with st.spinner("Probíhá výpočet..."):
                dim_weights_norm = normalize_weights(st.session_state.dim_weights)
                
                metric_weights_by_dim = {}
                for dim in dimensions:
                    dim_metrics = scores_df[scores_df['Dimension'] == dim]['Metric'].tolist()
                    dim_metric_w = {m: st.session_state.metric_weights[m] for m in dim_metrics}
                    metric_weights_by_dim[dim] = normalize_weights(dim_metric_w)
                
                hierarchical = calculate_hierarchical_weights(dim_weights_norm, metric_weights_by_dim)
                
                topsis_input = prepare_topsis_input(scores_df)
                topsis_results = run_topsis_analysis(topsis_input, hierarchical, metric_types)
                dimension_scores = calculate_dimension_scores(scores_df)
                
                st.session_state.results = {
                    'topsis': topsis_results,
                    'dimensions': dimension_scores,
                    'hierarchical': hierarchical,
                    'dim_weights': dim_weights_norm,
                    'metric_weights': metric_weights_by_dim
                }
                
                st.rerun()
    
    if st.session_state.results:
        results = st.session_state.results
        topsis_results = results['topsis']
        dimension_scores = results['dimensions']
        
        st.markdown("---")
        st.markdown("## Vaše výsledky")
        st.markdown("")
        
        # Display result cards
        display_result_cards(topsis_results['ranking'], topsis_results['topsis_scores'])
        
        st.markdown("##")
        
        # Display user's weights
        with st.expander("Zobrazit vaše váhy"):
            display_detailed_weights(results['dim_weights'], results['metric_weights'])
        
        st.markdown("---")
        
        tab1, tab2 = st.tabs(["TOPSIS skóre", "Srovnání podle dimenzí"])
        
        with tab1:
            platform_colors = get_platform_colors()
            fig_bar = create_topsis_bar_chart(topsis_results['topsis_scores'], platform_colors)
            st.plotly_chart(fig_bar, use_container_width=True)
            
            ranking_table = create_ranking_table(
                topsis_results['topsis_scores'],
                topsis_results['d_plus'],
                topsis_results['d_minus']
            )
            st.dataframe(ranking_table, hide_index=True, use_container_width=True)
        
        with tab2:
            fig_radar = create_radar_chart(dimension_scores, platform_colors)
            st.plotly_chart(fig_radar, use_container_width=True)
        
        st.markdown("---")
        st.markdown("## Export")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            csv_data = export_to_csv(topsis_results, dimension_scores, scores_df)
            st.download_button(
                "Stáhnout CSV (souhrn)",
                csv_data,
                create_download_filename("vlastni_souhrn", "csv"),
                "text/csv",
                use_container_width=True
            )
        
        with col2:
            detailed_csv = export_detailed_csv(topsis_results, scores_df, results['hierarchical'])
            st.download_button(
                "Stáhnout CSV (detail)",
                detailed_csv,
                create_download_filename("vlastni_detail", "csv"),
                "text/csv",
                use_container_width=True
            )
        
        with col3:
            pdf_data = generate_pdf_report(
                topsis_results, dimension_scores, scores_df,
                results['hierarchical'], results['dim_weights'], mode="custom"
            )
            st.download_button(
                "Stáhnout PDF zprávu",
                pdf_data,
                create_download_filename("vlastni_zprava", "pdf"),
                "application/pdf",
                use_container_width=True
            )


def main():
    init_session()
    
    if st.session_state.mode is None:
        show_landing()
    elif st.session_state.mode == "average":
        show_average_mode()
    elif st.session_state.mode == "custom":
        show_custom_mode()


if __name__ == "__main__":
    main()
