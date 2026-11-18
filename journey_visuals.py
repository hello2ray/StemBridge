
"""
StemBridge - Visual Transplant Journey
=====================================

Features:
- Autologous and allogeneic transplant journeys
- Clickable stage cards
- Cross-platform light/dark theme contrast
- Visual three-step process
- Short stage explanations
- Common checks and questions
- Expandable detailed education
- Previous / Next stage navigation
- Accessible native Streamlit controls

Integration:
    from journey_visuals import render_journey
    render_journey(phases, is_allo)

Educational prototype only.
"""

from html import escape
import streamlit as st


# ============================================================
# 1. AUTOLOGOUS TRANSPLANT STAGES
# ============================================================

AUTO = [
    {
        "icon": "🩺",
        "name": "Diagnosis",
        "short": "Understand the treatment plan",
        "color": "#E8F1FF",
        "steps": [
            ("🔎", "Understand diagnosis"),
            ("💬", "Discuss treatment"),
            ("📋", "Plan next steps"),
        ],
        "tests": [
            "Diagnosis-specific tests",
            "Treatment history review",
        ],
        "questions": [
            "Why is transplant being considered?",
            "What alternatives are available?",
        ],
        "detail": (
            "Your team explains the diagnosis, treatment goals, "
            "and why an autologous transplant may be considered."
        ),
        "terms": {
            "Autologous": "Using the patient's own stem cells.",
            "Remission": "A reduction or disappearance of signs of disease.",
        },
    },
    {
        "icon": "🫀",
        "name": "Evaluation",
        "short": "Check transplant readiness",
        "color": "#FFF1E8",
        "steps": [
            ("📄", "Review health"),
            ("🫀", "Check organs"),
            ("🤝", "Plan support"),
        ],
        "tests": [
            "Blood counts",
            "Heart and lung assessments",
            "Infection screening",
        ],
        "questions": [
            "Which tests will I need?",
            "What could change the transplant plan?",
        ],
        "detail": (
            "The transplant team assesses disease status, "
            "organ function, infections, and practical readiness."
        ),
        "terms": {
            "CBC": "Complete blood count.",
            "Conditioning": "Treatment used to prepare for transplant.",
        },
    },
    {
        "icon": "🩸",
        "name": "Stem Cell Collection",
        "short": "Collect and store stem cells",
        "color": "#FFF0F0",
        "steps": [
            ("💉", "Mobilize cells"),
            ("🩸", "Collect cells"),
            ("❄️", "Store cells"),
        ],
        "tests": [
            "Blood counts",
            "Stem cell collection yield",
        ],
        "questions": [
            "How long will collection take?",
            "Will I need a central line?",
        ],
        "detail": (
            "Medicines may move stem cells into the bloodstream. "
            "The cells are collected through apheresis and stored "
            "for later infusion."
        ),
        "terms": {
            "Mobilization": "Moving stem cells into the bloodstream.",
            "Apheresis": "A procedure that separates and collects cells from blood.",
        },
    },
    {
        "icon": "💊",
        "name": "Conditioning",
        "short": "Prepare the body for infusion",
        "color": "#F3ECFF",
        "steps": [
            ("💊", "Start treatment"),
            ("🛡️", "Manage effects"),
            ("📅", "Prepare for Day 0"),
        ],
        "tests": [
            "Blood counts",
            "Organ function",
            "Infection monitoring",
        ],
        "questions": [
            "What side effects should I expect?",
            "Will I stay in the hospital?",
        ],
        "detail": (
            "High-dose treatment prepares the body before "
            "the collected stem cells are returned."
        ),
        "terms": {
            "Conditioning": "Chemotherapy, sometimes with radiation, before transplant.",
            "Supportive care": "Care that helps manage symptoms and complications.",
        },
    },
    {
        "icon": "💧",
        "name": "Day 0",
        "short": "Receive your stem cells",
        "color": "#E8F7FF",
        "steps": [
            ("💧", "Cell infusion"),
            ("🩺", "Monitor"),
            ("🌱", "Watch engraftment"),
        ],
        "tests": [
            "Blood counts",
            "Vital signs",
            "Engraftment monitoring",
        ],
        "questions": [
            "How does the infusion work?",
            "When might engraftment occur?",
        ],
        "detail": (
            "Stored stem cells are infused through a vein. "
            "The transplant team monitors blood-cell recovery "
            "and possible complications."
        ),
        "terms": {
            "Day 0": "The day stem cells are infused.",
            "Engraftment": "When transplanted cells begin producing new blood cells.",
        },
    },
    {
        "icon": "🏠",
        "name": "Early Recovery",
        "short": "Monitor and recover",
        "color": "#FFF5E4",
        "steps": [
            ("🧪", "Check counts"),
            ("📅", "Attend follow-ups"),
            ("🏠", "Follow precautions"),
        ],
        "tests": [
            "Blood counts",
            "Infection checks",
            "Disease response monitoring",
        ],
        "questions": [
            "When should I contact my team?",
            "What precautions apply at home?",
        ],
        "detail": (
            "During early recovery, the team monitors blood counts, "
            "infections, symptoms, and treatment response."
        ),
        "terms": {
            "ANC": "Absolute neutrophil count, a measure of infection-fighting cells.",
            "Platelets": "Blood components that help with clotting.",
        },
    },
    {
        "icon": "🌱",
        "name": "Long-Term Care",
        "short": "Support long-term wellness",
        "color": "#E9F8ED",
        "steps": [
            ("📅", "Follow-up"),
            ("💉", "Review vaccines"),
            ("🌱", "Monitor wellness"),
        ],
        "tests": [
            "Disease surveillance",
            "Long-term health screening",
        ],
        "questions": [
            "What is my follow-up schedule?",
            "When should vaccines be reviewed?",
        ],
        "detail": (
            "Long-term care may include disease monitoring, "
            "vaccination planning, and screening for late effects."
        ),
        "terms": {
            "Survivorship": "Long-term health and well-being after treatment.",
            "Late effects": "Health problems that may appear months or years later.",
        },
    },
]


# ============================================================
# 2. ALLOGENEIC TRANSPLANT STAGES
# ============================================================

ALLO = [
    {
        "icon": "🩺",
        "name": "Diagnosis",
        "short": "Understand the treatment plan",
        "color": "#E8F1FF",
        "steps": [
            ("🔎", "Understand diagnosis"),
            ("💬", "Discuss options"),
            ("📋", "Plan next steps"),
        ],
        "tests": [
            "Diagnosis-specific tests",
            "Treatment history",
        ],
        "questions": [
            "Why is donor transplant considered?",
            "What alternatives are available?",
        ],
        "detail": (
            "The team explains why a donor stem cell transplant "
            "may be recommended and discusses benefits and risks."
        ),
        "terms": {
            "Allogeneic": "A transplant using stem cells from a donor.",
            "Remission": "A reduction or disappearance of signs of disease.",
        },
    },
    {
        "icon": "🫀",
        "name": "Evaluation",
        "short": "Check transplant readiness",
        "color": "#FFF1E8",
        "steps": [
            ("📄", "Review health"),
            ("🫀", "Assess organs"),
            ("🤝", "Plan support"),
        ],
        "tests": [
            "Blood counts",
            "Infection screening",
            "Heart and lung assessments",
        ],
        "questions": [
            "Which tests are required?",
            "What could affect the timeline?",
        ],
        "detail": (
            "The transplant team evaluates disease status, "
            "organ function, infection risk, and readiness."
        ),
        "terms": {
            "CBC": "Complete blood count.",
            "HLA": "Human leukocyte antigen, used in donor compatibility assessment.",
        },
    },
    {
        "icon": "🧬",
        "name": "HLA Search",
        "short": "Explore donor options",
        "color": "#F0EDFF",
        "steps": [
            ("🧬", "HLA typing"),
            ("🔎", "Search donors"),
            ("🤝", "Review options"),
        ],
        "tests": [
            "HLA typing",
            "Donor compatibility assessment",
        ],
        "questions": [
            "Which donor options are available?",
            "Who coordinates the donor search?",
        ],
        "detail": (
            "HLA typing helps the transplant team evaluate "
            "potential related and unrelated donors."
        ),
        "terms": {
            "HLA matching": "Comparison of tissue markers relevant to donor compatibility.",
            "Donor registry": "A system supporting searches for potential stem cell donors.",
        },
    },
    {
        "icon": "🤝",
        "name": "Donor Work-Up",
        "short": "Prepare the donor",
        "color": "#E8F7F2",
        "steps": [
            ("🧬", "Confirm match"),
            ("🩺", "Screen donor"),
            ("🩸", "Plan collection"),
        ],
        "tests": [
            "Confirmatory HLA typing",
            "Donor health screening",
        ],
        "questions": [
            "How is the donor selected?",
            "How will donor cells be collected?",
        ],
        "detail": (
            "The transplant center coordinates donor selection, "
            "health screening, and collection arrangements."
        ),
        "terms": {
            "Donor work-up": "Evaluation before stem cell donation.",
            "Apheresis": "A blood-cell collection procedure.",
        },
    },
    {
        "icon": "💊",
        "name": "Conditioning",
        "short": "Prepare for donor cells",
        "color": "#F3ECFF",
        "steps": [
            ("💊", "Start treatment"),
            ("🛡️", "Manage effects"),
            ("📅", "Prepare Day 0"),
        ],
        "tests": [
            "Blood counts",
            "Organ function",
            "Infection monitoring",
        ],
        "questions": [
            "What are the main risks?",
            "How is GVHD prevented?",
        ],
        "detail": (
            "Chemotherapy, sometimes with radiation, "
            "prepares the body to receive donor stem cells."
        ),
        "terms": {
            "Conditioning": "Treatment before the stem cell infusion.",
            "GVHD": "Graft-versus-host disease.",
        },
    },
    {
        "icon": "💧",
        "name": "Day 0",
        "short": "Receive donor stem cells",
        "color": "#E8F7FF",
        "steps": [
            ("💧", "Cell infusion"),
            ("🩺", "Monitor"),
            ("🌱", "Watch engraftment"),
        ],
        "tests": [
            "Blood counts",
            "Vital signs",
            "Engraftment monitoring",
        ],
        "questions": [
            "What happens during infusion?",
            "How will engraftment be assessed?",
        ],
        "detail": (
            "Donor stem cells are infused. The team monitors "
            "engraftment and possible complications."
        ),
        "terms": {
            "Day 0": "The day donor stem cells are infused.",
            "Engraftment": "When transplanted cells begin producing new blood cells.",
        },
    },
    {
        "icon": "🏠",
        "name": "Early Recovery",
        "short": "Monitor GVHD and recovery",
        "color": "#FFF5E4",
        "steps": [
            ("🛡️", "Prevent infections"),
            ("🩺", "Monitor GVHD"),
            ("📅", "Attend follow-ups"),
        ],
        "tests": [
            "Blood counts",
            "Chimerism testing",
            "GVHD assessment",
        ],
        "questions": [
            "Which symptoms require urgent contact?",
            "How are medicines managed?",
        ],
        "detail": (
            "Close monitoring includes blood counts, infection risk, "
            "GVHD, and donor-cell chimerism."
        ),
        "terms": {
            "GVHD": "A condition where donor immune cells attack recipient tissues.",
            "Chimerism": "A measure of donor-derived and recipient-derived blood cells.",
        },
    },
    {
        "icon": "🌱",
        "name": "Long-Term Care",
        "short": "Support immune recovery",
        "color": "#E9F8ED",
        "steps": [
            ("🛡️", "Immune recovery"),
            ("💉", "Review vaccines"),
            ("🌱", "Long-term follow-up"),
        ],
        "tests": [
            "Disease surveillance",
            "Chronic GVHD monitoring",
            "Long-term health screening",
        ],
        "questions": [
            "What follow-up is needed?",
            "When should vaccines be reviewed?",
        ],
        "detail": (
            "Long-term monitoring includes immune recovery, "
            "GVHD, disease surveillance, and late effects."
        ),
        "terms": {
            "Chronic GVHD": "GVHD that can affect multiple organs over time.",
            "Immune recovery": "The gradual rebuilding of immune defenses after transplant.",
        },
    },
]


# ============================================================
# 3. CROSS-PLATFORM CSS
# ============================================================

JOURNEY_CSS = """
<style>

/* Keep button contrast explicit across light/dark themes. */

.st-key-journey_stage_cards button[kind="secondary"],
.st-key-journey_stage_cards button[data-testid="stBaseButton-secondary"] {
    background: #FFFFFF !important;
    color: #18354A !important;
    border: 1.5px solid #D9E8ED !important;
    border-radius: 16px !important;
    min-height: 116px !important;
    width: 100% !important;
    white-space: pre-line !important;
    box-shadow: 0 6px 18px rgba(21,57,75,0.07) !important;
}

.st-key-journey_stage_cards button[kind="primary"],
.st-key-journey_stage_cards button[data-testid="stBaseButton-primary"] {
    background: #087E83 !important;
    color: #FFFFFF !important;
    border: 2px solid #087E83 !important;
    border-radius: 16px !important;
    min-height: 116px !important;
    width: 100% !important;
    white-space: pre-line !important;
    box-shadow: 0 8px 22px rgba(8,126,131,0.22) !important;
}

.st-key-journey_stage_cards button p,
.st-key-journey_stage_cards button span,
.st-key-journey_stage_cards button div {
    color: inherit !important;
    opacity: 1 !important;
    font-weight: 700 !important;
    line-height: 1.45 !important;
    text-align: center !important;
}

.st-key-journey_stage_cards button:hover {
    transform: translateY(-2px);
    border-color: #079A98 !important;
}

.jv-panel {
    background: linear-gradient(125deg, #F2FAFB, #FFFFFF);
    border: 1px solid #D8ECEC;
    border-radius: 22px;
    padding: 23px 25px;
    margin: 14px 0 18px;
}

.jv-hero {
    display: flex;
    align-items: center;
    gap: 18px;
    flex-wrap: wrap;
}

.jv-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 94px;
    height: 94px;
    border-radius: 25px;
    font-size: 49px;
    flex-shrink: 0;
}

.jv-title {
    font-size: clamp(1.5rem, 3vw, 2.25rem);
    font-weight: 800;
    color: #163B4B;
    line-height: 1.15;
}

.jv-subtitle {
    font-size: 1rem;
    color: #52717B;
    margin-top: 8px;
}

.jv-eyebrow {
    font-size: 0.76rem;
    letter-spacing: 0.13em;
    font-weight: 800;
    color: #087E83;
    margin-bottom: 9px;
}

.jv-step {
    border-radius: 14px;
    background: #E8F6F5;
    padding: 14px 9px;
    color: #145B61;
    text-align: center;
    font-weight: 700;
    min-height: 75px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 6px;
}

.jv-step-icon {
    font-size: 27px;
}

.jv-arrow {
    text-align: center;
    color: #159C97;
    font-size: 1.5rem;
    padding-top: 28px;
}

@media(max-width: 650px) {
    .jv-panel {
        padding: 17px;
    }

    .jv-icon {
        width: 70px;
        height: 70px;
        font-size: 35px;
    }

    .jv-step {
        padding: 10px 5px;
        font-size: 12px;
    }
}

</style>
"""


# ============================================================
# 4. STAGE NAVIGATION CALLBACKS
# ============================================================

def select_journey_stage(state_key, stage_index):
    """Select a stage before the next Streamlit render."""
    st.session_state[state_key] = stage_index


def move_journey_stage(state_key, direction, total_stages):
    """Move to the previous or next stage safely."""
    current = st.session_state.get(state_key, 0)

    new_stage = current + direction

    st.session_state[state_key] = max(
        0,
        min(total_stages - 1, new_stage)
    )


# ============================================================
# 5. VISUAL STAGE HEADER
# ============================================================

def render_stage_header(stage, selected, total, is_allo):

    transplant_label = (
        "DONOR TRANSPLANT"
        if is_allo
        else "OWN-CELL TRANSPLANT"
    )

    html = (
        '<div class="jv-panel">'
        '<div class="jv-eyebrow">'
        f'STAGE {selected + 1} OF {total} · {transplant_label}'
        '</div>'
        '<div class="jv-hero">'
        f'<div class="jv-icon" style="background:{stage["color"]}">'
        f'{stage["icon"]}'
        '</div>'
        '<div>'
        f'<div class="jv-title">{escape(stage["name"])}</div>'
        f'<div class="jv-subtitle">{escape(stage["short"])}</div>'
        '</div>'
        '</div>'
        '</div>'
    )

    st.markdown(
        html,
        unsafe_allow_html=True
    )


# ============================================================
# 6. THREE-STEP VISUAL PROCESS
# ============================================================

def render_visual_steps(stage):

    st.markdown("#### What Happens at This Stage?")

    columns = st.columns(
        [4, 1, 4, 1, 4],
        gap="small"
    )

    for index, (icon, label) in enumerate(stage["steps"]):

        with columns[index * 2]:

            html = (
                '<div class="jv-step">'
                f'<div class="jv-step-icon">{icon}</div>'
                f'<div>{escape(label)}</div>'
                '</div>'
            )

            st.markdown(
                html,
                unsafe_allow_html=True
            )

        if index < 2:

            with columns[index * 2 + 1]:

                st.markdown(
                    '<div class="jv-arrow">→</div>',
                    unsafe_allow_html=True
                )


# ============================================================
# 7. COMPACT INFORMATION PANELS
# ============================================================

def render_information_panels(stage):

    left, right = st.columns(
        2,
        gap="medium"
    )

    with left:

        with st.container(border=True):

            st.markdown("**🔬 Common Checks**")

            for item in stage["tests"]:
                st.markdown(f"- {item}")

    with right:

        with st.container(border=True):

            st.markdown("**💬 Ask Your Care Team**")

            for question in stage["questions"]:
                st.markdown(f"- {question}")


# ============================================================
# 8. EXPANDABLE MEDICAL INFORMATION
# ============================================================

def render_more_information(stage, phases, selected):

    with st.expander(
        "📖 More Details & Medical Terms",
        expanded=False
    ):

        st.markdown("#### Stage Overview")

        st.write(stage["detail"])

        if phases and selected < len(phases):

            phase = phases[selected]

            if len(phase) > 1:
                st.write(phase[1])

        st.markdown("#### Medical Terms")

        for term, explanation in stage["terms"].items():

            st.markdown(
                f"**{term}:** {explanation}"
            )

        st.info(
            "These explanations are educational. "
            "Your transplant team determines the "
            "appropriate tests and treatment plan."
        )


# ============================================================
# 9. MAIN RENDER FUNCTION
# ============================================================

def render_journey(phases, is_allo):
    """
    Render the complete interactive transplant journey.

    Parameters
    ----------
    phases:
        Existing journey phase tuples from app.py.

    is_allo:
        True for allogeneic transplant.
        False for autologous transplant.
    """

    stages = ALLO if is_allo else AUTO

    total_stages = len(stages)

    state_key = (
        "journey_allo_select"
        if is_allo
        else "journey_auto_select"
    )

    # Initialize state before creating the selectbox.
    if state_key not in st.session_state:
        st.session_state[state_key] = 0

    current = st.session_state[state_key]

    if not isinstance(current, int):
        current = 0

    st.session_state[state_key] = max(
        0,
        min(total_stages - 1, current)
    )

    # Apply journey-specific styling.
    st.markdown(
        JOURNEY_CSS,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # STAGE SELECTOR
    # --------------------------------------------------------

    selected = st.selectbox(
        "Jump to a Stage",
        options=list(range(total_stages)),
        format_func=lambda i: (
            f"Stage {i + 1}: {stages[i]['name']}"
        ),
        key=state_key
    )

    stage = stages[selected]

    # --------------------------------------------------------
    # PROGRESS
    # --------------------------------------------------------

    st.markdown("#### Journey Guide Position")

    st.progress(
        (selected + 1) / total_stages
    )

    st.caption(
        f"Viewing Stage {selected + 1} of {total_stages}. "
        "This shows navigation through the guide, "
        "not medical treatment progress."
    )

    # --------------------------------------------------------
    # CLICKABLE STAGE CARDS
    # --------------------------------------------------------

    st.markdown("#### Click a Stage to View Details")

    with st.container(
        key="journey_stage_cards"
    ):

        cards_per_row = 4

        for start in range(
            0,
            total_stages,
            cards_per_row
        ):

            columns = st.columns(
                cards_per_row,
                gap="small"
            )

            for offset, col in enumerate(columns):

                stage_index = start + offset

                if stage_index >= total_stages:
                    continue

                item = stages[stage_index]

                with col:

                    is_selected = (
                        stage_index == selected
                    )

                    label = (
                        f'{item["icon"]}\n'
                        f'Stage {stage_index + 1}\n'
                        f'{item["name"]}'
                    )

                    st.button(
                        label,
                        key=(
                            f"{state_key}_card_"
                            f"{stage_index}"
                        ),
                        use_container_width=True,
                        type=(
                            "primary"
                            if is_selected
                            else "secondary"
                        ),
                        on_click=select_journey_stage,
                        args=(
                            state_key,
                            stage_index
                        )
                    )

    st.caption(
        "Select any stage above to explore its details."
    )

    st.divider()

    # --------------------------------------------------------
    # VISUAL STAGE HEADER
    # --------------------------------------------------------

    render_stage_header(
        stage,
        selected,
        total_stages,
        is_allo
    )

    # --------------------------------------------------------
    # VISUAL PROCESS
    # --------------------------------------------------------

    render_visual_steps(stage)

    # --------------------------------------------------------
    # SHORT DESCRIPTION
    # --------------------------------------------------------

    st.caption(
        stage["detail"]
    )

    # --------------------------------------------------------
    # INFORMATION PANELS
    # --------------------------------------------------------

    render_information_panels(stage)

    # --------------------------------------------------------
    # EXPANDABLE DETAILS
    # --------------------------------------------------------

    render_more_information(
        stage,
        phases,
        selected
    )

    st.divider()

    # --------------------------------------------------------
    # PREVIOUS / NEXT BUTTONS
    # --------------------------------------------------------

    previous_col, next_col = st.columns(2)

    with previous_col:

        st.button(
            "← Previous Stage",
            key=f"{state_key}_previous",
            disabled=(selected == 0),
            use_container_width=True,
            on_click=move_journey_stage,
            args=(
                state_key,
                -1,
                total_stages
            )
        )

    with next_col:

        st.button(
            "Next Stage →",
            key=f"{state_key}_next",
            disabled=(
                selected == total_stages - 1
            ),
            use_container_width=True,
            type="primary",
            on_click=move_journey_stage,
            args=(
                state_key,
                1,
                total_stages
            )
        )

    st.caption(
        "StemBridge is an educational guide. "
        "The sequence, tests, and timing may differ "
        "for individual patients. Follow your "
        "transplant team's instructions."
    )


# ============================================================
# 10. STANDALONE TEST
# ============================================================

if __name__ == "__main__":

    st.set_page_config(
        page_title="StemBridge Journey",
        page_icon="🧬",
        layout="wide"
    )

    st.title("🧬 StemBridge Transplant Journey")

    transplant_type = st.radio(
        "Select Transplant Type",
        [
            "Autologous",
            "Allogeneic"
        ],
        horizontal=True
    )

    is_allo = (
        transplant_type == "Allogeneic"
    )

    stages = ALLO if is_allo else AUTO

    example_phases = [
        (
            stage["name"],
            stage["detail"]
        )
        for stage in stages
    ]

    render_journey(
        example_phases,
        is_allo
    )
