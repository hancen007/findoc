from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()

file_path = 'http://fintest.midea.com/fintest/'

dr.get(file_path)

print ("title of current page is %s" %(dr.title))
print ("url of current page is %s" %(dr.current_url))

sleep(1)

dr.quit()
