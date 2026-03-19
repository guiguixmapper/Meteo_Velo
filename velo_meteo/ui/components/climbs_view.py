"""
ui/components/climbs_view.py
=============================
Onglet Ascensions — tableau + profil détaillé.
"""

import streamlit as st
import pandas as pd
from config.settings import LEGENDE_UCI
from core.services.climbing_service import (
    estimer_watts, estimer_fc, get_zone, zones_actives,
)
from ui.components.profile_view import creer_figure_col


def render_climbs_view(ascensions, df_profil, vitesse, ref_val, ftp_fc, mode, poids):
    st.caption(LEGENDE_UCI)

    if not ascensions:
        st.success("🚴‍♂️ Aucune difficulté catégorisée — parcours roulant !")
        return

    for a in ascensions:
        w       = estimer_watts(a["_pente_moy"], vitesse, poids)
        _, zlbl, _ = get_zone(w, ref_val, zones_actives(mode))
        pct     = round(w / ref_val * 100) if ref_val > 0 else 0
        fc_est  = estimer_fc(w, ftp_fc, ref_val)
        a["Puissance"]  = f"{w} W"
        a["Effort val"] = (f"{pct}% FTP" if mode == "⚡ Puissance"
                           else f"~{fc_est} bpm" if fc_est else "—")
        a["Zone"]   = zlbl
        a["Effort"] = ("🔴 Max"       if pct > 105 else "🟠 Très dur"  if pct > 95
                       else "🟡 Difficile" if pct > 80  else "🟢 Modéré"    if pct > 60
                       else "🔵 Endurance")

    cols_aff = ["Catégorie", "Nom", "Départ (km)", "Sommet (km)", "Longueur",
                "Dénivelé", "Pente moy.", "Pente max", "Alt. sommet",
                "Score UCI", "Temps col", "Arrivée sommet", "Puissance", "Effort val", "Zone", "Effort"]
    df_asc = pd.DataFrame(ascensions)
    if "Nom" not in df_asc.columns:
        df_asc["Nom"] = "—"

    st.dataframe(df_asc[cols_aff], width='stretch', hide_index=True, key="climbs_df",
        column_config={
            "Nom":            st.column_config.TextColumn("🏔️ Nom OSM"),
            "Effort val":     st.column_config.TextColumn("% FTP" if mode == "⚡ Puissance" else "FC estimée"),
            "Temps col":      st.column_config.TextColumn("⏱️ Temps col"),
            "Arrivée sommet": st.column_config.TextColumn("🏁 Arrivée sommet"),
            "Zone":           st.column_config.TextColumn("Zone"),
            "Effort":         st.column_config.TextColumn("Effort"),
        })

    st.divider()
    st.subheader("🔍 Profil détaillé d'une montée")
    noms_cols = [
        f"{a.get('Nom','') + ' — ' if a.get('Nom','—') != '—' else ''}"
        f"{a['Catégorie']} — Km {a['Départ (km)']}→{a['Sommet (km)']} ({a['Longueur']}, {a['Dénivelé']})"
        for a in ascensions]
    col_choix = st.selectbox("Choisir une montée :", options=noms_cols, index=0, key="climbs_selectbox")
    asc_sel   = ascensions[noms_cols.index(col_choix)]
    dk_sel    = asc_sel["_sommet_km"] - asc_sel["_debut_km"]
    seg_defaut = 0.5 if dk_sel < 5 else 1.0 if dk_sel < 15 else 2.0
    col_ctrl1, col_ctrl2 = st.columns([3, 1])
    with col_ctrl1:
        seg_km = st.slider("Longueur des segments (km)", 0.25,
                           min(5.0, dk_sel / 2), float(seg_defaut), 0.25, key="climbs_slider")
    with col_ctrl2:
        nb_segs = max(2, int(dk_sel / seg_km))
        st.metric("Segments", nb_segs)
    if not df_profil.empty:
        fig_col = creer_figure_col(df_profil, asc_sel, nb_segments=nb_segs)
        if fig_col:
            st.plotly_chart(fig_col, width='stretch', key="climbs_fig_col")
        st.markdown("**Intensité de pente :** 🟢 <3% · 🟡 3–6% · 🟠 6–8% · 🔴 8–12% · 🟤 >12%")
