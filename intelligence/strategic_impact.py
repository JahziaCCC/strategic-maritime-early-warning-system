"""
Strategic Impact Analysis
Strategic Maritime Early Warning System
"""


def analyze_strategic_impact(zone, risk_level):

    impact = {

        "energy": "LOW",

        "trade": "LOW",

        "supply_chain": "LOW",

        "executive_note": "Normal Monitoring"

    }


    if zone == "مضيق هرمز":

        impact["energy"] = "HIGH"


    if zone == "باب المندب":

        impact["trade"] = "HIGH"

        impact["supply_chain"] = "MEDIUM"


    if zone == "قناة السويس":

        impact["trade"] = "HIGH"

        impact["supply_chain"] = "HIGH"


    if risk_level == "HIGH":

        impact["executive_note"] = "Immediate Executive Attention"

    elif risk_level == "MEDIUM":

        impact["executive_note"] = "Enhanced Monitoring"


    return impact
