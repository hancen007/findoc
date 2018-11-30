from selenium import webdriver
import time

dr = webdriver.Chrome()

file_path = 'http://fintest.midea.com/fintest/'

dr.get(file_path)

# click
dr.find_element_by_link_text('主页').click()
time.sleep(1)
dr.find_element_by_link_text('行业资讯').click()

# send_keys
dr.get('http://fintest.midea.com/fintest/wp-login.php')
element = dr.find_element_by_name('log')
element.send_keys('test')
time.sleep(1)

# clear
element.clear()
time.sleep(1)

dr.quit()