
"""
StemBridge - Unified Resource Navigation Center

Features:
1. Donor Registries
2. Financial Help
3. Education
4. Caregiver Support
5. Transplant Centers
6. Second Opinions

Additional features:
- Search and category filters
- Country / region filters
- Interactive resource cards
- Resource details
- Guided resource finder
- Bookmark resources
- Preparation checklists
- Personal notes
- External official websites

Educational prototype only.
"""

from html import escape
import streamlit as st


# ============================================================
# 1. RESOURCE DATA
# ============================================================

RESOURCES = [

    # ---------------- DONOR REGISTRIES ----------------

    {
        "id": "nmdp",
        "name": "NMDP",
        "category": "Donor Registries",
        "region": "United States",
        "icon": "🧬",
        "summary": (
            "Donor registry information, transplant "
            "education, and patient support."
        ),
        "helps": [
            "Understand how donor searches work",
            "Learn about stem cell transplantation",
            "Explore patient and caregiver support"
        ],
        "url": "https://www.nmdp.org/patients",
        "questions": [
            "How does my transplant team coordinate a donor search?",
            "What donor options might be considered?",
            "What support services are available?"
        ]
    },

    {
        "id": "gift",
        "name": "Gift of Life Marrow Registry",
        "category": "Donor Registries",
        "region": "United States",
        "icon": "🧬",
        "summary": (
            "Stem cell donor recruitment "
            "and patient education."
        ),
        "helps": [
            "Learn about joining a donor registry",
            "Understand stem cell donation",
            "Explore educational information"
        ],
        "url": "https://www.giftoflife.org",
        "questions": [
            "What does donor registration involve?",
            "Who can explain donor compatibility?",
            "How are potential donors contacted?"
        ]
    },

    {
        "id": "dkms",
        "name": "DKMS",
        "category": "Donor Registries",
        "region": "International",
        "icon": "🌍",
        "summary": (
            "International stem cell donor "
            "recruitment and education."
        ),
        "helps": [
            "Learn about stem cell donation",
            "Explore donor registration",
            "Find country-specific information"
        ],
        "url": "https://www.dkms.org",
        "questions": [
            "Which DKMS organization serves my country?",
            "How does donor registration work?",
            "How is donor registration different from patient matching?"
        ]
    },

    {
        "id": "anthony",
        "name": "Anthony Nolan",
        "category": "Donor Registries",
        "region": "United Kingdom",
        "icon": "🧬",
        "summary": (
            "Stem cell donor registry "
            "and transplant support."
        ),
        "helps": [
            "Understand donor registration",
            "Explore transplant education",
            "Find patient support information"
        ],
        "url": "https://www.anthonynolan.org",
        "questions": [
            "What patient support is available?",
            "How does donor registration work?",
            "What should I ask my transplant team?"
        ]
    },

    {
        "id": "wmda",
        "name": "World Marrow Donor Association",
        "category": "Donor Registries",
        "region": "International",
        "icon": "🌍",
        "summary": (
            "International donor registry "
            "coordination and standards."
        ),
        "helps": [
            "Understand international donor networks",
            "Learn about donor safety standards",
            "Explore registry coordination"
        ],
        "url": "https://wmda.info",
        "questions": [
            "How are international donor searches coordinated?",
            "Who can access donor registry systems?",
            "What standards guide donor safety?"
        ]
    },

    {
        "id": "datri",
        "name": "DATRI",
        "category": "Donor Registries",
        "region": "India",
        "icon": "🧬",
        "summary": (
            "Blood stem cell donor registration "
            "and education in India."
        ),
        "helps": [
            "Learn about stem cell donation in India",
            "Explore donor registration",
            "Understand donor awareness programs"
        ],
        "url": "https://datri.org",
        "questions": [
            "How does donor registration work in India?",
            "How can a transplant center explore donor options?",
            "What information is available for patients?"
        ]
    },

    {
        "id": "canada",
        "name": "Canadian Blood Services",
        "category": "Donor Registries",
        "region": "Canada",
        "icon": "🍁",
        "summary": (
            "Canadian stem cell donor registry "
            "and educational resources."
        ),
        "helps": [
            "Learn about the stem cell registry",
            "Explore donor registration",
            "Understand stem cell donation"
        ],
        "url": "https://www.blood.ca/en/stemcells",
        "questions": [
            "What is the role of the Canadian registry?",
            "How does donor registration work?",
            "What should patients ask their transplant team?"
        ]
    },

    # ---------------- FINANCIAL HELP ----------------

    {
        "id": "lls",
        "name": "Blood Cancer United",
        "category": "Financial Help",
        "region": "United States",
        "icon": "💙",
        "summary": (
            "Blood cancer information and "
            "financial assistance program resources."
        ),
        "helps": [
            "Explore financial assistance information",
            "Learn about patient support programs",
            "Find blood cancer educational resources"
        ],
        "url": "https://www.bloodcancerunited.org",
        "questions": [
            "Which assistance programs are currently available?",
            "What eligibility requirements apply?",
            "What documents might be needed?"
        ]
    },

    {
        "id": "nmdp_fin",
        "name": "NMDP Patient Support",
        "category": "Financial Help",
        "region": "United States",
        "icon": "💙",
        "summary": (
            "Patient support information, including "
            "potential financial resources."
        ),
        "helps": [
            "Explore patient assistance information",
            "Learn about transplant-related support",
            "Prepare questions for a social worker"
        ],
        "url": "https://www.nmdp.org/patients",
        "questions": [
            "What assistance might be available?",
            "Can a social worker help me apply?",
            "What eligibility conditions apply?"
        ]
    },

    {
        "id": "cancercare_fin",
        "name": "CancerCare",
        "category": "Financial Help",
        "region": "United States",
        "icon": "💙",
        "summary": (
            "Cancer support services and "
            "financial assistance information."
        ),
        "helps": [
            "Explore financial assistance",
            "Find cancer support information",
            "Learn about available services"
        ],
        "url": "https://www.cancercare.org",
        "questions": [
            "Are financial assistance programs open?",
            "Which programs apply to my situation?",
            "How can I contact a support professional?"
        ]
    },

    # ---------------- EDUCATION ----------------

    {
        "id": "nci",
        "name": "National Cancer Institute",
        "category": "Education",
        "region": "United States",
        "icon": "📚",
        "summary": (
            "Cancer and stem cell transplant "
            "educational information."
        ),
        "helps": [
            "Understand transplant procedures",
            "Learn common medical terminology",
            "Explore treatment-related risks"
        ],
        "url": (
            "https://www.cancer.gov/about-cancer/"
            "treatment/types/stem-cell-transplant"
        ),
        "questions": [
            "What type of transplant is being discussed?",
            "What risks should I discuss with my doctor?",
            "What happens during recovery?"
        ]
    },

    {
        "id": "acs",
        "name": "American Cancer Society",
        "category": "Education",
        "region": "United States",
        "icon": "📚",
        "summary": (
            "Plain-language information about "
            "cancer and stem cell transplants."
        ),
        "helps": [
            "Learn transplant basics",
            "Understand treatment stages",
            "Prepare questions for clinicians"
        ],
        "url": "https://www.cancer.org",
        "questions": [
            "What happens during conditioning?",
            "What side effects may occur?",
            "What follow-up care is usually needed?"
        ]
    },

    # ---------------- CAREGIVER SUPPORT ----------------

    {
        "id": "bmt",
        "name": "BMT InfoNet",
        "category": "Caregiver Support",
        "region": "International",
        "icon": "🤝",
        "summary": (
            "Education and support for "
            "transplant patients and caregivers."
        ),
        "helps": [
            "Explore caregiver education",
            "Understand recovery challenges",
            "Learn about transplant survivorship"
        ],
        "url": "https://www.bmtinfonet.org",
        "questions": [
            "What should caregivers prepare before discharge?",
            "What support is available during recovery?",
            "How can caregivers manage daily responsibilities?"
        ]
    },

    {
        "id": "cancercare_support",
        "name": "CancerCare Support Services",
        "category": "Caregiver Support",
        "region": "United States",
        "icon": "🤝",
        "summary": (
            "Counseling, education, and "
            "support for people affected by cancer."
        ),
        "helps": [
            "Explore caregiver support",
            "Find counseling information",
            "Learn about support services"
        ],
        "url": "https://www.cancercare.org",
        "questions": [
            "What caregiver support is available?",
            "Are counseling services offered?",
            "How can families find additional assistance?"
        ]
    },

    # ---------------- TRANSPLANT CENTERS ----------------

    {
        "id": "nmdp_centers",
        "name": "NMDP Transplant Center Information",
        "category": "Transplant Centers",
        "region": "United States",
        "icon": "🏥",
        "summary": (
            "Information to help patients "
            "explore transplant centers."
        ),
        "helps": [
            "Learn what to ask transplant centers",
            "Explore transplant care information",
            "Prepare for a consultation"
        ],
        "url": "https://www.nmdp.org/patients",
        "questions": [
            "Does the center treat my condition?",
            "What transplant types are available?",
            "How does the referral process work?"
        ]
    },

    {
        "id": "nci_centers",
        "name": "NCI Cancer Centers",
        "category": "Transplant Centers",
        "region": "United States",
        "icon": "🏥",
        "summary": (
            "Directory of NCI-designated cancer "
            "centers. Transplant services vary."
        ),
        "helps": [
            "Explore cancer center locations",
            "Learn about specialized cancer care",
            "Prepare transplant program questions"
        ],
        "url": (
            "https://www.cancer.gov/research/"
            "infrastructure/cancer-centers/find"
        ),
        "questions": [
            "Does the center offer my required transplant type?",
            "How do I request a consultation?",
            "Does the center accept my insurance?"
        ]
    },

    # ---------------- SECOND OPINIONS ----------------

    {
        "id": "nci_second",
        "name": "NCI Second Opinion Guidance",
        "category": "Second Opinions",
        "region": "United States",
        "icon": "🩺",
        "summary": (
            "Guidance about obtaining "
            "a second opinion for cancer care."
        ),
        "helps": [
            "Understand second opinions",
            "Prepare for specialist consultation",
            "Learn what information to discuss"
        ],
        "url": (
            "https://www.cancer.gov/about-cancer/"
            "managing-care/services/second-opinions"
        ),
        "questions": [
            "Which medical records should I bring?",
            "Will insurance cover the consultation?",
            "What treatment alternatives should I discuss?"
        ]
    },

    {
        "id": "acs_second",
        "name": "American Cancer Society Guidance",
        "category": "Second Opinions",
        "region": "United States",
        "icon": "🩺",
        "summary": (
            "Cancer education to help patients "
            "prepare for treatment discussions."
        ),
        "helps": [
            "Prepare questions about treatment options",
            "Understand cancer care decisions",
            "Explore educational information"
        ],
        "url": "https://www.cancer.org",
        "questions": [
            "What are the treatment alternatives?",
            "What should I discuss with another specialist?",
            "How should I share records securely?"
        ]
    }
]


CATEGORIES = [
    "All Resources",
    "Donor Registries",
    "Financial Help",
    "Education",
    "Caregiver Support",
    "Transplant Centers",
    "Second Opinions"
]


# ============================================================
# 2. CSS DESIGN
# ============================================================

CSS = """
<style>

.sb-hero {
    padding: 28px 30px;
    border-radius: 20px;
    background: linear-gradient(
        110deg,
        #103e52,
        #087f82
    );
    color: white;
    margin-bottom: 20px;
}

.sb-hero h2 {
    color: white;
    margin: 0 0 10px;
    font-size: 29px;
}

.sb-hero p {
    color: #e0f5f3;
    margin: 0;
    font-size: 15px;
}

.sb-card {
    border: 1px solid #d9e9e8;
    background: linear-gradient(
        135deg,
        #ffffff,
        #f2faf9
    );
    border-radius: 16px;
    padding: 18px;
    min-height: 170px;
    margin-bottom: 8px;
}

.sb-card h4 {
    margin: 8px 0;
    color: #12445b;
    font-size: 18px;
}

.sb-card p {
    margin: 7px 0;
    color: #496a76;
    font-size: 14px;
}

.sb-tag {
    display: inline-block;
    background: #e0f5f1;
    color: #116c6c;
    border-radius: 20px;
    padding: 5px 10px;
    font-size: 12px;
    font-weight: 700;
}

.sb-detail {
    background: #f1faf9;
    border-left: 4px solid #118f8b;
    padding: 16px;
    border-radius: 10px;
    margin-bottom: 16px;
}

</style>
"""


# ============================================================
# 3. NAVIGATION CALLBACKS
# ============================================================

def go_to_resource(resource_id):
    st.session_state["sb_selected_resource"] = resource_id


def back_to_directory():
    st.session_state["sb_selected_resource"] = None


def toggle_bookmark(resource_id):

    saved = st.session_state["sb_saved_resources"]

    if resource_id in saved:
        saved.remove(resource_id)
    else:
        saved.add(resource_id)


# ============================================================
# 4. RESOURCE CARD
# ============================================================

def render_resource_card(resource):

    name = escape(resource["name"])
    category = escape(resource["category"])
    region = escape(resource["region"])
    summary = escape(resource["summary"])
    icon = resource["icon"]

    card_html = (
        '<div class="sb-card">'
        f'<span class="sb-tag">{icon} {category}</span>'
        f'<h4>{name}</h4>'
        f'<p>📍 {region}</p>'
        f'<p>{summary}</p>'
        '</div>'
    )

    st.markdown(
        card_html,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([3, 1])

    with col1:

        st.button(
            "Explore Resource →",
            key=f'open_{resource["id"]}',
            use_container_width=True,
            type="primary",
            on_click=go_to_resource,
            args=(resource["id"],)
        )

    with col2:

        saved = (
            resource["id"]
            in st.session_state["sb_saved_resources"]
        )

        st.button(
            "★" if saved else "☆",
            key=f'save_{resource["id"]}',
            use_container_width=True,
            help=(
                "Remove bookmark"
                if saved else "Save resource"
            ),
            on_click=toggle_bookmark,
            args=(resource["id"],)
        )


# ============================================================
# 5. RESOURCE DETAIL PAGE
# ============================================================

def render_resource_details(resource):

    st.button(
        "← Back to Resource Center",
        on_click=back_to_directory
    )

    st.markdown(
        f'## {resource["icon"]} {resource["name"]}'
    )

    st.caption(
        f'{resource["category"]} · {resource["region"]}'
    )

    summary_html = (
        '<div class="sb-detail">'
        f'{escape(resource["summary"])}'
        '</div>'
    )

    st.markdown(
        summary_html,
        unsafe_allow_html=True
    )

    st.markdown("### How This Resource Can Help")

    for item in resource["helps"]:
        st.markdown(f"- {item}")

    tab1, tab2, tab3 = st.tabs([
        "📋 Preparation Checklist",
        "❓ Questions to Ask",
        "📝 My Notes"
    ])

    # ---------------- CHECKLIST ----------------

    with tab1:

        st.markdown(
            "#### Before You Visit This Organization"
        )

        checklist = [
            "Identify the information or support I need",
            "Prepare questions for my transplant care team",
            "Check whether services apply to my situation"
        ]

        for index, item in enumerate(checklist):

            st.checkbox(
                item,
                key=f'check_{resource["id"]}_{index}'
            )

        st.caption(
            "Checklist selections are stored "
            "only during the current session."
        )

    # ---------------- QUESTIONS ----------------

    with tab2:

        st.markdown(
            "#### Questions to Discuss"
        )

        for question in resource["questions"]:
            st.markdown(f"- {question}")

    # ---------------- NOTES ----------------

    with tab3:

        st.text_area(
            "Personal Notes",
            key=f'notes_{resource["id"]}',
            placeholder=(
                "Write general notes or questions here. "
                "Avoid sensitive patient information."
            ),
            height=150
        )

        st.caption(
            "Notes are temporary and are not "
            "saved in a database."
        )

    # ---------------- EXTERNAL LINK ----------------

    st.markdown("### Visit the Official Organization")

    st.link_button(
        "Open Official Website ↗",
        resource["url"],
        use_container_width=True,
        type="primary"
    )

    st.caption(
        "This opens an external organization website. "
        "Service availability and eligibility "
        "should be confirmed directly."
    )

    saved = (
        resource["id"]
        in st.session_state["sb_saved_resources"]
    )

    st.button(
        "★ Remove from Saved"
        if saved else "☆ Save This Resource",
        key=f'detail_save_{resource["id"]}',
        on_click=toggle_bookmark,
        args=(resource["id"],)
    )


# ============================================================
# 6. MAIN RESOURCE CENTER
# ============================================================

def render_resource_center():

    # Initialize session state
    st.session_state.setdefault(
        "sb_selected_resource",
        None
    )

    st.session_state.setdefault(
        "sb_saved_resources",
        set()
    )

    st.markdown(
        CSS,
        unsafe_allow_html=True
    )

    # ---------------- HERO ----------------

    hero_html = (
        '<div class="sb-hero">'
        '<h2>🌿 Resource Navigation Center</h2>'
        '<p>Find, understand, prepare for, and save '
        'transplant support resources in one place.</p>'
        '</div>'
    )

    st.markdown(
        hero_html,
        unsafe_allow_html=True
    )

    # ---------------- DETAILS ----------------

    selected_id = st.session_state[
        "sb_selected_resource"
    ]

    if selected_id:

        resource = next(
            (
                r for r in RESOURCES
                if r["id"] == selected_id
            ),
            None
        )

        if resource:

            render_resource_details(resource)
            return

        st.session_state[
            "sb_selected_resource"
        ] = None

    st.info(
        "StemBridge provides educational resource navigation. "
        "It does not perform donor matching, verify eligibility, "
        "make referrals, or provide medical advice."
    )

    tab_directory, tab_guide, tab_saved = st.tabs([
        "🔎 Explore Resources",
        "🧭 Guided Resource Finder",
        "⭐ My Saved Resources"
    ])

    # ========================================================
    # TAB 1 - RESOURCE DIRECTORY
    # ========================================================

    with tab_directory:

        search_col, category_col, region_col = st.columns(
            [2, 2, 1.5]
        )

        with search_col:

            search_query = st.text_input(
                "Search Resources",
                placeholder=(
                    "Search by organization or support need"
                ),
                key="sb_search"
            )

        with category_col:

            selected_category = st.selectbox(
                "Category",
                CATEGORIES,
                key="sb_category"
            )

        with region_col:

            regions = [
                "All Regions"
            ] + sorted({
                r["region"]
                for r in RESOURCES
            })

            selected_region = st.selectbox(
                "Region",
                regions,
                key="sb_region"
            )

        search_query = search_query.strip().lower()

        filtered_resources = []

        for resource in RESOURCES:

            category_match = (
                selected_category == "All Resources"
                or resource["category"] == selected_category
            )

            region_match = (
                selected_region == "All Regions"
                or resource["region"] == selected_region
            )

            searchable_text = " ".join([
                resource["name"],
                resource["summary"],
                resource["category"],
                resource["region"],
                " ".join(resource["helps"])
            ]).lower()

            search_match = (
                not search_query
                or search_query in searchable_text
            )

            if (
                category_match
                and region_match
                and search_match
            ):
                filtered_resources.append(resource)

        st.caption(
            f"{len(filtered_resources)} resources found"
        )

        if not filtered_resources:

            st.warning(
                "No resources match your search. "
                "Try another keyword or filter."
            )

        # Display two resource cards per row
        for start in range(
            0,
            len(filtered_resources),
            2
        ):

            columns = st.columns(
                2,
                gap="large"
            )

            current_resources = (
                filtered_resources[start:start + 2]
            )

            for col, resource in zip(
                columns,
                current_resources
            ):

                with col:
                    render_resource_card(resource)

    # ========================================================
    # TAB 2 - GUIDED RESOURCE FINDER
    # ========================================================

    with tab_guide:

        st.markdown(
            "### Find Resources Based on Your Needs"
        )

        st.write(
            "Answer two simple questions to find "
            "relevant educational starting points."
        )

        selected_need = st.radio(
            "What kind of support are you looking for?",
            CATEGORIES[1:],
            key="sb_need"
        )

        guide_regions = [
            "Any Region"
        ] + sorted({
            r["region"]
            for r in RESOURCES
        })

        selected_guide_region = st.selectbox(
            "Which region are you interested in?",
            guide_regions,
            key="sb_guide_region"
        )

        if st.button(
            "Find Suggested Resources",
            type="primary",
            key="sb_find_resources"
        ):

            st.session_state[
                "sb_guide_results"
            ] = (
                selected_need,
                selected_guide_region
            )

        if "sb_guide_results" in st.session_state:

            chosen_need, chosen_region = (
                st.session_state["sb_guide_results"]
            )

            suggested_resources = [
                r for r in RESOURCES
                if (
                    r["category"] == chosen_need
                    and (
                        chosen_region == "Any Region"
                        or r["region"] in (
                            chosen_region,
                            "International"
                        )
                    )
                )
            ]

            st.markdown(
                "### Suggested Starting Points"
            )

            if not suggested_resources:

                st.warning(
                    "No matching resources are currently "
                    "listed for this combination."
                )

            for resource in suggested_resources:

                st.button(
                    f'{resource["icon"]} '
                    f'{resource["name"]} '
                    f'— {resource["region"]}',
                    key=f'guided_{resource["id"]}',
                    use_container_width=True,
                    on_click=go_to_resource,
                    args=(resource["id"],)
                )

            st.caption(
                "Suggestions are based on directory "
                "categories and regions. They are not "
                "personalized medical recommendations."
            )

    # ========================================================
    # TAB 3 - SAVED RESOURCES
    # ========================================================

    with tab_saved:

        saved_resources = [
            r for r in RESOURCES
            if r["id"] in st.session_state[
                "sb_saved_resources"
            ]
        ]

        st.markdown("### My Saved Resources")

        if not saved_resources:

            st.info(
                "You have not saved any resources yet. "
                "Use the ☆ button on a resource card "
                "to bookmark it."
            )

        else:

            st.caption(
                f"{len(saved_resources)} "
                "resources saved in this session."
            )

            for resource in saved_resources:

                st.button(
                    f'{resource["icon"]} '
                    f'{resource["name"]} '
                    "— Explore →",
                    key=f'saved_{resource["id"]}',
                    use_container_width=True,
                    on_click=go_to_resource,
                    args=(resource["id"],)
                )

    st.caption(
        "StemBridge Resource Navigation Center — "
        "Educational prototype. External resources "
        "should be checked for current information."
    )


# ============================================================
# 7. STANDALONE EXECUTION
# ============================================================

if __name__ == "__main__":

    st.set_page_config(
        page_title="StemBridge Resource Center",
        page_icon="🌿",
        layout="wide"
    )

    render_resource_center()
