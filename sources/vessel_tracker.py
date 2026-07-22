"""
Vessel Intelligence Tracker
Strategic Maritime Early Warning System
"""


from intelligence.geo_engine import locate_vessel


def get_tracked_vessels():

    vessels = [

        # Strait of Hormuz
        {
            "name": "Tanker-001",
            "type": "Oil Tanker",
            "lat": 26.2,
            "lon": 56.1
        },

        {
            "name": "Tanker-002",
            "type": "Oil Tanker",
            "lat": 26.1,
            "lon": 56.0
        },

        {
            "name": "Cargo-001",
            "type": "Cargo Ship",
            "lat": 26.3,
            "lon": 56.2
        },


        # Bab el Mandeb
        {
            "name": "Cargo-002",
            "type": "Cargo Ship",
            "lat": 12.8,
            "lon": 43.2
        },

        {
            "name": "Tanker-003",
            "type": "Oil Tanker",
            "lat": 12.7,
            "lon": 43.3
        },


        # Suez Canal
        {
            "name": "Container-001",
            "type": "Container Ship",
            "lat": 30.5,
            "lon": 32.5
        },

        {
            "name": "Tanker-004",
            "type": "Oil Tanker",
            "lat": 30.6,
            "lon": 32.6
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
