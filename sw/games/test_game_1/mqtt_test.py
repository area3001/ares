import paho.mqtt.publish as publish
import random
import sys
import json

ID_MAX = sys.maxint

payload = {"test": 1,
           "hide": 0,
           "version": 1,
           "position": [200, 400],
           "id": str(random.randint(0, ID_MAX)),
           "source": "real",
           "type": "marker_1"
           }

publish.single("ares/video/markers", json.dumps(payload), hostname="localhost")