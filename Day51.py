from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

driver.get('https://www.speedtest.net/')
start = driver.find_element_by_class_name('start-text')
start.click()
up = "-10"
down = "-20"
while True:
    try:
        if driver.current_url == 'https://www.speedtest.net/':
            raise Exception
        
        down = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        up = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        break
    except Exception as e:
        print("Not finished yet/ could not get the download and upload speed")
        print(e)
        print(up)
        print(down)
        sleep(5)

print(down)
print(up)
message = f"My upload speed is {up}Mbps and download speed is {down}Mbps"


driver.get('https://twitter.com/i/flow/login')
while True:
    try:
        email = driver.find_element(By.TAG_NAME, 'input')
        email.send_keys('YOur twitter username/email')
        email.send_keys(Keys.ENTER)
        break
    except:
        sleep(1)
    
sleep(1)

password = driver.find_element(By.NAME, 'password')
password.send_keys('your twitter password')
password.send_keys(Keys.ENTER)

sleep(3)


while True:
    try:
        tweet = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        driver.execute_script('arguments[0].click();', tweet)
        break
    except Exception as e:
        # print("didnt click the tweet box")
        # print(e)
        sleep(2)

actions = ActionChains(driver)
actions.send_keys(message)
actions.perform()
driver.find_element_by_css_selector('div[data-testid="tweetButtonInline"]').click()

