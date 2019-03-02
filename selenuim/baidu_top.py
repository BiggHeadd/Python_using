# -*- coding:utf-8 -*-
# Edited by bighead 19-3-2

from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.get("http://top.baidu.com/")

# e.g.
# //*[@id="hot-list"]/li[1]
# //*[@id="hot-list"]/li[2]
# //*[@id="hot-list"]/li[1]/a[1]
top = []
for i in range(1, 10):
    title = dr.find_element_by_xpath('//*[@id="hot-list"]/li[' + str(i) +']/a[1]').get_attribute('title')
    top.append(title)
    print(title)

dr.find_element_by_xpath('//*[@id="hot-list"]/li[1]/a[1]').click()


time.sleep(2)
dr.quit()
