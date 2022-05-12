from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import requests

google_form_url = "YOUR FORM"    
def send_response(address, price, url):
    driver.get(google_form_url)
    sleep(1)
    driver.find_element_by_css_selector('div.Qr7Oae:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys(address)
    driver.find_element_by_css_selector('div.Qr7Oae:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys(price)
    driver.find_element_by_css_selector('div.Qr7Oae:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys(url)
    
    sub = driver.find_element_by_css_selector('.Y5sE8d > span:nth-child(3) > span:nth-child(1)')
    sub.click()
    sleep(1)
    
    


def scrape_zillow():
    '''
    Need to do headless browsing and scroll to bottom to find the additional listings.
    '''
    scrape_url = 'https://www.zillow.com/homes/San-Francisco,-CA_rb/'

    req_headers = {
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'en-US,en;q=0.5',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    }

    res = requests.get(scrape_url, headers=req_headers)
    soup = BeautifulSoup(res.text, 'lxml')

    # print(soup)
    prices = [i.getText() for i in soup.find_all(class_='list-card-price')]
    addresses = [i.getText() for i in soup.find_all(class_='list-card-addr')]
    links = [i.get('href') for i in soup.find_all(class_='list-card-img')][:-1]
    return list(zip(addresses, prices, links))
    
    
data = scrape_zillow()
driver = webdriver.Firefox()

for address, price, url in data:
    send_response(address, price, url)

driver.quit()