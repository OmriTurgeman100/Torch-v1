import requests
import time
import logging
import json
from datetime import datetime
import random

def black_box_script():
    try:

        api = "http://localhost/api/v1/post/reports"

        headers = {
            "Content-Type": "application/json"
        }

        body = {
            "report_id": 'sample report dev',
            "title": 'sample report dev',
            "description": 'sample report description',
            "value": 60
        }

        response = requests.post(api, data=json.dumps(body), headers=headers)
 

        print(body["report_id"], body["title"], body["description"], body["value"])
        print(response.status_code)
        data = response.json()

        print(data)

    except Exception as e:
        print(e)

while True:
    black_box_script()
    # time.sleep(1)