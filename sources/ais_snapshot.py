"""
AIS Snapshot Module
Strategic Maritime Early Warning System
"""

from sources.ais_provider import fetch_vessels


def get_vessel_data(chokepoint):

    data = fetch_vessels(chokepoint)

    if not data:
        return {
            "vessel_count": 0,
            "oil_tankers": 0,
            "stopped_vessels": 0,
            "abnormal_movements": 0
        }


    return {

        "vessel_count": data["total_vessels"],

        "oil_tankers": data["oil_tankers"],

        "stopped_vessels": data["stopped_vessels"],

        # مؤقتاً حتى نربط تحليل الحركة لاحقاً
        "abnormal_movements": 0

    }
