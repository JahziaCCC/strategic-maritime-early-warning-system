import json
from datetime import datetime

from intelligence.risk_engine import calculate_risk, risk_level
from intelligence.impact_analysis import analyze_impact
from sources.ais_snapshot import get_vessel_data
from reports.executive_report import generate_report


def load_chokepoints():

    with open("data/chokepoints.json", "r", encoding="utf-8") as file:
        return json.load(file)


def main():

    data = load_chokepoints()

    results = []

    for point in data["chokepoints"]:

        vessel_data = get_vessel_data(point["name"])

        risk_score = calculate_risk(
            vessel_data["vessel_count"],
            vessel_data["abnormal_movements"],
            vessel_data["stopped_vessels"],
            0
        )

        level = risk_level(risk_score)

        impact = analyze_impact(
            point["name"],
            risk_score
        )

        results.append({

            "name": point["arabic_name"],

            "risk_score": risk_score,

            "risk_level": level,

            "impact": impact

        })


    generate_report(results)


if __name__ == "__main__":
    main()
