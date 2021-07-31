from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r'./webdriver/chromedriver.exe')
driver.get("https://meroshare.cdsc.com.np/#/login")

time.sleep(2)
select = Select(driver.find_element_by_class_name('select2-hidden-accessible'))
select.select_by_visible_text('AGRICULTURAL DEVELOPMENT BANK LIMITED (17200)')

username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
login = driver.find_element_by_class_name('sign-in')

username.send_keys("username")
time.sleep(2)
password.send_keys("password")
time.sleep(2)

login.click()



