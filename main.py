"""
Strategic Maritime Early Warning System
Main Controller
"""

from intelligence.maritime_engine import generate_maritime_assessment
from reports.executive_report import generate_report


def main():

    assessments = generate_maritime_assessment()

    generate_report(
        assessments
    )


if __name__ == "__main__":
    main()
