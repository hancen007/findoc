# Select

### 场景

在处理下拉框(select)的时候selenium给我们提供了一系列的便捷方法，我们只需要使用```selenium.webdriver.support.select.Select```类来稍微封装一下就好了。


下面是我们经常会用到的一些方法

* options: 返回下拉框里所有的选项
* all_selected_options: 返回所有选中的选项
* select_by_value(value): 通过option的value值来选择
* select_by_index(index) 通过option的顺序来选择
* select_by_visible_text(text): 通过option的text来选择