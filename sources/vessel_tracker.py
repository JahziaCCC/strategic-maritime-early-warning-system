"""
Vessel Tracker
Strategic Maritime Early Warning System

تجميع مواقع السفن وتحديد المضيق
"""

from intelligence.geo_engine import locate_vessel


def get_tracked_vessels():

    vessels = [

        {
            "name": "Tanker A",
            "type": "Oil Tanker",
            "lat": 26.2,
            "lon": 56.1
        },

        {
            "name": "Cargo B",
            "type": "Cargo Ship",
            "lat": 12.8,
            "lon": 43.2
        },

        {
            "name": "Ship C",
            "type": "Container Ship",
            "lat": 30.5,
            "lon": 32.5
        }

    ]


    results = []


    for vessel in vessels:

        location = locate_vessel(
            vessel["lat"],
            vessel["lon"]
        )

        vessel["zone"] = location["arabic_name"]

        results.append(vessel)


    return results
