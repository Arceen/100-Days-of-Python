# Create a google sheets exercise tracker using api
from datetime import datetime
import os
import requests

sheety_api_end_point = os.getenv('SHEETY_API_END_POINT1')

NUTRITIONIX_APP_ID = os.getenv('NTX_APP_ID')
NUTRITIONIX_API_KEY = os.getenv('NTX_API_KEY')
SHEETY_AUTH = os.getenv('SHEETY_AUTH')

ntx_exercise_end_point = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
    'Content-Type': 'application/json'
    # 'x-remote-uesr-id':0
}


req_body = {
# "query": input("Tell me which exercises you performed: "),
"query": input("Tell me about your exercises: "),
"gender":"male",
"weight_kg":74.9,
"height_cm":168.64,
"age":23
}

res = requests.post(ntx_exercise_end_point, json=req_body ,headers=headers)
res.raise_for_status()
data = res.json()['exercises']
for row in data:
    ex = row['name'].title()
    dur = row['duration_min']
    cal = row['nf_calories']


    d = datetime.now()
    req_headers = {
        'Authorization': SHEETY_AUTH
    }
    req_body = {
        'sheet1': {
                "date": d.strftime("%d/%m/%Y"),
                "time": d.strftime("%H:%M:%S"),
                "exercise": ex,
                "duration": dur,
                "calories": cal
                }
    }

    res = requests.post(sheety_api_end_point, json=req_body, headers=req_headers)
    # res = requests.get(sheety_api_end_point)
    res.raise_for_status()
    print(res.text)
