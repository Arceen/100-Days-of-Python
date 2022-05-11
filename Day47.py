import requests
import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup

scrape_url = "https://www.amazon.com/Acer-Predator-PH315-54-760S-i7-11800H-Keyboard/dp/B092YHJLS6/ref=sr_1_6?qid=1652247602&s=computers-intl-ship&sr=1-6"
req_headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
    "Accept-Language": "en-US,en",
}
res = requests.get(scrape_url, headers=req_headers)
soup = BeautifulSoup(res.text, 'lxml')
# print(soup)
price_finder = ''
price = soup.find(attrs={'data-a-color':'price'}).find('span').getText()[1:]
price = float(price.replace(',',''))
# print(price)
title = soup.find('span', id='productTitle').getText().strip()
# print(title.getText().strip())

my_best = 1450
if price <= my_best:
    print("sending email")
    msg = title +'\n\n$'+ str(price) +'\n\n' + scrape_url

    # send email
    email = my_email
    password = my_password
    
    server = smtplib.SMTP_SSL('smtp.google.com', port=993)
    server.login(user=email, password=password)
    
    email = EmailMessage()
    email.set_content(msg)
    email['Subject'] = 'Amazon Price Alert!'
    email['From'] = email
    email['To'] = email
    server.send_message(email)
    print("Email sent")