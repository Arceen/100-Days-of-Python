from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


geoAllowed = webdriver.FirefoxOptions()
geoAllowed.set_preference('geo.prompt.testing', True)
geoAllowed.set_preference('geo.prompt.testing.allow', True)
geoAllowed.set_preference('geo.provider.network.url',
    'data:application/json,{"location": {"lat": 51.47, "lng": 0.0}, "accuracy": 100.0}')
driver = webdriver.Firefox(options=geoAllowed)
driver.get('https://tinder.com')

# driver.find_element('data-testid',"appLoginBtn").click()
while True:
    try:
        driver.find_element_by_css_selector('a[data-testid="appLoginBtn"]').click()
    except:
        pass
    else:
        break

sleep(5)

# driver.get('https://google.com')
last_handle = driver.current_window_handle
print(last_handle)
# driver.execute_script('window.open("https://google.com", "new window")')
# driver.switch_to.window(last_handle)
# driver.close()
# for i in driver.window_handles:
#     driver.switch_to.window(i)
# driver.get('https://google.com.ua/')

while True:
    try:
        # didn't work last night. Now literally everything works LOL.
        
        # d = driver.find_elements_by_tag_name('button')
        x = driver.find_element_by_css_selector('button[data-testid="loginWithGoogle"]')
        # x =  driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[1]/div/button')
        print("Clicking: "+x.text)
        driver.execute_script("arguments[0].click();", x)
        
        driver.execute_script("arguments[0].click();", x)
        
        driver.execute_script("arguments[0].click();", x)
        
        driver.execute_script("arguments[0].click();", x)
        # print(len(d))
        # for i in d:
        #     print(i.text)
    
        # print("clicking: "+d[7].text)
        # driver.execute_script("arguments[0].click();",d[7])
    except:
        print("couln't find any class named button")
        sleep(1)
    else:
        break


sleep(5)
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[-1])
while True:
    try:
        # didn't work last night. Now literally everything works LOL.

        # d = driver.find_elements_by_tag_name('button')
        x = driver.find_element_by_id('identifierId')
        # x =  driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[1]/div/button')
        # print("Clicking: "+x.text)
        x.send_keys('Your Email')
        x.send_keys(Keys.ENTER)
    except Exception as e:
        print("couln't go to the new tab")
        sleep(3)
    else:
        break

sleep(3)
while True:
    try:
        # didn't work last night. Now literally everything works LOL.
        
        # d = driver.find_elements_by_tag_name('button')
        x = driver.find_element_by_name('password')
        # x =  driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[1]/div/button')
        # print("Clicking: "+x.text)
        x.send_keys('Your Password')
        x.send_keys(Keys.ENTER)
    except:
        print("couln't type email")
        sleep(1)
    else:
        break

driver.switch_to.window(last_handle)
sleep(8)   
while True:
    try:
        x = driver.find_element_by_css_selector('button[data-testid="allow"]')
        # x =  driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[1]/div/button')
        print("Clicking: "+x.text)
        driver.execute_script("arguments[0].click();", x)
    except:
        print("Couln't switch window/click allow location")
        sleep(2)
    else:
        break
sleep(2)
        
while True:
    try:
        x = driver.find_element_by_css_selector('button[data-testid="decline"]')
        # x =  driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[1]/div/button')
        print("Clicking: "+x.text)
        driver.execute_script("arguments[0].click();", x)
    except:
        print("Couln't click disallow")
        sleep(2)
    else:
        break
sleep(2)

while True:
    try:
        x = driver.find_element_by_css_selector('button[data-testid="gamepadDislike"]')
        # x =  driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[1]/div/button')
        print("Clicking: "+x.text)
        driver.execute_script("arguments[0].click();", x)
    except:
        print("Couln't click disallow")
        sleep(2)



# driver.switch_to.alert.accept();

# driver.quit()
# x.click()
# driver.find_element_by_css_selector('button[data-testid="loginWithGoogle"]')


# driver.find_element(By.ID, 'username').send_keys('YOURUSERNAME')
# driver.find_element(By.ID, 'password').send_keys('YOURPASSWORD')
# driver.find_element(By.ID, 'password').send_keys(Keys.ENTER)

# sleep(10)
# # print(boxes[0])
# # boxes[0].send_keys('faketester6000@gmail.com')
# driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')

# all_jobs = driver.find_elements_by_class_name('job-card-container')
# print(len(all_jobs))
# for i in all_jobs:
#     sleep(2)
#     i.click()
#     sleep(2)
#     driver.execute_script("arguments[0].click();", driver.find_element_by_class_name('jobs-save-button'))
#     # c = driver.find_element_by_css_selector('#urn\:li\:fs_easyApplyFormElement\:\(urn\:li\:fs_normalized_jobPosting\:3070290368\,56118474\,phoneNumber\~nationalNumber\)')
#     # c.send_keys('11111111')
#     # driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//*[@id="ember333"]'))
#     # sleep(2)
#     # driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//*[@id="ember347"]'))
    
    