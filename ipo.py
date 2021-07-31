from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

total = int(input("How many users do u have ?"))
with open('Credentials.txt') as fo:
        for line in fo:
            arr = line.split('?')
            for x in range(total):
                print("User "+str(x+1)+" :"+arr[x])

            
            no = int(input("Which user's ipo to apply? "))
            
            get_user = arr[no-1].split('-')
            bankB = get_user[0]
            user = get_user[1]
            passB = get_user[2]
            crn = get_user[3]
            row = get_user[4]

driver = webdriver.Chrome(executable_path=r'./webdriver/chromedriver.exe')
driver.get("https://meroshare.cdsc.com.np/#/login")

time.sleep(2)

    

    
            


drop = driver.find_element_by_class_name('select2-selection__rendered')
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
login = driver.find_element_by_class_name('sign-in')
drop.click()
bank = driver.find_element_by_class_name('select2-search__field')
bank.send_keys(bankB)
toselect = driver.find_element_by_tag_name('li')
toselect.click()
username.send_keys(user)
password.send_keys(passB)
login.click()
time.sleep(2)
asba = driver.find_element_by_link_text('My ASBA')
asba.click()
time.sleep(1)
check_ipo = driver.find_element_by_class_name('share-of-type').text

                                      # //*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div[1]/div/div[2]/div/div[4]/button
apply = driver.find_element_by_xpath('//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div['+row+']/div/div[2]/div/div[4]/button')
apply.click()
time.sleep(0.5)

tap = driver.find_element_by_id('selectBank')
tap.click()
time.sleep(0.5)
tap.send_keys(bankB)
totap = driver.find_element_by_xpath('//*[@id="selectBank"]/option[2]')

kitta = driver.find_element_by_id('appliedKitta')
kitta.send_keys(10)
amount = driver.find_element_by_id('amount')
amount.send_keys(1000)
crnNumber = driver.find_element_by_id('crnNumber')
crnNumber.send_keys(crn)
disclaimer = driver.find_element_by_id('disclaimer')
disclaimer.click()





