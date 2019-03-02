# -*-coding:utf-8-*-
# Edited by bighead 19-2-26

from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.toutiao.com")
#driver.set_window_size(800, 480)
driver.maximize_window()

## js
# js = 'var q=document.documentElement.scrollTop=10000'
# js = "window.scrollTo(10000,document.body.scrollHeight)"
# driver.execute_script(js)


# like mouse act
# # driver.save_screenshot("save_1.png")
# #
# # ac = driver.find_element_by_xpath("//ul[@infinite-scroll-disabled]/li[last()]")
# # ActionChains(driver).move_to_element(ac).perform()
# #
# # driver.save_screenshot("save_2.png")

time.sleep(2)
driver.quit()
