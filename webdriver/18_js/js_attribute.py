from selenium import webdriver
from time import sleep

driver =webdriver.Chrome()

driver.maximize_window()

driver.get("http://www.baidu.com")
#dr.find_element_by_id('kw')
element = driver.find_element_by_id('su')

driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",element,'background:yellow')

sleep(3)


#removeAttribute

element = driver.find_element_by_id('data')

driver.execute_script("document.getElementById('data').removeAttribute('readonly');")
driver.execute_script(c)


driver.execute_script("argument[0].removeArrt('readnoly');",element)
driver.quit()