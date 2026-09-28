reference_data = [
    {
        "condition": "Common Cold",
        "symptoms": ["cough", "runny nose", "sneezing", "sore throat"],
        "description": "A common respiratory illness.",
        "medicines": ["Paracetamol", "Saline nasal spray"]
    },
    {
        "condition": "Influenza",
        "symptoms": ["fever", "cough", "sore throat", "headache", "fatigue"],
        "description": "A respiratory illness that may include fever, cough, headache and fatigue.",
        "medicines": ["Paracetamol"]
    },
    {
        "condition": "Migraine",
        "symptoms": ["headache", "nausea", "light sensitivity", "vomiting"],
        "description": "A type of headache that may be associated with nausea and sensitivity to light.",
        "medicines": ["Paracetamol"]
    },
    {
        "condition": "Gastroenteritis",
        "symptoms": ["nausea", "vomiting", "diarrhea", "abdominal pain", "fever"],
        "description": "An illness involving the gastrointestinal system.",
        "medicines": ["Oral rehydration solution"]
    },
    {
        "condition": "Allergic Rhinitis",
        "symptoms": ["sneezing", "runny nose", "nasal congestion", "itchy eyes"],
        "description": "An allergic condition involving nasal symptoms and itchy eyes.",
        "medicines": ["Cetirizine"]
    },
    {
        "condition": "Asthma",
        "symptoms": ["cough", "wheezing", "shortness of breath", "chest tightness"],
        "description": "A respiratory condition associated with breathing difficulty and wheezing.",
        "medicines": ["Prescribed inhaler as directed by a doctor"]
    }
]


def find_matches(symptoms):
    symptoms = symptoms.lower().split(",")

    cleaned_symptoms = []

    for symptom in symptoms:
        symptom = symptom.strip()

        if symptom != "":
            cleaned_symptoms.append(symptom)

    matches = []

    for condition in reference_data:
        matched = []

        for symptom in cleaned_symptoms:
            if symptom in condition["symptoms"]:
                matched.append(symptom)

        if len(matched) > 0:
            percentage = (
                len(matched) / len(condition["symptoms"])
            ) * 100

            matches.append({
                "condition": condition["condition"],
                "matched": matched,
                "percentage": round(percentage, 1),
                "description": condition["description"],
                "medicines": condition["medicines"]
            })

    matches.sort(
        key=lambda item: item["percentage"],
        reverse=True
    )

    return matches