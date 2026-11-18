
"""
StemBridge - Interactive Visual Transplant Journey

Features:
- Autologous transplant: 7 stages
- Allogeneic transplant: 8 stages
- Clickable stage cards
- Previous / Next navigation
- Dropdown selection
- Automatic progress percentage
- Visual illustrations
- Detailed educational information
- Tests, questions, and medical terms

This is an educational prototype.
Progress represents navigation through the guide,
not actual medical treatment or recovery.
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
        "heading": "Understanding the Diagnosis",
        "description": """
The transplant journey begins with understanding the
patient's diagnosis and available treatment options.

The medical team explains why a stem cell transplant
may be recommended and discusses possible alternatives.

Not every patient with blood cancer needs a transplant.
""",
        "tests": """
- Medical history review
- Complete blood count (CBC)
- Bone marrow examination when appropriate
- Disease-specific testing
- Review of previous treatments
""",
        "questions": """
- Why is a transplant recommended?
- What other treatments are available?
- What are the possible benefits and risks?
- What should my family know?
""",
        "terms": """
**Stem cell transplant:** A treatment that provides
blood-forming stem cells to restore blood-cell production.
"""
    },
    {
        "icon": "🫀",
        "name": "Evaluation",
        "heading": "Checking Transplant Readiness",
        "description": """
Before transplantation, doctors evaluate whether the
patient is ready for the procedure.

The team reviews overall health, disease status,
organ function, and support needs.

The exact tests vary by patient and transplant center.
""",
        "tests": """
- Complete blood count
- Kidney and liver function tests
- Heart evaluation
- Lung function testing
- Infection screening
- Disease assessment
""",
        "questions": """
- Am I ready for transplantation?
- What do my test results mean?
- What risks apply to my health?
- Will I need to stay near the hospital?
""",
        "terms": """
**CBC:** Complete blood count.

This test measures red blood cells, white blood cells,
and platelets.
"""
    },
    {
        "icon": "🩸",
        "name": "Stem Cell Collection",
        "heading": "Collecting the Patient's Stem Cells",
        "description": """
In an autologous transplant, the patient's own
stem cells are collected.

Medicines may be used to move stem cells from
bone marrow into the bloodstream.

The cells are commonly collected using a process
called apheresis and stored until transplantation.
""",
        "tests": """
- Blood count monitoring
- Mobilization medicines
- Peripheral blood stem cell collection
- Assessment of collected cell quantity
- Cell processing and storage
""",
        "questions": """
- How will stem cells be collected?
- Will collection be painful?
- How long will collection take?
- Could I need more than one collection session?
""",
        "terms": """
**Apheresis:** A process that collects selected
blood components and returns the remaining
components to the patient.
"""
    },
    {
        "icon": "💊",
        "name": "Conditioning",
        "heading": "Preparing for Transplantation",
        "description": """
Conditioning is treatment given before stem cell infusion.

In autologous transplantation, high-dose chemotherapy
is commonly used to treat the underlying disease.

The medical team also provides supportive care
and monitors treatment-related side effects.
""",
        "tests": """
- Blood count monitoring
- Kidney and liver tests
- Infection monitoring
- Side-effect assessment
- Hydration and nutritional support
""",
        "questions": """
- What chemotherapy will I receive?
- What side effects should I expect?
- Will I need hospitalization?
- What symptoms should I report immediately?
""",
        "terms": """
**Conditioning:** Treatment given before
stem cell infusion.
"""
    },
    {
        "icon": "💧",
        "name": "Day 0",
        "heading": "Stem Cell Infusion and Engraftment",
        "description": """
Day 0 is the day the collected stem cells
are returned to the patient.

The cells are infused through a vein,
usually using an intravenous or central line.

After infusion, the transplant team monitors
the patient while waiting for new blood-cell
production to begin.

Engraftment occurs when transplanted cells
begin producing new blood cells.
""",
        "tests": """
- Absolute neutrophil count (ANC)
- Hemoglobin
- Platelet count
- Temperature and infection monitoring
- Infusion-related reactions
""",
        "questions": """
- How is the infusion performed?
- What is engraftment?
- How will doctors know the cells are working?
- Will blood transfusions be needed?
""",
        "terms": """
**Engraftment:** The process in which transplanted
stem cells begin producing new blood cells.

Engraftment does not automatically mean cancer remission.
"""
    },
    {
        "icon": "🏠",
        "name": "Early Recovery",
        "heading": "Monitoring After Transplantation",
        "description": """
After transplantation, patients need
close medical follow-up.

The team monitors blood-cell recovery,
infections, treatment side effects,
and the underlying disease.

The first 100 days are often an important
follow-up period, but recovery can take longer.
""",
        "tests": """
- Complete blood counts
- Infection monitoring
- Kidney and liver tests
- Disease-specific monitoring
- Medication review
""",
        "questions": """
- How frequently are follow-up visits needed?
- Which symptoms require urgent medical attention?
- What precautions should I follow at home?
- When can I resume normal activities?
""",
        "terms": """
**Early recovery:** The period after transplant
when blood counts, symptoms, and complications
are monitored closely.
"""
    },
    {
        "icon": "🌱",
        "name": "Long-Term Care",
        "heading": "Recovery and Survivorship",
        "description": """
Long-term follow-up helps monitor health
after transplantation.

Care may include monitoring for disease recurrence,
late effects of treatment, infections,
and physical or emotional challenges.

Vaccination and wellness plans are determined
by the transplant team.
""",
        "tests": """
- Disease surveillance
- Blood counts
- Organ health monitoring
- Vaccination planning
- Long-term treatment-effect screening
""",
        "questions": """
- How often should I see my transplant team?
- Which vaccinations will I need?
- What long-term complications should I know about?
- When can I return to work or school?
""",
        "terms": """
**Survivorship:** Long-term health and support
following cancer treatment.
"""
    }
]


# ============================================================
# 2. ALLOGENEIC TRANSPLANT STAGES
# ============================================================

ALLO = [
    {
        "icon": "🩺",
        "name": "Diagnosis",
        "heading": "Understanding Donor Transplantation",
        "description": """
The medical team explains the diagnosis
and why an allogeneic stem cell transplant
may be recommended.

In an allogeneic transplant, stem cells
come from a donor rather than the patient.

The team discusses potential benefits,
risks, and other treatment options.
""",
        "tests": """
- Medical history
- Blood tests
- Disease assessment
- Review of previous treatments
""",
        "questions": """
- Why is donor transplantation recommended?
- What are the alternatives?
- What are the major risks?
- How can my family prepare?
""",
        "terms": """
**Allogeneic transplant:** A transplant using
blood-forming stem cells from a donor.
"""
    },
    {
        "icon": "🫀",
        "name": "Evaluation",
        "heading": "Checking Transplant Readiness",
        "description": """
Before transplantation, the team evaluates
the patient's health and disease status.

Doctors review organ function, infections,
previous treatment, and practical support needs.

This helps the team assess transplant suitability.
""",
        "tests": """
- Complete blood count
- Kidney and liver tests
- Heart and lung evaluation
- Infection screening
- Disease-specific testing
""",
        "questions": """
- Am I medically ready for transplantation?
- What tests are needed?
- What risks are most important for me?
- What support will I need?
""",
        "terms": """
**Transplant evaluation:** Medical assessments
used to help determine readiness for transplantation.
"""
    },
    {
        "icon": "🧬",
        "name": "HLA Search",
        "heading": "Finding Possible Donors",
        "description": """
HLA typing helps the transplant team
identify possible donor options.

Potential sources may include family donors,
unrelated donors, and other stem cell sources.

Donor searches are managed by transplant centers
and authorized registry systems.

StemBridge does not search donor registries
or identify donor matches.
""",
        "tests": """
- HLA tissue typing
- Family donor testing when appropriate
- Registry-based donor search
- Donor compatibility evaluation
""",
        "questions": """
- What does HLA matching mean?
- Can a family member be a donor?
- What happens if no closely matched donor is found?
- How long might the donor search take?
""",
        "terms": """
**HLA:** Human leukocyte antigen.

HLA markers help the medical team
assess donor-recipient compatibility.
"""
    },
    {
        "icon": "🤝",
        "name": "Donor Work-Up",
        "heading": "Confirming Donor Suitability",
        "description": """
After identifying possible donor options,
the transplant center performs additional checks.

These may include confirmatory HLA typing,
donor health screening, and collection planning.

The team selects the donor and collection approach
based on medical and logistical considerations.
""",
        "tests": """
- Confirmatory HLA testing
- Donor health assessment
- Infectious disease screening
- Stem cell collection planning
""",
        "questions": """
- How is the final donor selected?
- What medical checks are performed?
- How will donor cells be collected?
- What happens if the selected donor becomes unavailable?
""",
        "terms": """
**Donor work-up:** Medical and logistical
assessments completed before donor cell collection.
"""
    },
    {
        "icon": "💊",
        "name": "Conditioning",
        "heading": "Preparing for Donor Stem Cells",
        "description": """
Conditioning prepares the patient
for donor stem cell transplantation.

Treatment may involve chemotherapy
and sometimes radiation.

The medical team also plans medicines
to reduce infection risks and help prevent
graft-versus-host disease (GVHD).
""",
        "tests": """
- Blood counts
- Kidney and liver monitoring
- Infection surveillance
- Side-effect assessment
- GVHD prevention planning
""",
        "questions": """
- What conditioning treatment will I receive?
- What side effects are possible?
- How will GVHD be prevented?
- How long might hospitalization last?
""",
        "terms": """
**GVHD:** Graft-versus-host disease.

It can occur when donor immune cells
react against the recipient's tissues.
"""
    },
    {
        "icon": "💧",
        "name": "Day 0",
        "heading": "Donor Stem Cell Infusion",
        "description": """
Day 0 is the day donor stem cells
are infused into the patient.

The cells travel through the bloodstream
and may establish blood-cell production
in the bone marrow.

The transplant team closely monitors
blood counts, infection risks, and complications.
""",
        "tests": """
- Absolute neutrophil count (ANC)
- Hemoglobin
- Platelet count
- Temperature monitoring
- Infusion reactions
- Engraftment assessment
""",
        "questions": """
- How will the infusion work?
- How will engraftment be monitored?
- What complications should I know about?
- Which medicines will I receive?
""",
        "terms": """
**Engraftment:** When transplanted stem cells
begin producing new blood cells.
"""
    },
    {
        "icon": "🛡️",
        "name": "Early Recovery",
        "heading": "Monitoring Infection and GVHD",
        "description": """
During early recovery, the team
monitors blood counts, infections,
GVHD symptoms, and medication effects.

Some patients undergo chimerism testing
to assess the proportion of donor-derived
blood cells.

Recovery and follow-up requirements vary.
""",
        "tests": """
- Complete blood count
- Infection monitoring
- GVHD assessment
- Kidney and liver tests
- Chimerism testing when indicated
- Immunosuppressive medication monitoring
""",
        "questions": """
- What symptoms could indicate GVHD?
- What is chimerism testing?
- How frequently are follow-up visits needed?
- What precautions should I follow at home?
""",
        "terms": """
**Chimerism:** A measurement of the proportion
of donor-derived blood cells after transplantation.
"""
    },
    {
        "icon": "🌱",
        "name": "Long-Term Care",
        "heading": "Immune Recovery and Survivorship",
        "description": """
Long-term care focuses on immune recovery,
disease monitoring, and overall health.

Some patients require ongoing monitoring
or treatment for chronic GVHD.

The transplant team may also recommend
vaccination, late-effects screening,
and rehabilitation support.
""",
        "tests": """
- Immune function monitoring
- Disease surveillance
- Chronic GVHD assessment
- Organ health monitoring
- Vaccination planning
- Long-term complication screening
""",
        "questions": """
- How long will immune recovery take?
- What are the signs of chronic GVHD?
- Which vaccinations are recommended?
- How frequently should I attend follow-up visits?
""",
        "terms": """
**Chronic GVHD:** A form of graft-versus-host
disease that can affect patients during
longer-term recovery after allogeneic transplant.
"""
    }
]


# ============================================================
# 3. STYLING
# ============================================================

JOURNEY_CSS = """
<style>
.journey-illustration {
    padding: 28px 14px;
    border-radius: 22px;
    border: 1px solid #d8e9eb;
    background: linear-gradient(120deg, #e6f7f4, #edf4ff);
    text-align: center;
    min-height: 235px;
}

.journey-illustration .big-icon {
    font-size: 85px;
    margin-bottom: 15px;
}

.journey-illustration .heading {
    font-size: 17px;
    font-weight: 800;
    color: #16485b;
}

.journey-illustration .subheading {
    font-size: 12px;
    color: #68818d;
    margin-top: 12px;
}
</style>
"""


# ============================================================
# 4. NAVIGATION CALLBACKS
# ============================================================

def change_stage(state_key, direction, total_stages):
    """
    Move forward or backward safely.

    Called before Streamlit recreates the selectbox.
    """

    current = st.session_state.get(state_key, 0)

    new_stage = current + direction

    st.session_state[state_key] = max(
        0,
        min(total_stages - 1, new_stage)
    )


def select_journey_stage(state_key, stage_index):
    """
    Select a stage by clicking its visual card.
    """

    st.session_state[state_key] = stage_index


# ============================================================
# 5. RENDER INTERACTIVE JOURNEY
# ============================================================

def render_journey(phases, is_allo):
    """
    Main function called from app.py:

        render_journey(phases, is_allo)

    phases:
        Existing stage summaries in app.py.

    is_allo:
        True  = Allogeneic
        False = Autologous
    """

    st.markdown(
        JOURNEY_CSS,
        unsafe_allow_html=True
    )

    if is_allo:
        items = ALLO
        state_key = "journey_allo_select"
    else:
        items = AUTO
        state_key = "journey_auto_select"

    total_stages = len(items)

    # Initialize session state before creating widgets
    if state_key not in st.session_state:
        st.session_state[state_key] = 0

    if not 0 <= st.session_state[state_key] < total_stages:
        st.session_state[state_key] = 0

    # --------------------------------------------------------
    # STAGE DROPDOWN
    # --------------------------------------------------------

    st.markdown("### 🧭 Interactive Transplant Journey")

    st.caption(
        "Click any stage card or use the dropdown "
        "to explore the transplant journey."
    )

    selected = st.selectbox(
        "Select a stage to explore",
        options=list(range(total_stages)),
        format_func=lambda i: (
            f"Stage {i + 1}: {items[i]['name']}"
        ),
        key=state_key
    )

    # --------------------------------------------------------
    # PROGRESS PERCENTAGE
    # --------------------------------------------------------

    current_stage = selected + 1

    percentage = round(
        (current_stage / total_stages) * 100
    )

    st.markdown("### Journey Progress")

    progress_col, percent_col = st.columns(
        [5, 1],
        vertical_alignment="center"
    )

    with progress_col:
        st.progress(
            current_stage / total_stages
        )

    with percent_col:
        st.markdown(
            f"### {percentage}%"
        )

    st.caption(
        f"Stage {current_stage} of {total_stages} "
        "in the educational journey."
    )

    st.info(
        "The percentage represents how far you have navigated "
        "through this educational guide. "
        "It does not represent medical treatment completion "
        "or recovery."
    )

    # --------------------------------------------------------
    # CLICKABLE STAGE CARDS
    # --------------------------------------------------------

    st.markdown("### Click a Stage to View Details")

    cards_per_row = 4

    for start in range(0, total_stages, cards_per_row):

        columns = st.columns(
            cards_per_row,
            gap="small"
        )

        for col_index in range(cards_per_row):

            stage_index = start + col_index

            if stage_index >= total_stages:
                continue

            stage = items[stage_index]

            with columns[col_index]:

                is_selected = (
                    stage_index == selected
                )

                button_label = (
                    f"{stage['icon']}\n\n"
                    f"Stage {stage_index + 1}\n\n"
                    f"{stage['name']}"
                )

                st.button(
                    button_label,
                    key=f"{state_key}_card_{stage_index}",
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
        "The highlighted card shows your currently selected stage."
    )

    # --------------------------------------------------------
    # CURRENT STAGE DETAILS
    # --------------------------------------------------------

    stage = items[selected]

    icon = stage["icon"]
    stage_name = stage["name"]
    stage_heading = stage["heading"]

    st.divider()

    st.markdown(
        f"## Stage {selected + 1}: {stage_name}"
    )

    illustration_col, details_col = st.columns(
        [1, 2],
        gap="large"
    )

    # --------------------------------------------------------
    # STAGE ILLUSTRATION
    # --------------------------------------------------------

    with illustration_col:

        illustration_html = (
            '<div class="journey-illustration" '
            f'role="img" aria-label="{escape(stage_name)}">'
            f'<div class="big-icon">{icon}</div>'
            f'<div class="heading">{escape(stage_heading)}</div>'
            '<div class="subheading">'
            'StemBridge Educational Journey'
            '</div>'
            '</div>'
        )

        st.markdown(
            illustration_html,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # STAGE EXPLANATION
    # --------------------------------------------------------

    with details_col:

        st.markdown(
            "### What Happens During This Stage?"
        )

        st.markdown(
            stage["description"]
        )

        st.markdown(
            "### What to Expect"
        )

        if selected < len(phases):
            st.write(
                phases[selected][1]
            )

    # --------------------------------------------------------
    # EDUCATIONAL TABS
    # --------------------------------------------------------

    st.markdown(
        "### Learn More About This Stage"
    )

    tab1, tab2, tab3, tab4 = st.tabs([
        "🧪 Tests & Monitoring",
        "❓ Questions to Ask",
        "📖 Medical Terms",
        "🔗 Trusted Resources"
    ])

    with tab1:

        st.markdown(
            "#### Common Tests and Monitoring"
        )

        st.markdown(
            stage["tests"]
        )

    with tab2:

        st.markdown(
            "#### Questions for Your Care Team"
        )

        st.markdown(
            stage["questions"]
        )

    with tab3:

        st.markdown(
            "#### Understanding Medical Terms"
        )

        st.markdown(
            stage["terms"]
        )

    with tab4:

        st.write(
            "Explore educational information "
            "from trusted organizations."
        )

        st.link_button(
            "National Cancer Institute ↗",
            "https://www.cancer.gov/about-cancer/treatment/types/stem-cell-transplant"
        )

        st.link_button(
            "American Cancer Society ↗",
            "https://www.cancer.org/cancer/treatment-types/stem-cell-transplant.html"
        )

        if is_allo:

            st.link_button(
                "NMDP Patient Resources ↗",
                "https://www.nmdp.org/patients"
            )

    # --------------------------------------------------------
    # PREVIOUS AND NEXT STAGE BUTTONS
    # --------------------------------------------------------

    st.divider()

    previous_col, next_col = st.columns(2)

    with previous_col:

        st.button(
            "← Previous Stage",
            key=f"{state_key}_previous",
            disabled=(selected == 0),
            use_container_width=True,
            on_click=change_stage,
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
            on_click=change_stage,
            args=(
                state_key,
                1,
                total_stages
            )
        )

    # --------------------------------------------------------
    # COMPLETE JOURNEY SUMMARY
    # --------------------------------------------------------

    with st.expander(
        "📋 View All Journey Stages"
    ):

        for index, item in enumerate(items):

            st.markdown(
                f"**{index + 1}. "
                f"{item['icon']} "
                f"{item['name']}**"
            )

            st.caption(
                item["heading"]
            )

    st.caption(
        "StemBridge is an educational prototype. "
        "The information is not a substitute "
        "for advice from the transplant team."
    )
