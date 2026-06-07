import streamlit as st
import sys
import os
from datetime import datetime

st.set_page_config(
    page_title="Research Core — Multi Agent Orchestration & Retrieval Framework",
    page_icon="🍀",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@300;400;500;600;700&display=swap');

:root {
    --bg:        #030a05;
    --bg2:       #071008;
    --bg3:       #0d1a0f;
    --bg4:       #142616;
    --border:    #1a3a1c;
    --border2:   #244d27;
    --g1:        #22c55e;
    --g2:        #16a34a;
    --g3:        #15803d;
    --g4:        #4ade80;
    --g5:        #86efac;
    --gold:      #fbbf24;
    --goldlo:    rgba(251,191,36,0.10);
    --g1lo:      rgba(34,197,94,0.10);
    --g1md:      rgba(34,197,94,0.20);
    --g4lo:      rgba(74,222,128,0.08);
    --emerald:   #10b981;
    --emeraldlo: rgba(16,185,129,0.10);
    --mint:      #6ee7b7;
    --mintlo:    rgba(110,231,183,0.10);
    --red:       #f87171;
    --redlo:     rgba(248,113,113,0.10);
    --amber:     #fbbf24;
    --amberlo:   rgba(251,191,36,0.10);
    --text:      #f0fdf4;
    --text2:     #86efac;
    --text3:     #4ade80;
    --text4:     #166534;
    --muted:     #365314;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; }

html, body, [class*="css"], .stApp {
    font-family: 'DM Sans', sans-serif !important;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}

#MainMenu, footer, header, .stDeployButton { visibility: hidden !important; }
.block-container { padding: 0 2.5rem 5rem !important; max-width: 1100px !important; }

/* ══════════════ ANIMATED BG ══════════════ */
.clover-bg {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}
.clover-bg::before {
    content: '';
    position: absolute;
    top: -200px; left: -200px;
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(34,197,94,0.07) 0%, transparent 60%);
    animation: drift1 18s ease-in-out infinite;
}
.clover-bg::after {
    content: '';
    position: absolute;
    bottom: -150px; right: -100px;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(16,185,129,0.06) 0%, transparent 60%);
    animation: drift2 22s ease-in-out infinite;
}
@keyframes drift1 {
    0%,100% { transform: translate(0,0) scale(1); }
    33%      { transform: translate(80px,60px) scale(1.1); }
    66%      { transform: translate(-40px,90px) scale(0.95); }
}
@keyframes drift2 {
    0%,100% { transform: translate(0,0) scale(1); }
    50%      { transform: translate(-70px,-50px) scale(1.15); }
}

/* floating clovers */
.clover-float {
    position: fixed;
    font-size: 1.2rem;
    opacity: 0.06;
    animation: floatUp linear infinite;
    pointer-events: none;
    z-index: 0;
}
@keyframes floatUp {
    0%   { transform: translateY(100vh) rotate(0deg);   opacity: 0; }
    10%  { opacity: 0.06; }
    90%  { opacity: 0.06; }
    100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
}

/* ══════════════ HERO ══════════════ */
.hero-wrap {
    position: relative;
    z-index: 1;
    text-align: center;
    padding: 4.5rem 0 3rem;
}
.hero-glow {
    position: absolute;
    top: 20px; left: 50%;
    transform: translateX(-50%);
    width: 700px; height: 350px;
    background: radial-gradient(ellipse, rgba(34,197,94,0.14) 0%, rgba(16,185,129,0.05) 45%, transparent 70%);
    pointer-events: none;
}
.hero-vines {
    position: absolute;
    inset: 0;
    background-image:
        radial-gradient(circle at 15% 50%, rgba(34,197,94,0.03) 0%, transparent 50%),
        radial-gradient(circle at 85% 30%, rgba(16,185,129,0.03) 0%, transparent 50%);
}

.hero-clover {
    font-size: 2.8rem;
    margin-bottom: 1rem;
    display: block;
    animation: sway 4s ease-in-out infinite;
    filter: drop-shadow(0 0 20px rgba(34,197,94,0.6));
}
@keyframes sway {
    0%,100% { transform: rotate(-8deg) scale(1); }
    50%      { transform: rotate(8deg) scale(1.08); }
}

.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--bg3);
    border: 1px solid var(--border2);
    border-radius: 999px;
    padding: 0.3rem 1rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.25em;
    color: var(--g4);
    text-transform: uppercase;
    margin-bottom: 1.25rem;
}
.live-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--g1);
    box-shadow: 0 0 10px var(--g1);
    animation: pulse-dot 2s infinite;
}
@keyframes pulse-dot {
    0%,100% { box-shadow: 0 0 6px var(--g1); }
    50%      { box-shadow: 0 0 16px var(--g1), 0 0 30px rgba(34,197,94,0.4); }
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 5.5rem;
    font-weight: 900;
    line-height: 1;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #f0fdf4 0%, #4ade80 35%, #22c55e 60%, #fbbf24 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
    text-shadow: none;
    white-space: nowrap;
}
@media (max-width: 768px) {
    .hero-title { font-size: 3rem !important; white-space: normal !important; }
    .hero-sub   { font-size: 0.9rem !important; }
    .block-container { padding: 0 1rem 3rem !important; }
}

.hero-sub {
    font-size: 1rem;
    color: var(--text2);
    max-width: 460px;
    margin: 0 auto;
    line-height: 1.65;
    font-weight: 400;
}

.hero-divider {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin: 1.75rem auto 0;
    max-width: 300px;
    color: var(--border2);
    font-size: 0.75rem;
}
.hero-divider::before, .hero-divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border2));
}
.hero-divider::after {
    background: linear-gradient(90deg, var(--border2), transparent);
}

/* ══════════════ INPUT ══════════════ */
.stTextInput > div > div {
    background: var(--bg2) !important;
    border: 1px solid var(--border2) !important;
    border-radius: 14px !important;
    padding: 0.9rem 1.25rem !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    color: var(--text) !important;
    transition: all 0.3s !important;
    box-shadow: 0 4px 30px rgba(0,0,0,0.4), inset 0 1px 0 rgba(34,197,94,0.05) !important;
}
.stTextInput > div > div:focus-within {
    border-color: var(--g1) !important;
    box-shadow: 0 0 0 3px var(--g1lo), 0 4px 30px rgba(0,0,0,0.4) !important;
}
.stTextInput input { color: var(--text) !important; font-family: 'DM Sans', sans-serif !important; }
.stTextInput input::placeholder { color: var(--muted) !important; }

/* hide "Press Enter to submit form" hint */
.stForm small, .stForm [data-testid="InputInstructions"],
small[data-testid="InputInstructions"],
div[data-testid="InputInstructions"] {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
}

/* ══════════════ BUTTON ══════════════ */
.stButton > button {
    background: linear-gradient(135deg, #16a34a 0%, #15803d 50%, #166534 100%) !important;
    color: #f0fdf4 !important;
    border: 1px solid rgba(74,222,128,0.3) !important;
    border-radius: 12px !important;
    padding: 0.85rem 0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    letter-spacing: 0.04em !important;
    width: 100% !important;
    transition: all 0.25s !important;
    box-shadow: 0 4px 24px rgba(22,163,74,0.35), inset 0 1px 0 rgba(255,255,255,0.1) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 36px rgba(22,163,74,0.55), 0 0 0 1px rgba(74,222,128,0.4) !important;
    background: linear-gradient(135deg, #22c55e 0%, #16a34a 50%, #15803d 100%) !important;
}

/* form submit button — same green style */
.stFormSubmitButton > button {
    background: linear-gradient(135deg, #16a34a 0%, #15803d 50%, #166534 100%) !important;
    color: #f0fdf4 !important;
    border: 1px solid rgba(74,222,128,0.3) !important;
    border-radius: 12px !important;
    padding: 0.85rem 0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    letter-spacing: 0.04em !important;
    width: 100% !important;
    transition: all 0.25s !important;
    box-shadow: 0 4px 24px rgba(22,163,74,0.35), inset 0 1px 0 rgba(255,255,255,0.1) !important;
}
.stFormSubmitButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 36px rgba(22,163,74,0.55), 0 0 0 1px rgba(74,222,128,0.4) !important;
    background: linear-gradient(135deg, #22c55e 0%, #16a34a 50%, #15803d 100%) !important;
}

/* remove form border/background */
.stForm {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}

/* ══════════════ SECTION LABEL ══════════════ */
.nx-label {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--g1);
    margin: 2.5rem 0 1.25rem;
    position: relative;
    z-index: 1;
}
.nx-label-icon { font-size: 0.9rem; }
.nx-label::after {
    content:'';
    flex:1;
    height:1px;
    background: linear-gradient(90deg, var(--border2), transparent);
}

/* ══════════════ STEP CARDS ══════════════ */
.nx-card {
    position: relative;
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.15rem 1.4rem;
    margin-bottom: 0.7rem;
    overflow: hidden;
    transition: all 0.3s;
    z-index: 1;
}
.nx-card::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: transparent;
    transition: background 0.3s;
    border-radius: 0 0 0 16px;
}
.nx-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: transparent;
    transition: background 0.3s;
    border-radius: 16px;
    pointer-events: none;
}
.nx-card.active {
    border-color: var(--g1);
    box-shadow: 0 0 30px var(--g1lo), 0 4px 20px rgba(0,0,0,0.3);
}
.nx-card.active::before { background: linear-gradient(180deg, var(--g4), var(--g1)); }
.nx-card.active::after  { background: linear-gradient(135deg, rgba(34,197,94,0.04), transparent 60%); }
.nx-card.done { border-color: var(--border2); }
.nx-card.done::before { background: linear-gradient(180deg, var(--emerald), var(--g3)); }

.nx-head {
    display: flex;
    align-items: center;
    gap: 0.9rem;
}
.nx-ico {
    width: 38px; height: 38px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem;
    flex-shrink: 0;
    background: var(--bg4);
    border: 1px solid var(--border2);
    transition: all 0.3s;
}
.nx-card.active .nx-ico {
    background: var(--g1lo);
    border-color: var(--g1);
    box-shadow: 0 0 12px var(--g1lo);
}
.nx-card.done .nx-ico {
    background: var(--emeraldlo);
    border-color: var(--emerald);
}
.nx-ttl {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text);
    line-height: 1.2;
}
.nx-sub {
    font-family: 'Space Mono', monospace;
    font-size: 0.6rem;
    color: var(--muted);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-top: 3px;
    transition: color 0.3s;
}
.nx-card.active .nx-sub { color: var(--g4); }
.nx-card.done .nx-sub   { color: var(--emerald); }
.nx-status {
    margin-left: auto;
    font-size: 0.72rem;
    font-weight: 700;
    font-family: 'Space Mono', monospace;
    transition: color 0.3s;
}
.nx-card.active .nx-status { color: var(--g1); }
.nx-card.done .nx-status   { color: var(--emerald); }

.nx-body {
    margin-top: 0.9rem;
    padding-top: 0.9rem;
    border-top: 1px solid var(--border);
    font-size: 0.82rem;
    color: var(--text2);
    line-height: 1.65;
    white-space: pre-wrap;
    max-height: 250px;
    overflow-y: auto;
}

/* ══════════════ IDLE CARDS ══════════════ */
.idle-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.2rem 1.35rem;
    margin-bottom: 0.7rem;
    transition: all 0.25s;
    position: relative;
    overflow: hidden;
    z-index: 1;
}
.idle-card::before {
    content: '';
    position: absolute;
    top: -30px; right: -30px;
    width: 80px; height: 80px;
    border-radius: 50%;
    background: var(--card-glow, rgba(34,197,94,0.05));
    transition: all 0.3s;
}
.idle-card:hover {
    border-color: var(--border2);
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
}
.idle-card:hover::before { transform: scale(2); opacity: 0.5; }
.ic-top { display:flex; align-items:center; gap:0.85rem; }
.ic-ico {
    width: 40px; height: 40px;
    border-radius: 11px;
    display:flex; align-items:center; justify-content:center;
    font-size: 1.2rem;
    flex-shrink: 0;
    transition: all 0.25s;
}
.ic-name { font-size:0.95rem; font-weight:700; color:var(--text); }
.ic-role {
    font-family:'Space Mono',monospace;
    font-size:0.58rem;
    color: var(--muted);
    letter-spacing:0.1em;
    text-transform:uppercase;
    margin-top:3px;
}

/* ══════════════ TABS ══════════════ */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    padding: 5px !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--text2) !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 0.5rem 1.3rem !important;
    transition: all 0.2s !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--g2), var(--g3)) !important;
    color: #f0fdf4 !important;
    box-shadow: 0 2px 12px rgba(22,163,74,0.35) !important;
}
.stTabs [data-baseweb="tab-panel"] {
    background: transparent !important;
    padding: 1.5rem 0 0 !important;
}

/* ══════════════ REPORT ══════════════ */
.nx-report {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 2rem 2.25rem;
    position: relative;
    overflow: hidden;
}
.nx-report::before {
    content: '🍀';
    position: absolute;
    top: 1.25rem; right: 1.5rem;
    font-size: 1.5rem;
    opacity: 0.08;
}
.nx-report-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 1.25rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--border);
    display:flex; align-items:center; gap:0.5rem;
}
.nx-report-body {
    font-size: 0.9rem;
    line-height: 1.85;
    color: var(--text2);
    white-space: pre-wrap;
}

/* ══════════════ FACT CHECK ══════════════ */
.fc {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 13px;
    padding: 1.1rem 1.3rem;
    margin-bottom: 0.75rem;
    border-left: 3px solid var(--border2);
    transition: transform 0.2s;
}
.fc:hover { transform: translateX(3px); }
.fc.verified { border-left-color: var(--g1); background: linear-gradient(135deg, var(--g1lo), var(--bg3)); }
.fc.false    { border-left-color: var(--red);  background: linear-gradient(135deg, var(--redlo), var(--bg3)); }
.fc.partial  { border-left-color: var(--gold); background: linear-gradient(135deg, var(--goldlo), var(--bg3)); }
.fc.overall  { border-left-color: var(--emerald); background: linear-gradient(135deg, var(--emeraldlo), var(--bg3)); }
.fc-claim   { font-size:0.92rem; font-weight:700; color:var(--text); margin-bottom:0.4rem; }
.fc-verdict { font-size:0.84rem; font-weight:600; color:var(--text); margin-bottom:0.35rem; }
.fc-evid    { font-size:0.81rem; color:var(--text2); line-height:1.55; }

/* ══════════════ SCORE ══════════════ */
.score-wrap {
    display: inline-flex;
    align-items: center;
    gap: 1.25rem;
    background: var(--bg3);
    border: 1px solid var(--border2);
    border-radius: 18px;
    padding: 1.1rem 2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 24px rgba(0,0,0,0.3);
}
.score-num {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 900;
    background: linear-gradient(135deg, var(--g4), var(--gold));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
}
.score-label { font-size:0.78rem; color:var(--text2); font-weight:500; line-height:1.4; }

/* ══════════════ DOWNLOAD ══════════════ */
.stDownloadButton > button {
    background: var(--bg3) !important;
    border: 1px solid var(--border2) !important;
    color: var(--text) !important;
    border-radius: 12px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 0.75rem !important;
    width: 100% !important;
    transition: all 0.25s !important;
}
.stDownloadButton > button:hover {
    border-color: var(--g1) !important;
    color: var(--g4) !important;
    box-shadow: 0 0 20px var(--g1lo) !important;
    background: var(--bg4) !important;
}

/* ══════════════ FOOTER HINT ══════════════ */
.hint-box {
    text-align:center;
    margin-top:3rem;
    padding:1.5rem 2rem;
    background:var(--bg2);
    border:1px solid var(--border);
    border-radius:16px;
    color:var(--muted);
    font-family:'Space Mono',monospace;
    font-size:0.68rem;
    letter-spacing:0.15em;
    position: relative;
    z-index: 1;
}

/* ══════════════ SCROLLBAR ══════════════ */
::-webkit-scrollbar { width:4px; height:4px; }
::-webkit-scrollbar-track { background:var(--bg2); }
::-webkit-scrollbar-thumb { background:var(--border2); border-radius:4px; }
::-webkit-scrollbar-thumb:hover { background:var(--g3); }

.stAlert { border-radius:12px !important; }

/* ══════════════ SIDEBAR ══════════════ */
[data-testid="stSidebar"] {
    background: var(--bg2) !important;
    border-right: 1px solid var(--border2) !important;
    min-width: 280px !important;
}
/* hide the collapse arrow button */
[data-testid="collapsedControl"],
button[kind="header"],
[data-testid="stSidebarCollapseButton"] {
    display: none !important;
}
[data-testid="stSidebar"] * { color: var(--text) !important; }
[data-testid="stSidebar"] .stTextInput > div > div {
    background: var(--bg3) !important;
    border: 1px solid var(--border2) !important;
    border-radius: 10px !important;
    font-size: 0.85rem !important;
}
[data-testid="stSidebar"] .stTextInput > div > div:focus-within {
    border-color: var(--g1) !important;
}
[data-testid="stSidebar"] input { color: var(--text) !important; font-size:0.85rem !important; }
[data-testid="stSidebar"] input::placeholder { color: var(--muted) !important; }
</style>

<!-- floating clovers -->
<div class="clover-bg"></div>
<span class="clover-float" style="left:5%;  animation-duration:14s; animation-delay:0s;  font-size:1rem;">🍀</span>
<span class="clover-float" style="left:18%; animation-duration:18s; animation-delay:3s;  font-size:0.8rem;">🍀</span>
<span class="clover-float" style="left:35%; animation-duration:22s; animation-delay:7s;  font-size:1.3rem;">🍀</span>
<span class="clover-float" style="left:55%; animation-duration:16s; animation-delay:1s;  font-size:0.7rem;">🍀</span>
<span class="clover-float" style="left:72%; animation-duration:20s; animation-delay:5s;  font-size:1.1rem;">🍀</span>
<span class="clover-float" style="left:88%; animation-duration:13s; animation-delay:9s;  font-size:0.9rem;">🍀</span>
""", unsafe_allow_html=True)


# ── helpers ────────────────────────────────────────────────────────────────────

def nx_card(icon, title, subtitle, status="pending", content=None, status_text=""):
    cls  = f"nx-card {status}"
    body = f'<div class="nx-body">{content}</div>' if content else ""
    st_t = status_text or ("● Working" if status == "active" else ("✓ Done" if status == "done" else ""))
    st.markdown(f"""
    <div class="{cls}">
        <div class="nx-head">
            <div class="nx-ico">{icon}</div>
            <div>
                <div class="nx-ttl">{title}</div>
                <div class="nx-sub">{subtitle}</div>
            </div>
            <div class="nx-status">{st_t}</div>
        </div>
        {body}
    </div>
    """, unsafe_allow_html=True)


AGENTS = [
    ("🧭", "Supervisor",   "Plans research strategy",  "#22c55e", "rgba(34,197,94,0.12)"),
    ("🔍", "Search Agent", "Searches the web",         "#4ade80", "rgba(74,222,128,0.10)"),
    ("📖", "Reader Agent", "Scrapes URLs for content", "#10b981", "rgba(16,185,129,0.10)"),
    ("✍️", "Writer",       "Drafts research report",   "#fbbf24", "rgba(251,191,36,0.10)"),
    ("🔬", "Fact Checker", "Verifies all claims",      "#34d399", "rgba(52,211,153,0.10)"),
    ("⚖️", "Critic Agent", "Scores report quality",    "#6ee7b7", "rgba(110,231,183,0.10)"),
]


def parse_fc(text):
    cards, current = [], {}
    for line in text.strip().split('\n'):
        line = line.strip()
        if line.startswith("Claim"):
            if current: cards.append(current)
            current = {"claim":line,"verdict":"","evidence":"","type":"partial"}
        elif line.startswith("Verdict:"):
            current["verdict"] = line
            current["type"] = "verified" if "✅" in line else ("false" if "❌" in line else "partial")
        elif line.startswith("Evidence:"):
            current["evidence"] = line.replace("Evidence:","").strip()
        elif line.startswith("Overall"):
            if current: cards.append(current)
            current = {}
            cards.append({"claim":line,"verdict":"","evidence":"","type":"overall"})
    if current and current.get("claim"): cards.append(current)
    return cards


def parse_score(text):
    for line in text.split('\n'):
        if line.strip().startswith("Score:"):
            return line.replace("Score:","").strip()
    return "—"


def section(label, icon="🍀"):
    st.markdown(f"""
    <div class="nx-label">
        <span class="nx-label-icon">{icon}</span>
        {label}
    </div>""", unsafe_allow_html=True)


# ── API KEYS — inline on main page (works on mobile too) ──────────────────────
st.markdown("""
<div style='background:#0d1a0f; border:1px solid #1a3a1c; border-radius:14px;
            padding:1.25rem 1.5rem; margin: 0 auto 1.5rem; max-width:600px;'>
    <div style='font-family:Space Mono,monospace; font-size:0.65rem;
                letter-spacing:0.2em; color:#4ade80; text-transform:uppercase;
                margin-bottom:1rem;'>🔑 API Keys Required</div>
    <div style='font-size:0.78rem; color:#4ade80; line-height:1.8;'>
        Get free keys at:
        <a href='https://console.groq.com' target='_blank' style='color:#22c55e;'>console.groq.com</a>
        &nbsp;and&nbsp;
        <a href='https://tavily.com' target='_blank' style='color:#22c55e;'>tavily.com</a>
        <br>
        <span style='color:#365314; font-size:0.72rem;'>
            Your keys are never stored — used only for this session.
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

_, keycol, _ = st.columns([1, 5, 1])
with keycol:
    groq_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="🔑  Groq API Key — gsk_...",
        label_visibility="collapsed"
    )
    tavily_key = st.text_input(
        "Tavily API Key",
        type="password",
        placeholder="🔑  Tavily API Key — tvly-...",
        label_visibility="collapsed"
    )

keys_ready = bool(groq_key.strip() and tavily_key.strip())

# ── HERO ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="hero-glow"></div>
    <div class="hero-vines"></div>
    <span class="hero-clover">🍀</span>
    <div class="hero-eyebrow">
        <span class="live-dot"></span>
        Multi Agent Orchestration & Retrieval Framework
    </div>
    <div class="hero-title">Research Core</div>
    <div class="hero-sub">Six autonomous AI agents that search, read, verify and write research reports</div>
    <div class="hero-divider">🍀 &nbsp; 🍀 &nbsp; 🍀</div>
</div>
""", unsafe_allow_html=True)


# ── INPUT ──────────────────────────────────────────────────────────────────────
_, col, _ = st.columns([1, 5, 1])
with col:
    with st.form(key="research_form"):
        topic = st.text_input(
            "Research Topic",
            placeholder="🍀  Enter a research topic — e.g. impact of AI on healthcare...",
            label_visibility="collapsed",
            key="topic_input",
            disabled=not keys_ready
        )
        run_btn = st.form_submit_button(
            "🍀  Run Research Pipeline" if keys_ready else "⚠️  Enter API Keys in Sidebar First",
            use_container_width=True,
            disabled=not keys_ready
        )


# ── SESSION STATE INIT ─────────────────────────────────────────────────────────
if "results" not in st.session_state:
    st.session_state.results = None
if "report_md" not in st.session_state:
    st.session_state.report_md = None
if "result_topic" not in st.session_state:
    st.session_state.result_topic = None

# ── PIPELINE ───────────────────────────────────────────────────────────────────
if run_btn and topic.strip():

    # check keys entered
    if not groq_key.strip() or not tavily_key.strip():
        st.warning("⚠️ Please enter your Groq and Tavily API keys in the sidebar first.")
        st.stop()

    # set keys in environment for this session
    os.environ["GROQ_API_KEY"]   = groq_key.strip()
    os.environ["TAVILY_API_KEY"] = tavily_key.strip()

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        from agents import (build_search_agent, build_reader_agent,
                            build_fact_checker_agent,
                            get_writer_chain, get_critic_chain, get_fact_checker_chain)
        from supervisor import run_supervisor
    except ImportError as e:
        st.error(f"Import error: {e}. Make sure agents.py, supervisor.py and tools.py are in the same folder.")
        st.stop()

    # build chains at runtime so they use the user's API key
    writer_chain       = get_writer_chain()
    critic_chain       = get_critic_chain()
    fact_checker_chain = get_fact_checker_chain()

    state = {}
    section("Pipeline Execution")
    ph = [st.empty() for _ in range(6)]

    # 0 — supervisor
    with ph[0]: nx_card("🧭","Supervisor Agent","Planning research strategy","active")
    with st.spinner("🧭 Supervisor planning research strategy..."):
        sup = run_supervisor(topic)
    state["plan"] = sup["plan"]; state["queries"] = sup["queries"]
    with ph[0]: nx_card("🧭","Supervisor Agent","Research plan ready","done", state["plan"])

    # 1 — search (direct tool call — no agent overhead)
    with ph[1]: nx_card("🔍","Search Agent","Searching the web","active")
    sa = build_search_agent(); all_r = []
    for q in state["queries"]:
        with st.spinner(f"🔍 Searching: {q[:60]}..."):
            all_r.append(sa(q))
    state["search_results"] = "\n\n---\n\n".join(all_r)
    with ph[1]: nx_card("🔍","Search Agent",f"{len(state['queries'])} queries completed","done", state["search_results"])

    # 2 — reader (extract URL from results, scrape directly)
    import re
    with ph[2]: nx_card("📖","Reader Agent","Scraping top resources","active")
    ra = build_reader_agent()
    urls = re.findall(r'https?://[^\s\n<>"]+', state["search_results"])
    with st.spinner("📖 Reader agent scraping top resources..."):
        state["scraped_content"] = ra(urls[0]) if urls else "No URLs found to scrape."
    with ph[2]: nx_card("📖","Reader Agent","Content extracted","done", state["scraped_content"])

    # 3 — writer
    with ph[3]: nx_card("✍️","Writer","Drafting research report","active")
    rc = (f"SUPERVISOR PLAN:\n{state['plan'][:800]}\n\nSEARCH RESULTS:\n{state['search_results'][:2000]}\n\nDETAILED SCRAPED CONTENT:\n{state['scraped_content'][:1000]}")
    with st.spinner("✍️ Writer drafting the research report..."):
        state["report"] = writer_chain.invoke({"topic":topic,"research":rc})
    with ph[3]: nx_card("✍️","Writer","Report drafted","done","Full report available in Results ↓")

    # 4 — fact checker (direct tool call — no agent overhead)
    with ph[4]: nx_card("🔬","Fact Checker","Verifying claims","active")
    fa = build_fact_checker_agent()
    with st.spinner("🔬 Fact checker verifying claims..."):
        state["fact_check_evidence"] = fa(state["report"][:500])
        state["fact_check"] = fact_checker_chain.invoke({"report":state["report"],"evidence":state["fact_check_evidence"]})
    with ph[4]: nx_card("🔬","Fact Checker","Claims verified","done","Results available in Results ↓")

    # 5 — critic
    with ph[5]: nx_card("⚖️","Critic Agent","Reviewing report quality","active")
    with st.spinner("⚖️ Critic reviewing report quality..."):
        state["feedback"] = critic_chain.invoke({"report":state["report"]})
    sc = parse_score(state["feedback"])
    with ph[5]: nx_card("⚖️","Critic Agent","Report scored","done", state["feedback"], f"Score {sc}")

    # save to file
    os.makedirs("output", exist_ok=True)
    fname = f"output/{topic[:50].replace(' ','_')}.md"
    report_md = (
        f"# Research Report: {topic}\n\n"
        f"## Supervisor Plan\n{state['plan']}\n\n"
        f"## Report\n{state['report']}\n\n"
        f"## Fact Check\n{state['fact_check']}\n\n"
        f"## Critic Feedback\n{state['feedback']}\n"
    )
    with open(fname,"w",encoding="utf-8") as f: f.write(report_md)

    # save to session state so results persist after button clicks
    st.session_state.results  = state
    st.session_state.report_md = report_md
    st.session_state.result_topic = topic

elif run_btn and not topic.strip():
    st.warning("Please enter a research topic first.")

# ── RESULTS — shown from session state so they survive reruns ─────────────────
if st.session_state.results:
    state    = st.session_state.results
    topic_r  = st.session_state.result_topic
    report_md = st.session_state.report_md

    section("Results")
    tab1, tab2, tab3 = st.tabs(["📄  Final Report","🔬  Fact Check","⚖️  Critic Review"])

    with tab1:
        st.markdown(f"""
        <div class="nx-report">
            <div class="nx-report-title">📄 Research Report</div>
            <div class="nx-report-body">{state['report']}</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        # download as txt so anyone can open it
        st.download_button(
            "🍀  Download Report (.txt)",
            data=report_md,
            file_name=f"researchcore_{topic_r[:35].replace(' ','_')}_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )

    with tab2:
        for c in parse_fc(state["fact_check"]):
            st.markdown(f"""
            <div class="fc {c.get('type','partial')}">
                <div class="fc-claim">{c.get('claim','')}</div>
                <div class="fc-verdict">{c.get('verdict','')}</div>
                <div class="fc-evid">{c.get('evidence','')}</div>
            </div>""", unsafe_allow_html=True)

    with tab3:
        sc2 = parse_score(state["feedback"])
        st.markdown(f"""
        <div class="score-wrap">
            <div class="score-num">{sc2}</div>
            <div class="score-label">Overall<br>Report Score</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div class="nx-report">
            <div class="nx-report-title">⚖️ Critic Feedback</div>
            <div class="nx-report-body">{state['feedback']}</div>
        </div>""", unsafe_allow_html=True)

    # new research button
    st.markdown("<br>", unsafe_allow_html=True)
    _, btnc, _ = st.columns([2,2,2])
    with btnc:
        if st.button("🔄  Run New Research", key="new_research"):
            st.session_state.results = None
            st.session_state.report_md = None
            st.session_state.result_topic = None
            st.rerun()

else:
    # ── IDLE ──────────────────────────────────────────────────────────────────
    section("Your Research Agents")
    c1, c2, c3 = st.columns(3)
    cols = [c1, c2, c3, c1, c2, c3]
    for i, (icon, name, role, color, bg) in enumerate(AGENTS):
        with cols[i]:
            st.markdown(f"""
            <div class="idle-card" style="--card-glow:{bg};">
                <div class="ic-top">
                    <div class="ic-ico" style="background:{bg}; border:1px solid {color};">{icon}</div>
                    <div>
                        <div class="ic-name">{name}</div>
                        <div class="ic-role">{role}</div>
                    </div>
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="hint-box">
        🍀 &nbsp; ENTER A TOPIC ABOVE AND HIT RUN TO START THE PIPELINE &nbsp; 🍀
    </div>""", unsafe_allow_html=True)