import json
from datetime import datetime

from intelligence.risk_engine import calculate_risk, risk_level


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

        # بيانات تجريبية مؤقتة
        vessel_density = 50
        abnormal_movements = 2
        stopped_vessels = 3
        security_events = 1

        score = calculate_risk(
            vessel_density,
            abnormal_movements,
            stopped_vessels,
            security_events
        )

        level = risk_level(score)

        print("📍", point["arabic_name"])
        print("Risk Score:", score, "/100")
        print("Level:", level)
        print("-" * 40)


    print()
    print("Last Update:")
    print(datetime.now())


if __name__ == "__main__":
    main()
