from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Firefox()
driver.get('https://www.linkedin.com/login')

driver.find_element(By.ID, 'username').send_keys('YOURUSERNAME')
driver.find_element(By.ID, 'password').send_keys('YOURPASSWORD')
driver.find_element(By.ID, 'password').send_keys(Keys.ENTER)

sleep(10)
# print(boxes[0])
# boxes[0].send_keys('faketester6000@gmail.com')
driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')

all_jobs = driver.find_elements_by_class_name('job-card-container')
print(len(all_jobs))
for i in all_jobs:
    sleep(2)
    i.click()
    sleep(2)
    driver.execute_script("arguments[0].click();", driver.find_element_by_class_name('jobs-save-button'))
    # c = driver.find_element_by_css_selector('#urn\:li\:fs_easyApplyFormElement\:\(urn\:li\:fs_normalized_jobPosting\:3070290368\,56118474\,phoneNumber\~nationalNumber\)')
    # c.send_keys('11111111')
    # driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//*[@id="ember333"]'))
    # sleep(2)
    # driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//*[@id="ember347"]'))
    
    