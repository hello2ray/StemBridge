
"""
StemBridge Educational Chatbot

This is a keyword-based educational FAQ.
It is not a generative AI model.
It does not provide medical advice.
"""

NCI = (
    "https://www.cancer.gov/about-cancer/"
    "treatment/types/stem-cell-transplant"
)

ACS = (
    "https://www.cancer.org/cancer/"
    "treatment-types/stem-cell-transplant.html"
)

NMDP = "https://www.nmdp.org/"
GIFT_OF_LIFE = "https://www.giftoflife.org/"
DKMS = "https://www.dkms.org/"
WMDA = "https://wmda.info/"

FAQ = [
    (
        "What is a stem cell transplant?",
        ("stem cell transplant", "bone marrow transplant"),
        "A stem cell transplant provides blood-forming "
        "stem cells that can develop into new blood cells.",
        [("NCI", NCI)]
    ),

    (
        "Autologous vs Allogeneic",
        ("autologous", "allogeneic", "transplant type"),
        "Autologous transplants use the patient's own stem cells. "
        "Allogeneic transplants use donor stem cells.",
        [("NCI", NCI), ("ACS", ACS)]
    ),

    (
        "How does donor search work?",
        ("donor search", "donor matching", "hla"),
        "For allogeneic transplants, the transplant center "
        "coordinates HLA testing, donor search, and donor selection. "
        "StemBridge cannot identify matching donors.",
        [("NMDP", NMDP)]
    ),

    (
        "What donor registries are available?",
        ("donor registry", "registries", "gift of life", "dkms"),
        "Organizations include NMDP, Gift of Life, DKMS, "
        "Anthony Nolan, DATRI, Canadian Blood Services, "
        "and the international WMDA network. "
        "The transplant center manages the actual donor search.",
        [
            ("NMDP", NMDP),
            ("Gift of Life", GIFT_OF_LIFE),
            ("DKMS", DKMS),
            ("WMDA", WMDA)
        ]
    ),

    (
        "What is HLA matching?",
        ("hla matching", "hla typing", "tissue matching"),
        "HLA markers help the transplant team evaluate "
        "donor compatibility. Other factors are also considered.",
        [("NMDP", NMDP)]
    ),

    (
        "What is conditioning?",
        ("conditioning", "chemotherapy", "radiation"),
        "Conditioning is treatment given before transplant, "
        "often chemotherapy and sometimes radiation.",
        [("NCI", NCI)]
    ),

    (
        "What happens on Day 0?",
        ("day 0", "day zero", "infusion"),
        "Day 0 is the day stem cells are infused into the patient.",
        [("ACS", ACS)]
    ),

    (
        "What is engraftment?",
        ("engraftment", "engraft", "anc"),
        "Engraftment means transplanted stem cells begin "
        "producing new blood cells. The care team monitors "
        "blood counts to assess recovery.",
        [("NCI", NCI)]
    ),

    (
        "What is GVHD?",
        ("gvhd", "graft versus host"),
        "Graft-versus-host disease can happen after an "
        "allogeneic transplant when donor immune cells "
        "attack the patient's tissues.",
        [("NCI", NCI)]
    ),

    (
        "How long does recovery take?",
        ("recovery", "recover", "day +100"),
        "Recovery varies from person to person. "
        "Follow-up may continue for months or years.",
        [("NCI", NCI)]
    ),

    (
        "Where can I get financial help?",
        ("financial", "insurance", "cost", "grant"),
        "Ask your transplant center's financial counselor. "
        "You can also explore the StemBridge Financial Help page.",
        [("NMDP", NMDP)]
    ),

    (
        "How do I find a transplant center?",
        ("transplant center", "hospital", "find center"),
        "Use the StemBridge Transplant Centers page "
        "and confirm services directly with each hospital.",
        [("NMDP", NMDP)]
    ),

    (
        "How do I get a second opinion?",
        ("second opinion", "another doctor"),
        "You can ask your current care team for a referral "
        "or contact another transplant center. "
        "Check insurance and required medical records.",
        [("NCI", NCI)]
    ),

    (
        "What does a caregiver do?",
        ("caregiver", "family support"),
        "Caregivers may help with transportation, "
        "daily activities, appointments, and practical support.",
        [("NMDP", NMDP)]
    )
]


URGENT_TERMS = (
    "chest pain",
    "trouble breathing",
    "cannot breathe",
    "severe bleeding",
    "unconscious",
    "high fever",
    "fever",
    "emergency",
    "shortness of breath"
)


def answer(question: str):

    text = question.lower().strip()

    if any(term in text for term in URGENT_TERMS):

        return (
            "This may need urgent medical attention. "
            "Contact your transplant team immediately "
            "or seek emergency care. "
            "For life-threatening symptoms, call emergency services. "
            "StemBridge cannot assess symptoms.",
            []
        )

    for title, phrases, response, sources in FAQ:

        if any(phrase in text for phrase in phrases):
            return response, sources

    return (
        "I do not have a verified answer to that question. "
        "Please ask your transplant team or use "
        "the official educational resources.",
        [
            ("NCI", NCI),
            ("ACS", ACS)
        ]
    )
