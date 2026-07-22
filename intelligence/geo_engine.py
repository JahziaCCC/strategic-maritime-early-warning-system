"""
Geo Engine
Strategic Maritime Early Warning System

تحديد موقع السفن داخل مناطق المضائق
"""


import json


def load_zones():

    with open(
        "data/maritime_zones.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def locate_vessel(latitude, longitude):

    zones = load_zones()


    for zone in zones["zones"]:

        bbox = zone["bbox"]


        if (
            bbox["min_lat"] <= latitude <= bbox["max_lat"]
            and
            bbox["min_lon"] <= longitude <= bbox["max_lon"]
        ):

            return {
                "zone": zone["name"],
                "arabic_name": zone["arabic_name"]
            }


    return {
        "zone": "Unknown",
        "arabic_name": "خارج نطاق المراقبة"
    }
