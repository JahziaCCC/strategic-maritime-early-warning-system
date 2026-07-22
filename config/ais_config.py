"""
AIS Configuration
Strategic Maritime Early Warning System
"""

import os


AIS_API_KEY = os.getenv(
    "AIS_API_KEY"
)


AIS_ZONES = {

    "مضيق هرمز": {

        "lat_min": 25.5,
        "lat_max": 27.5,
        "lon_min": 55.0,
        "lon_max": 57.0

    },


    "باب المندب": {

        "lat_min": 12.0,
        "lat_max": 13.5,
        "lon_min": 42.5,
        "lon_max": 44.5

    },


    "قناة السويس": {

        "lat_min": 29.5,
        "lat_max": 31.0,
        "lon_min": 31.5,
        "lon_max": 33.0

    }

}
