## 第4章 WebDriverAPI

本章内容参考官方 API，将最常用的一些方法结合具体 Web 应用进行学习。

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

### 2. 鼠标事件

在 WebDriver 中，将这些关于鼠标操作的方法封装在 ActionChains 类提供。
ActionChains 类提供了鼠标操作的常用方法：

```
* perform()： 执行所有 ActionChains 中存储的行为；
* context_click()： 右击；
* double_click()： 双击；
* drag_and_drop()： 拖动；
* move_to_element()： 鼠标悬停
```

- 鼠标悬停操作

对于 ActionChains 类所提供的鼠标方法与前面学过的 click()方法的用法有所不同。如百度“设置”悬停菜
单。

```
> baidu.py
from selenium import webdriver
#引入 ActionChains 类
from selenium.webdriver.common.action_chainimport ActionChains
driver = webdriver.Chrome()
driver.get("https://www.baidu.cn")
```

------

- 定位到要悬停的元素
```
above = driver.find_element_by_link_text("设置")
对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()
from selenium.webdriver importActionChains
```
---
导入提供鼠标操作的 ActionChains 类。
ActionChains(driver)
调用 ActionChains()类，将浏览器驱动 driver 作为参数传入。
move_to_element(above)
context_click()方法用于模拟鼠标右键操作，在调用时需要指定元素定位。
perform()
执行所有 ActionChains 中存储的行为，可以理解成是对整个操作的提交动作。

### 3. 键盘事件

Keys()类提供了键盘上几乎所有按键的方法。前面了解到，send_keys()方法可以用来模拟键盘输入，除此
之外，我们还可以用它来输入键盘上的按键，甚至是组合键，如 Ctrl+A、Ctrl+C 等。

```
baidu.py
from selenium import webdriver

# 引入 Keys 模块
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# 输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
# 删除多输入的一个 m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
# 输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")
# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
# ctrl+v 粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
# 通过回车键来代替单击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
driver.quit()
```

------

需要说明的是，上面的脚本没有什么实际意义，仅向我们展示模拟键盘各种按键与组合键的用法。
​```from selenium.webdriver.common.keys import Keys```
在使用键盘按键方法前需要先导入 keys 类。
以下为常用的键盘操作：

```
send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
send_keys(Keys.SPACE) 空格键(Space)
send_keys(Keys.TAB) 制表键(Tab)
send_keys(Keys.ESCAPE) 回退键（Esc）
send_keys(Keys.ENTER) 回车键（Enter）
send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
send_keys(Keys.F1) 键盘 F1
……
send_keys(Keys.F12) 键盘 F12
```

### 4. 设置元素等待

WebDriver 提供了两种类型的等待：显式等待和隐式等待

#### 4.1 显示等待

显式等待使 WebdDriver 等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常
（TimeoutException）。
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
element = WebDriverWait(driver, 5, 0.5).until(
EC.presence_of_element_located((By.ID, "kw")))
element.send_keys('selenium')
driver.quit()
```

------

​WebDriverWait 类是由 WebDirver 提供的等待方法。在设置时间内，默认每隔一段时间检测一次当前页面
元素是否存在，如果超过设置时间检测不到则抛出异常。具体格式如下：
WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
driver ：浏览器驱动。
timeout ：最长超时时间，默认以秒为单位。
poll_frequency ：检测的间隔（步长）时间，默认为 0.5S。
ignored_exceptions ：超时后的异常信息，默认情况下抛 NoSuchElementException 异常。
WebDriverWait()一般由 until()或 until_not()方法配合使用，下面是 until()和 until_not()方法的说明。

- until(method, message=‘ ’)
  调用该方法提供的驱动程序作为一个参数，直到返回值为 True。
- until_not(method, message=’’)
  调用该方法提供的驱动程序作为一个参数，直到返回值为 False。
  在本例中，通过 as 关键字将 expected_conditions 重命名为 EC，并调用 presence_of_element_located()方法判断元素是否存在。

#### 4.2 隐式等待

WebDriver 提供了 implicitly_wait()方法来实现隐式等待，默认设置为 0。它的用法相对来说要简单得多。

```
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime
driver = webdriver.Firefox()
# 设置隐式等待为 10 秒
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
try:
print(ctime())
driver.find_element_by_id("kw22").send_keys('selenium')
except NoSuchElementException as e:
print(e)
finally:
print(ctime())
driver.quit()
```
------

​implicitly_wait()默认参数的单位为秒，本例中设置等待时长为 10 秒。首先这 10 秒并非一个固定的等待时间，它并不影响脚本的执行速度。其次，它并不针对页面上的某一元素进行等待。当脚本执行到某个元素定位时，如果元素可以定位，则继续执行；如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到。假设在第 6 秒定位到了元素则继续执行，若直到超出设置时长（10 秒）还没有定位到元素，则抛出异常。

### 5. 定位一组元素

WebDriver 还提供了 8 种用于定位方法来定位一组元素。

```
find_elements_by_id()
find_elements_by_name()
find_elements_by_class_name()
find_elements_by_tag_name()
find_elements_by_link_text()
find_elements_by_partial_link_text()
```

------

定位一组元素的方法与定位单个元素的方法类似，唯一的区别是在单词 element 后面多了一个 s 表示复数

### 6. 多表单切换

在 Web 应用中经常会遇到 frame/iframe 表单嵌套页面的应用，WebDriver 只能在一个页面上对元素识别与定位，对于 frame/iframe 表单内嵌页面上的元素无法直接定位。这时就需要通过 switch_to.frame()方法将当前定位的主体切换为 frame/iframe 表单的内嵌页面中。
```
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.126.com")
driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()
driver.quit()
```

------

switch_to.frame() 默认可以直接取表单的 id 或 name 属性。如果 iframe 没有可用的 id 和 name 属性，则可以通过下面的方式进行定位

### 7. 多窗口切换

在页面操作过程中有时候点击某个链接会弹出新的窗口，这时就需要主机切换到新打开的窗口上进行操作。WebDriver 提供了 switch_to.window()方法，可以实现在不同的窗口之间切换。
以百度首页和百度注册页为例，在两个窗口之间的切换

> windows.py

```
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle
driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text("立即注册").click()
# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles
# 进入注册窗口
for handle in all_handles:
if handle != sreach_windows:
driver.switch_to.window(handle)
print('now register window!')
driver.find_element_by_name("account").send_keys('username')
driver.find_element_by_name('password').send_keys('password')
time.sleep(2)
# ……
# 回到搜索窗口
for handle in all_handles:
if handle == sreach_windows:
driver.switch_to.window(handle)
print('now sreach window!')
driver.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(2)
driver.quit()
```

------

脚本的执行过程：首先打开百度首页，通过 current_window_handle 获得当前窗口的句柄，并赋值给变量
sreach_handle。接着打开登录弹窗，在登录弹窗上单击“立即注册”，从而打开新的注册窗口。通过
window_handles 获得当前打开的所有窗口的句柄，并赋值给变量 all_handles。
第一个循环遍历 all_handles，如果 handle 不等于 sreach_handle，那么一定是注册窗口，因为脚本执行过程
中只打开了两个窗口。所以，通过 switch_to.window()切换到注册页进行注册操作。第二个循环类似，不过这
一次判断如果 handle 等于 sreach_handle，那么切换到百度搜索页，然后进行搜索操作。
在本例中所涉及的新方法如下：
current_window_handle：获得当前窗口句柄。
window_handles：返回所有窗口的句柄到当前会话。
switch_to.window()：用于切换到相应的窗口，与上一节的 switch_to.frame()类似，前者用于不同窗口的切
换，后者用于不同表单之间的切换。

### 8. 警告框处理

在 WebDriver 中处理 JavaScript 所生成的 alert、confirm 以及 prompt 十分简单，具体做法是使用
switch_to_alert()方法定位到 alert/confirm/prompt，然后使用 text/accept/dismiss/ send_keys 等方法进行操作。

```
- text：返回 alert/confirm/prompt 中的文字信息。
- accept()：接受现有警告框。
- dismiss()：解散现有警告框。
- send_keys(keysToSend)： 发送文本至警告框。keysToSend：将文本发送至警告框。
```

百度搜索设置弹出的窗口是不能通过前端工具对其进行定位的，这个时候就可以通过switch_to_alert()方法接受这个弹窗。

> alerts.py

```
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 鼠标悬停至“设置”链接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()
# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
# 保存设置
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(2)
# 接受警告框
driver.switch_to_alert().accept()
driver.quit()
```

------

从这个例子中我们重温了 4.4 节中 ActionChains 类所提供的 move_to_element()鼠标悬停的使用，将鼠标悬停在“设置”链接上，然后在弹出的下拉菜单中单击“搜索设置”按钮，设置完成后单击“保存设置”，弹出保存确认警告框。通过 switch_to_alert()方法获取当前页面上的警告框，并使用 accept()方法接受警告框。

### 9.窗口截图

自动化用例是由程序去执行的，因此有时候打印的错误信息并不十分明确。如果在脚本执行出错的时候能对当前窗口截图保存，那么通过图片就可以非常直观地看出出错的原因。WebDriver 提供了截图函数

```
get_screenshot_as_file()来截取当前窗口。
baidu.py
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)
# 截取当前窗口，并指定截图图片的保存位置
driver.get_screenshot_as_file("D:\\pyse\\baidu_img.jpg")
driver.quit()
```

------

脚本运行完成后打开 D 盘，就可以找到 baidu_error.jpg 图片文件了。

### 10. 下拉框处理

Selenium 专门使用 Select 类来处理下接框

```
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 鼠标悬停至“设置”链接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()
sleep(1)
# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
sleep(2)
# 搜索结果显示条数
select = driver.find_element_by_xpath("//select[@id='nr']")
Select(select).select_by_value('20') # 显示 20 条
driver.quit()
```

------

Select 用于定位<select>标签。
select_by_value() 方法用于定位下接选项中的 value 值。
