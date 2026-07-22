import json
from datetime import datetime


SYSTEM_NAME = "Strategic Maritime Early Warning System"


def load_chokepoints():
    with open("data/chokepoints.json", "r", encoding="utf-8") as file:
        return json.load(file)


def main():

    print("=" * 60)
    print(SYSTEM_NAME)
    print("=" * 60)

    print()
    print("🌐 Maritime Strategic Monitoring")
    print()

    data = load_chokepoints()

    print(" monitored chokepoints:")
    print()

    for point in data["chokepoints"]:
        print(f"📍 {point['arabic_name']}")
        print(f"   Region: {point['region']}")
        print(f"   Importance: {point['importance']}")
        print(f"   Risk Score: {point['risk_score']}/100")
        print()

    print("System Status:")
    print("🟢 Operational")

    print()
    print("Last Update:")
    print(datetime.now())


if __name__ == "__main__":
    main()
