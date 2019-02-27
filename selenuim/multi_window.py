# -*- coding:utf-8 -*-
# Edited by bighead 19-2-27

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.baidu.com")

time.sleep(2)
JS1 = 'window.open("https://www.sogou.com")'
driver.execute_script(JS1)
time.sleep(2)
JS2 = 'window.open("https://fanyi.youdao.com")'
driver.execute_script(JS2)
