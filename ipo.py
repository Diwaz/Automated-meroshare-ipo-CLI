from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r'./webdriver/chromedriver.exe')
driver.get("https://meroshare.cdsc.com.np/#/login")

time.sleep(2)

drop = driver.find_element_by_class_name('select2-selection__rendered')
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
login = driver.find_element_by_class_name('sign-in')
drop.click()
bank = driver.find_element_by_class_name('select2-search__field')
bank.send_keys('nmb')
toselect = driver.find_element_by_tag_name('li')
toselect.click()
username.send_keys("username")
password.send_keys("password")
login.click()
time.sleep(2)
asba = driver.find_element_by_link_text('My ASBA')
asba.click()
time.sleep(1)
check_ipo = driver.find_element_by_class_name('share-of-type').text


apply = driver.find_element_by_xpath('//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div[2]/div/div[2]/div/div[4]/button')
apply.click()
time.sleep(0.5)

tap = driver.find_element_by_id('selectBank')
tap.click()
time.sleep(0.5)
tap.send_keys('nmb')
totap = driver.find_element_by_xpath('//*[@id="selectBank"]/option[2]')

kitta = driver.find_element_by_id('appliedKitta')
kitta.send_keys(10)
amount = driver.find_element_by_id('amount')
amount.send_keys(1000)
crnNumber = driver.find_element_by_id('crnNumber')
crnNumber.send_keys(289798792)
disclaimer = driver.find_element_by_id('disclaimer')
disclaimer.click()





