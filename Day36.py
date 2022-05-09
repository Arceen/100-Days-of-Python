# Day36 stock market email notifier
import os
import re
import requests
import smtplib
import html
from email.message import EmailMessage
STOCK = "NFLX"
COMPANY_NAME = "Apple Inc."

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWSAPI_API_KEY = os.getenv("NEWSAPI_API_KEY")
YAHOO_EMAIL_API_KEY = os.getenv("YAHOO_EMAIL_API_KEY")
my_email = "faketester6000@yahoo.com"
# get price from alphavantage
url = 'https://www.alphavantage.co/query'
parameters = {
    "function": 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'datatype': 'json',
    'apikey': ALPHAVANTAGE_API_KEY,
}
res = requests.get(url= url, params=parameters)
data = res.json()['Time Series (Daily)']
prev_day = list(data.keys())[1]
next_day = list(data.keys())[0]
print(data[prev_day]['4. close'])
print(data[next_day]['4. close'])
prev_price = float(data[prev_day]['4. close'])
next_price = float(data[next_day]['4. close'])
# prev_price = 900
# next_price = 1000
change = next_price - prev_price
percent_change = round(change/prev_price, 4)*100
print(change)
print(f"Percent {'increase' if change>0 else 'decrease'} is: {percent_change}%")
# print(API_KEY)
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# as per recommendation from @freylis, compile once only
CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

if abs(percent_change)>3:
    print("Get News")
    url = 'https://newsapi.org/v2/everything'
    parameters = {
        'q': COMPANY_NAME,
        'from': next_day,
        'sortBy':'popularity',
        'apikey': NEWSAPI_API_KEY,
    }
    res = requests.get(url= url, params=parameters)
    news = res.json()['articles'][:3]
    server = smtplib.SMTP_SSL('smtp.mail.yahoo.com')
    server.login(user=my_email, password=YAHOO_EMAIL_API_KEY)
    email = EmailMessage()
    message = '\n\n'.join([str(i+1)+". " + news[i]['title']+'\n'+cleanhtml(news[i]['description']) for i in range(3)])
    email.set_content(message)
    email['From'] = my_email
    email['Subject'] = f'{next_day} - {STOCK}: {"🔺" if change>0 else "🔻"}{percent_change}%'
    email['To'] = my_email
    try:
        print("Sending Stock Message")
        server.send_message(email)
        print("Stock Message Sent")
        
    except:
        print('Error sending. Trying again')

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

