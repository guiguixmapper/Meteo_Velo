"""
ui/styles/theme.py
==================
Tout le CSS de l'application en un seul endroit.
"""

CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

  html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  }

  footer { visibility: hidden; }
  .block-container { padding-top: 4rem !important; padding-bottom: 2rem !important; }

  /* ── Palette Teal ── */
  :root {
    --teal:      #0d9488;
    --teal-dark: #0f766e;
    --teal-l:    rgba(13,148,136,0.12);
  }

  /* ── Sidebar ── */
  [data-testid="stSidebar"] { padding-top: 0 !important; }
  [data-testid="stSidebar"] hr { margin: 0.4rem 0 !important; opacity: 0.3; }
  [data-testid="stSidebar"] h1,
  [data-testid="stSidebar"] h2,
  [data-testid="stSidebar"] h3 { font-size: 0.88rem !important; font-weight: 700 !important; }
  [data-testid="stSidebar"] label,
  [data-testid="stSidebar"] p  { font-size: 0.82rem !important; }

  .sb-section {
    font-size: 0.65rem; font-weight: 700; text-transform: uppercase;
    letter-spacing: 0.8px; opacity: 0.45; margin: 12px 0 6px 0;
  }

  /* Export button */
  .export-btn a {
    display: block; text-align: center;
    background: var(--teal); color: white !important;
    padding: 10px 16px; border-radius: 10px;
    text-decoration: none; font-weight: 700;
    font-size: 0.85rem; letter-spacing: 0.2px;
    transition: background 0.15s ease;
    box-shadow: 0 2px 8px rgba(13,148,136,0.3);
  }
  .export-btn a:hover { background: var(--teal-dark); }

  /* ── Score / métriques banner ── */
  .score-banner {
    display: flex; align-items: stretch;
    border: 1px solid rgba(128,128,128,0.18);
    border-radius: 14px; overflow: hidden;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
    margin-bottom: 16px;
    background: rgba(128,128,128,0.04);
  }
  .score-left {
    background: linear-gradient(135deg, #0f766e, #0d9488);
    color: white !important; padding: 16px 20px; min-width: 145px;
    display: flex; flex-direction: column; justify-content: center; flex-shrink: 0;
  }
  .score-left * { color: white !important; }
  .score-left .score-num { font-size: 2.5rem; font-weight: 900; line-height: 1; letter-spacing: -1px; }
  .score-left .score-lbl { font-size: 0.78rem; font-weight: 600; margin-top: 3px; opacity: 0.92; }
  .score-left .score-badges { display: flex; gap: 5px; margin-top: 8px; flex-wrap: wrap; }
  .score-left .score-badge {
    background: rgba(255,255,255,0.18); border-radius: 20px;
    padding: 2px 8px; font-size: 0.68rem; font-weight: 500;
  }
  .metric-grid { display: flex; flex: 1; overflow: hidden; }
  .metric-cell {
    flex: 1; min-width: 75px; text-align: center; padding: 14px 6px;
    border-right: 1px solid rgba(128,128,128,0.12);
    display: flex; flex-direction: column; justify-content: center;
  }
  .metric-cell:last-child { border-right: none; }
  .metric-cell .mv { font-size: 1.45rem; font-weight: 800; letter-spacing: -0.5px; line-height: 1.1; }
  .metric-cell .mu { font-size: 0.68rem; font-weight: 500; margin-top: 1px; opacity: 0.45; }
  .metric-cell .ml { font-size: 0.62rem; margin-top: 2px; opacity: 0.4; }
  .metric-cell .mv.green { color: #10b981 !important; }

  /* ── Soleil pill ── */
  .soleil-row {
    display: inline-flex; gap: 18px; align-items: center; flex-wrap: wrap;
    background: rgba(251,191,36,0.1); border: 1px solid rgba(251,191,36,0.3);
    border-radius: 10px; padding: 8px 16px; margin: 8px 0 12px;
  }
  .soleil-item .s-val { font-size: 0.88rem; font-weight: 700; }
  .soleil-item .s-lbl { font-size: 0.62rem; opacity: 0.6; text-transform: uppercase; letter-spacing: 0.4px; }

  /* ── Tabs ── */
  [data-testid="stTabs"] [data-testid="stTab"] {
    font-size: 0.84rem !important; font-weight: 600 !important;
    padding: 6px 16px !important; background: transparent !important; opacity: 0.7 !important;
  }
  [data-testid="stTabs"] [data-testid="stTab"]:hover { opacity: 1 !important; }
  [data-testid="stTabs"] [aria-selected="true"]       { opacity: 1 !important; }
  [data-testid="stTabsContent"] { padding-top: 14px !important; }

  /* ── Buttons ── */
  .stButton > button {
    border-radius: 9px !important; font-weight: 600 !important;
    font-size: 0.83rem !important; padding: 7px 16px !important;
    border: 1px solid rgba(128,128,128,0.25) !important;
    background: rgba(128,128,128,0.06) !important;
    transition: all 0.15s ease !important;
  }
  .stButton > button:hover {
    background: rgba(128,128,128,0.12) !important;
    border-color: rgba(128,128,128,0.35) !important;
  }

  /* ── Expander ── */
  [data-testid="stExpander"] {
    border: 1px solid rgba(128,128,128,0.2) !important;
    border-radius: 10px !important; overflow: hidden;
  }
  [data-testid="stExpander"] summary {
    font-size: 0.83rem !important; font-weight: 600 !important; padding: 10px 14px !important;
  }

  /* ── Misc ── */
  .stAlert { border-radius: 10px !important; font-size: 0.83rem !important; }
  [data-testid="stDataFrame"] { border-radius: 10px !important; overflow: hidden; }
  .stCaption, [data-testid="stCaptionContainer"] { font-size: 0.75rem !important; opacity: 0.6 !important; }

  @media (max-width: 768px) {
    .metric-cell .mv { font-size: 1.1rem; }
    .score-left { min-width: 105px; padding: 12px; }
    .score-left .score-num { font-size: 2rem; }
  }
</style>
"""
