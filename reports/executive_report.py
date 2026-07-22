"""
Executive Report Generator
Strategic Maritime Early Warning System
"""


from datetime import datetime


def generate_report(assessments):

    print("=" * 70)

    print("Strategic Maritime Early Warning System")

    print("Executive Maritime Risk Report")

    print("Report Time:", datetime.now())

    print("=" * 70)


    for item in assessments:

        print()

        print("📍", item["zone"])

        print("-" * 40)

        print(
            "Risk Level:",
            item["risk_level"]
        )

        print(
            "Risk Score:",
            item["risk_score"],
            "/100"
        )

        print(
            "Detected Vessels:",
            item["vessel_count"]
        )

        print(
            "Oil Tankers:",
            item["oil_tankers"]
        )

        print()

        print("Strategic Impact:")

        impact = item["impact"]

        print(
            "Energy:",
            impact["energy"]
        )

        print(
            "Trade:",
            impact["trade"]
        )

        print(
            "Supply Chain:",
            impact["supply_chain"]
        )

        print()

        print(
            "Recommendation:",
            impact["executive_note"]
        )

        print("=" * 70)
