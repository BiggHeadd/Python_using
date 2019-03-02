# -*- coding:utf-8 -*-
# Edited by bighead 19-3-2

from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.get("https://www.python.org/")

dr.find_element_by_id("id-search-field").send_keys("fuck")
dr.find_element_by_id("submit").click()

time.sleep(2)
dr.quit()
