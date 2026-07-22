"""
Maritime Alert Engine
Strategic Maritime Early Warning System
"""


def generate_alert(assessment):

    level = assessment["risk_level"]


    if level == "LOW":

        return None


    impact = assessment["impact"]


    alert = {

        "title": "🚨 Maritime Early Warning Alert",

        "zone": assessment["zone"],

        "risk_level": level,

        "risk_score": assessment["risk_score"],

        "vessels": assessment["vessel_count"],

        "oil_tankers": assessment["oil_tankers"],

        "energy": impact["energy"],

        "trade": impact["trade"],

        "supply_chain": impact["supply_chain"],

        "recommendation": impact["executive_note"]

    }


    return alert
