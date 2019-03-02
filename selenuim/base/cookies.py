# -*-coding:utf-8-*-
# Edited by bighead 19-2-27

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

cookies = driver.get_cookies()

cookie = driver.get_cookie("BAIDUID")


driver.add_cookie({"name":"testname_1","value":"testvalue_1"})

print cookies
# print cookie

driver.delete_all_cookies()
driver.quit()
