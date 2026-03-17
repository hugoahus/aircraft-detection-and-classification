# Mapping from aircraft type → operator group
# Values: "NATO": , "Non-NATO": , "Both"
# The mapping was created by Microsoft Copilot (2026-03-14)

OPERATOR_MAP = {
    "C130": "Both",
    "EF2000": "Both",
    "EMB314": "Non-NATO",
    "F15": "Both",
    "F16": "Both",
    "F18": "NATO",
    "F35": "Both",
    "J10": "Non-NATO",
    "Rafale": "Both",
    "TB2": "NATO"
}

def get_operator(class_id, class_names):
    """Return operator group (NATO / Non-NATO / Both) for a given class ID."""
    name = class_names[class_id]
    return OPERATOR_MAP.get(name, "Unknown")
