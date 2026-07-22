"""
Strategic Maritime Early Warning System
Main Controller
"""


from intelligence.maritime_engine import generate_maritime_assessment
from reports.executive_report import generate_report



def main():


    assessments = generate_maritime_assessment()


    # التقرير التنفيذي

    generate_report(
        assessments
    )


    # التنبيهات

    for item in assessments:


        if item["alert"]:


            print()

            print("=" * 70)

            print(
                item["alert"]["title"]
            )


            print(
                "Location:",
                item["alert"]["zone"]
            )


            print(
                "Risk Level:",
                item["alert"]["risk_level"]
            )


            print(
                "Risk Score:",
                item["alert"]["risk_score"],
                "/100"
            )


            print(
                "Recommendation:",
                item["alert"]["recommendation"]
            )


            print("=" * 70)



if __name__ == "__main__":

    main()
