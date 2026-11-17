
import streamlit as st
from html import escape
from chat_knowledge import FAQ, NCI, ACS, answer

# --------------------------------------------------
# STREAMLIT CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="StemBridge | Transplant Education",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# EXISTING STEMBRIDGE DESIGN
# --------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap');

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
}

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

.stButton > button {
    border-radius: 13px !important;
    min-height: 43px;
    font-weight: 700;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(
        110deg,
        #078b8e,
        #13a99d
    ) !important;
    color: white !important;
    border: 0 !important;
}

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
    margin-bottom: 22px;
}

.hero h1, .hero p {
    color: white !important;
}

.hero h1 {
    font-size: 2.6rem;
}

.hero p {
    max-width: 690px;
    line-height: 1.65;
}

.eyebrow {
    font-size: .73rem;
    letter-spacing: .15em;
    text-transform: uppercase;
    font-weight: 800;
    color: #b6f6e9;
    margin-bottom: 9px;
}

.tile {
    background: white;
    border: 1px solid #e4ecef;
    border-radius: 19px;
    padding: 21px;
    min-height: 124px;
    margin: 4px 0 12px;
}

.tile .symbol {
    font-size: 1.6rem;
    margin-bottom: 9px;
}

.tile h4 {
    font-size: 1.12rem;
    color: #18354a;
    margin-bottom: 5px;
}

.tile p {
    color: #65798a;
    font-size: .89rem;
    line-height: 1.5;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# TRANSPLANT JOURNEY INFORMATION
# --------------------------------------------------

AUTO = [
    (
        "Diagnosis and Education",
        "Learn about the diagnosis, treatment options, and why a transplant may be considered.",
        "Ask about the benefits, risks, alternatives, and expected treatment plan.",
        "Diagnosis, treatment choices, education"
    ),
    (
        "Transplant Evaluation",
        "The transplant team reviews the patient's health and readiness for treatment.",
        "Ask which blood tests, heart tests, lung tests, and infection screenings are needed.",
        "CBC, kidney and liver tests, ECG, echocardiogram, lung tests"
    ),
    (
        "Mobilization and Collection",
        "Medicines may help move stem cells into the bloodstream. The patient's stem cells are collected and stored.",
        "Ask how stem cell collection works and how long it may take.",
        "Mobilization, apheresis, stem cell storage"
    ),
    (
        "Conditioning and Hospitalization",
        "High-dose chemotherapy prepares the body before the stored stem cells are returned.",
        "Ask about side effects, infection precautions, and hospital or outpatient care.",
        "Chemotherapy, supportive care, admission"
    ),
    (
        "Day 0 and Engraftment",
        "Collected stem cells are infused. The care team monitors blood counts and recovery.",
        "Ask about engraftment, blood counts, transfusions, and infection risks.",
        "Stem cell infusion, ANC, platelets, hemoglobin"
    ),
    (
        "Early Recovery",
        "The transplant team monitors recovery, infections, side effects, and disease response.",
        "Ask about follow-up visits, warning signs, and recovery instructions.",
        "First 100 days, monitoring, follow-up"
    ),
    (
        "Long-Term Recovery",
        "Long-term follow-up may include disease monitoring, vaccines, and recovery support.",
        "Ask about vaccinations, late effects, and returning to daily activities.",
        "Survivorship, vaccines, long-term monitoring"
    )
]

ALLO = [
    (
        "Diagnosis and Education",
        "Learn about the diagnosis and why a donor transplant may be recommended.",
        "Discuss benefits, risks, treatment options, and caregiver needs.",
        "Diagnosis, treatment choices"
    ),
    (
        "Transplant Evaluation",
        "The transplant team checks disease status, organ function, infections, and readiness.",
        "Ask about required tests and practical arrangements.",
        "Blood tests, heart and lung tests, infection screening"
    ),
    (
        "HLA Typing and Donor Search",
        "HLA testing helps the transplant team identify possible compatible donors.",
        "Ask about family donors, unrelated donors, cord blood, and donor-search timelines.",
        "HLA testing, donor registries, donor search"
    ),
    (
        "Donor Selection and Work-Up",
        "The transplant team evaluates donor compatibility and arranges stem cell collection.",
        "Ask how a donor is selected and how the collection process works.",
        "Confirmatory typing, donor screening, collection"
    ),
    (
        "Conditioning and Hospitalization",
        "Chemotherapy and sometimes radiation prepare the body for donor stem cells.",
        "Ask about treatment side effects, infection prevention, and GVHD prevention.",
        "Conditioning, chemotherapy, supportive care"
    ),
    (
        "Day 0 and Engraftment",
        "Donor stem cells are infused and the team monitors blood cell recovery.",
        "Ask about engraftment, blood counts, and possible complications.",
        "Infusion, ANC, platelets, GVHD prevention"
    ),
    (
        "Early Recovery",
        "The team monitors infections, GVHD, medicines, blood counts, and donor-cell chimerism.",
        "Ask about warning signs, medications, and follow-up visits.",
        "GVHD, chimerism, infection monitoring"
    ),
    (
        "Long-Term Recovery",
        "Long-term care includes immune recovery, GVHD monitoring, and disease surveillance.",
        "Ask about vaccines, late effects, and long-term follow-up.",
        "Immune recovery, chronic GVHD, survivorship"
    )
]


# --------------------------------------------------
# DONOR REGISTRIES AND SUPPORT ORGANIZATIONS
# --------------------------------------------------

DONOR_REGISTRIES = [
    (
        "NMDP – United States",
        "Stem cell donor registry, donor-search education, and patient support.",
        "https://www.nmdp.org/"
    ),
    (
        "Gift of Life Marrow Registry – United States",
        "Donor recruitment, registry information, and patient resources.",
        "https://www.giftoflife.org/"
    ),
    (
        "DKMS – International",
        "Stem cell donor recruitment, education, and support.",
        "https://www.dkms.org/"
    ),
    (
        "Anthony Nolan – United Kingdom",
        "Stem cell donor registry, patient information, and support.",
        "https://www.anthonynolan.org/"
    ),
    (
        "World Marrow Donor Association (WMDA)",
        "International donor registry network and registry information.",
        "https://wmda.info/"
    ),
    (
        "DATRI – India",
        "Blood stem cell donor registry and donor awareness.",
        "https://datri.org/"
    ),
    (
        "Canadian Blood Services – Canada",
        "Canadian stem cell donor registry and transplant information.",
        "https://www.blood.ca/en/stemcells"
    )
]

EDUCATION_RESOURCES = [
    (
        "National Cancer Institute",
        "Stem cell transplant treatment, benefits, and risks.",
        NCI
    ),
    (
        "American Cancer Society",
        "Stem cell transplant information and patient support.",
        ACS
    ),
    (
        "BMT InfoNet",
        "Education for transplant patients, survivors, and caregivers.",
        "https://www.bmtinfonet.org/"
    ),
    (
        "Leukemia & Lymphoma Society",
        "Blood cancer education and patient support.",
        "https://www.lls.org/"
    )
]

FINANCIAL = [
    (
        "NMDP Patient Support",
        "Information about transplant-related financial and practical support.",
        "https://www.nmdp.org/patients"
    ),
    (
        "Leukemia & Lymphoma Society",
        "Financial assistance programs and eligibility information.",
        "https://www.lls.org/support-resources/financial-support"
    ),
    (
        "Patient Advocate Foundation",
        "Insurance and financial access assistance.",
        "https://www.patientadvocate.org/"
    ),
    (
        "CancerCare",
        "Financial and practical support information.",
        "https://www.cancercare.org/"
    ),
    (
        "HealthWell Foundation",
        "Financial assistance for eligible patients.",
        "https://www.healthwellfoundation.org/"
    )
]


# --------------------------------------------------
# TRANSPLANT CENTERS
# --------------------------------------------------

CENTERS = [
    ("MD Anderson Cancer Center", "Houston", "TX", "https://www.mdanderson.org/"),
    ("UT Southwestern Medical Center", "Dallas", "TX", "https://utswmed.org/"),
    ("Baylor University Medical Center", "Dallas", "TX", "https://www.bswhealth.com/"),
    ("Mayo Clinic", "Rochester", "MN", "https://www.mayoclinic.org/"),
    ("Memorial Sloan Kettering Cancer Center", "New York", "NY", "https://www.mskcc.org/"),
    ("Dana-Farber Cancer Institute", "Boston", "MA", "https://www.dana-farber.org/"),
    ("Fred Hutchinson Cancer Center", "Seattle", "WA", "https://www.fredhutch.org/"),
    ("Stanford Health Care", "Stanford", "CA", "https://stanfordhealthcare.org/"),
    ("City of Hope", "Duarte", "CA", "https://www.cityofhope.org/"),
    ("Johns Hopkins Medicine", "Baltimore", "MD", "https://www.hopkinsmedicine.org/")
]


# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------

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

ICONS = {
    "Home": "🏠",
    "Transplant Journey": "🧭",
    "Ask StemBridge": "💬",
    "Resource Directory": "📚",
    "Financial Help": "💚",
    "Caregiver Guide": "🤝",
    "Transplant Centers": "🏥",
    "Second Opinion": "🩺"
}

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "chat" not in st.session_state:
    st.session_state.chat = []

if "transplant_type" not in st.session_state:
    st.session_state.transplant_type = "Autologous (own stem cells)"


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def go(page):
    st.session_state.page = page
    st.rerun()


def hero(title, subtitle, eyebrow="STEMBRIDGE"):
    st.markdown(
        f"""
        <div class="hero">
            <div class="eyebrow">{escape(eyebrow)}</div>
            <h1>{escape(title)}</h1>
            <p>{escape(subtitle)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def tile(icon, title, body):
    st.markdown(
        f"""
        <div class="tile">
            <div class="symbol">{icon}</div>
            <h4>{escape(title)}</h4>
            <p>{escape(body)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def show_resources(resources):
    for name, description, url in resources:
        with st.container(border=True):
            col1, col2 = st.columns(
                [4, 1],
                vertical_alignment="center"
            )

            with col1:
                st.markdown(f"**{name}**")
                st.caption(description)

            with col2:
                st.link_button(
                    "Visit Website ↗",
                    url,
                    use_container_width=True
                )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("## 💠 StemBridge")
    st.caption("TRANSPLANT EDUCATION & SUPPORT")

    st.markdown("##### EXPLORE")

    for page_name in PAGES:
        if st.button(
            f"{ICONS[page_name]} {page_name}",
            use_container_width=True,
            key="nav_" + page_name,
            type="primary"
            if st.session_state.page == page_name
            else "secondary"
        ):
            go(page_name)

    st.divider()

    st.caption("No patient login required.")
    st.caption("Educational prototype only.")
    st.caption("No medical records or personal journey tracking.")


# --------------------------------------------------
# HOME
# --------------------------------------------------

page = st.session_state.page

if page == "Home":

    hero(
        "A clearer transplant journey",
        "Learn about stem cell transplants, find trusted resources, "
        "and prepare questions for your care team.",
        "WELCOME TO STEMBRIDGE"
    )

    st.info(
        "StemBridge provides general education only. "
        "Your transplant team makes all medical decisions."
    )

    st.subheader("Explore transplant types")

    col1, col2 = st.columns(2)

    with col1:
        tile(
            "🧬",
            "Autologous Transplant",
            "Uses the patient's own stem cells. "
            "The guide includes seven phases."
        )

    with col2:
        tile(
            "🤲",
            "Allogeneic Transplant",
            "Uses donor stem cells. "
            "The guide includes eight phases."
        )

    st.selectbox(
        "Select transplant type",
        [
            "Autologous (own stem cells)",
            "Allogeneic (donor stem cells)"
        ],
        key="transplant_type"
    )

    if st.button(
        "View Transplant Journey →",
        type="primary"
    ):
        go("Transplant Journey")

    st.subheader("Explore StemBridge")

    features = [
        ("🧭", "Transplant Journey", "Learn about each transplant phase."),
        ("💬", "Ask StemBridge", "Educational chatbot with trusted sources."),
        ("📚", "Resource Directory", "Donor registries and support organizations."),
        ("💚", "Financial Help", "Explore financial assistance resources."),
        ("🤝", "Caregiver Guide", "Support information for caregivers."),
        ("🏥", "Transplant Centers", "Find transplant programs and second opinions.")
    ]

    for start in range(0, len(features), 3):
        cols = st.columns(3)

        for col, feature in zip(cols, features[start:start + 3]):
            with col:
                tile(*feature)


# --------------------------------------------------
# TRANSPLANT JOURNEY
# --------------------------------------------------

elif page == "Transplant Journey":

    hero(
        "Transplant Journey Guide",
        "Select a transplant type to understand the different phases.",
        "GENERAL TRANSPLANT INFORMATION"
    )

    transplant_type = st.selectbox(
        "Select Transplant Type",
        [
            "Autologous (own stem cells)",
            "Allogeneic (donor stem cells)"
        ],
        key="transplant_type"
    )

    is_allo = transplant_type.startswith("Allogeneic")

    phases = ALLO if is_allo else AUTO

    if is_allo:
        st.info(
            "Allogeneic transplant uses donor stem cells. "
            "The journey includes HLA testing, donor search, "
            "donor selection, and GVHD monitoring."
        )
    else:
        st.info(
            "Autologous transplant uses the patient's own stem cells. "
            "A separate donor search is not required."
        )

    st.metric("Number of Phases", len(phases))

    st.subheader("Transplant Phases")

    for index, (title, description, questions, topics) in enumerate(
        phases,
        start=1
    ):

        with st.expander(
            f"Phase {index}: {title}",
            expanded=index == 1
        ):

            st.markdown("**What happens?**")
            st.write(description)

            st.markdown("**Questions to ask the care team**")
            st.write(questions)

            st.markdown("**Important topics**")
            st.write(topics)

    st.subheader("Common Tests and Monitoring")

    with st.expander("Pre-Transplant Tests"):
        st.write(
            "Tests may include blood counts, kidney and liver tests, "
            "infection screening, heart tests, lung tests, "
            "and disease-specific assessments."
        )

    with st.expander("Day 0 and Engraftment"):
        st.write(
            "Day 0 is the day stem cells are infused. "
            "Engraftment means the transplanted cells begin "
            "producing new blood cells."
        )

    with st.expander("Recovery"):
        st.write(
            "Recovery may take months or longer. "
            "The transplant team monitors infections, "
            "blood counts, medicines, and disease response."
        )

    if is_allo:
        with st.expander("GVHD"):
            st.write(
                "Graft-versus-host disease can occur when "
                "donor immune cells attack the patient's tissues. "
                "The transplant team monitors and manages this risk."
            )

        st.subheader("Donor Registry Information")

        st.info(
            "Donor searches are managed by transplant centers. "
            "StemBridge provides information only and cannot "
            "identify matching donors."
        )

        show_resources(DONOR_REGISTRIES)

    st.warning(
        "This guide is not a treatment plan. "
        "Contact your transplant team for medical questions "
        "or urgent symptoms."
    )


# --------------------------------------------------
# EDUCATIONAL CHATBOT
# --------------------------------------------------

elif page == "Ask StemBridge":

    hero(
        "Ask StemBridge",
        "Ask general questions about stem cell transplantation.",
        "EDUCATIONAL CHATBOT"
    )

    st.info(
        "This is a curated educational chatbot, not a live AI model. "
        "Do not enter personal medical information."
    )

    with st.expander("Suggested Questions"):

        for index, item in enumerate(FAQ):

            if st.button(
                item[0],
                key=f"faq_{index}",
                use_container_width=True
            ):

                response, sources = answer(item[0])

                st.session_state.chat.append(
                    ("user", item[0], [])
                )

                st.session_state.chat.append(
                    ("assistant", response, sources)
                )

                st.rerun()

    for role, message, sources in st.session_state.chat:

        with st.chat_message(role):

            st.write(message)

            for label, url in sources:
                st.markdown(f"[{label} Source]({url})")

    prompt = st.chat_input(
        "Ask about transplant types, donors, recovery..."
    )

    if prompt:

        response, sources = answer(prompt)

        st.session_state.chat.append(
            ("user", prompt, [])
        )

        st.session_state.chat.append(
            ("assistant", response, sources)
        )

        st.rerun()

    st.subheader("Official Educational Sources")

    st.link_button("National Cancer Institute", NCI)
    st.link_button("American Cancer Society", ACS)


# --------------------------------------------------
# RESOURCE DIRECTORY
# --------------------------------------------------

elif page == "Resource Directory":

    hero(
        "Resource Directory",
        "Find donor registries, transplant education, "
        "and patient support organizations.",
        "TRUSTED EXTERNAL RESOURCES"
    )

    tab1, tab2 = st.tabs([
        "🧬 Donor Registries",
        "📚 Education & Support"
    ])

    with tab1:

        st.info(
            "For allogeneic transplants, donor searches are "
            "managed by the transplant center. "
            "These organizations provide donor registry information "
            "and educational resources. "
            "StemBridge does not search donor databases."
        )

        show_resources(DONOR_REGISTRIES)

    with tab2:

        show_resources(EDUCATION_RESOURCES)

    st.caption(
        "These are external organizations. "
        "StemBridge does not have live integrations "
        "or partnerships with them."
    )


# --------------------------------------------------
# FINANCIAL HELP
# --------------------------------------------------

elif page == "Financial Help":

    hero(
        "Financial Resource Navigator",
        "Explore organizations that may help with "
        "transplant-related expenses.",
        "FINANCIAL SUPPORT"
    )

    st.subheader("Questions to Ask")

    st.markdown("""
- What transplant expenses does my insurance cover?
- Do I need prior authorization?
- Is financial assistance available?
- Can I receive help with travel or temporary housing?
- Are there grants for eligible patients?
- Who can help if my insurance denies coverage?
    """)

    st.subheader("Financial Support Organizations")

    show_resources(FINANCIAL)

    st.info(
        "Financial assistance depends on eligibility "
        "and available funding. StemBridge does not "
        "submit financial applications."
    )


# --------------------------------------------------
# CAREGIVER GUIDE
# --------------------------------------------------

elif page == "Caregiver Guide":

    hero(
        "Caregiver Resources",
        "Practical information for family members "
        "and caregivers.",
        "CAREGIVER SUPPORT"
    )

    caregiver_sections = [
        (
            "Before Transplant",
            [
                "Understand the transplant process.",
                "Discuss caregiver responsibilities with the care team.",
                "Arrange transportation and accommodation.",
                "Prepare for time away from work."
            ]
        ),
        (
            "During Transplant",
            [
                "Follow infection-prevention instructions.",
                "Help with practical daily needs.",
                "Support communication with the care team.",
                "Understand hospital visiting rules."
            ]
        ),
        (
            "After Transplant",
            [
                "Review discharge instructions.",
                "Help arrange follow-up visits.",
                "Learn the warning signs explained by the care team.",
                "Support recovery at home."
            ]
        ),
        (
            "Caregiver Well-Being",
            [
                "Ask for help from family and friends.",
                "Consider counseling or support groups.",
                "Discuss financial concerns with a social worker.",
                "Arrange backup caregiver support when possible."
            ]
        )
    ]

    for title, items in caregiver_sections:

        with st.expander(title):

            for item in items:
                st.write("• " + item)

    st.subheader("Caregiver Support Organizations")

    show_resources([
        EDUCATION_RESOURCES[2],
        EDUCATION_RESOURCES[3],
        DONOR_REGISTRIES[0]
    ])


# --------------------------------------------------
# TRANSPLANT CENTERS
# --------------------------------------------------

elif page == "Transplant Centers":

    hero(
        "Find a Transplant Center",
        "Explore example transplant programs "
        "and official center directories.",
        "TRANSPLANT CENTER DIRECTORY"
    )

    st.warning(
        "This is an example list, not a complete or ranked directory. "
        "Confirm transplant services, insurance, and appointments "
        "directly with the center."
    )

    search = st.text_input(
        "Search by center, city, or state",
        placeholder="Dallas, Houston, Mayo..."
    )

    filtered = [
        center for center in CENTERS
        if search.lower().strip()
        in " ".join(center[:3]).lower()
    ]

    for name, city, state, url in filtered:

        with st.container(border=True):

            st.markdown(f"**{name}**")
            st.caption(f"{city}, {state}")

            st.link_button(
                "Visit Center Website ↗",
                url
            )

    if not filtered:
        st.info("No matching center in this example list.")

    st.subheader("Additional Directories")

    st.link_button(
        "NMDP Patient Resources",
        "https://www.nmdp.org/patients"
    )

    st.link_button(
        "NCI Cancer Center Directory",
        "https://www.cancer.gov/research/infrastructure/cancer-centers/find"
    )

    st.link_button(
        "HRSA Transplant Center Data",
        "https://bloodstemcell.hrsa.gov/data/donation-and-transplantation-statistics/transplant-center-data"
    )

    if st.button(
        "Learn About Second Opinions →",
        type="primary"
    ):
        go("Second Opinion")


# --------------------------------------------------
# SECOND OPINION
# --------------------------------------------------

elif page == "Second Opinion":

    hero(
        "Getting a Second Opinion",
        "Learn how to consult another transplant specialist.",
        "SECOND OPINION GUIDE"
    )

    steps = [
        (
            "Talk to Your Current Doctor",
            "Ask whether another transplant specialist "
            "can review the treatment recommendation."
        ),
        (
            "Find Another Transplant Center",
            "Look for a program that treats your condition "
            "and provides the transplant type being considered."
        ),
        (
            "Prepare Medical Records",
            "The specialist may request test results, "
            "treatment history, pathology reports, "
            "and HLA results when relevant."
        ),
        (
            "Check Insurance",
            "Ask about referrals, authorization, "
            "consultation costs, and appointment availability."
        ),
        (
            "Compare Recommendations",
            "Discuss treatment benefits, risks, "
            "alternatives, and possible donor options."
        )
    ]

    for index, (title, description) in enumerate(
        steps,
        start=1
    ):

        with st.expander(f"{index}. {title}"):
            st.write(description)

    st.subheader("Questions for a Second Opinion")

    st.markdown("""
- Do you agree with the recommended transplant type?
- Are there other treatment options?
- What are the main benefits and risks?
- How much experience does your center have with this condition?
- What donor options are available if needed?
- What support is available for caregivers?
    """)

    st.info(
        "StemBridge does not schedule appointments "
        "or send medical records to hospitals."
    )

    if st.button(
        "Browse Transplant Centers →",
        type="primary"
    ):
        go("Transplant Centers")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "StemBridge | Educational Prototype | "
    "SDG 3 – Good Health and Well-Being | "
    "No patient data, donor matching, or hospital integration. "
    "Medical content requires clinical review before real-world use."
)
