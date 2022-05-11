from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
url="https://orteil.dashnet.org/cookieclicker/"

driver.get(url)
# email_box = driver.find_element_by_id('email')
# password_box = driver.find_element_by_id('pass')
# email_box.send_keys('faketester6000@gmail.com') 
# password_box.send_keys('')

login_button = driver.find_element(By.ID, 'bigCookie')
# buys = driver.find_element(By.ID, f'product0')

while True:
    driver.execute_script("arguments[0].click();", login_button)
    try:
        driver.execute_script("arguments[0].click();", driver.find_element(By.ID, 'upgrade0'))
    except:
        # print('buying grandmas charm')
        pass
    try:
        for i in range(7):
            up = driver.find_element(By.ID, f'product{i}')
            driver.execute_script("arguments[0].click();", up)
    except:
        pass