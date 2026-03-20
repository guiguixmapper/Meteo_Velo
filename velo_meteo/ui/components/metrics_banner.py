"""
ui/components/metrics_banner.py
================================
Bannière score + métriques — ultra compacte, style Strava.
"""

import streamlit as st


def render_metrics_banner(score: dict, dist_tot: float, d_plus: float, d_moins: float,
                           temps_s: float, vit_moy_reelle: float,
                           heure_arr, calories: int):
    dh = int(temps_s // 3600)
    dm = int((temps_s % 3600) // 60)

    def cell(val, unit):
        return (f'<div class="metric-cell">'
                f'<div class="mv">{val}</div>'
                f'<div class="mu">{unit}</div>'
                f'</div>')

    st.markdown(f"""
    <div class="score-banner">
      <div class="score-left">
        <div class="score-num">{score['total']}<span>/10</span></div>
        <div class="score-lbl">{score['label']}</div>
        <div class="score-badges">
          <span class="score-badge">🌤️ {score['score_meteo']}/6</span>
          <span class="score-badge">🏔️ {score['score_cols']}/4</span>
        </div>
      </div>
      <div class="metric-grid">
        {cell(round(dist_tot/1000,1), "km")}
        {cell(int(d_plus), "D+ m")}
        {cell(int(d_moins), "D− m")}
        {cell(f"{dh}h{dm:02d}", "durée")}
        <div class="metric-cell">
          <div class="mv orange">{vit_moy_reelle}</div>
          <div class="mu">km/h moy.</div>
        </div>
        {cell(heure_arr.strftime('%H:%M'), "arrivée")}
        {cell(calories, "kcal")}
      </div>
    </div>""", unsafe_allow_html=True)
