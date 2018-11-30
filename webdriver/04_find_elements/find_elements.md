定位一组对象
============

场景
----
从上一节的例子中可以看出，webdriver可以很方便的使用find_element方法来定位某个特定的对象，不过有时候我们却需要定位一组对象，这时候就需要使用find_elements方法。

定位一组对象一般用于以下场景：

* 批量操作对象，比如将页面上所有的checkbox都勾上
* 先获取一组对象，再在这组对象中过滤出需要具体定位的一些对象。比如定位出页面上所有的checkbox，然后选择最后一个




```

# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os

dr = webdriver.Chrome()
file_path =  'file:///' + os.path.abspath('checkbox.html')
dr.get(file_path)


# 选择所有的checkbox并全部勾上
checkboxes = dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
	checkbox.click()
time.sleep(1)
dr.refresh()
time.sleep(2)

# 打印当前页面上有多少个checkbox
print (len(dr.find_elements_by_css_selector('input[type=checkbox]')))

# 选择页面上所有的input，然后从中过滤出所有的checkbox并勾选之
inputs = dr.find_elements_by_tag_name('input')
for input in inputs:
	if input.get_attribute('type') == 'checkbox':
		input.click()

time.sleep(1)

# 把页面上最后1个checkbox的勾给去掉
dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()

time.sleep(1)

dr.quit()

```