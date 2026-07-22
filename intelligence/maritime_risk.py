"""
Maritime Risk Intelligence
Strategic Maritime Early Warning System
"""


def calculate_maritime_risk(vessels):

    score = 0

    vessel_count = len(vessels)

    oil_tankers = 0


    for vessel in vessels:

        if vessel["type"] == "Oil Tanker":
            oil_tankers += 1


    # كثافة المرور
    score += vessel_count * 10

    # ناقلات النفط
    score += oil_tankers * 15


    if score > 100:
        score = 100


    if score < 30:
        level = "LOW"

    elif score < 70:
        level = "MEDIUM"

    else:
        level = "HIGH"


    return {
        "risk_score": score,
        "risk_level": level,
        "vessel_count": vessel_count,
        "oil_tankers": oil_tankers
    }
