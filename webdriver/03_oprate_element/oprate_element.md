操作测试对象
============

场景
----
定位到具体的对象后，我们就可以对这个对象进行具体的操作，比如先前已经看到过的点击操作(click)。一般来说，webdriver中比较常用的操作对象的方法有下面几个

* click 点击对象
* send_keys 在对象上模拟按键输入
* clear 清除对象的内容，如果可以的话



```
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
```