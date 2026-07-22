"""
Maritime Intelligence Engine
Strategic Maritime Early Warning System
"""

from sources.vessel_tracker import get_tracked_vessels
from intelligence.maritime_risk import calculate_maritime_risk


def generate_maritime_assessment():

    vessels = get_tracked_vessels()

    zones = {}


    for vessel in vessels:

        zone = vessel["zone"]

        if zone not in zones:
            zones[zone] = []

        zones[zone].append(vessel)


    assessments = []


    for zone, zone_vessels in zones.items():

        risk = calculate_maritime_risk(
            zone_vessels
        )

        assessments.append({

            "zone": zone,

            "risk_score": risk["risk_score"],

            "risk_level": risk["risk_level"],

            "vessel_count": risk["vessel_count"],

            "oil_tankers": risk["oil_tankers"]

        })


    return assessments
