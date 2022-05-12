from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

driver.get('https://www.instagram.com/')
while True:
    try:
        username = driver.find_element_by_css_selector('input[name="username"]')
        username.send_keys('YOUR EMAIL')
        password = driver.find_element_by_css_selector('input[name="password"]')
        password.send_keys('YOUR PASSWORD')
        password.send_keys(Keys.ENTER)
        break
    except Exception as e:
        print(e)
        sleep(1)

while True:
    try:
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        break
    except Exception as e:
        print(e)
        sleep(1)

sleep(3)
while True:
    try:
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        break
    except Exception as e:
        print(e)
        sleep(1)

sleep(1)
#rock followers
driver.get('https://www.instagram.com/cristiano/')

driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div').click()
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
sleep(2)
while True:
    try:
        all_buttons = driver.find_elements_by_css_selector('li button')
        print(len(all_buttons))
        for button in all_buttons:
            # driver.refresh()
            # driver.implicitly_wait(1)
            # driver.execute_script('arguments[0].click();', button)
            button.click()
        #     except Exception as e:
        #         print("Error clilcking a button")
        #         print(e)
        #         pass
        #     sleep(1)
        # break
    except Exception as e:
        print(e)
        print('Button cant be found')
        sleep(3)





# while True:
#     try:
#         tweet = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
#         driver.execute_script('arguments[0].click();', tweet)
#         break
#     except Exception as e:
#         # print("didnt click the tweet box")
#         # print(e)
#         sleep(2)

# actions = ActionChains(driver)
# actions.send_keys(message)
# actions.perform()
# driver.find_element_by_css_selector('div[data-testid="tweetButtonInline"]').click()

