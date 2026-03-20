"""
ui/components/metrics_banner.py
================================
Bannière score + métriques — colonnes Streamlit natives, hauteur minimale garantie.
"""

import streamlit as st


def render_metrics_banner(score: dict, dist_tot: float, d_plus: float, d_moins: float,
                           temps_s: float, vit_moy_reelle: float,
                           heure_arr, calories: int):
    dh = int(temps_s // 3600)
    dm = int((temps_s % 3600) // 60)

    # Couleur du score
    score_color = (
        "#ef4444" if score['total'] < 3.5 else
        "#f97316" if score['total'] < 5.0 else
        "#eab308" if score['total'] < 6.5 else
        "#22c55e" if score['total'] < 8.0 else
        "#FC4C02"
    )

    cols = st.columns([1.4, 1, 1, 1, 1, 1, 1, 1])

    with cols[0]:
        st.markdown(
            f'<div style="background:#FC4C02;border-radius:10px;padding:8px 12px;text-align:center">'
            f'<div style="color:white;font-size:1.6rem;font-weight:900;line-height:1;letter-spacing:-1px">'
            f'{score["total"]}<span style="font-size:0.8rem;opacity:0.8">/10</span></div>'
            f'<div style="color:white;font-size:0.58rem;font-weight:700;text-transform:uppercase;'
            f'letter-spacing:0.4px;margin-top:2px;opacity:0.95">{score["label"]}</div>'
            f'<div style="display:flex;gap:3px;margin-top:4px;justify-content:center;flex-wrap:wrap">'
            f'<span style="background:rgba(255,255,255,0.2);border-radius:10px;padding:1px 5px;'
            f'font-size:0.58rem;color:white;font-weight:600">🌤️ {score["score_meteo"]}/6</span>'
            f'<span style="background:rgba(255,255,255,0.2);border-radius:10px;padding:1px 5px;'
            f'font-size:0.58rem;color:white;font-weight:600">🏔️ {score["score_cols"]}/4</span>'
            f'</div></div>',
            unsafe_allow_html=True)

    metrics = [
        (round(dist_tot/1000, 1), "km"),
        (int(d_plus),             "D+ m"),
        (int(d_moins),            "D− m"),
        (f"{dh}h{dm:02d}",        "durée"),
        (vit_moy_reelle,          "km/h moy.", True),
        (heure_arr.strftime('%H:%M'), "arrivée"),
        (calories,                "kcal"),
    ]

    for i, item in enumerate(metrics):
        val, unit = item[0], item[1]
        is_orange = len(item) > 2 and item[2]
        color = "#FC4C02" if is_orange else "inherit"
        with cols[i + 1]:
            st.markdown(
                f'<div style="text-align:center;padding:4px 0">'
                f'<div style="font-size:1.15rem;font-weight:900;letter-spacing:-0.3px;'
                f'line-height:1;color:{color}">{val}</div>'
                f'<div style="font-size:0.6rem;font-weight:600;text-transform:uppercase;'
                f'letter-spacing:0.3px;opacity:0.5;margin-top:2px">{unit}</div>'
                f'</div>',
                unsafe_allow_html=True)
