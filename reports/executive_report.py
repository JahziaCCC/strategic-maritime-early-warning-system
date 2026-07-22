from datetime import datetime


def generate_report(results):

    print("=" * 70)
    print("🌐 Strategic Maritime Early Warning System")
    print("Executive Maritime Situation Report")
    print("=" * 70)

    print()
    print("Report Time:")
    print(datetime.now())

    print()

    for item in results:

        print("📍", item["name"])
        print("-----------------------------")

        print("Risk Score:",
              item["risk_score"],
              "/100")

        print("Risk Level:",
              item["risk_level"])

        print("Energy Impact:",
              item["impact"]["energy"])

        print("Trade Impact:",
              item["impact"]["trade"])

        print("Supply Chain Impact:",
              item["impact"]["supply_chain"])

        print("Recommendation:")
        print(item["impact"]["recommendation"])

        print("=" * 70)
