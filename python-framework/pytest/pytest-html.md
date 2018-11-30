# Pytest的报告输出方式
- JunitXml格式的报告文件：pytest --junitxml=path
- resultlog文本格式的报告文件：pytest --resultlog=path(不常用，预计在4.0移除)
- 第三方插件：pytest-html
## Pytest测试报告示例
### 1、JunitXML格式的测试报告
- 1、JunitXML格式的报告是在pytest命令后加上--junitxml=path。
运行测试集中的用例：pytest -q --tb=no --junitxml='E:\python_interface_test\results\makejunitstyle.xml'
--tb=no是不输出traceback信息
看图：4个用例失败，25个用例通过，1个用例xfailed，1个用例错误


查看生成的报告，报告路径和名称为--junitxml=之后设定的
看图：
1）、testsuit中的信息包含：总运行时间、总用例数、跳过或执行不成功的用例数；
2）、testcase中的信息包括：case运行时间、case名、case所在的行数、case所在的模块名、case所在的类名；
3）、如果case有输出信息或错误信息，也会在对应的元素中显示，参见有输出或错误的用例。
2、resultlog文本格式的测试报告（预计在4.0移除）
运行命令：pytest -q --tb=no --resultlog='E:\python_interface_test\results\resultlog2.txt'


3、pytest-html第三方插件生成的测试报告
秉持拿来主义的精神，这个报告应该会好看一点
4.1.安装pytest-html
pytest插件的安装和卸载方式为：

pip install pytest-NAME
pip uninstall pytest-NAME

4.2.pytest-html的使用
pytest-html顾名思义，生成的报告格式为html的。

运行命令：pytest -q --tb=no --html=E:\python_interface_test\results\makehtml.html

查看结果：结果中分为3部分，Environment、Summary、Results；
1）、在html报告中会有报告生成日期及采用的pytest-html版本；
2）、Environment：记录了运行的环境信息；
3）、Summary：描述了运行用例数、时间及用例的状态；
4）、Results：记录了每个用例的执行状态、用例名称及路径、执行时间；（ps：执行时间只精确到2位小数，所以好多用例的时间都为0）


总结
从上面的介绍中看出，JunitXML和pytest-html的可读性和可分析性更好。

JunitXML可用于持续集成，格式为xml；
pytest-html界面美观，执行信息及结果信息全面。

