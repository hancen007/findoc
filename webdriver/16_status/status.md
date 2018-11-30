获取测试对象的状态
===================

场景
----
在web自动化测试中，我们需要获取测试对象的四种状态

* 是否显示。使用element.displayed?()方法；
* 是否存在。使用find_element方法，捕获其抛出的异常，如果是NoSuchElement异常的话则可以确定该元素不存在；
* 是否被选中。一般是判断表单元素，比如radio或checkbox是否被选中。使用element.selected?()方法；
* 是否enable，也就是是否是灰化状态。使用element.enabled?()方法；