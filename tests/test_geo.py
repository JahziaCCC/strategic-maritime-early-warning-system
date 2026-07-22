from intelligence.geo_engine import locate_vessel


test_vessels = [

    {
        "name": "Tanker A",
        "lat": 26.2,
        "lon": 56.1
    },

    {
        "name": "Cargo B",
        "lat": 12.8,
        "lon": 43.2
    },

    {
        "name": "Ship C",
        "lat": 30.5,
        "lon": 32.5
    }

]


for vessel in test_vessels:

    location = locate_vessel(
        vessel["lat"],
        vessel["lon"]
    )

    print(
        vessel["name"],
        "→",
        location["arabic_name"]
    )
