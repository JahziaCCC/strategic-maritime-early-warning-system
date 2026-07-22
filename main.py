import json
from datetime import datetime

from intelligence.risk_engine import calculate_risk, risk_level
from sources.ais_snapshot import get_vessel_data


SYSTEM_NAME = "Strategic Maritime Early Warning System"


def load_chokepoints():
    with open("data/chokepoints.json", "r", encoding="utf-8") as file:
        return json.load(file)


def main():

    print("=" * 60)
    print(SYSTEM_NAME)
    print("=" * 60)

    print()
    print("🌐 Executive Maritime Intelligence Report")
    print()

    data = load_chokepoints()

    for point in data["chokepoints"]:

        vessel_data = get_vessel_data(point["name"])

        score = calculate_risk(
            vessel_data["vessel_count"],
            vessel_data["abnormal_movements"],
            vessel_data["stopped_vessels"],
            0
        )

        level = risk_level(score)

        print("📍", point["arabic_name"])
        print("----------------------------")

        print("Vessels:", vessel_data["vessel_count"])
        print("Oil Tankers:", vessel_data["oil_tankers"])
        print("Stopped Vessels:", vessel_data["stopped_vessels"])

        print()
        print("Risk Score:", score, "/100")
        print("Risk Level:", level)

        print("============================")


    print()
    print("Last Update:")
    print(datetime.now())


if __name__ == "__main__":
    main()
