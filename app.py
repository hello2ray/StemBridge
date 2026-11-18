
"""
StemBridge - Educational Transplant Navigation Application

Main Streamlit application.

Modules:
    journey_visuals.py
    resource_center.py
    chat_knowledge.py

Run:
    python -m streamlit run app.py

Educational prototype only.
Not a medical device or clinical decision-support system.
"""

from html import escape

import streamlit as st

from chat_knowledge import FAQ, NCI, ACS, answer
from journey_visuals import render_journey
from resource_center import render_resource_center


# ============================================================
# 1. STREAMLIT CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="StemBridge | Transplant Education",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# 2. GLOBAL CSS
# ============================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap'
);

:root {
    --teal: #067f83;
    --navy: #18354a;
    --muted: #66798a;
}

html, body, [class*="css"], .stApp {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: linear-gradient(
        120deg,
        #f5fbfc 0%,
        #f8fafc 55%,
        #f4f4ff 100%
    );
    color: #18354a;
}

.block-container {
    max-width: 1160px;
    padding-top: 1.7rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    font-family: 'Outfit', sans-serif !important;
    color: #18354a !important;
    letter-spacing: -.025em;
}

h1 {
    font-weight: 800 !important;
}

h3 {
    font-weight: 700 !important;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background: linear-gradient(
        175deg,
        #103c51,
        #115e69 75%,
        #177f80
    );
}

[data-testid="stSidebar"] * {
    color: #f4fbff !important;
}

[data-testid="stSidebar"] button {
    background: rgba(255,255,255,.08) !important;
    border: 1px solid rgba(255,255,255,.16) !important;
    text-align: left;
}

[data-testid="stSidebar"] button:hover {
    background: rgba(255,255,255,.20) !important;
}

/* Buttons */

.stButton > button[kind="primary"],
button[data-testid="stBaseButton-primary"] {
    background: linear-gradient(
        110deg,
        #078b8e,
        #13a99d
    ) !important;
    border: 0 !important;
    color: white !important;
    box-shadow: 0 5px 15px #0b939226;
}

.stButton > button {
    border-radius: 13px !important;
    min-height: 43px;
    font-weight: 700;
    border: 1px solid #d8e8ea;
}

.stButton > button:hover {
    border-color: #0b9d9b;
}

/* Metrics */

[data-testid="stMetric"] {
    border-radius: 17px;
    background: white;
    padding: 18px;
    border: 1px solid #e6edf1;
    box-shadow: 0 8px 24px #174a5610;
}

[data-testid="stMetricValue"] {
    color: #067f83;
    font-family: 'Outfit', sans-serif;
}

/* Hero */

.hero {
    padding: 33px 34px;
    border-radius: 24px;
    background: linear-gradient(
        112deg,
        #113e53 0%,
        #096b75 65%,
        #0b9c91 100%
    );
    color: white;
    box-shadow: 0 18px 35px #0a697528;
    margin-bottom: 22px;
    position: relative;
    overflow: hidden;
}

.hero:after {
    content: '✦';
    position: absolute;
    right: 55px;
    top: -50px;
    font-size: 190px;
    opacity: .08;
}

.hero h1,
.hero h2,
.hero h3,
.hero p {
    color: white !important;
    margin: 0 0 10px;
}

.hero h1 {
    font-size: 2.6rem;
}

.hero p {
    max-width: 690px;
    line-height: 1.65;
    opacity: .92;
}

.eyebrow {
    font-size: .73rem;
    letter-spacing: .15em;
    text-transform: uppercase;
    font-weight: 800;
    margin-bottom: 9px;
}

.hero .eyebrow {
    color: #b6f6e9;
}

/* Home cards */

.tile {
    background: white;
    border: 1px solid #e4ecef;
    border-radius: 19px;
    padding: 21px;
    min-height: 135px;
    box-shadow: 0 8px 22px #123a4a0b;
    margin: 4px 0 12px;
}

.tile .symbol {
    font-size: 1.6rem;
    margin-bottom: 9px;
}

.tile h4 {
    font-family: 'Outfit', sans-serif;
    font-size: 1.12rem;
    color: #18354a;
    margin: 0 0 5px;
}

.tile p {
    color: #65798a;
    font-size: .89rem;
    line-height: 1.5;
    margin: 0;
}

[data-testid="stTabs"] button {
    font-weight: 700;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# 3. TRANSPLANT JOURNEY DATA
# ============================================================

# These summaries are passed to journey_visuals.py.
# The detailed explanations and clickable cards are
# maintained inside that module.

AUTO = [
    (
        "Diagnosis and education",
        "Learn about the diagnosis, treatment choices, "
        "and why transplantation may be considered.",
        "Ask about benefits, risks, and alternatives.",
        "Diagnosis and treatment options"
    ),
    (
        "Transplant evaluation",
        "The team reviews disease status, blood tests, "
        "infections, heart and lung function, and readiness.",
        "Ask which tests are needed.",
        "CBC, organ tests, infection screening"
    ),
    (
        "Mobilization and collection",
        "Medicines may move stem cells into the bloodstream. "
        "Cells are collected by apheresis and stored.",
        "Ask how collection works.",
        "Mobilization, apheresis, storage"
    ),
    (
        "Conditioning and hospitalization",
        "High-dose treatment prepares the body before "
        "the collected cells are returned.",
        "Discuss side effects and supportive care.",
        "Chemotherapy and monitoring"
    ),
    (
        "Day 0 and engraftment",
        "Stored stem cells are infused through an IV "
        "or central line. The team monitors blood-cell recovery.",
        "Ask about engraftment and blood counts.",
        "Infusion, ANC, platelets, hemoglobin"
    ),
    (
        "Early recovery / first 100 days",
        "Frequent follow-up checks blood counts, symptoms, "
        "organ function, and disease response.",
        "Review urgent contact instructions.",
        "Follow-up and infection monitoring"
    ),
    (
        "Long-term survivorship",
        "Long-term care may include disease surveillance, "
        "vaccines, late-effects screening, and recovery support.",
        "Ask about long-term follow-up.",
        "Survivorship and revaccination"
    )
]


ALLO = [
    (
        "Diagnosis and education",
        "Learn about the diagnosis and why "
        "a donor transplant may be recommended.",
        "Discuss benefits, risks, and alternatives.",
        "Donor transplant basics"
    ),
    (
        "Transplant evaluation",
        "The team checks disease status, organ function, "
        "infections, and transplant readiness.",
        "Ask about required tests.",
        "CBC, organ tests, infection screening"
    ),
    (
        "HLA typing and donor search",
        "HLA tissue typing helps the transplant team "
        "identify suitable donor options.",
        "Ask about donor sources and search coordination.",
        "HLA testing and donor registries"
    ),
    (
        "Donor selection and work-up",
        "The transplant center evaluates donor compatibility "
        "and health and arranges cell collection.",
        "Ask how donors are selected.",
        "Donor screening and collection"
    ),
    (
        "Conditioning and hospitalization",
        "Chemotherapy, sometimes with radiation, "
        "prepares the body for donor stem cells.",
        "Discuss conditioning and GVHD prevention.",
        "Conditioning and supportive care"
    ),
    (
        "Day 0 and engraftment",
        "Donor stem cells are infused. "
        "Blood counts and complications are monitored.",
        "Ask about engraftment and GVHD prevention.",
        "Infusion, ANC, GVHD"
    ),
    (
        "Early recovery / first 100 days",
        "The team monitors blood counts, infections, "
        "GVHD symptoms, medicines, and chimerism.",
        "Ask when to contact the transplant team.",
        "GVHD, chimerism, infection monitoring"
    ),
    (
        "Long-term recovery and survivorship",
        "Immune recovery, GVHD monitoring, disease surveillance, "
        "and revaccination may continue for a long time.",
        "Ask about vaccines and long-term follow-up.",
        "Immune recovery and survivorship"
    )
]


# ============================================================
# 4. EXAMPLE TRANSPLANT CENTERS
# ============================================================

CENTERS = [
    (
        "MD Anderson Cancer Center",
        "Houston",
        "TX",
        "https://www.mdanderson.org/"
    ),
    (
        "UT Southwestern Medical Center",
        "Dallas",
        "TX",
        "https://utswmed.org/"
    ),
    (
        "Baylor University Medical Center",
        "Dallas",
        "TX",
        "https://www.bswhealth.com/"
    ),
    (
        "Mayo Clinic",
        "Rochester",
        "MN",
        "https://www.mayoclinic.org/"
    ),
    (
        "Memorial Sloan Kettering Cancer Center",
        "New York",
        "NY",
        "https://www.mskcc.org/"
    ),
    (
        "Dana-Farber Cancer Institute",
        "Boston",
        "MA",
        "https://www.dana-farber.org/"
    ),
    (
        "Fred Hutchinson Cancer Center",
        "Seattle",
        "WA",
        "https://www.fredhutch.org/"
    ),
    (
        "City of Hope",
        "Duarte",
        "CA",
        "https://www.cityofhope.org/"
    ),
    (
        "Stanford Health Care",
        "Stanford",
        "CA",
        "https://stanfordhealthcare.org/"
    ),
    (
        "Johns Hopkins Medicine",
        "Baltimore",
        "MD",
        "https://www.hopkinsmedicine.org/"
    )
]


# ============================================================
# 5. REUSABLE UI FUNCTIONS
# ============================================================

def hero(
    title,
    subtitle,
    eyebrow="STEMBRIDGE • PATIENT EDUCATION"
):
    html = (
        '<div class="hero">'
        f'<div class="eyebrow">{escape(eyebrow)}</div>'
        f'<h1>{escape(title)}</h1>'
        f'<p>{escape(subtitle)}</p>'
        '</div>'
    )

    st.markdown(
        html,
        unsafe_allow_html=True
    )


def tile(symbol, title, body):
    html = (
        '<div class="tile">'
        f'<div class="symbol">{symbol}</div>'
        f'<h4>{escape(title)}</h4>'
        f'<p>{escape(body)}</p>'
        '</div>'
    )

    st.markdown(
        html,
        unsafe_allow_html=True
    )


def go(page_name):
    st.session_state.page = page_name
    st.rerun()


def open_resource_category(category):
    st.session_state["sb_selected_resource"] = None
    st.session_state["sb_category"] = category
    go("Resource Directory")


# ============================================================
# 6. SIDEBAR NAVIGATION
# ============================================================

PAGES = [
    "Home",
    "Transplant Journey",
    "Ask StemBridge",
    "Resource Directory",
    "Financial Help",
    "Caregiver Guide",
    "Transplant Centers",
    "Second Opinion"
]

ICONS = [
    "🏠",
    "🧭",
    "💬",
    "📚",
    "💚",
    "🤝",
    "🏥",
    "🩺"
]


st.session_state.setdefault(
    "page",
    "Home"
)

st.session_state.setdefault(
    "transplant_type",
    "Autologous (own stem cells)"
)

st.session_state.setdefault(
    "chat",
    []
)


with st.sidebar:

    st.markdown("## 💠 StemBridge")

    st.caption(
        "TRANSPLANT EDUCATION & SUPPORT"
    )

    st.divider()

    for page_name, icon in zip(PAGES, ICONS):

        if st.button(
            f"{icon}  {page_name}",
            key=f"nav_{page_name}",
            use_container_width=True,
            type=(
                "primary"
                if st.session_state.page == page_name
                else "secondary"
            )
        ):
            go(page_name)

    st.divider()

    st.caption(
        "Standalone educational prototype. "
        "No accounts, medical records, "
        "or patient tracking."
    )

    st.caption(
        "Clinical review required before public use."
    )


# ============================================================
# 7. MAIN PAGE ROUTING
# ============================================================

page = st.session_state.page


# ============================================================
# HOME
# ============================================================

if page == "Home":

    hero(
        "Understand the transplant journey",
        "Explore blood stem cell transplantation, "
        "find support resources, and prepare questions "
        "for your care team.",
        "WELCOME TO STEMBRIDGE"
    )

    st.info(
        "StemBridge provides general education only. "
        "Your transplant team determines which care, "
        "tests, medicines, and schedule are appropriate."
    )

    st.subheader(
        "Explore the Two Transplant Types"
    )

    left, right = st.columns(2)

    with left:

        tile(
            "🧬",
            "Autologous Transplant",
            "Uses the patient's own collected stem cells. "
            "Explore seven educational stages."
        )

    with right:

        tile(
            "🤲",
            "Allogeneic Transplant",
            "Uses donor stem cells. Explore eight stages, "
            "including HLA matching and donor work-up."
        )

    st.selectbox(
        "Choose a transplant type",
        [
            "Autologous (own stem cells)",
            "Allogeneic (donor stem cells)"
        ],
        key="transplant_type"
    )

    if st.button(
        "Explore Transplant Journey →",
        type="primary"
    ):
        go("Transplant Journey")

    st.divider()

    st.subheader(
        "How StemBridge Can Help"
    )

    features = [
        (
            "🧭",
            "Interactive Journey",
            "Explore transplant stages using clickable "
            "cards and educational explanations."
        ),
        (
            "💬",
            "Ask StemBridge",
            "Find curated answers to common "
            "transplant questions."
        ),
        (
            "🌿",
            "Resource Navigation",
            "Find donor registries, education, "
            "financial assistance, and support."
        ),
        (
            "💚",
            "Financial Help",
            "Learn what to ask about insurance, "
            "travel, lodging, and assistance."
        ),
        (
            "🤝",
            "Caregiver Guide",
            "Explore practical information "
            "for families and caregivers."
        ),
        (
            "🏥",
            "Transplant Centers",
            "Explore center information and "
            "prepare for specialist consultations."
        )
    ]

    for start in range(0, len(features), 3):

        cols = st.columns(3)

        for col, feature in zip(
            cols,
            features[start:start + 3]
        ):

            with col:
                tile(*feature)

    st.divider()

    st.subheader(
        "Explore Support Resources"
    )

    st.write(
        "The Resource Navigation Center brings "
        "six types of support into one place."
    )

    resource_col1, resource_col2, resource_col3 = (
        st.columns(3)
    )

    with resource_col1:

        if st.button(
            "🧬 Donor Registries",
            use_container_width=True
        ):
            open_resource_category(
                "Donor Registries"
            )

        if st.button(
            "💚 Financial Help",
            use_container_width=True
        ):
            open_resource_category(
                "Financial Help"
            )

    with resource_col2:

        if st.button(
            "📚 Education",
            use_container_width=True
        ):
            open_resource_category(
                "Education"
            )

        if st.button(
            "🤝 Caregiver Support",
            use_container_width=True
        ):
            open_resource_category(
                "Caregiver Support"
            )

    with resource_col3:

        if st.button(
            "🏥 Transplant Centers",
            use_container_width=True
        ):
            open_resource_category(
                "Transplant Centers"
            )

        if st.button(
            "🩺 Second Opinions",
            use_container_width=True
        ):
            open_resource_category(
                "Second Opinions"
            )

    if st.button(
        "Open Resource Navigation Center →",
        type="primary",
        use_container_width=True
    ):
        go("Resource Directory")


# ============================================================
# TRANSPLANT JOURNEY
# ============================================================

elif page == "Transplant Journey":

    hero(
        "Interactive Transplant Journey",
        "Explore each transplant stage, understand "
        "what happens, and prepare questions "
        "for your transplant team.",
        "INTERACTIVE EDUCATIONAL JOURNEY"
    )

    transplant_type = st.selectbox(
        "Select Transplant Type",
        [
            "Autologous (own stem cells)",
            "Allogeneic (donor stem cells)"
        ],
        key="transplant_type"
    )

    is_allo = transplant_type.startswith(
        "Allogeneic"
    )

    phases = ALLO if is_allo else AUTO

    if is_allo:

        st.info(
            "Allogeneic transplantation uses donor "
            "stem cells. HLA matching, donor selection, "
            "GVHD prevention, and immune recovery "
            "are important topics."
        )

    else:

        st.info(
            "Autologous transplantation uses the "
            "patient's own collected stem cells. "
            "It does not require a donor search."
        )

    # Interactive journey from journey_visuals.py
    render_journey(
        phases,
        is_allo
    )

    st.divider()

    st.warning(
        "Contact the transplant team promptly for "
        "concerning symptoms, including fever at the "
        "threshold they provided. For life-threatening "
        "symptoms, call emergency services. "
        "Do not use this educational guide for triage."
    )


# ============================================================
# ASK STEMBRIDGE
# ============================================================

elif page == "Ask StemBridge":

    hero(
        "Ask StemBridge",
        "Simple educational answers about "
        "blood stem cell transplantation.",
        "CURATED FAQ • NOT MEDICAL ADVICE"
    )

    st.info(
        "This is a keyword-based educational FAQ, "
        "not a generative AI model. Do not enter "
        "names, medical records, or other private "
        "information. It cannot diagnose symptoms "
        "or make treatment decisions."
    )

    with st.expander(
        "Suggested Questions",
        expanded=not bool(st.session_state.chat)
    ):

        for i, item in enumerate(FAQ):

            if st.button(
                item[0],
                key=f"faq_{i}",
                use_container_width=True
            ):

                response, sources = answer(
                    item[0]
                )

                st.session_state.chat.extend([
                    (
                        "user",
                        item[0],
                        []
                    ),
                    (
                        "assistant",
                        response,
                        sources
                    )
                ])

                st.rerun()

    for role, message, sources in (
        st.session_state.chat
    ):

        with st.chat_message(role):

            st.write(message)

            for label, url in sources:

                st.markdown(
                    f"[{label} source]({url})"
                )

    prompt = st.chat_input(
        "Ask a general transplant question..."
    )

    if prompt:

        response, sources = answer(prompt)

        st.session_state.chat.extend([
            (
                "user",
                prompt,
                []
            ),
            (
                "assistant",
                response,
                sources
            )
        ])

        st.rerun()

    if st.session_state.chat:

        if st.button("Clear Conversation"):

            st.session_state.chat = []

            st.rerun()

    st.divider()

    st.markdown("### Trusted Educational Sources")

    source_col1, source_col2 = st.columns(2)

    with source_col1:

        st.link_button(
            "National Cancer Institute ↗",
            NCI,
            use_container_width=True
        )

    with source_col2:

        st.link_button(
            "American Cancer Society ↗",
            ACS,
            use_container_width=True
        )


# ============================================================
# RESOURCE NAVIGATION CENTER
# ============================================================

elif page == "Resource Directory":

    # All six categories, filters, bookmarks,
    # guided finder, details, notes, and checklists
    # are rendered by resource_center.py.

    render_resource_center()


# ============================================================
# FINANCIAL HELP
# ============================================================

elif page == "Financial Help":

    hero(
        "Financial Resource Navigator",
        "Understand possible transplant-related costs "
        "and discover organizations that may provide "
        "financial or practical support.",
        "FINANCIAL EDUCATION"
    )

    st.info(
        "Financial assistance varies by diagnosis, "
        "insurance, location, program funding, "
        "and eligibility. StemBridge does not "
        "submit applications or guarantee assistance."
    )

    st.subheader(
        "Questions to Ask a Financial Counselor"
    )

    financial_questions = [
        "What does my insurance cover, including "
        "evaluation and follow-up?",

        "Do I need prior authorization "
        "or a referral?",

        "What travel, lodging, or caregiver "
        "costs should I plan for?",

        "Are there grants or assistance "
        "programs I may qualify for?",

        "Who can help with appeals "
        "or denied insurance claims?"
    ]

    for question in financial_questions:

        st.markdown(f"- {question}")

    st.divider()

    st.subheader(
        "Explore Financial Support Organizations"
    )

    st.write(
        "The Resource Navigation Center includes "
        "financial support organizations with "
        "descriptions, preparation checklists, "
        "questions, and official website links."
    )

    if st.button(
        "Explore Financial Resources →",
        type="primary",
        use_container_width=True
    ):

        open_resource_category(
            "Financial Help"
        )

    st.caption(
        "Check each organization's website "
        "for current eligibility and availability."
    )


# ============================================================
# CAREGIVER GUIDE
# ============================================================

elif page == "Caregiver Guide":

    hero(
        "Caregiver Guide",
        "Practical educational information for "
        "family members and caregivers supporting "
        "a transplant patient.",
        "CARE AND FAMILY SUPPORT"
    )

    st.info(
        "Caregiver responsibilities vary by patient "
        "and transplant center. Follow instructions "
        "provided by the patient's clinical team."
    )

    caregiver_sections = [

        (
            "Before Transplant",
            [
                "Ask the center what help is expected "
                "from a caregiver.",

                "Plan transportation, temporary housing, "
                "and time away from work.",

                "Learn infection-prevention guidance "
                "and emergency contact procedures.",

                "Discuss backup caregiving arrangements."
            ]
        ),

        (
            "During Treatment",
            [
                "Follow the transplant center's "
                "visitor and hygiene instructions.",

                "Help communicate questions to "
                "the care team when requested.",

                "Ask about food, hydration, "
                "and activity guidance.",

                "Support practical daily needs."
            ]
        ),

        (
            "After Discharge",
            [
                "Review discharge instructions "
                "with the transplant team.",

                "Understand which symptoms require "
                "immediate medical contact.",

                "Help organize appointments "
                "and transportation.",

                "Do not change medicines or "
                "interpret test results independently."
            ]
        ),

        (
            "Supporting the Caregiver",
            [
                "Arrange backup caregivers "
                "or respite support.",

                "Discuss emotional and practical "
                "concerns with a social worker.",

                "Explore counseling and peer support.",

                "Plan time for rest and personal needs."
            ]
        )
    ]

    st.subheader(
        "Caregiver Preparation Guide"
    )

    for title, items in caregiver_sections:

        with st.expander(
            title,
            expanded=(title == "Before Transplant")
        ):

            for item in items:

                st.markdown(f"- {item}")

    st.divider()

    st.subheader(
        "Find Caregiver Support"
    )

    st.write(
        "Explore caregiver education, support "
        "organizations, and questions to prepare."
    )

    if st.button(
        "Explore Caregiver Resources →",
        type="primary",
        use_container_width=True
    ):

        open_resource_category(
            "Caregiver Support"
        )


# ============================================================
# TRANSPLANT CENTERS
# ============================================================

elif page == "Transplant Centers":

    hero(
        "Find a Transplant Center",
        "Explore example transplant programs "
        "and use official directories to confirm "
        "available services.",
        "TRANSPLANT CENTER EDUCATION"
    )

    st.warning(
        "This is an illustrative list, not a "
        "complete or verified current directory. "
        "Confirm transplant services, referrals, "
        "insurance, and availability directly "
        "with each center."
    )

    search = st.text_input(
        "Search by Center, City, or State",
        placeholder="Example: Dallas, Houston, Mayo"
    )

    search_text = search.strip().casefold()

    matching_centers = [
        center
        for center in CENTERS
        if search_text in (
            " ".join(center[:3]).casefold()
        )
    ]

    st.caption(
        f"{len(matching_centers)} centers found"
    )

    for start in range(
        0,
        len(matching_centers),
        2
    ):

        columns = st.columns(2)

        for col, center in zip(
            columns,
            matching_centers[start:start + 2]
        ):

            name, city, state, url = center

            with col:

                with st.container(border=True):

                    st.markdown(
                        f"### 🏥 {name}"
                    )

                    st.caption(
                        f"📍 {city}, {state}"
                    )

                    st.link_button(
                        "Visit Official Website ↗",
                        url,
                        use_container_width=True
                    )

    if not matching_centers:

        st.info(
            "No centers in the example list "
            "match your search. Try an official "
            "national directory."
        )

    st.divider()

    st.subheader(
        "Official Center Directories"
    )

    st.link_button(
        "NCI Cancer Centers ↗",
        "https://www.cancer.gov/research/"
        "infrastructure/cancer-centers/find"
    )

    st.link_button(
        "NMDP Patient Resources ↗",
        "https://www.nmdp.org/patients"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Explore Center Resources →",
            use_container_width=True
        ):

            open_resource_category(
                "Transplant Centers"
            )

    with col2:

        if st.button(
            "How to Get a Second Opinion →",
            type="primary",
            use_container_width=True
        ):

            go("Second Opinion")


# ============================================================
# SECOND OPINION
# ============================================================

elif page == "Second Opinion":

    hero(
        "Getting a Second Opinion",
        "Learn how another transplant specialist "
        "may help you understand treatment options "
        "and prepare for an informed discussion.",
        "SECOND OPINION EDUCATION"
    )

    st.info(
        "StemBridge does not schedule appointments, "
        "transmit medical records, or provide "
        "medical recommendations."
    )

    second_opinion_steps = [

        (
            "Talk With Your Current Care Team",
            "Ask whether another specialist can review "
            "the treatment recommendation and how "
            "urgent the decision is."
        ),

        (
            "Find Another Transplant Program",
            "Use transplant center directories and "
            "confirm that the center evaluates your "
            "condition and transplant type."
        ),

        (
            "Ask Which Records Are Needed",
            "The receiving center may request "
            "pathology, treatment history, imaging, "
            "blood tests, and HLA results. "
            "Share records through secure channels."
        ),

        (
            "Check Insurance and Scheduling",
            "Ask about referrals, authorization, "
            "consultation costs, and appointment timing."
        ),

        (
            "Compare Recommendations",
            "Discuss the benefits, risks, alternatives, "
            "donor options when relevant, and next steps "
            "with your treating clinicians."
        )
    ]

    st.subheader(
        "Steps to Request a Second Opinion"
    )

    for index, (title, description) in enumerate(
        second_opinion_steps,
        start=1
    ):

        with st.expander(
            f"{index}. {title}",
            expanded=(index == 1)
        ):

            st.write(description)

    st.divider()

    st.subheader(
        "Questions for the Second Specialist"
    )

    questions = [
        "Do you agree with the recommended "
        "transplant type and timing?",

        "What are the main benefits, risks, "
        "and alternatives?",

        "What experience does your program "
        "have with this condition?",

        "For an allogeneic transplant, "
        "what donor options would you consider?",

        "What support is available for caregivers, "
        "housing, and costs?"
    ]

    for question in questions:

        st.markdown(f"- {question}")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Browse Transplant Centers →",
            use_container_width=True
        ):

            go("Transplant Centers")

    with col2:

        if st.button(
            "Explore Second Opinion Resources →",
            type="primary",
            use_container_width=True
        ):

            open_resource_category(
                "Second Opinions"
            )

    st.warning(
        "Do not delay urgent treatment without "
        "discussing the timing with your clinical team."
    )


# ============================================================
# 8. FOOTER
# ============================================================

st.divider()

st.caption(
    "StemBridge • Educational Prototype • "
    "No real patient data, donor matching, "
    "medical advice, financial applications, "
    "or hospital integration. "
    "Clinical review required before publication."
)
