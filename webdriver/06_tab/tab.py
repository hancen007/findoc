from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()

first_url = 'https://www.baidu.com'
dr.get(first_url)

# 方法1：层级定位，先定位ul再定位li
dr.find_element_by_class_name('nav').find_element_by_link_text('About').click()
sleep(1)

# 方法2: 直接定位link
dr.find_element_by_link_text('Home').click()
sleep(1)

dr.quit()
