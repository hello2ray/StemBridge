
"""StemBridge visual journey. Drop-in replacement; render_journey(phases, is_allo)."""

from html import escape
import streamlit as st


AUTO = [
    dict(
        icon='🩺',
        name='Diagnosis',
        short='Understand the plan',
        color='#e8f1ff',
        steps=[
            'Understand diagnosis',
            'Discuss treatment options',
            'Plan next steps'
        ],
        tests=[
            'Diagnosis-specific tests',
            'Treatment history review'
        ],
        ask=[
            'Why is a transplant being considered?',
            'What other treatments are possible?'
        ],
        detail='Your team explains the diagnosis, goals of treatment, and whether a transplant may be appropriate.'
    ),
    dict(
        icon='🫀',
        name='Evaluation',
        short='Check transplant readiness',
        color='#fff1e8',
        steps=[
            'Review medical history',
            'Check heart and lungs',
            'Discuss support needs'
        ],
        tests=[
            'Blood counts and organ function',
            'Infection screening',
            'Heart and lung assessments'
        ],
        ask=[
            'Which tests do I need?',
            'What could change the plan?'
        ],
        detail='The transplant team assesses overall health, disease status, and practical readiness.'
    ),
    dict(
        icon='🩸',
        name='Stem Cell Collection',
        short='Collect and store cells',
        color='#fff0f0',
        steps=[
            'Mobilize stem cells',
            'Collect by apheresis',
            'Store collected cells'
        ],
        tests=[
            'Blood counts',
            'Collection yield'
        ],
        ask=[
            'How long will collection take?',
            'Will I need a central line?'
        ],
        detail='Medicines may help move stem cells into the bloodstream. The cells are collected and stored for later infusion.'
    ),
    dict(
        icon='💊',
        name='Conditioning',
        short='Prepare for infusion',
        color='#f3ecff',
        steps=[
            'Start conditioning',
            'Manage side effects',
            'Prepare for Day 0'
        ],
        tests=[
            'Blood counts',
            'Organ function',
            'Infection monitoring'
        ],
        ask=[
            'What side effects should I expect?',
            'Will I be in hospital?'
        ],
        detail='High-dose treatment prepares the body before the collected cells are returned.'
    ),
    dict(
        icon='💧',
        name='Day 0',
        short='Receive stem cells',
        color='#e8f7ff',
        steps=[
            'Stem cell infusion',
            'Supportive monitoring',
            'Watch for engraftment'
        ],
        tests=[
            'Blood counts',
            'Vital signs',
            'Infection monitoring'
        ],
        ask=[
            'How does the infusion work?',
            'How will we know engraftment has started?'
        ],
        detail='Stored stem cells are infused through a vein. The team monitors blood-cell recovery and complications.'
    ),
    dict(
        icon='🏠',
        name='Early Recovery',
        short='Monitor and recover',
        color='#fff5e4',
        steps=[
            'Monitor blood counts',
            'Attend follow-ups',
            'Follow safety guidance'
        ],
        tests=[
            'Blood counts',
            'Infection checks',
            'Disease response'
        ],
        ask=[
            'When should I call the care team?',
            'What precautions apply at home?'
        ],
        detail='The team monitors recovery closely, particularly during the early months after transplant.'
    ),
    dict(
        icon='🌱',
        name='Long-Term Care',
        short='Plan ongoing wellness',
        color='#e9f8ed',
        steps=[
            'Long-term follow-up',
            'Review vaccines',
            'Monitor late effects'
        ],
        tests=[
            'Disease surveillance',
            'Long-term health screening'
        ],
        ask=[
            'What is my follow-up schedule?',
            'When should vaccines be reviewed?'
        ],
        detail='Long-term follow-up may include disease monitoring, revaccination, and attention to late effects.'
    ),
]


ALLO = [
    dict(
        icon='🩺',
        name='Diagnosis',
        short='Understand the plan',
        color='#e8f1ff',
        steps=[
            'Understand diagnosis',
            'Discuss transplant options',
            'Plan next steps'
        ],
        tests=[
            'Diagnosis-specific tests',
            'Treatment history'
        ],
        ask=[
            'Why a donor transplant?',
            'What alternatives are available?'
        ],
        detail='The care team explains why donor stem cell transplantation may be considered.'
    ),
    dict(
        icon='🫀',
        name='Evaluation',
        short='Check readiness',
        color='#fff1e8',
        steps=[
            'Review health',
            'Assess organs',
            'Plan support'
        ],
        tests=[
            'Blood counts',
            'Infection screening',
            'Heart and lung assessments'
        ],
        ask=[
            'Which tests do I need?',
            'What could change the timeline?'
        ],
        detail='The team assesses disease status, health, and practical readiness.'
    ),
    dict(
        icon='🧬',
        name='HLA Search',
        short='Explore donor options',
        color='#f0edff',
        steps=[
            'HLA typing',
            'Review donor sources',
            'Coordinate donor search'
        ],
        tests=[
            'HLA typing',
            'Donor compatibility review'
        ],
        ask=[
            'Which donor options are available?',
            'Who coordinates the search?'
        ],
        detail='HLA tissue typing helps the team evaluate related and unrelated donor options.'
    ),
    dict(
        icon='🤝',
        name='Donor Work-Up',
        short='Prepare the donor',
        color='#e8f7f2',
        steps=[
            'Confirm donor match',
            'Complete donor screening',
            'Plan collection'
        ],
        tests=[
            'Confirmatory typing',
            'Donor health screening'
        ],
        ask=[
            'How is the donor selected?',
            'How are cells collected?'
        ],
        detail='The transplant team confirms the donor plan and coordinates screening and collection.'
    ),
    dict(
        icon='💊',
        name='Conditioning',
        short='Prepare for infusion',
        color='#f3ecff',
        steps=[
            'Begin conditioning',
            'Manage side effects',
            'Prepare for Day 0'
        ],
        tests=[
            'Blood counts',
            'Organ function',
            'Infection monitoring'
        ],
        ask=[
            'What are the main risks?',
            'How is GVHD prevented?'
        ],
        detail='Chemotherapy, sometimes with radiation, prepares the body for donor stem cells.'
    ),
    dict(
        icon='💧',
        name='Day 0',
        short='Receive donor cells',
        color='#e8f7ff',
        steps=[
            'Donor cell infusion',
            'Monitor closely',
            'Watch for engraftment'
        ],
        tests=[
            'Blood counts',
            'Vital signs',
            'Engraftment monitoring'
        ],
        ask=[
            'What happens during infusion?',
            'How will engraftment be assessed?'
        ],
        detail='Donor stem cells are infused. The team monitors recovery and possible complications.'
    ),
    dict(
        icon='🏠',
        name='Early Recovery',
        short='Monitor GVHD and recovery',
        color='#fff5e4',
        steps=[
            'Monitor infections',
            'Watch for GVHD',
            'Attend follow-ups'
        ],
        tests=[
            'Blood counts',
            'Chimerism',
            'GVHD assessment'
        ],
        ask=[
            'What symptoms require a call?',
            'How are medicines managed?'
        ],
        detail='Close monitoring includes blood counts, infection risk, GVHD, and donor-cell chimerism.'
    ),
    dict(
        icon='🌱',
        name='Long-Term Care',
        short='Support immune recovery',
        color='#e9f8ed',
        steps=[
            'Monitor immune recovery',
            'Review vaccines',
            'Long-term follow-up'
        ],
        tests=[
            'Disease surveillance',
            'Chronic GVHD assessment',
            'Long-term screening'
        ],
        ask=[
            'What follow-up is needed?',
            'When should vaccines be reviewed?'
        ],
        detail='Immune recovery and monitoring for GVHD and late effects can continue for a long time.'
    ),
]


CSS = """
<style>
/* Journey-specific styles */
.st-key-journey_stage_cards button,
.st-key-journey_stage_cards button[kind="secondary"],
.st-key-journey_stage_cards button[data-testid="stBaseButton-secondary"] {
    background: #ffffff !important;
    color: #18354a !important;
    border: 1.5px solid #d9e8ed !important;
    border-radius: 17px !important;
    min-height: 112px !important;
    width: 100% !important;
    white-space: pre-line !important;
    box-shadow: 0 6px 18px rgba(21,57,75,.06) !important;
    transition: transform .12s ease, border-color .12s ease !important;
}

.st-key-journey_stage_cards button[kind="primary"],
.st-key-journey_stage_cards button[data-testid="stBaseButton-primary"] {
    background: #087e83 !important;
    color: #ffffff !important;
    border: 2px solid #087e83 !important;
    border-radius: 17px !important;
    min-height: 112px !important;
    width: 100% !important;
    white-space: pre-line !important;
    box-shadow: 0 8px 22px rgba(8,126,131,.22) !important;
}

.st-key-journey_stage_cards button p,
.st-key-journey_stage_cards button span,
.st-key-journey_stage_cards button div {
    color: inherit !important;
    opacity: 1 !important;
    font-weight: 700 !important;
    line-height: 1.5 !important;
    text-align: center !important;
}

.st-key-journey_stage_cards button:hover {
    transform: translateY(-2px);
    border-color: #079a98 !important;
}

.jv-panel {
    background: linear-gradient(125deg,#f2fafb,#ffffff);
    border: 1px solid #d8ecec;
    border-radius: 22px;
    padding: 23px 25px;
    margin: 12px 0 18px;
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
    font-size: clamp(1.5rem,3vw,2.25rem);
    font-weight: 800;
    color: #163b4b;
    line-height: 1.15;
}

.jv-subtitle {
    font-size: 1rem;
    color: #52717b;
    margin-top: 8px;
}

.jv-eyebrow {
    font-size: .76rem;
    letter-spacing: .13em;
    font-weight: 800;
    color: #087e83;
    margin-bottom: 9px;
}

.jv-step {
    border-radius: 14px;
    background: #e8f6f5;
    padding: 13px 9px;
    color: #145b61;
    text-align: center;
    font-weight: 700;
    min-height: 64px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.jv-arrow {
    text-align: center;
    color: #159c97;
    font-size: 1.5rem;
    padding-top: 13px;
}

@media (max-width: 650px) {
    .jv-panel {
        padding: 17px;
    }

    .jv-icon {
        width: 70px;
        height: 70px;
        font-size: 35px;
    }
}

@media (max-width: 767px) {
    .st-key-journey_stage_cards [data-testid="stHorizontalBlock"] {
        display: grid !important;
        grid-template-columns: repeat(2,minmax(0,1fr)) !important;
        gap: 9px !important;
    }

    .st-key-journey_stage_cards
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
        width: auto !important;
        min-width: 0 !important;
        flex: none !important;
    }

    .st-key-journey_stage_cards button {
        min-height: 100px !important;
        font-size: .83rem !important;
    }
}
</style>
"""


def _select_stage(state_key, index):
    st.session_state[state_key] = index


def _move_stage(state_key, amount, count):
    current = st.session_state.get(state_key, 0)
    st.session_state[state_key] = max(
        0,
        min(count - 1, current + amount)
    )


def render_journey(phases, is_allo):
    """Interactive visual journey compatible with existing app.py."""

    stages = ALLO if is_allo else AUTO
    count = len(stages)

    state_key = (
        'journey_allo_select'
        if is_allo
        else 'journey_auto_select'
    )

    if (
        state_key not in st.session_state
        or not isinstance(st.session_state[state_key], int)
    ):
        st.session_state[state_key] = 0

    st.session_state[state_key] = max(
        0,
        min(count - 1, st.session_state[state_key])
    )

    st.markdown(CSS, unsafe_allow_html=True)

    # Native stage selector
    selected = st.selectbox(
        'Jump to a stage',
        list(range(count)),
        format_func=lambda i: f'{i+1}. {stages[i]["name"]}',
        key=state_key
    )

    stage = stages[selected]

    st.markdown('#### Explore the journey')

    # This measures guide navigation, not medical recovery.
    st.progress((selected + 1) / count)

    st.caption(
        f'Viewing stage {selected+1} of {count} · '
        'This is guide navigation, not medical progress.'
    )

    # Clickable stage cards
    st.markdown('#### Select any stage')

    with st.container(key='journey_stage_cards'):

        for start in range(0, count, 4):

            cols = st.columns(4, gap='small')

            for offset, col in enumerate(cols):

                idx = start + offset

                if idx >= count:
                    continue

                item = stages[idx]

                with col:

                    st.button(
                        f'{item["icon"]}\n'
                        f'Stage {idx+1}\n'
                        f'{item["name"]}',
                        key=f'{state_key}_card_{idx}',
                        use_container_width=True,
                        type=(
                            'primary'
                            if idx == selected
                            else 'secondary'
                        ),
                        on_click=_select_stage,
                        args=(state_key, idx)
                    )

    # Visual stage hero
    st.markdown(
        '<div class="jv-panel">'
        '<div class="jv-eyebrow">'
        f'STAGE {selected+1} OF {count} · '
        f'{"DONOR" if is_allo else "OWN-CELL"} TRANSPLANT'
        '</div>'
        '<div class="jv-hero">'
        f'<div class="jv-icon" '
        f'style="background:{stage["color"]}">'
        f'{stage["icon"]}'
        '</div>'
        '<div>'
        f'<div class="jv-title">'
        f'{escape(stage["name"])}'
        '</div>'
        f'<div class="jv-subtitle">'
        f'{escape(stage["short"])}'
        '</div>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # Three-step process
    st.markdown('#### What happens at this stage?')

    step_cols = st.columns(
        [4, 1, 4, 1, 4],
        gap='small'
    )

    for idx, text in enumerate(stage['steps']):

        with step_cols[idx * 2]:

            st.markdown(
                f'<div class="jv-step">'
                f'{escape(text)}'
                '</div>',
                unsafe_allow_html=True
            )

        if idx < 2:

            with step_cols[idx * 2 + 1]:

                st.markdown(
                    '<div class="jv-arrow">→</div>',
                    unsafe_allow_html=True
                )

    st.caption(stage['detail'])

    # Compact information panels
    left, right = st.columns(2, gap='medium')

    with left:

        with st.container(border=True):

            st.markdown('**🔬 Common checks**')

            for test in stage['tests']:
                st.markdown(f'• {test}')

    with right:

        with st.container(border=True):

            st.markdown('**💬 Ask your care team**')

            for question in stage['ask']:
                st.markdown(f'• {question}')

    # Expandable details
    with st.expander('📖 More detail and medical terms'):

        st.write(stage['detail'])

        if phases and selected < len(phases):
            st.write(phases[selected][1])

        if is_allo and selected >= 5:
            st.write(
                '**GVHD:** Graft-versus-host disease occurs '
                'when donor immune cells attack the '
                'recipient’s tissues. The transplant team '
                'manages prevention and monitoring.'
            )

        if selected >= (5 if is_allo else 4):
            st.write(
                '**Engraftment:** Transplanted cells begin '
                'producing new blood cells. Engraftment '
                'is not the same as cancer remission.'
            )

    # Navigation
    previous, next_col = st.columns(2)

    with previous:

        st.button(
            '← Previous stage',
            key=f'{state_key}_prev',
            disabled=selected == 0,
            use_container_width=True,
            on_click=_move_stage,
            args=(state_key, -1, count)
        )

    with next_col:

        st.button(
            'Next stage →',
            key=f'{state_key}_next',
            disabled=selected == count - 1,
            use_container_width=True,
            type='primary',
            on_click=_move_stage,
            args=(state_key, 1, count)
        )

    st.caption(
        'Educational overview only. Stage order and '
        'tests vary by patient and center; follow '
        'your transplant team’s guidance.'
    )
