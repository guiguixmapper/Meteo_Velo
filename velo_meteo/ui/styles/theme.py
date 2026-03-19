"""
ui/styles/theme.py
==================
Thème Strava — orange #FC4C02, blanc, épuré, cartes avec ombre.
"""

CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

  html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  }

  footer { visibility: hidden; }
  .block-container { padding-top: 1.5rem !important; padding-bottom: 2rem !important; }

  :root {
    --strava:      #FC4C02;
    --strava-dark: #E03D00;
    --strava-light: rgba(252,76,2,0.08);
    --gray-100: #F5F5F5;
    --gray-200: #E8E8E8;
    --gray-500: #9CA3AF;
    --gray-700: #4B5563;
    --gray-900: #111827;
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.08),0 1px 2px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.08),0 2px 4px rgba(0,0,0,0.05);
    --radius: 12px;
  }

  /* ── Sidebar ── */
  [data-testid="stSidebar"] {
    background: #FFFFFF !important;
    border-right: 1px solid #E8E8E8 !important;
    padding-top: 0 !important;
  }
  [data-testid="stSidebar"] hr { margin: 0.5rem 0 !important; border-color: #E8E8E8 !important; opacity: 1 !important; }
  [data-testid="stSidebar"] h1,
  [data-testid="stSidebar"] h2,
  [data-testid="stSidebar"] h3 { font-size: 0.85rem !important; font-weight: 700 !important; }
  [data-testid="stSidebar"] label,
  [data-testid="stSidebar"] p   { font-size: 0.82rem !important; }

  .sb-section {
    font-size: 0.62rem; font-weight: 800; text-transform: uppercase;
    letter-spacing: 1px; color: #FC4C02 !important;
    margin: 14px 0 5px 0;
  }

  /* Export button */
  .export-btn a {
    display: block; text-align: center;
    background: #FC4C02; color: white !important;
    padding: 11px 16px; border-radius: 12px;
    text-decoration: none; font-weight: 800; font-size: 0.85rem;
    transition: all 0.15s ease;
    box-shadow: 0 2px 8px rgba(252,76,2,0.35);
  }
  .export-btn a:hover { background: #E03D00; transform: translateY(-1px); }

  /* ── Score banner Strava ── */
  .score-banner {
    display: flex; align-items: stretch;
    border-radius: 12px; overflow: hidden;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    background: #FFFFFF;
    border: 1px solid #E8E8E8;
  }
  .score-left {
    background: #FC4C02;
    color: white !important; padding: 18px 22px; min-width: 155px;
    display: flex; flex-direction: column; justify-content: center; flex-shrink: 0;
    position: relative; overflow: hidden;
  }
  .score-left::after {
    content: ""; position: absolute; right: -20px; top: -20px;
    width: 90px; height: 90px; border-radius: 50%;
    background: rgba(255,255,255,0.10);
  }
  .score-left * { color: white !important; }
  .score-left .score-num { font-size: 3rem; font-weight: 900; line-height: 1; letter-spacing: -2px; position: relative; z-index: 1; }
  .score-left .score-lbl { font-size: 0.72rem; font-weight: 700; margin-top: 4px; opacity: 0.95; text-transform: uppercase; letter-spacing: 0.5px; position: relative; z-index: 1; }
  .score-left .score-badges { display: flex; gap: 5px; margin-top: 10px; flex-wrap: wrap; position: relative; z-index: 1; }
  .score-left .score-badge {
    background: rgba(255,255,255,0.22); border-radius: 20px;
    padding: 2px 8px; font-size: 0.67rem; font-weight: 600;
    border: 1px solid rgba(255,255,255,0.25);
  }

  .metric-grid { display: flex; flex: 1; overflow: hidden; }
  .metric-cell {
    flex: 1; min-width: 72px; text-align: center; padding: 16px 8px;
    border-right: 1px solid #E8E8E8;
    display: flex; flex-direction: column; justify-content: center;
    transition: background 0.1s;
  }
  .metric-cell:last-child { border-right: none; }
  .metric-cell:hover { background: #F5F5F5; }
  .metric-cell .mv { font-size: 1.5rem; font-weight: 900; letter-spacing: -0.5px; line-height: 1; color: #111827; }
  .metric-cell .mu { font-size: 0.62rem; font-weight: 700; margin-top: 2px; color: #9CA3AF; text-transform: uppercase; letter-spacing: 0.5px; }
  .metric-cell .ml { font-size: 0.6rem; margin-top: 3px; color: #9CA3AF; }
  .metric-cell .mv.orange { color: #FC4C02 !important; }

  /* ── Soleil pill ── */
  .soleil-row {
    display: inline-flex; gap: 20px; align-items: center; flex-wrap: wrap;
    background: #FFFBF5; border: 1px solid rgba(252,76,2,0.2);
    border-radius: 12px; padding: 10px 18px; margin: 8px 0 14px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
  }
  .soleil-item .s-val { font-size: 0.9rem; font-weight: 800; color: #111827; }
  .soleil-item .s-lbl { font-size: 0.6rem; color: #9CA3AF; text-transform: uppercase; letter-spacing: 0.5px; }

  /* ── Tabs ── */
  [data-testid="stTabs"] [data-testid="stTab"] {
    font-size: 0.83rem !important; font-weight: 700 !important;
    padding: 8px 18px !important; background: transparent !important;
    opacity: 0.55 !important; transition: all 0.15s !important;
  }
  [data-testid="stTabs"] [data-testid="stTab"]:hover { opacity: 0.85 !important; }
  [data-testid="stTabs"] [aria-selected="true"]       { opacity: 1 !important; color: #FC4C02 !important; }
  [data-testid="stTabsContent"] { padding-top: 16px !important; }

  /* ── Buttons ── */
  .stButton > button {
    border-radius: 12px !important; font-weight: 700 !important;
    font-size: 0.83rem !important; padding: 8px 18px !important;
    border: 2px solid #E8E8E8 !important;
    background: #FFFFFF !important; color: #111827 !important;
    transition: all 0.15s ease !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08) !important;
  }
  .stButton > button:hover {
    border-color: #FC4C02 !important; color: #FC4C02 !important;
    background: rgba(252,76,2,0.06) !important;
    transform: translateY(-1px) !important;
  }

  /* ── Expander ── */
  [data-testid="stExpander"] {
    border: 1px solid #E8E8E8 !important;
    border-radius: 12px !important; overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06) !important;
  }
  [data-testid="stExpander"] summary {
    font-size: 0.83rem !important; font-weight: 700 !important;
    padding: 10px 14px !important; background: #F5F5F5 !important;
  }

  /* ── DataFrames ── */
  [data-testid="stDataFrame"] {
    border-radius: 12px !important; overflow: hidden;
    border: 1px solid #E8E8E8 !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06) !important;
  }

  /* ── Misc ── */
  .stAlert { border-radius: 12px !important; font-size: 0.83rem !important; }
  .stCaption, [data-testid="stCaptionContainer"] { font-size: 0.73rem !important; color: #9CA3AF !important; }
  hr { border-color: #E8E8E8 !important; }

  /* ── Strava card component ── */
  .strava-card {
    background: #FFFFFF; border: 1px solid #E8E8E8; border-radius: 12px;
    padding: 16px 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    transition: box-shadow 0.15s;
  }
  .strava-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
  .strava-card .card-label {
    font-size: 0.62rem; font-weight: 800; text-transform: uppercase;
    letter-spacing: 0.8px; color: #9CA3AF; margin-bottom: 4px;
  }
  .strava-card .card-value { font-size: 1.8rem; font-weight: 900; color: #111827; letter-spacing: -1px; line-height: 1; }
  .strava-card .card-unit  { font-size: 0.8rem; font-weight: 600; color: #9CA3AF; margin-left: 3px; }
  .strava-card .card-sub   { font-size: 0.72rem; color: #9CA3AF; margin-top: 4px; }

  /* ── Page header ── */
  .strava-page-header {
    display: flex; align-items: center; gap: 12px;
    padding-bottom: 14px; border-bottom: 2px solid #E8E8E8; margin-bottom: 18px;
  }
  .strava-page-header .ph-icon {
    width: 38px; height: 38px; border-radius: 10px;
    background: #FC4C02; display: flex; align-items: center; justify-content: center;
    font-size: 1.2rem; box-shadow: 0 2px 8px rgba(252,76,2,0.3); flex-shrink: 0;
  }
  .strava-page-header .ph-title { font-size: 1.3rem; font-weight: 900; color: #111827; letter-spacing: -0.5px; }
  .strava-page-header .ph-sub   { font-size: 0.72rem; color: #9CA3AF; margin-top: 1px; }

  @media (max-width: 768px) {
    .metric-cell .mv { font-size: 1.15rem; }
    .score-left { min-width: 110px; padding: 14px; }
    .score-left .score-num { font-size: 2.2rem; }
  }
</style>
"""
