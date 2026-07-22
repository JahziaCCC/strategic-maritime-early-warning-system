"""
AIS Provider
Strategic Maritime Early Warning System

مسؤول عن جلب بيانات السفن
وسيتم ربطه لاحقاً بمصدر AIS حقيقي
"""


def fetch_vessels(region):

    # بيانات تجريبية مؤقتة
    # سيتم استبدالها بمصدر AIS فعلي

    vessels = {

        "Strait of Hormuz": {
            "total_vessels": 145,
            "oil_tankers": 42,
            "cargo_ships": 58,
            "stopped_vessels": 4
        },

        "Bab el Mandeb": {
            "total_vessels": 86,
            "oil_tankers": 18,
            "cargo_ships": 45,
            "stopped_vessels": 2
        },

        "Suez Canal": {
            "total_vessels": 120,
            "oil_tankers": 25,
            "cargo_ships": 70,
            "stopped_vessels": 3
        }

    }

    return vessels.get(region, {})
