from selenium import webdriver
import random

baseUrl = "https://docs.google.com/forms/d/e/1FAIpQLSf94g2-TSUgduHEoTI8Ecjrd2074M6rB6vEEGwmQwuu7jN3zw/viewform"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(3)

driver.execute_script("arguments[0].scrollIntoView(true);", '//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[7]/div[1]/div[1]/div[3]/div[1]')
print('k')
driver.execute_script("arguments[0].scrollIntoView(true);", "//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
print('o')