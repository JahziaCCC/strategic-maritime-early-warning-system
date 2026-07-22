from datetime import datetime

from intelligence.maritime_engine import generate_maritime_assessment


SYSTEM_NAME = "Strategic Maritime Early Warning System"


def main():

    print("=" * 70)
    print(SYSTEM_NAME)
    print("Executive Maritime Intelligence Report")
    print("=" * 70)

    print()
    print("Report Time:")
    print(datetime.now())

    print()


    assessments = generate_maritime_assessment()


    for item in assessments:

        print("📍", item["zone"])
        print("------------------------------")

        print(
            "Detected Vessels:",
            item["vessel_count"]
        )

        print(
            "Oil Tankers:",
            item["oil_tankers"]
        )

        print(
            "Risk Score:",
            item["risk_score"],
            "/100"
        )

        print(
            "Risk Level:",
            item["risk_level"]
        )

        print("==============================")


if __name__ == "__main__":
    main()
