处理alert/confirm/prompt
========================

场景
----
webdriver中处理原生的js alert confirm 以及prompt是很简单的。具体思路是使用switch_to.alert()方法定位到alert/confirm/prompt。然后使用text/accept/dismiss/send_keys按需进行操做

* text。返回alert/confirm/prompt中的文字信息
* accept。点击确认按钮
* dismiss。点击取消按钮，如果有的话
* send_keys。向prompt中输入文字

```
# 点击链接弹出alert
dr.find_element_by_id('tooltip').click()

try:
	alert = dr.switch_to_alert()
	alert.accept()
except:
	print ('no alerts display')

sleep(1)
dr.quit()
```