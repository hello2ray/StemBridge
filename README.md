# StemBridge clickable Streamlit MVP

A classroom/demo-only standalone prototype based on the supplied StemBridge pitch deck. It uses fictional information and local Streamlit session state; data is not saved permanently.

## Run on Ubuntu, Windows, or macOS

1. Install Python 3.10+.
2. In a terminal, open this folder.
3. Run:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

4. Open the local URL printed by Streamlit (usually http://localhost:8501).

## Demonstration path

Welcome → Today → Journey → My Care → Chat → Caregiver → Finance → Match Finder → Support.

Try checking off a task, adding a symptom note, adding a question, updating finance status, and switching between Patient and Caregiver roles in the sidebar. Turn off sharing as Patient, then switch to Caregiver to see the limited demo access behavior.

## Safety and scope

- Not a clinical product. No diagnosis, treatment advice, or triage.
- Chat uses fixed demo replies, not a live AI model.
- Match Finder only explains the registry process. No actual matching, ranking, or donor identities.
- Financial statuses are user-entered notes; no verified eligibility, approvals, or payment.
- Caregiver access is a UI simulation, not production authentication/authorization.
- No EHR, hospital, registry, or insurer integration.
- Do not enter real patient or sensitive data.

For real-world deployment, the project would need clinical, privacy, security, accessibility, and research ethics reviews.
