from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.facebook.com/')
# time.sleep(5)
user = "channojusonu36@gmail.com"
password = "nityasantosh123"
browser.find_element_by_name("email").send_keys(user)
# time.sleep(2)
browser.find_element_by_name("pass").send_keys(password)
browser.find_element_by_class_name("_6ltg").click()
time.sleep(10)



