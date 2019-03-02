# -*- coding:utf-8 -*-
# Edited by bighead 19-3-2

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

dr = webdriver.Chrome()
dr.get("https://toutiao.com")

dr.find_element_by_xpath('//*[@id="rightModule"]/div[1]/div/div/div/input').send_keys(u"手指被可乐炸骨折")
dr.find_element_by_xpath('//*[@id="rightModule"]/div[1]/div/div/div/div').click()

# switch to new page
num=dr.window_handles
print(num)
dr.switch_to_window(num[1])

# click first passage's title
try:
    WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_section_2"]/div/div/div[1]/div/div[1]/a/span')))
finally:
    dr.find_element_by_xpath('//*[@id="J_section_2"]/div/div/div[1]/div/div[1]/a/span').click()

time.sleep(2)
dr.quit()
