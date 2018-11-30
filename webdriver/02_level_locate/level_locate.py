# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

dr = webdriver.Chrome()

file_path = 'http://efssit.midea.com/admin/'

dr.get(file_path)

dr.find_element_by_id('mobile').send_keys('duyl')
dr.find_element_by_id('password').send_keys('Mid201608')
dr.find_element_by_id('login').click()
time.sleep(2)
dr.execute_script("refreshLeft('bizsys-240288a81549ee23a01549ee533e90000','授信中心')")
#dr.find_element_by_id('topMenu').find_element_by_link_text('授信中心')

time.sleep(2)

dr.quit()
