JSON_SG0_GOOD = {
    "donation": 10,
    "stretch_goal": 0,
    "items": 0,
    "notes": "Solo donazione, PoliEdro i migliori <3"
}

JSON_SG1_GOOD = {
    "donation": 10,
    "stretch_goal": 1,
    "items": 2,
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "bovisa"
    }
}

JSON_SG2_GOOD = {
    "donation": 17,
    "stretch_goal": 2,
    "items": 3,
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "leonardo"
    }
}

JSON_SG3_GOOD = {
    "donation": 35,
    "stretch_goal": 3,
    "items": 3,
    "shirts": [
        {"size": "XS", "type": "tank_top"},
        {"size": "L", "type": "t-shirt"},
        {"size": "XXL", "type": "t-shirt"}
    ],
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "leonardo"
    }
}

JSON_NOTCOVERED = {
    "donation": 1,
    "stretch_goal": 2,
    "items": 2,
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "bovisa"
    }
}

JSON_INVALID_STRETCH_GOAL = {
    "donation": 10,
    "stretch_goal": -7,
    "items": 2,
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "bovisa"
    }
}

JSON_SG3_SHIRTS_ITEMS_MISMATCH = {
    "donation": 100,
    "stretch_goal": 3,
    "items": 5,
    "shirts": [
        {"size": "XS", "type": "tank_top"},
        {"size": "L", "type": "t-shirt"},
        {"size": "XXL", "type": "t-shirt"}
    ],
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "leonardo"
    }
}

JSON_SG3_SHIRTS_MISSING = {
    "donation": 500,
    "stretch_goal": 3,
    "items": 5,
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "leonardo"
    }
}

JSON_SGgt0_REFERENCE_MISSING = {
    "donation": 100,
    "stretch_goal": 1,
    "items": 5,
    "notes": "",
}

JSON_DONATION_NULL = {
    "donation": None,
    "stretch_goal": 0,
    "items": 0,
    "notes": "Solo donazione, PoliEdro i migliori <3"
}

JSON_STRETCH_GOAL_NULL = {
    "donation": 10,
    "stretch_goal": None,
    "items": 0,
    "notes": "Solo donazione, PoliEdro i migliori <3"
}

JSON_REFERENCE_NULL = {
    "donation": 10,
    "stretch_goal": 0,
    "items": 0,
    "notes": "Solo donazione, PoliEdro i migliori <3",
    "reference": None
}

JSON_STRETCH_GOAL_MISSING = {
    "donation": 10,
    "items": 0,
    "notes": "Solo donazione, PoliEdro i migliori <3",
    "reference": None
}

JSON_INVALID_LANG = {
    "donation": 35,
    "stretch_goal": 3,
    "items": 3,
    "shirts": [
        {"size": "XS", "type": "tank_top"},
        {"size": "L", "type": "t-shirt"},
        {"size": "XXL", "type": "t-shirt"}
    ],
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "leonardo"
    },
    "lang": "sardu"
}

JSON_VALID_LANG = {
    "donation": 35,
    "stretch_goal": 3,
    "items": 3,
    "shirts": [
        {"size": "XS", "type": "tank_top"},
        {"size": "L", "type": "t-shirt"},
        {"size": "XXL", "type": "t-shirt"}
    ],
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "leonardo"
    },
    "lang": "it"
}

REFERENCE_WRONG_LOCATION = {
    "firstname": "Davide",
    "lastname": "Depau",
    "email": "email@domain.com",
    "phone": "+393200000000",
    "location": "bovisasca"
}

REFERENCE_WRONG_EMAIL = {
    "firstname": "Davide",
    "lastname": "Depau",
    "email": "culo",
    "phone": "+393200000000",
    "location": "leonardo"
}

REFERENCE_NAME_EMPTY = {
    "firstname": "",
    "lastname": "Depau",
    "email": "email@domain.com",
    "phone": "+393200000000",
    "location": "leonardo"
}

SHIRTS_WRONG_SIZE = [
    {"size": "XXS", "type": "tank_top"},
    {"size": "Z", "type": "t-shirt"},
    {"size": "XXX", "type": "t-shirt"}
]

SHIRTS_WRONG_TYPE = [
    {"size": "XS", "type": "tank_top"},
    {"size": "L", "type": "jockstrap"},
    {"size": "XXL", "type": "t-shirt"}
]
