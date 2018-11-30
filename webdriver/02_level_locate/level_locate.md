层级定位
========

场景
----
在实际的项目测试中，经常会有这样的需求：页面上有很多个属性基本相同的元素，现在需要具体定位到其中的一个。由于属性基本相当，所以在定位的时候会有些麻烦，这时候就需要用到层级定位。先定位父元素，然后再通过父元素定位子孙元素。

代码
----
下面的代码演示了如何通过层级定位来定位下拉菜单中的某一项。由于两个下拉菜单中每个选项的link text都相同，href也一样，所以在这里就需要使用层级定位了。

具体思路是：先点击显示出1个下拉菜单，然后再定位到该下拉菜单所在的ul，再定位这个ul下的某个具体的link。在这里，我们定位第1个下拉菜单中的Another action这个选项。



```
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

dr = webdriver.Chrome()

file_path = 'http://efssit.midea.com/admin/'

dr.get(file_path)

dr.find_elements_by_id('mobile').send_keys('fanyc2')
dr.find_elemnets_by_id('password').send_keys('Mid201608')
dr.find_elements_by_id('login').click()

dr.find_element_by_link_text('范轶聪').click()


logout = dr.find_element_by_id('logout').find_element_by_link_text('Another action')

webdriver.ActionChains(dr).move_to_element(logout).perform()

time.sleep(2)

dr.quit()
```