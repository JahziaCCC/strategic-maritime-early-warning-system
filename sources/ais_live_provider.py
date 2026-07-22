"""
AIS Live Data Provider
Strategic Maritime Early Warning System
"""

import json
import websocket
import os

from config.ais_config import AIS_API_KEY


def get_live_vessels():

    vessels = []


    if not AIS_API_KEY:

        print("⚠️ AIS API Key not found")

        return vessels



    try:

        ws = websocket.create_connection(
            "wss://stream.aisstream.io/v0/stream",
            timeout=10
        )


        subscribe_message = {

            "APIKey": AIS_API_KEY,

            "BoundingBoxes": [

                [
                    [25.5, 55.0],
                    [27.5, 57.0]
                ],

                [
                    [12.0, 42.5],
                    [13.5, 44.5]
                ],

                [
                    [29.5, 31.5],
                    [31.0, 33.0]
                ]

            ]

        }


        ws.send(
            json.dumps(subscribe_message)
        )


        print(
            "📡 AIS connection established"
        )


        for _ in range(20):

            message = ws.recv()

            data = json.loads(message)


            if "Message" in data:


                meta = data.get(
                    "MetaData",
                    {}
                )


                position = data["Message"].get(
                    "PositionReport"
                )


                if position:

                    vessels.append({

                        "name":
                        meta.get(
                            "ShipName",
                            "Unknown"
                        ),

                        "type":
                        "Unknown",

                        "lat":
                        position.get(
                            "Latitude"
                        ),

                        "lon":
                        position.get(
                            "Longitude"
                        )

                    })


        ws.close()



    except Exception as e:

        print(
            "AIS Error:",
            e
        )



    return vessels
