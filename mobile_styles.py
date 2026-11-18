
"""Responsive styling for the StemBridge educational Streamlit app."""

import streamlit as st

MOBILE_CSS = """
<style>
/* Shared page spacing and typography */
html {
    -webkit-text-size-adjust: 100%;
}

.stApp {
    overflow-x: hidden;
}

.block-container {
    width: 100%;
    max-width: 1160px;
    padding: 1.3rem 1.5rem 3rem;
}

.stButton > button,
.stLinkButton > a {
    min-height: 46px;
    border-radius: 13px;
    white-space: normal;
    overflow-wrap: anywhere;
    touch-action: manipulation;
}

.stTextInput input,
.stSelectbox input,
.stTextArea textarea {
    font-size: 16px !important;
}

/* Main content contrast; leave the dark sidebar intact */
[data-testid="stMain"] {
    color: #18354a;
}

[data-testid="stMain"] button[kind="secondary"] {
    background: #ffffff !important;
    color: #18354a !important;
    border: 1px solid #cbdfe4 !important;
}

[data-testid="stMain"] button[kind="secondary"] p,
[data-testid="stMain"] button[kind="secondary"] span {
    color: inherit !important;
}

[data-testid="stMain"] button[kind="primary"] {
    background: #087e83 !important;
    color: #ffffff !important;
    border: 1px solid #087e83 !important;
}

[data-testid="stMain"] button[kind="primary"] p,
[data-testid="stMain"] button[kind="primary"] span {
    color: inherit !important;
}

/* Prevent content overflow on narrow screens */
[data-testid="stMain"] img,
[data-testid="stMain"] svg {
    max-width: 100%;
}

[data-testid="stMain"] p,
[data-testid="stMain"] a {
    overflow-wrap: anywhere;
}

[data-testid="stMain"] [data-testid="stHorizontalBlock"] {
    min-width: 0;
}

/* Mobile screens */
@media (max-width: 767px) {
    .block-container {
        padding: .75rem .85rem 5rem !important;
    }

    h1 {
        font-size: 1.65rem !important;
        line-height: 1.2 !important;
    }

    h2 {
        font-size: 1.35rem !important;
    }

    h3 {
        font-size: 1.12rem !important;
    }

    .hero,
    .sb-hero {
        padding: 18px 16px !important;
        border-radius: 16px !important;
    }

    .hero h1,
    .sb-hero h2 {
        font-size: 1.55rem !important;
    }

    .stButton > button,
    .stLinkButton > a {
        min-height: 48px !important;
    }

    [data-testid="stMetric"] {
        padding: 12px !important;
    }

    /* Two-column journey stage grid */
    .st-key-journey_stage_cards [data-testid="stHorizontalBlock"] {
        display: grid !important;
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 9px !important;
    }

    .st-key-journey_stage_cards
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
        width: auto !important;
        min-width: 0 !important;
        flex: none !important;
    }

    .st-key-journey_stage_cards button {
        min-height: 102px !important;
        font-size: .83rem !important;
    }

    .jv-panel {
        padding: 16px !important;
    }

    .jv-step {
        min-height: 62px !important;
        padding: 8px 5px !important;
        font-size: .78rem !important;
    }

    .jv-arrow {
        font-size: 1rem !important;
        padding-top: 14px !important;
    }

    /* Single-column resource directory on phones */
    .st-key-sb_resource_filters [data-testid="stHorizontalBlock"],
    .st-key-sb_resource_cards [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        gap: 8px !important;
    }

    .st-key-sb_resource_filters [data-testid="stColumn"],
    .st-key-sb_resource_cards [data-testid="stColumn"] {
        width: 100% !important;
        min-width: 0 !important;
    }
}

/* Very small phones */
@media (max-width: 380px) {
    .block-container {
        padding-left: .65rem !important;
        padding-right: .65rem !important;
    }

    .st-key-journey_stage_cards button {
        font-size: .76rem !important;
    }
}
</style>
"""


def apply_mobile_styles():
    """Call immediately after st.set_page_config in app.py."""
    st.markdown(MOBILE_CSS, unsafe_allow_html=True)
