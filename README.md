# StemBridge – Streamlit Prototype

**Project:** StemBridge  
**SDG:** SDG 3 – Good Health and Well-Being  
**Team Members:** Santanu Ray, Mohammed AlZahrani, Janis Yohannan

## 1. Project Overview

StemBridge is a Streamlit-based educational application designed to help stem cell transplant patients and caregivers understand the transplant process and find useful support resources.

The application provides information about different transplant types, treatment stages, donor registries, financial assistance, caregiver support, transplant centers, and second opinions.

StemBridge is currently a classroom prototype. It does not provide medical advice or replace healthcare professionals.

## 2. Main Features

### Transplant Journey Guide

Users can select one of two transplant types:

**Autologous Transplant**

Uses the patient's own stem cells. The guide includes seven phases:

1. Diagnosis and Education
2. Transplant Evaluation
3. Mobilization and Collection
4. Conditioning and Hospitalization
5. Day 0 and Engraftment
6. Early Recovery
7. Long-Term Recovery

**Allogeneic Transplant**

Uses stem cells from a donor. The guide includes eight phases:

1. Diagnosis and Education
2. Transplant Evaluation
3. HLA Typing and Donor Search
4. Donor Selection and Work-Up
5. Conditioning and Hospitalization
6. Day 0 and Engraftment
7. Early Recovery
8. Long-Term Recovery

Each phase provides general information about what happens, important topics, and questions patients can ask their transplant team.

The application does not track an individual patient's progress.

### Educational Chatbot

StemBridge includes a simple educational chatbot that answers common questions about:

- Stem cell transplantation and transplant types
- HLA matching and donor searches
- Conditioning, engraftment, and GVHD
- Recovery and caregiver support
- Financial assistance
- Transplant centers and second opinions

The chatbot uses predefined answers and provides links to educational sources such as the National Cancer Institute and American Cancer Society.

It is not a generative AI chatbot and cannot provide personalized medical advice.

### Resource Directory

The application provides links to donor registries and support organizations.

**Donor Registries and Networks**

- NMDP – United States
- Gift of Life Marrow Registry – United States
- DKMS – International
- Anthony Nolan – United Kingdom
- World Marrow Donor Association (WMDA)
- DATRI – India
- Canadian Blood Services – Canada

**Education and Support Organizations**

- National Cancer Institute (NCI)
- American Cancer Society (ACS)
- BMT InfoNet
- Leukemia & Lymphoma Society (LLS)

These are external reference links only. StemBridge does not connect to donor registry databases or identify matching donors. Donor searching is managed by the transplant center.

### Financial Resource Navigator

Provides links to organizations that may offer financial and practical assistance.

The resources include NMDP, Leukemia & Lymphoma Society, Patient Advocate Foundation, CancerCare, and HealthWell Foundation.

The application also provides general questions patients can ask about insurance coverage, treatment costs, travel, lodging, and financial assistance.

StemBridge does not check eligibility or submit financial applications.

### Caregiver Resources

Provides general guidance for caregivers before, during, and after transplant.

Topics include transportation, hospital visits, infection precautions, recovery support, and caregiver well-being.

### Transplant Center Directory

Includes a searchable example list of U.S. transplant centers, such as MD Anderson, Mayo Clinic, UT Southwestern, Memorial Sloan Kettering, and others.

Users can search by center name, city, or state and open the center's official website.

The list is not complete or ranked. Patients should confirm available services, insurance, referrals, and appointments directly with the center.

### Second Opinion Guide

Provides general steps for getting a second opinion from another transplant specialist.

Topics include finding another center, preparing medical records, checking insurance, and comparing treatment recommendations.

StemBridge does not schedule appointments or share medical records.

## 3. Technology Used

| Component | Technology |
|---|---|
| Application | Python |
| User interface | Streamlit |
| Educational chatbot | Python keyword-based FAQ |
| Styling | Custom CSS |
| External resources | Official website links |
| Database | Not required |
| Authentication | Not required |

## 4. Project Structure

```text
StemBridge/
├── app.py
├── chat_knowledge.py
├── requirements.txt
└── README.md
```

**app.py:** Main Streamlit application, navigation, transplant journeys, resource directories, and support pages.

**chat_knowledge.py:** Educational chatbot questions, answers, and source links.

**requirements.txt:** Python package requirements.

**README.md:** Project information and setup instructions.

The previous `nmdp_features.py` module is no longer needed for this version.

## 5. Installation and Setup

### Prerequisites

- Python 3.10 or later
- pip
- Internet connection to open external resource websites

### Step 1: Open the Project Directory

```bash
cd StemBridge
```

### Step 2: Create a Virtual Environment (Optional)

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python -m streamlit run app.py
```

### Step 5: Open StemBridge

Open the following address in your browser:

http://localhost:8501

## 6. How to Use

1. Open StemBridge in your browser.
2. Select Autologous or Allogeneic transplant on the Home page.
3. Open Transplant Journey to view the relevant phases.
4. Use Ask StemBridge for common educational questions.
5. Open Resource Directory to explore donor registries and support organizations.
6. Use Financial Help and Caregiver Guide for additional information.
7. Browse Transplant Centers and Second Opinion for information about other transplant programs.

No login or patient registration is required.

## 7. Current Scope and Limitations

StemBridge is an educational prototype.

The current version does not include:

- Patient login or individual journey tracking
- Electronic health record (EHR) integration
- HLA report uploads or donor matching
- Direct NMDP, DKMS, Gift of Life, or other registry API integrations
- Appointment booking or second-opinion requests
- Financial applications or payments
- Live generative AI medical consultation

The chatbot does not automatically retrieve updated medical information from external websites.

The transplant center directory contains example centers and is not a verified national directory.

## 8. Privacy and Safety

StemBridge does not require patients to create accounts or upload medical records.

Users should not enter personal medical information into the educational chatbot.

The application is not intended for diagnosis, treatment decisions, emergency assessment, or clinical use.

All medical content should be reviewed by qualified healthcare professionals before the application is made available for real patient use.

For urgent medical concerns, patients should follow their transplant team's instructions or seek emergency care.

## 9. Future Improvements

Based on feedback from our mentor and potential users, future improvements may include:

- Improving the transplant journey information and navigation
- Reviewing medical content with healthcare professionals
- Adding more verified transplant center information
- Improving accessibility and mobile usability
- Exploring human-supported chat
- Adding more financial and caregiver resources
- Conducting usability testing with patients and caregivers

Any future integration with donor registries or healthcare organizations would require the necessary permissions, technical access, and privacy safeguards.

## 10. Educational References

- [National Cancer Institute](https://www.cancer.gov/about-cancer/treatment/types/stem-cell-transplant)
- [American Cancer Society](https://www.cancer.org/cancer/treatment-types/stem-cell-transplant.html)
- [NMDP](https://www.nmdp.org/)
- [Gift of Life Marrow Registry](https://www.giftoflife.org/)
- [DKMS](https://www.dkms.org/)
- [World Marrow Donor Association](https://wmda.info/)
- [BMT InfoNet](https://www.bmtinfonet.org/)

## 11. Project Status

StemBridge is under active development as part of our SDG 3 project.

The current MVP focuses on providing clear transplant information and useful support resources. We are continuing to improve the prototype based on our updated transplant journey document and mentor feedback.

**Disclaimer:** StemBridge is a classroom demonstration and educational resource. It is not a medical device or a substitute for professional medical care.