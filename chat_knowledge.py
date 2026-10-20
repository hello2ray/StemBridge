"""Short educational paraphrases based on NCI and ACS public patient guides.
This is a curated keyword FAQ, not an AI model, medical advice, or live web retrieval.
"""
NCI = 'https://www.cancer.gov/about-cancer/treatment/types/stem-cell-transplant'
ACS = 'https://www.cancer.org/cancer/treatment-types/stem-cell-transplant.html'
ACS_TYPES = 'https://www.cancer.org/cancer/treatment-types/stem-cell-transplant/types-of-transplants.html'
ACS_DONOR = 'https://www.cancer.org/cancer/treatment-types/stem-cell-transplant/finding-a-donor.html'
ACS_PROCESS = 'https://www.cancer.org/cancer/treatment-types/stem-cell-transplant/process.html'

FAQ = [
    ('What is a stem cell transplant?', ('what is a stem cell', 'stem cell transplant', 'bone marrow transplant', 'hsct'), 'A blood stem cell transplant restores blood-forming cells after disease or treatment has damaged them. Healthy stem cells are given through a vein and can grow into new blood cells.', [('NCI', NCI), ('ACS', ACS)]),
    ('Autologous vs. allogeneic', ('autologous', 'allogeneic', 'auto transplant', 'allo transplant', 'types of transplant', 'own cells'), 'An autologous transplant uses your own collected stem cells. An allogeneic transplant uses stem cells from another person. Your care team decides which approach may be suitable.', [('NCI', NCI), ('ACS', ACS_TYPES)]),
    ('What is HLA matching?', ('hla', 'tissue match', 'donor matching', 'find a donor', 'donor search', 'match donor'), 'HLA markers help the transplant team evaluate whether donor cells may be compatible with a patient. The team checks these and other factors before selecting a donor.', [('NCI', NCI), ('ACS', ACS_DONOR)]),
    ('What happens on Day 0?', ('day 0', 'day zero', 'transplant day', 'infusion'), 'Day 0 is the day blood-forming stem cells are infused through an IV line. The care team monitors the patient during and after the infusion.', [('NCI', NCI), ('ACS', ACS_PROCESS)]),
    ('What is engraftment?', ('engraft', 'blood counts', 'new blood cells'), 'Engraftment means the transplanted stem cells begin producing new blood cells. The care team follows blood counts to monitor this process.', [('ACS', ACS), ('NCI', NCI)]),
    ('What is conditioning?', ('conditioning', 'chemotherapy', 'radiation', 'pre transplant treatment'), 'Conditioning is treatment given before the transplant, often chemotherapy and sometimes radiation. It prepares the body for the transplant; the exact plan varies.', [('ACS', ACS), ('NCI', NCI)]),
    ('What is GVHD?', ('gvhd', 'graft versus host', 'graft-versus-host'), 'Graft-versus-host disease can occur after an allogeneic transplant when donor immune cells attack the recipient’s tissues. Your transplant team monitors for this complication.', [('NCI', NCI), ('ACS', ACS)]),
    ('What side effects are possible?', ('side effect', 'infection', 'nausea', 'mouth sore', 'fatigue', 'tired', 'risk'), 'Transplant treatment may cause infection risk, fatigue, nausea, mouth sores, and other short- or long-term problems. Tell your transplant team about symptoms; they can explain what matters for you.', [('NCI', NCI), ('ACS', ACS)]),
    ('What does a caregiver do?', ('caregiver', 'family help', 'care partner'), 'Caregivers may help with appointments, daily care, transport, and watching for concerns after discharge. The transplant team should explain the responsibilities and available support.', [('ACS', ACS)]),
    ('How long is recovery?', ('recover', 'recovery', 'how long', 'follow-up'), 'Recovery and follow-up can take months or longer and vary widely. Your team checks blood counts and other health concerns and explains your individual recovery plan.', [('NCI', NCI), ('ACS', ACS_PROCESS)]),
    ('How do I decide about transplant?', ('decide', 'decision', 'benefit', 'success rate', 'eligible'), 'A transplant has potential benefits and serious risks. Discuss your diagnosis, treatment options, expected benefits, and possible complications with your transplant team before deciding.', [('ACS', ACS), ('NCI', NCI)]),
]

EMERGENCY_TERMS = ('chest pain', 'trouble breathing', 'cannot breathe', 'severe bleeding', 'unconscious', 'emergency', 'high fever', 'fever after transplant')

def answer(question: str):
    text = question.lower().strip()
    if any(term in text for term in EMERGENCY_TERMS):
        return ('This could need urgent medical attention. Contact your transplant team immediately or seek emergency care. StemBridge cannot assess symptoms.', [])
    for _, phrases, response, sources in FAQ:
        if any(phrase in text for phrase in phrases):
            return response, sources
    return ('I do not have a verified answer to that question in my NCI/ACS guide. Please ask your transplant team. You can also open the official guides below.', [('NCI', NCI), ('ACS', ACS)])
