
获取测试对象的属性及内容
========================

场景
----
获取测试对象的内容是前端自动化测试里一定会使用到的技术。比如我们要判断页面上是否显示了一个提示，那么我们就需要找到这个提示对象，然后获取其中的文字，再跟我们的预期进行比较。在webdriver中使用element.attribute()方法可以获取dom元素(测试对象)的属性。

获取测试对象的属性能够帮我们更好的进行对象的定位。比如页面上有很多class都是'btn'的div，而我们需要定位其中1个有具有title属性的div。由于selenium-webdriver是不支持直接使用title来定位对象的，所以我们只能先把所有class是btn的div都找到，然后遍历这些div，获取这些div的title属性，一旦发现具体title属性的div，那么返回这个div既可。在webdriver中，使用element.text()方法可以返回dom节点的内容(text)。

代码
----
下面的代码演示了如何获取测试对象的title属性和该对象的文字内容


```
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import os

dr = webdriver.Chrome()

dr.get(file_path)

link = dr.find_element_by_id('tooltip')

sleep(1)
# 获得tooltip的内容
print (link.get_attribute('data-original-title'))

# 获取该链接的text
print (link.text)

dr.quit()
```