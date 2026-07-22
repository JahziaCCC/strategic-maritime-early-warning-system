"""
Maritime Intelligence Engine
Strategic Maritime Early Warning System
"""

from sources.vessel_tracker import get_tracked_vessels
from intelligence.maritime_risk import calculate_maritime_risk
from intelligence.movement_analysis import analyze_movement


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


        movement = analyze_movement(
            zone_vessels
        )


        # إضافة تأثير الحركة إلى التقييم
        final_score = risk["risk_score"]

        final_score += movement["stopped_vessels"] * 10

        final_score += movement["abnormal_movements"] * 15


        if final_score > 100:
            final_score = 100


        if final_score < 30:
            level = "LOW"

        elif final_score < 70:
            level = "MEDIUM"

        else:
            level = "HIGH"


        assessments.append({

            "zone": zone,

            "risk_score": final_score,

            "risk_level": level,

            "vessel_count": risk["vessel_count"],

            "oil_tankers": risk["oil_tankers"],

            "stopped_vessels": movement["stopped_vessels"],

            "abnormal_movements": movement["abnormal_movements"]

        })


    return assessments
