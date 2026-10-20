"""Official NMDP reference links only; no external API or campaign creation."""
import streamlit as st

SEARCH = 'https://network.nmdp.org/services-support/transplant-centers/search-services'
FIND_DONOR = 'https://www.nmdp.org/patients/understanding-transplant/finding-a-donor'
JOIN = 'https://my.nmdp.org/s/join'
FUNDRAISE = 'https://www.nmdp.org/en/get-involved/fundraise'
FUNDRAISE_START = 'https://fundraise.nmdp.org/events/889'


def render_nmdp_features(patient_id: str, transplant_type: str, questions: list):
    st.title('🔎 Match Finder | NMDP Resources')
    st.caption('Official NMDP reference links only. No donor search, API connection, or campaign submission inside StemBridge.')
    donor_tab, awareness_tab, fundraiser_tab = st.tabs([
        '🧬 Donor search', '📣 Donor campaign', '💚 NMDP fundraiser'
    ])
    with donor_tab:
        st.subheader('Find a stem cell donor')
        if 'Autologous' in transplant_type:
            st.info('Your demo journey uses your own stem cells. Donor searching generally applies to allogeneic transplants. Ask your transplant team about your plan.')
        else:
            st.write('A transplant center coordinates HLA testing, donor searching, and donor selection. StemBridge cannot view or determine donor matches.')
        st.link_button('NMDP: Finding a donor ↗', FIND_DONOR, use_container_width=True)
        st.link_button('NMDP: Search services for transplant centers ↗', SEARCH, use_container_width=True)
        st.caption('The search-services link is intended for transplant professionals, not a patient donor-search tool.')
    with awareness_tab:
        st.subheader('Donor recruitment / awareness campaign')
        st.write('NMDP offers information for patients and families who want to raise awareness and encourage potential donors to join the registry. NMDP handles any official recruitment process.')
        st.link_button('NMDP: Finding a donor and patient support ↗', FIND_DONOR, use_container_width=True)
        st.link_button('NMDP: Join the donor registry ↗', JOIN, use_container_width=True)
        st.info('This is a reference link only. StemBridge does not create a recruitment campaign, register donors, or promise a match for a particular patient.')
    with fundraiser_tab:
        st.subheader('Fundraise for NMDP')
        st.write('Visit NMDP’s official fundraising program to learn about creating a fundraiser that supports its mission and programs.')
        st.link_button('NMDP: Fundraise for NMDP ↗', FUNDRAISE, use_container_width=True)
        st.link_button('NMDP: Fundraise Your Way ↗', FUNDRAISE_START, use_container_width=True)
        st.info('NMDP fundraising supports its mission. It is different from a personal campaign to pay an individual patient’s expenses. No payments or campaigns are created in StemBridge.')
