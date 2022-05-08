# Day 35 - Api keys, authentication, environment variables and sending sms
# project Weather app sms sender
import requests
import json
import smtplib
from email.message import EmailMessage
my_email = "faketester6000@yahoo.com"
my_password = "ippbixizmqwyadad" #
api_key = '1b8b9e86467723162b081e6b6803fdc2'
url = 'https://api.openweathermap.org/data/2.5/onecall'
parameters = {
    # 16°38'S / Lon.: 93°52'
    'lat': 23.810331,
    'lon': 90.412521,
    # 'lat': 16.38,
    # 'lon': 93.52,
    'units': 'metric',
    'exclude': 'current,minutely,daily',
    # 'q': 'Dhaka',
    'appid': api_key
}
res = requests.get(url, params=parameters)
res.raise_for_status()
data = res.json()
hourly_data = data["hourly"][:12]
# print(hourly_data)
bring_umbrella = False
weather_codes_hourly = [hr_data["weather"][0]["id"] for hr_data in hourly_data]
print(weather_codes_hourly)
for code in weather_codes_hourly:
    if code < 700:
        bring_umbrella = True
        break

server = smtplib.SMTP_SSL('smtp.mail.yahoo.com')
server.login(user=my_email, password=my_password)
email = EmailMessage()
email.set_content("Bring an umbrella" if bring_umbrella else "Don't bring an umbrella")
email['From'] = my_email
email['Subject'] = 'Weather Advice'
email['To'] = my_email
try:
    server.send_message(email)
    print("message sent")
except:
    print('Error sending. Trying again')

    

# with open('myweatherdata.json', 'w+') as f:
#     json.dump(res.json(), f)
