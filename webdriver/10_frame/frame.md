定位frame中的元素
=================

场景
----
处理frame需要用到2个方法，分别是switch_to.frame(name_or_id)和switch_to.default_content()

switch_to.frame方法把当前定位的主体切换了frame里。怎么理解这句话呢？我们可以从frame的实质去理解。frame中实际上是嵌入了另一个页面，而webdriver每次只能在一个页面识别，因此才需要用switch_to.frame方法去获取frame中嵌入的页面，对那个页面里的元素进行定位。

switch_to.default_content方法的话则是从frame中嵌入的页面里跳出，跳回到最外面的原始页面中。

如果页面上只有1个frame的话那么这一切都是很好理解的，但如果页面上有多个frame，情况有稍微有点复杂了。