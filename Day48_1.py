from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://python.org')
menu = driver.find_element_by_xpath('/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul')
event_name = menu.find_elements(By.TAG_NAME, 'a')
event_time = menu.find_elements(By.TAG_NAME, 'time')
d = {i:{'time':event_time[i].text, 'name': event_name[i].text.strip()} for i in range(len(event_name))}
print(d)
driver.quit()