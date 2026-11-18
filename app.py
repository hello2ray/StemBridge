
"""StemBridge - responsive educational transplant companion."""

from html import escape
import streamlit as st

from chat_knowledge import FAQ, NCI, ACS, answer
from journey_visuals import render_journey
from resource_center import render_resource_center
from mobile_styles import apply_mobile_styles

st.set_page_config(
    page_title="StemBridge | Transplant Education",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="auto",
)

apply_mobile_styles()

st.markdown("""
<style>
.stApp {
    background: linear-gradient(120deg,#f5fbfc,#f8fafc 55%,#f4f4ff);
}
.block-container {
    max-width:1160px;
}
h1,h2,h3 {
    color:#18354a;
    letter-spacing:-.025em;
}
[data-testid="stSidebar"] {
    background:linear-gradient(175deg,#103c51,#115e69 75%,#177f80);
}
[data-testid="stSidebar"] * {
    color:#f4fbff !important;
}
[data-testid="stSidebar"] button {
    background:rgba(255,255,255,.08) !important;
    border:1px solid rgba(255,255,255,.16) !important;
}
[data-testid="stSidebar"] button:hover {
    background:rgba(255,255,255,.20) !important;
}
.sb-home-hero {
    padding:32px;
    border-radius:24px;
    background:linear-gradient(110deg,#123e53,#087e83);
    margin-bottom:20px;
    color:white;
}
.sb-home-hero h1 {
    color:white !important;
    margin:0 0 10px;
    font-size:clamp(1.65rem,4vw,2.5rem);
}
.sb-home-hero p {
    color:#e3f7f4;
    line-height:1.6;
    margin:0;
}
.sb-eyebrow {
    font-size:.75rem;
    letter-spacing:.12em;
    font-weight:800;
    color:#b8f5e9;
    margin-bottom:10px;
}
.sb-tile {
    background:#fff;
    border:1px solid #e0ebed;
    border-radius:18px;
    padding:20px;
    min-height:145px;
    margin-bottom:10px;
    box-shadow:0 5px 16px rgba(20,70,80,.05);
}
.sb-tile-icon {
    font-size:30px;
    margin-bottom:8px;
}
.sb-tile-title {
    font-size:1.05rem;
    font-weight:750;
    color:#18354a;
    margin-bottom:6px;
}
.sb-tile-text {
    font-size:.88rem;
    color:#58717f;
    line-height:1.5;
}
.sb-section {
    margin:18px 0 12px;
}
@media(max-width:767px) {
    .sb-home-hero {
        padding:20px 17px;
        border-radius:17px;
    }
    .sb-tile {
        padding:15px;
        min-height:125px;
    }
    .sb-tile-icon {
        font-size:26px;
    }
    .sb-tile-title {
        font-size:.95rem;
    }
    .sb-tile-text {
        font-size:.8rem;
    }
}
</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# Transplant education data
# ------------------------------------------------------------

AUTO = [
    (
        "Diagnosis and education",
        "Learn about the diagnosis, treatment choices, and why transplant may be considered.",
        "Ask about treatment goals, alternatives, benefits, and risks.",
        "Diagnosis, treatment options, support needs",
    ),
    (
        "Transplant evaluation",
        "The team reviews disease status, blood tests, infections, heart and lung function, and readiness.",
        "Ask which tests are needed and what each one checks.",
        "CBC, organ tests, infection screening, ECG, echo, lung tests",
    ),
    (
        "Mobilization and collection",
        "Medicines may move stem cells into the bloodstream. Cells are collected by apheresis and stored.",
        "Ask how collection works and whether a central line is needed.",
        "Mobilization medicines, apheresis, cell storage",
    ),
    (
        "Conditioning and hospitalization",
        "High-dose treatment prepares the body before collected cells are returned.",
        "Discuss side effects, infection precautions, and caregiver support.",
        "Chemotherapy, supportive care, inpatient or outpatient care",
    ),
    (
        "Day 0 and engraftment",
        "Stored stem cells are infused. The team monitors blood-cell recovery.",
        "Ask about blood counts, transfusions, and infection risks.",
        "Infusion, ANC, platelets, hemoglobin",
    ),
    (
        "Early recovery / first 100 days",
        "Follow-up checks blood counts, symptoms, organ function, and disease response.",
        "Know the transplant center's urgent contact instructions.",
        "Follow-up visits, medicines, infection monitoring",
    ),
    (
        "Long-term survivorship",
        "Long-term care may include disease surveillance, vaccines, and late-effects screening.",
        "Ask about follow-up frequency and return to daily activities.",
        "Survivorship, revaccination, late effects",
    ),
]

ALLO = [
    (
        "Diagnosis and education",
        "Learn about the diagnosis and why donor transplant may be recommended.",
        "Discuss benefits, risks, alternatives, and caregiver needs.",
        "Donor transplant basics, treatment choices",
    ),
    (
        "Transplant evaluation",
        "The team checks disease status, organ function, infections, and transplant readiness.",
        "Ask about required tests and practical arrangements.",
        "CBC, organ tests, infection screening",
    ),
    (
        "HLA typing and donor search",
        "HLA tissue typing helps the team identify suitable donor options.",
        "Ask who manages the search and which donor sources are possible.",
        "HLA typing, family donors, registries, cord blood",
    ),
    (
        "Donor selection and work-up",
        "The transplant center evaluates donor compatibility and health.",
        "Ask how the donor is selected and how cells will be collected.",
        "Confirmatory typing, screening, collection",
    ),
    (
        "Conditioning and hospitalization",
        "Chemotherapy, sometimes with radiation, prepares the body for donor stem cells.",
        "Discuss side effects and GVHD prevention.",
        "Conditioning, supportive care, GVHD prevention",
    ),
    (
        "Day 0 and engraftment",
        "Donor stem cells are infused and blood counts are monitored.",
        "Ask about engraftment, GVHD prevention, and complications.",
        "Infusion, ANC, platelets, GVHD",
    ),
    (
        "Early recovery / first 100 days",
        "The team monitors blood counts, infections, GVHD, medicines, and chimerism.",
        "Ask when to call the care team and how follow-up is managed.",
        "GVHD, chimerism, immunosuppression",
    ),
    (
        "Long-term recovery and survivorship",
        "Immune recovery, GVHD monitoring, disease surveillance, and revaccination may continue.",
        "Ask about vaccines, late effects, and long-term follow-up.",
        "Immune recovery, chronic GVHD, survivorship",
    ),
]


FINANCIAL = [
    ("NMDP Patient Support", "Transplant support and financial resource information",
     "https://www.nmdp.org/patients"),
    ("Blood Cancer United", "Blood cancer support and assistance information",
     "https://www.bloodcancerunited.org"),
    ("Patient Advocate Foundation", "Insurance and financial access support",
     "https://www.patientadvocate.org/"),
    ("CancerCare", "Cancer support and financial assistance information",
     "https://www.cancercare.org/"),
    ("HealthWell Foundation", "Financial assistance information",
     "https://www.healthwellfoundation.org/"),
    ("National Cancer Institute", "Support services and paying for care",
     "https://www.cancer.gov/about-cancer/managing-care"),
]

CENTERS = [
    ("MD Anderson Cancer Center", "Houston", "TX", "https://www.mdanderson.org/"),
    ("UT Southwestern Medical Center", "Dallas", "TX", "https://utswmed.org/"),
    ("Baylor University Medical Center", "Dallas", "TX", "https://www.bswhealth.com/"),
    ("Mayo Clinic", "Rochester", "MN", "https://www.mayoclinic.org/"),
    ("Memorial Sloan Kettering Cancer Center", "New York", "NY", "https://www.mskcc.org/"),
    ("Dana-Farber Cancer Institute", "Boston", "MA", "https://www.dana-farber.org/"),
    ("Fred Hutchinson Cancer Center", "Seattle", "WA", "https://www.fredhutch.org/"),
    ("City of Hope", "Duarte", "CA", "https://www.cityofhope.org/"),
    ("Stanford Health Care", "Stanford", "CA", "https://stanfordhealthcare.org/"),
    ("Johns Hopkins Medicine", "Baltimore", "MD", "https://www.hopkinsmedicine.org/"),
]


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

PAGES = [
    "Home",
    "Transplant Journey",
    "Ask StemBridge",
    "Resource Directory",
    "Financial Help",
    "Caregiver Guide",
    "Transplant Centers",
    "Second Opinion",
]

ICONS = [
    "🏠", "🧭", "💬", "📚",
    "💚", "🤝", "🏥", "🩺",
]


def hero(title, subtitle, eyebrow="STEMBRIDGE • PATIENT EDUCATION"):
    st.markdown(
        '<div class="sb-home-hero">'
        f'<div class="sb-eyebrow">{escape(eyebrow)}</div>'
        f'<h1>{escape(title)}</h1>'
        f'<p>{escape(subtitle)}</p>'
        '</div>',
        unsafe_allow_html=True,
    )


def tile(icon, title, description):
    st.markdown(
        '<div class="sb-tile">'
        f'<div class="sb-tile-icon">{icon}</div>'
        f'<div class="sb-tile-title">{escape(title)}</div>'
        f'<div class="sb-tile-text">{escape(description)}</div>'
        '</div>',
        unsafe_allow_html=True,
    )


def resource_links(items):
    for name, description, url in items:
        with st.container(border=True):
            st.markdown(f"**{name}**")
            st.caption(description)
            st.link_button(
                "Open official website ↗",
                url,
                use_container_width=True,
            )


def go(page):
    st.session_state.page = page
    st.rerun()


def go_resource(category):
    st.session_state["sb_category"] = category
    st.session_state["sb_selected_resource"] = None
    go("Resource Directory")


# ------------------------------------------------------------
# Session state
# ------------------------------------------------------------

st.session_state.setdefault("page", "Home")
st.session_state.setdefault(
    "transplant_type",
    "Autologous (own stem cells)",
)
st.session_state.setdefault("chat", [])


# ------------------------------------------------------------
# Sidebar navigation
# ------------------------------------------------------------

with st.sidebar:
    st.markdown("## 💠 StemBridge")
    st.caption("TRANSPLANT EDUCATION & SUPPORT")
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
            ),
        ):
            go(page_name)

    st.divider()
    st.caption(
        "Educational prototype. No patient records "
        "or clinical decision-making."
    )


# ------------------------------------------------------------
# Main pages
# ------------------------------------------------------------

page = st.session_state.page


if page == "Home":

    hero(
        "Understand the transplant journey",
        "Explore transplant stages, trusted resources, "
        "and support for patients and caregivers.",
        "WELCOME TO STEMBRIDGE",
    )

    st.info(
        "General education only. Your transplant team "
        "determines your care and treatment plan."
    )

    st.subheader("Choose your transplant journey")

    col1, col2 = st.columns(2)

    with col1:
        tile(
            "🧬",
            "Autologous transplant",
            "Uses the patient's own stem cells.",
        )

    with col2:
        tile(
            "🤝",
            "Allogeneic transplant",
            "Uses donor stem cells.",
        )

    st.selectbox(
        "Transplant type",
        [
            "Autologous (own stem cells)",
            "Allogeneic (donor stem cells)",
        ],
        key="transplant_type",
    )

    if st.button(
        "🧭 Explore transplant journey →",
        type="primary",
        use_container_width=True,
    ):
        go("Transplant Journey")

    st.markdown("### Explore StemBridge")

    features = [
        ("🧭", "Journey Guide", "Explore treatment stages.", "Transplant Journey"),
        ("💬", "Ask StemBridge", "Educational questions.", "Ask StemBridge"),
        ("📚", "Resource Center", "Find trusted organizations.", "Resource Directory"),
        ("💚", "Financial Help", "Explore support options.", "Financial Help"),
        ("🤝", "Caregiver Guide", "Support family and caregivers.", "Caregiver Guide"),
        ("🏥", "Transplant Centers", "Explore transplant programs.", "Transplant Centers"),
        ("🩺", "Second Opinion", "Prepare for another consultation.", "Second Opinion"),
    ]

    for start in range(0, len(features), 2):
        columns = st.columns(2, gap="medium")

        for col, feature in zip(columns, features[start:start + 2]):
            icon, name, description, target = feature

            with col:
                tile(icon, name, description)

                if st.button(
                    f"Open {name} →",
                    key=f"home_{target}",
                    use_container_width=True,
                ):
                    go(target)


elif page == "Transplant Journey":

    hero(
        "Your Transplant Journey",
        "Explore each stage visually, with concise "
        "information and questions for your care team.",
        "VISUAL EDUCATION GUIDE",
    )

    transplant_type = st.selectbox(
        "Select transplant type",
        [
            "Autologous (own stem cells)",
            "Allogeneic (donor stem cells)",
        ],
        key="transplant_type",
    )

    is_allo = transplant_type.startswith("Allogeneic")
    phases = ALLO if is_allo else AUTO

    render_journey(phases, is_allo)

    with st.expander("🩺 Important medical information"):
        st.write(
            "Day 0 is the stem cell infusion day. "
            "Engraftment means transplanted cells begin "
            "producing new blood cells. It is not the "
            "same as disease remission."
        )

        if is_allo:
            st.write(
                "After donor transplantation, care teams "
                "also monitor GVHD, chimerism, immune "
                "recovery, and immunosuppression."
            )

    st.warning(
        "For fever, bleeding, or other concerning symptoms, "
        "follow your transplant team's urgent-contact plan. "
        "For life-threatening symptoms, call emergency services."
    )


elif page == "Ask StemBridge":

    hero(
        "Ask StemBridge",
        "Get concise educational answers about stem cell transplantation.",
        "CURATED EDUCATIONAL FAQ",
    )

    st.info(
        "This is a keyword-based educational chatbot, "
        "not a medical diagnosis service. "
        "Do not enter private health information."
    )

    with st.expander(
        "💡 Suggested questions",
        expanded=not bool(st.session_state.chat),
    ):
        for i, item in enumerate(FAQ):
            question = item[0]

            if st.button(
                question,
                key=f"faq_{i}",
                use_container_width=True,
            ):
                response, sources = answer(question)

                st.session_state.chat.extend([
                    ("user", question, []),
                    ("assistant", response, sources),
                ])
                st.rerun()

    for role, message, sources in st.session_state.chat:
        with st.chat_message(role):
            st.write(message)

            for label, url in sources:
                st.markdown(f"[{label} source]({url})")

    prompt = st.chat_input(
        "Ask a general transplant question..."
    )

    if prompt:
        response, sources = answer(prompt)

        st.session_state.chat.extend([
            ("user", prompt, []),
            ("assistant", response, sources),
        ])
        st.rerun()

    st.link_button("National Cancer Institute ↗", NCI)
    st.link_button("American Cancer Society ↗", ACS)


elif page == "Resource Directory":

    render_resource_center()


elif page == "Financial Help":

    hero(
        "Financial Help",
        "Explore assistance with treatment costs, "
        "insurance, transportation, and lodging.",
        "FINANCIAL RESOURCE NAVIGATOR",
    )

    st.markdown("### What do you need help with?")

    needs = [
        ("💳", "Insurance", "Coverage and prior authorization"),
        ("🚗", "Travel", "Transportation and lodging"),
        ("💚", "Financial Support", "Assistance programs and grants"),
        ("🤝", "Care Coordination", "Social workers and support teams"),
    ]

    for start in range(0, len(needs), 2):
        cols = st.columns(2)

        for col, (icon, title, description) in zip(
            cols, needs[start:start + 2]
        ):
            with col:
                tile(icon, title, description)

    with st.expander("Questions for a financial counselor"):
        st.markdown(
            "- What does my insurance cover?\n"
            "- Do I need prior authorization?\n"
            "- What travel or lodging costs should I plan for?\n"
            "- Are there assistance programs I may qualify for?"
        )

    st.markdown("### Organizations to explore")
    resource_links(FINANCIAL)

    if st.button(
        "Explore all financial resources →",
        use_container_width=True,
        type="primary",
    ):
        go_resource("Financial Help")

    st.caption(
        "Funding and eligibility change. "
        "StemBridge does not determine eligibility or submit applications."
    )


elif page == "Caregiver Guide":

    hero(
        "Caregiver Guide",
        "Simple guidance for family members "
        "supporting someone through transplant.",
        "PATIENT & FAMILY SUPPORT",
    )

    sections = [
        (
            "🧳",
            "Before Transplant",
            [
                "Understand caregiver responsibilities.",
                "Plan transportation and accommodation.",
                "Prepare important contact information.",
            ],
        ),
        (
            "🏥",
            "During Transplant",
            [
                "Follow the care team's visitor guidance.",
                "Help organize questions and appointments.",
                "Support communication with the care team.",
            ],
        ),
        (
            "🏠",
            "After Discharge",
            [
                "Understand follow-up appointments.",
                "Follow infection-prevention instructions.",
                "Know when and whom to contact.",
            ],
        ),
        (
            "💚",
            "Caregiver Well-Being",
            [
                "Arrange backup support.",
                "Take breaks and seek assistance.",
                "Ask the social worker about available services.",
            ],
        ),
    ]

    for icon, title, points in sections:
        with st.expander(f"{icon} {title}"):
            for point in points:
                st.markdown(f"- {point}")

    if st.button(
        "Explore caregiver resources →",
        type="primary",
        use_container_width=True,
    ):
        go_resource("Caregiver Support")

    st.caption(
        "Caregiver needs differ by patient and transplant center."
    )


elif page == "Transplant Centers":

    hero(
        "Transplant Centers",
        "Explore example U.S. centers and prepare "
        "questions before contacting a program.",
        "CENTER DIRECTORY",
    )

    st.warning(
        "This is an illustrative list, not a ranking "
        "or a verified current service directory. "
        "Confirm services directly with each center."
    )

    query = st.text_input(
        "Search by center, city, or state",
        placeholder="Dallas, Mayo, TX...",
    ).strip().casefold()

    matches = [
        center for center in CENTERS
        if query in " ".join(center[:3]).casefold()
    ]

    st.caption(f"{len(matches)} centers found")

    for name, city, state, url in matches:
        with st.container(border=True):
            st.markdown(f"### 🏥 {name}")
            st.caption(f"📍 {city}, {state}, USA")
            st.link_button(
                "Official center website ↗",
                url,
                use_container_width=True,
            )

    if not matches:
        st.info("No centers match your search.")

    st.markdown("### Additional directories")

    st.link_button(
        "NCI Cancer Centers ↗",
        "https://www.cancer.gov/research/infrastructure/cancer-centers/find",
    )

    st.link_button(
        "NMDP Patient Resources ↗",
        "https://www.nmdp.org/patients",
    )

    if st.button(
        "How to get a second opinion →",
        type="primary",
        use_container_width=True,
    ):
        go("Second Opinion")


elif page == "Second Opinion":

    hero(
        "Getting a Second Opinion",
        "Understand how another transplant specialist "
        "can help you explore treatment options.",
        "SECOND OPINION GUIDE",
    )

    steps = [
        (
            "💬",
            "Discuss with your doctor",
            "Ask about timing and the reason for another consultation.",
        ),
        (
            "🏥",
            "Find a specialist",
            "Identify a center experienced with your condition.",
        ),
        (
            "📄",
            "Prepare medical records",
            "Ask which records should be securely transferred.",
        ),
        (
            "💳",
            "Check insurance",
            "Confirm referrals, authorization, and consultation costs.",
        ),
        (
            "🤝",
            "Compare recommendations",
            "Review benefits, risks, alternatives, and next steps.",
        ),
    ]

    for index, (icon, title, description) in enumerate(steps, 1):
        with st.expander(f"{icon} Step {index}: {title}"):
            st.write(description)

    with st.expander("Questions for the specialist"):
        st.markdown(
            "- Do you agree with the proposed transplant type?\n"
            "- What are the main benefits and risks?\n"
            "- Are there other treatment options?\n"
            "- What experience does your center have with this condition?\n"
            "- What support is available for patients and caregivers?"
        )

    if st.button(
        "Browse transplant centers →",
        type="primary",
        use_container_width=True,
    ):
        go("Transplant Centers")

    if st.button(
        "Explore second opinion resources →",
        use_container_width=True,
    ):
        go_resource("Second Opinions")

    st.caption(
        "StemBridge does not schedule appointments or transmit medical records."
    )


st.divider()
st.caption(
    "StemBridge • Educational prototype • "
    "No real patient data, donor matching, medical advice, "
    "or hospital integration. Clinical review is required before public use."
)
