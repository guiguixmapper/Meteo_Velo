"""
ui/components/metrics_banner.py
================================
Bandeau score + métriques — design Strava.
"""

import streamlit as st


def render_metrics_banner(score: dict, dist_tot: float, d_plus: float, d_moins: float,
                           temps_s: float, vit_moy_reelle: float,
                           heure_arr, calories: int):
    dh = int(temps_s // 3600)
    dm = int((temps_s % 3600) // 60)

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
        <div class="metric-cell">
          <div class="mv">{round(dist_tot/1000,1)}</div>
          <div class="mu">km · Distance</div>
        </div>
        <div class="metric-cell">
          <div class="mv">{int(d_plus)}</div>
          <div class="mu">m · D+</div>
        </div>
        <div class="metric-cell">
          <div class="mv">{int(d_moins)}</div>
          <div class="mu">m · D−</div>
        </div>
        <div class="metric-cell">
          <div class="mv">{dh}h{dm:02d}</div>
          <div class="mu">Durée</div>
        </div>
        <div class="metric-cell">
          <div class="mv orange">{vit_moy_reelle}</div>
          <div class="mu">km/h · Moy.</div>
        </div>
        <div class="metric-cell">
          <div class="mv">{heure_arr.strftime('%H:%M')}</div>
          <div class="mu">Arrivée</div>
        </div>
        <div class="metric-cell">
          <div class="mv">{calories}</div>
          <div class="mu">kcal</div>
        </div>
      </div>
    </div>""", unsafe_allow_html=True)
