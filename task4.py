from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://mbasic.facebook.com/')
# time.sleep(5)
user = "channojusonu36@gmail.com"
password = "nityasantosh123"
browser.find_element_by_name("email").send_keys(user)
# time.sleep(2)
browser.find_element_by_name("pass").send_keys(password)
browser.find_element_by_name("login").click();
browser.find_element_by_class_name("bl.bm.bn.bo.bp.bq").click()
v = Select(browser.find_element_by_name("verification_method"))
v.select_by_index(1)
browser.find_element_by_class_name("bi.bj.bk.bl.bm.bn").click()
date = Select(browser.find_element_by_name("birthday_captcha_day"));
date.select_by_index(25)
month = Select(browser.find_element_by_name("birthday_captcha_month"))
month.select_by_visible_text("Sep")
year = Select(browser.find_element_by_name("birthday_captcha_year"))
for opt in year.options:
            year.select_by_visible_text("2001")
browser.find_element_by_class_name("bj.bk.bl.bm.bn.bo").click()
browser.find_element_by_class_name("bg.bh.bi.bj.bk.bl").click()
browser.find_element_by_class_name("bh.bf.bg").click()
browser.find_element_by_xpath("//*[@id=\"m-timeline-cover-section\"]/div[3]/a[2]").click()
browser.find_element_by_xpath("//*[@id=\"root\"]/div[1]/div[2]/div/div[2]/div[1]/table/tbody/tr/td[2]/a").click()
browser.find_element_by_xpath("//*[@id=\"u_0_i\"]/footer/div[2]/a[1]").click()
browser.find_element_by_xpath("//*[@id=\"composerInput\"]").send_keys("Happy Birthday!!")
browser.find_element_by_xpath("//*[@id=\"u_0_0\"]/tbody/tr/td[2]/div/input").click()