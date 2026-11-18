
"""Educational, keyword-based FAQ. No AI model or medical decision support."""

NCI = "https://www.cancer.gov/about-cancer/treatment/types/stem-cell-transplant"
ACS = "https://www.cancer.org/cancer/treatment-types/stem-cell-transplant.html"
NMDP = "https://www.nmdp.org/patients"

FAQ = [
    (
        "What is a stem cell transplant?",
        ("stem cell transplant", "bone marrow transplant", "what is a stem cell"),
        "A blood stem cell transplant provides blood-forming stem cells. "
        "The cells are infused through a vein and can grow into new blood cells.",
        [("NCI", NCI)]
    ),
    (
        "What is the difference between autologous and allogeneic?",
        ("autologous", "allogeneic", "transplant type", "own cells"),
        "Autologous uses the patient's own stem cells and this guide has seven phases. "
        "Allogeneic uses donor cells and this guide has eight phases, including "
        "HLA typing, donor selection, and GVHD monitoring. "
        "The transplant team decides what is appropriate.",
        [("NCI", NCI), ("ACS", ACS)]
    ),
    (
        "How does donor search work?",
        ("donor", "hla", "matching", "registry"),
        "For allogeneic transplants, the transplant center arranges HLA testing, "
        "donor searching, and donor selection. StemBridge cannot search "
        "donor registries or identify a match.",
        [("NMDP", NMDP)]
    ),
    (
        "What happens during evaluation?",
        ("evaluation", "test", "heart", "lung", "screening"),
        "Evaluation may include blood tests, infection screening, heart and lung "
        "tests, and disease-specific assessments. The exact tests depend on "
        "the patient and transplant center.",
        [("NCI", NCI)]
    ),
    (
        "What is mobilization?",
        ("mobilization", "apheresis", "collection"),
        "For many autologous transplants, medicines help move stem cells into "
        "the bloodstream so they can be collected by apheresis and stored "
        "for later infusion.",
        [("ACS", ACS)]
    ),
    (
        "What is conditioning?",
        ("conditioning", "chemotherapy", "radiation"),
        "Conditioning is treatment before stem cell infusion, often "
        "chemotherapy and sometimes radiation. The care team chooses the regimen.",
        [("NCI", NCI)]
    ),
    (
        "What happens on Day 0?",
        ("day 0", "day zero", "infusion"),
        "Day 0 is the day the stem cells are infused. The team monitors "
        "for reactions and follows blood counts afterward.",
        [("ACS", ACS)]
    ),
    (
        "What is engraftment?",
        ("engraftment", "engraft", "anc", "platelets"),
        "Engraftment means transplanted cells begin producing new blood cells. "
        "The transplant team monitors blood counts. Engraftment does not "
        "by itself mean cancer remission.",
        [("NCI", NCI)]
    ),
    (
        "What is GVHD?",
        ("gvhd", "graft versus host", "graft-versus-host"),
        "GVHD can occur after allogeneic transplant when donor immune cells "
        "attack the recipient's tissues. The team provides prevention, "
        "monitoring, and treatment.",
        [("NMDP", NMDP)]
    ),
    (
        "What is chimerism?",
        ("chimerism",),
        "Chimerism testing measures the proportion of blood cells that "
        "come from the donor after an allogeneic transplant. "
        "The transplant team interprets the results.",
        [("NMDP", NMDP)]
    ),
    (
        "How long does recovery take?",
        ("recovery", "recover", "day +100", "long term"),
        "Recovery varies widely. Follow-up may continue for months or years, "
        "especially after an allogeneic transplant. Day +100 is a milestone, "
        "not the end of recovery.",
        [("NCI", NCI)]
    ),
    (
        "What can caregivers do?",
        ("caregiver", "family support"),
        "Caregivers can help with transport, daily needs, understanding "
        "instructions, and arranging support. They should follow "
        "the transplant team's guidance.",
        [("NMDP", NMDP)]
    ),
    (
        "Where can I find financial help?",
        ("financial", "insurance", "money", "cost", "grant", "lodging"),
        "Ask the transplant center's financial counselor about insurance, "
        "travel, lodging, and assistance programs. StemBridge's Financial "
        "Help page links to organizations that may offer support.",
        [("NMDP", NMDP)]
    ),
    (
        "How do I find a transplant center?",
        ("transplant center", "hospital", "clinic", "find center"),
        "Use the Transplant Centers page for example programs and official "
        "directories. Confirm that the program treats your condition "
        "and transplant type.",
        [("NMDP", NMDP)]
    ),
    (
        "How do I get a second opinion?",
        ("second opinion", "another doctor", "another specialist"),
        "Ask your care team for a referral or contact another transplant center. "
        "Check insurance, timing, and what records the specialist needs. "
        "Do not delay urgent care without medical advice.",
        [("NCI", NCI)]
    )
]

URGENT = (
    "chest pain",
    "trouble breathing",
    "cannot breathe",
    "severe bleeding",
    "unconscious",
    "high fever",
    "fever",
    "emergency",
    "shortness of breath",
    "severe diarrhea"
)


def answer(question: str):
    q = question.lower().strip()

    if any(term in q for term in URGENT):
        return (
            "Symptoms after transplant may need urgent care. "
            "Follow your transplant center's emergency instructions "
            "and contact the team immediately. For life-threatening "
            "symptoms call emergency services. "
            "This chatbot cannot assess symptoms.",
            []
        )

    for title, phrases, response, sources in FAQ:
        if any(term in q for term in phrases):
            return response, sources

    return (
        "I do not have a reviewed answer to that question. "
        "Please ask your transplant team or use the official resources.",
        [("NCI", NCI), ("ACS", ACS)]
    )
