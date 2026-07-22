"""
Movement Analysis Engine
Strategic Maritime Early Warning System
"""


def analyze_movement(vessels):

    stopped = 0
    abnormal = 0


    for vessel in vessels:

        if vessel.get("status") == "Stopped":
            stopped += 1

        if vessel.get("course_change") == True:
            abnormal += 1


    return {

        "stopped_vessels": stopped,

        "abnormal_movements": abnormal

    }
