##  页面元素定位方法



### 1. 定位元素方法

WebDriver 提供了八种元素定位方法，在 Python 语言中，所对应的方法如下：

```
find_element_by_id()
find_element_by_name
find_element_by_class_name
find_element_by_tag_name
find_element_by_link_text
find_element_by_partial_link_text
find_elements_by_xpath
find_element_by_css_selector

```

[示例地址](http://efssit.midea.com/)

## 对应方法如下：

### ID定位

find_element_by_id()

### Name定位
find_element_by_name

### Class


### tag


### link_text 和 partial_link_text


-----

###  css_selector


0. 使用绝对路径定位元素


1. 使用相对路径定位元素


2. 使用class名称定位元素


3. 使用ID属性定位元素


4. 使用页面其他属性定位

表达式1 ```img[alt = 'div1']```
表达式1 ```img[alt = 'div1'][href='http://xxx.com']```

5. 使用属性值的一部分内容定位元素


表达式1  ```a[herf^ ='http://news.' ]```

表达式2  ```a[herf$ = 'baidu.com']```

表达式2  ```a[herf* = 'baidu']```

代码解释：
 - 字符^ 指明从字符串开始匹配
 - 字符$ 指明从字符串结束匹配
 - 字符* 指明模拟匹配

6. 使用页面元素进行子页面元素查找

表达式1  ```div#div1 > input#div1input```

表达式2 ```div input```

代码解释：
- 表达式1 定位一个id为div1的页面元素，“>” 它的子页面元素进行查找，input#div1input
- 表达式2 匹配所有 div元素后代的 input元素，父元素div和子元素input要用空格分隔

7. 查找同级兄弟页面元素

表达式1 div#div1 > input + a
表达式2 div#div1 > input + a + img
表达式3 div#div1 > input + * + img
表达式4 ul#recordlist>p~li
---
代码解释
- 表达式1 查找input 页面元素后面同级且相近的链接元素
- 表达式2 查找input 页面元素后面同级且相近的链接后面 img元素
- 表达式3 查找input 页面元素后面同级且相近的链接元素
- 表达式4 id属性为recordlist的ul页面元素下，查看p页面元素以后所有li元素



8. 多元素选择器
```
div#div1,input,a
```





### XPath

绝对路径和相对路径的区别


绝对路径  以 "/"  开头， 让xpath 从文档的根节点开始解析

相对路径  以"//" 开头， 让xpath 从文档的任何元素节点开始解析


相对路径定位方式
在被测试网页中，查找第一个div标签中的按钮

XPath的表达式
```
//input[@value="查询"]

WebElement button = driver.findElement(By.xpath("//input[@value='查询']"));
```


使用索引号定位
在被测试网页中， 查找第二个div标签中的"查询"按钮
```
//input[2]

WebElement button = driver.findElement(By.xpath("//input[2]"));
```


使用页面属性定位
定位被测试页面中的第一个图片元素
```
//img[@alt='div1-img1']

WebElement button = driver.findElement(By.xpath("//img[@alt='div1-img1']"));
```


模糊定位starts-with关键字
查找图片alt属性开始位置包含'div1'关键字的元素

```
//img[starts-with(@alt,'div')]

```

模糊定位contains关键字
查找图片alt属性包含'g1'关键字的元素
```
//img[contains(@alt,'g1')]
```

text() 函数 文本定位

查找所有文本为"百度搜索" 的元素

```
driver.findElement(By.xpath("//*[text()='百度搜索']"));

```


查找所有文本为“搜索” 的超链接
```
driver.findElement(By.xpath("//a[contains(text(),'搜索')]"));
```


