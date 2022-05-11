from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# x = driver.find_element(By.ID, 'articlecount').find_element(By.TAG_NAME,'a')
# print(x.text)

driver.get('http://secure-retreat-92358.herokuapp.com/')
input_boxes = driver.find_elements(By.TAG_NAME, 'input')
for i in input_boxes:
    i.send_keys('asdf@asdfas')
input_boxes[-1].send_keys(Keys.ENTER)
# driver.quit()