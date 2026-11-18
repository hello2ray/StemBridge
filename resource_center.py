
"""StemBridge - Mobile Responsive Resource Navigation Center."""

from html import escape
import streamlit as st


# ------------------------------------------------------------
# Resource data
# ------------------------------------------------------------

def resource(
    id, name, category, region, icon,
    summary, url, helps, questions
):
    return dict(
        id=id,
        name=name,
        category=category,
        region=region,
        icon=icon,
        summary=summary,
        url=url,
        helps=helps,
        questions=questions,
    )


RESOURCES = [
    resource(
        "nmdp", "NMDP", "Donor Registries",
        "United States", "🧬",
        "Donor search education and patient support.",
        "https://www.nmdp.org/patients",
        ["Understand donor search", "Explore patient support"],
        ["Who coordinates the donor search?", "What donor options are possible?"],
    ),
    resource(
        "gift", "Gift of Life Marrow Registry",
        "Donor Registries", "United States", "🧬",
        "Stem cell donor recruitment and education.",
        "https://www.giftoflife.org",
        ["Learn about donor registration", "Explore donor education"],
        ["How does registration work?", "How is compatibility assessed?"],
    ),
    resource(
        "dkms", "DKMS", "Donor Registries",
        "International", "🧬",
        "Stem cell donor recruitment and education.",
        "https://www.dkms.org",
        ["Learn about stem cell donation", "Explore country-specific information"],
        ["Which organization is relevant?", "How does donor registration work?"],
    ),
    resource(
        "anthony", "Anthony Nolan", "Donor Registries",
        "United Kingdom", "🧬",
        "Donor registry and transplant support.",
        "https://www.anthonynolan.org",
        ["Explore donor registration", "Learn about transplant support"],
        ["What support is available?", "How do donor searches work?"],
    ),
    resource(
        "wmda", "World Marrow Donor Association",
        "Donor Registries", "International", "🌍",
        "International donor registry coordination and standards.",
        "https://wmda.info",
        ["Understand international networks", "Explore donor safety standards"],
        ["How are international searches coordinated?", "Who can search registries?"],
    ),
    resource(
        "datri", "DATRI", "Donor Registries",
        "India", "🧬",
        "Blood stem cell donor registry and education.",
        "https://datri.org",
        ["Learn about donation in India", "Explore donor education"],
        ["How does registration work?", "Who coordinates patient searches?"],
    ),
    resource(
        "cbs", "Canadian Blood Services",
        "Donor Registries", "Canada", "🍁",
        "Canadian stem cell donor registry information.",
        "https://www.blood.ca/en/stemcells",
        ["Learn about the registry", "Explore donor information"],
        ["What is the registry's role?", "What should I ask my team?"],
    ),
    resource(
        "lls", "Blood Cancer United",
        "Financial Help", "United States", "💙",
        "Blood cancer support and financial assistance information.",
        "https://www.bloodcancerunited.org",
        ["Explore assistance programs", "Find support services"],
        ["Which programs are open?", "What eligibility rules apply?"],
    ),
    resource(
        "nmdp_fin", "NMDP Patient Support",
        "Financial Help", "United States", "💙",
        "Transplant support and possible financial resources.",
        "https://www.nmdp.org/patients",
        ["Explore assistance information", "Prepare social worker questions"],
        ["What support is available?", "Who can help me apply?"],
    ),
    resource(
        "cancer_fin", "CancerCare",
        "Financial Help", "United States", "💙",
        "Cancer support and financial assistance information.",
        "https://www.cancercare.org",
        ["Explore support services", "Review financial assistance"],
        ["Which programs are open?", "What support fits my needs?"],
    ),
    resource(
        "nci", "National Cancer Institute",
        "Education", "United States", "📚",
        "Evidence-based cancer and transplant education.",
        "https://www.cancer.gov/about-cancer/treatment/types/stem-cell-transplant",
        ["Learn transplant terminology", "Understand treatment risks"],
        ["Which transplant type is planned?", "What risks should I discuss?"],
    ),
    resource(
        "acs", "American Cancer Society",
        "Education", "United States", "📚",
        "Plain-language stem cell transplant information.",
        "https://www.cancer.org/cancer/managing-cancer/treatment-types/stem-cell-transplant.html",
        ["Understand transplant basics", "Prepare care-team questions"],
        ["What happens during conditioning?", "What follow-up is needed?"],
    ),
    resource(
        "bmtinfonet", "BMT InfoNet",
        "Caregiver Support", "International", "🤝",
        "Education and support for transplant recipients and caregivers.",
        "https://www.bmtinfonet.org",
        ["Explore caregiver education", "Learn about recovery"],
        ["How should caregivers prepare?", "What recovery support exists?"],
    ),
    resource(
        "cancercare_support", "CancerCare Support Services",
        "Caregiver Support", "United States", "🤝",
        "Counseling, education, and support for people affected by cancer.",
        "https://www.cancercare.org",
        ["Explore counseling", "Find caregiver support"],
        ["What support is available?", "How can we find assistance?"],
    ),
    resource(
        "nmdp_centers", "NMDP Transplant Center Information",
        "Transplant Centers", "United States", "🏥",
        "Information about transplant centers and care teams.",
        "https://www.nmdp.org/patients",
        ["Explore transplant center information", "Prepare consultation questions"],
        ["Does the center treat my condition?", "How do referrals work?"],
    ),
    resource(
        "nci_centers", "NCI Cancer Centers",
        "Transplant Centers", "United States", "🏥",
        "Directory of NCI-designated cancer centers.",
        "https://www.cancer.gov/research/infrastructure/cancer-centers/find",
        ["Explore cancer centers", "Prepare transplant program questions"],
        ["Does this center provide my transplant type?", "How do I request a visit?"],
    ),
    resource(
        "nci_second", "NCI Second Opinions",
        "Second Opinions", "United States", "🩺",
        "Guidance about obtaining another opinion on cancer treatment.",
        "https://www.cancer.gov/about-cancer/managing-care/services/second-opinions",
        ["Understand second opinions", "Prepare for a consultation"],
        ["Which records are needed?", "Will insurance cover the visit?"],
    ),
    resource(
        "acs_second", "American Cancer Society Guidance",
        "Second Opinions", "United States", "🩺",
        "Cancer care information for treatment discussions.",
        "https://www.cancer.org",
        ["Prepare treatment questions", "Understand available choices"],
        ["What alternatives exist?", "How should records be shared?"],
    ),
]


CATEGORIES = [
    "All Resources",
    "Donor Registries",
    "Financial Help",
    "Education",
    "Caregiver Support",
    "Transplant Centers",
    "Second Opinions",
]

ICONS = {
    "Donor Registries": "🧬",
    "Financial Help": "💙",
    "Education": "📚",
    "Caregiver Support": "🤝",
    "Transplant Centers": "🏥",
    "Second Opinions": "🩺",
}


# ------------------------------------------------------------
# Responsive styling
# ------------------------------------------------------------

CSS = """
<style>
.sb-hero {
    background:linear-gradient(110deg,#103e52,#087f82);
    border-radius:20px;
    padding:25px 28px;
    color:white;
    margin-bottom:16px;
}
.sb-hero h2 {
    color:white !important;
    font-size:clamp(1.5rem,3vw,2rem);
    margin:0 0 8px;
}
.sb-hero p {
    color:#e0f5f3;
    margin:0;
}
.sb-card {
    background:linear-gradient(135deg,#ffffff,#f2faf9);
    border:1px solid #d9e9e8;
    border-radius:17px;
    padding:18px;
    min-height:170px;
    margin:8px 0 10px;
}
.sb-card h4 {
    color:#12445b;
    font-size:1.08rem;
    margin:10px 0 7px;
}
.sb-card p {
    color:#496a76;
    font-size:.88rem;
    line-height:1.5;
    margin:5px 0;
}
.sb-tag {
    display:inline-block;
    background:#e0f5f1;
    color:#116c6c;
    border-radius:20px;
    padding:5px 10px;
    font-size:.75rem;
    font-weight:750;
}
.sb-detail {
    background:#f1faf9;
    border-left:4px solid #118f8b;
    border-radius:12px;
    padding:16px;
    color:#244d58;
    margin:15px 0;
}
.st-key-sb_resource_cards button,
.st-key-sb_resource_filters button {
    min-height:46px;
}
@media(max-width:767px) {
    .sb-hero {
        padding:18px 16px;
        border-radius:16px;
    }
    .sb-card {
        padding:15px;
        min-height:0;
    }
    .st-key-sb_resource_filters [data-testid="stHorizontalBlock"],
    .st-key-sb_resource_cards [data-testid="stHorizontalBlock"] {
        display:flex !important;
        flex-direction:column !important;
        gap:8px !important;
    }
    .st-key-sb_resource_filters [data-testid="stColumn"],
    .st-key-sb_resource_cards [data-testid="stColumn"] {
        width:100% !important;
        min-width:0 !important;
    }
}
</style>
"""


# ------------------------------------------------------------
# Session callbacks
# ------------------------------------------------------------

def _go_to(resource_id):
    st.session_state["sb_selected_resource"] = resource_id


def _back():
    st.session_state["sb_selected_resource"] = None


def _toggle_bookmark(resource_id):
    saved = st.session_state["sb_saved_resources"]

    if resource_id in saved:
        saved.remove(resource_id)
    else:
        saved.add(resource_id)


# ------------------------------------------------------------
# Resource card
# ------------------------------------------------------------

def _card(item):
    name = escape(item["name"])
    summary = escape(item["summary"])
    category = escape(item["category"])
    region = escape(item["region"])

    st.markdown(
        '<div class="sb-card">'
        f'<span class="sb-tag">{item["icon"]} {category}</span>'
        f'<h4>{name}</h4>'
        f'<p>📍 {region}</p>'
        f'<p>{summary}</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns([3, 1], gap="small")

    with left:
        st.button(
            "Explore resource →",
            key=f'open_{item["id"]}',
            use_container_width=True,
            type="primary",
            on_click=_go_to,
            args=(item["id"],),
        )

    with right:
        saved = item["id"] in st.session_state["sb_saved_resources"]

        st.button(
            "★" if saved else "☆",
            key=f'save_{item["id"]}',
            help="Remove bookmark" if saved else "Save resource",
            use_container_width=True,
            on_click=_toggle_bookmark,
            args=(item["id"],),
        )


# ------------------------------------------------------------
# Detailed resource view
# ------------------------------------------------------------

def _details(item):

    st.button(
        "← Back to resources",
        on_click=_back,
    )

    st.markdown(f'## {item["icon"]} {item["name"]}')

    st.caption(
        f'{item["category"]} · {item["region"]}'
    )

    st.markdown(
        f'<div class="sb-detail">{escape(item["summary"])}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("### How this resource may help")

    for help_text in item["helps"]:
        st.markdown(f"- {help_text}")

    tab1, tab2, tab3 = st.tabs([
        "📋 Prepare",
        "💬 Questions",
        "📝 Notes",
    ])

    with tab1:
        st.markdown("**Before visiting the organization**")

        checklist = [
            "Identify the information or support needed",
            "Prepare questions for the transplant care team",
            "Check service availability and eligibility",
        ]

        for index, text in enumerate(checklist):
            st.checkbox(
                text,
                key=f'check_{item["id"]}_{index}',
            )

        st.caption(
            "Checklist selections last only for this session."
        )

    with tab2:
        for question in item["questions"]:
            st.markdown(f"- {question}")

    with tab3:
        st.text_area(
            "Personal notes",
            key=f'notes_{item["id"]}',
            placeholder=(
                "Write general questions or reminders. "
                "Do not enter sensitive medical information."
            ),
            height=130,
        )

        st.caption(
            "Notes are temporary and are not stored in a database."
        )

    st.markdown("### Visit the organization")

    st.link_button(
        "Open official website ↗",
        item["url"],
        type="primary",
        use_container_width=True,
    )

    st.caption(
        "External information and availability are controlled "
        "by the organization. Listings have not been live-verified."
    )

    saved = item["id"] in st.session_state["sb_saved_resources"]

    st.button(
        "★ Remove from saved" if saved else "☆ Save this resource",
        key=f'detail_save_{item["id"]}',
        use_container_width=True,
        on_click=_toggle_bookmark,
        args=(item["id"],),
    )


# ------------------------------------------------------------
# Main resource center
# ------------------------------------------------------------

def render_resource_center():

    st.session_state.setdefault(
        "sb_selected_resource", None
    )

    st.session_state.setdefault(
        "sb_saved_resources", set()
    )

    st.markdown(
        CSS,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sb-hero">'
        '<h2>🌿 Resource Navigation Center</h2>'
        '<p>Explore trusted starting points for transplant '
        'education, donor information, and practical support.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    selected_id = st.session_state["sb_selected_resource"]

    if selected_id:
        selected = next(
            (
                item for item in RESOURCES
                if item["id"] == selected_id
            ),
            None,
        )

        if selected:
            _details(selected)
            return

        st.session_state["sb_selected_resource"] = None

    st.caption(
        "Educational directory only. No donor matching, "
        "eligibility determination, referrals, or medical advice."
    )

    tab_directory, tab_guide, tab_saved = st.tabs([
        "🔎 Explore",
        "🧭 Guided Finder",
        "⭐ Saved",
    ])

    # --------------------------------------------------------
    # Directory tab
    # --------------------------------------------------------

    with tab_directory:

        with st.container(key="sb_resource_filters"):

            qcol, ccol, rcol = st.columns(
                [2, 2, 1.5],
                gap="small",
            )

            with qcol:
                query = st.text_input(
                    "Search resources",
                    placeholder="Search name or support need",
                    key="sb_search",
                )

            with ccol:
                category = st.selectbox(
                    "Category",
                    CATEGORIES,
                    key="sb_category",
                )

            with rcol:
                region = st.selectbox(
                    "Region",
                    ["All Regions"] + sorted(
                        {item["region"] for item in RESOURCES}
                    ),
                    key="sb_region",
                )

        query = query.strip().casefold()

        matches = [
            item for item in RESOURCES
            if (
                category == "All Resources"
                or item["category"] == category
            )
            and (
                region == "All Regions"
                or item["region"] == region
            )
            and (
                not query
                or query in " ".join([
                    item["name"],
                    item["summary"],
                    item["category"],
                    item["region"],
                    *item["helps"],
                ]).casefold()
            )
        ]

        st.caption(
            f"{len(matches)} resources found"
        )

        if not matches:
            st.warning(
                "No resources found. Try a different search or filter."
            )

        with st.container(key="sb_resource_cards"):

            for start in range(0, len(matches), 2):

                cols = st.columns(
                    2,
                    gap="medium",
                )

                for col, item in zip(
                    cols,
                    matches[start:start + 2],
                ):
                    with col:
                        _card(item)

    # --------------------------------------------------------
    # Guided finder
    # --------------------------------------------------------

    with tab_guide:

        st.markdown("### What support are you looking for?")

        need = st.radio(
            "Choose a support category",
            CATEGORIES[1:],
            key="sb_need",
        )

        place = st.selectbox(
            "Region of interest",
            ["Any Region"] + sorted(
                {item["region"] for item in RESOURCES}
            ),
            key="sb_guide_region",
        )

        if st.button(
            "Find resources →",
            type="primary",
            use_container_width=True,
        ):
            st.session_state["sb_guide_results"] = (
                need,
                place,
            )

        if "sb_guide_results" in st.session_state:

            chosen_need, chosen_place = (
                st.session_state["sb_guide_results"]
            )

            suggestions = [
                item for item in RESOURCES
                if item["category"] == chosen_need
                and (
                    chosen_place == "Any Region"
                    or item["region"] in (
                        chosen_place,
                        "International",
                    )
                )
            ]

            st.markdown("#### Suggested starting points")

            if not suggestions:
                st.info(
                    "No matching resources are listed. "
                    "Try another region."
                )

            for item in suggestions:
                st.button(
                    f'{item["icon"]} {item["name"]} →',
                    key=f'guided_{item["id"]}',
                    use_container_width=True,
                    on_click=_go_to,
                    args=(item["id"],),
                )

        st.caption(
            "Suggestions use category and region only, "
            "not medical eligibility or personal circumstances."
        )

    # --------------------------------------------------------
    # Saved resources
    # --------------------------------------------------------

    with tab_saved:

        saved_items = [
            item for item in RESOURCES
            if item["id"] in st.session_state["sb_saved_resources"]
        ]

        if not saved_items:
            st.info(
                "No saved resources yet. "
                "Select ☆ on a resource card to bookmark it."
            )

        else:
            st.caption(
                f"{len(saved_items)} saved resources"
            )

            for item in saved_items:
                st.button(
                    f'{item["icon"]} {item["name"]} →',
                    key=f'saved_{item["id"]}',
                    use_container_width=True,
                    on_click=_go_to,
                    args=(item["id"],),
                )

    st.caption(
        "Bookmarks and notes are session-only. "
        "Check official websites for current information."
    )


# ------------------------------------------------------------
# Standalone testing
# ------------------------------------------------------------

if __name__ == "__main__":

    st.set_page_config(
        page_title="StemBridge Resources",
        page_icon="🌿",
        layout="wide",
        initial_sidebar_state="auto",
    )

    try:
        from mobile_styles import apply_mobile_styles
        apply_mobile_styles()
    except ImportError:
        pass

    render_resource_center()
