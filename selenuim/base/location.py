# -*- coding:utf-8 -*-
# Edited by bighead 19-3-2

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_partial_link_text("新").click()
driver.back()

# driver.find_element_by_xpath(r'//*[@id="kw"]').send_keys("selenium")
# driver.find_element_by_class_name("s_ipt").send_keys("selenium")
# driver.find_element_by_id("su").click()


# elements = driver.find_element_by_tag_name("input")
# print(elements)
# for element in elements:
#     className = element.get_attribute('class')
#     print(className)
#     if className == 'bg s_btn':
#         subscript = elements.index(element)
# elements[subscript].click()

time.sleep(2)
driver.quit()
