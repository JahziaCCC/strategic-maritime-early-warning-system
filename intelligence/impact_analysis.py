def analyze_impact(chokepoint, risk_score):

    impact = {
        "energy": "LOW",
        "trade": "LOW",
        "supply_chain": "LOW",
        "recommendation": "Continue Monitoring"
    }


    if chokepoint == "Strait of Hormuz":
        impact["energy"] = "HIGH"

    if chokepoint == "Bab el Mandeb":
        impact["trade"] = "HIGH"
        impact["supply_chain"] = "MEDIUM"

    if chokepoint == "Suez Canal":
        impact["trade"] = "HIGH"
        impact["supply_chain"] = "HIGH"


    if risk_score >= 70:
        impact["recommendation"] = "Immediate Executive Review"

    elif risk_score >= 40:
        impact["recommendation"] = "Enhanced Monitoring"


    return impact
