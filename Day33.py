# Day 33 API, python requests module
import requests
import datetime as dt
import time
import smtplib
from email.message import EmailMessage

my_email = "faketester6000@yahoo.com"
my_password = "vtqnlafqmpqtfgdw" # app key for sending email

def is_iss_close(my_position):
    iss_position = get_iss_pos()
    print(iss_position)
    if abs(iss_position[0]-my_position[0])<=5 and abs(iss_position[1]-my_position[1])<=5:
        return True
    return False

def get_iss_pos():
    res = None
    res = requests.get('http://api.open-notify.org/iss-now.json')
    res.raise_for_status()
    position = res.json()['iss_position']
    longitude = position['longitude']
    latitude = position['latitude']
    iss_position = (float(latitude),float(longitude))
    return iss_position

def get_sunrise_sunset():
    parameters = {
    'lng':90.412521,
    'lat':23.810331,
    'formatted': 0
    }
    res = requests.get('http://api.sunrise-sunset.org/json', params=parameters)
    res.raise_for_status()
    data = res.json()
    sunrise = (int(data['results']['sunrise'].split("T")[1].split(':')[0])+6)%24
    sunset = (int(data['results']['sunset'].split("T")[1].split(':')[0])+6)%24
    return [sunrise, sunset]




# # print(data)
# # print(sunrise)
# print(sunrise)
# print(sunset)
# print(hour_now)

print(str(dt.datetime.today().date()))
my_position = (23.8103, 90.4125)
# my_position = iss_position

sent_for_days=[]

while True:
    today = str(dt.datetime.today().date())
    hour_now = dt.datetime.utcnow().hour
    sunrise, sunset = get_sunrise_sunset()
    # changing my_position and hour_now to get the email
    iss_position = get_iss_pos()
    hour_now = 22 # night
    my_position = (iss_position[0]-4, iss_position[1]+4) # close to the iss
    if today not in sent_for_days and is_iss_close(my_position) and not sunrise<=hour_now<=sunset:
        print("ISS can be seen!")
        print("Sending email")
        server = smtplib.SMTP_SSL('smtp.mail.yahoo.com')
        server.login(user=my_email, password=my_password)
        email = EmailMessage()
        email.set_content('Look up at the sky. ISS is right above you')
        email['From'] = my_email
        email['Subject'] = 'ISS'
        email['To'] = my_email
        try:
            server.send_message(email)
        except:
            print('Error sending. Trying again')
        else:
            sent_for_days.append(today)
    time.sleep(60)
    print("checking again")



# print(time_now.utcnow())

# from tkinter import *


# def get_quote():
#     try:
#         res = requests.get('https://api.kanye.rest/')
#         res.raise_for_status()
#     except:
#         print('Link does not exist')
#     q = res.json()['quote']
#     if len(q)<=50:
#         print(len(q))
#         canvas.itemconfig(quote_text, text=q) 
#     else:
#         get_quote()
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="Day33_background.png")
# canvas.create_image(148, 205, image=background_img)
# quote_text = canvas.create_text(148, 205, text="", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="Day33_kanye.png")
# kanye_button = Button(image=kanye_img, bd=0, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
# get_quote()


# window.mainloop()