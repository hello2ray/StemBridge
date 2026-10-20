# StemBridge – Streamlit classroom prototype

Includes private fictional demo patient views, personalized transplant journey, care coordination, finance demonstration, NMDP **reference links only**, and an NCI/ACS source-linked educational FAQ chat.

## Run

```bash
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py
```

Open http://localhost:8501

Demo login: `alex` / `Alex2026!`. Other fictional logins: `priya` / `Priya2026!`, `daniel` / `Daniel2026!`, `maya` / `Maya2026!`.

## Match Finder
Three tabs: **Donor search** (NMDP links), **Donor campaign** (NMDP donor-recruitment references), **NMDP fundraiser** (official fundraising references). No donor matching, API access, campaign creation, or payments.

## Chat
Curated educational Q&A, paraphrased from official NCI and American Cancer Society pages with links to original sources. Not a generative chatbot and does not automatically update from the websites.

**Safety:** Entire project uses fictional data and demonstration credentials. Login/session isolation is not production security. Do not enter real health or donor information. Session data is not persistent across logouts. No clinical advice.
