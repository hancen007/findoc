# Pytest是什么
Pytest是Python的一个测试工具，可以用于所有类型和级别的软件测试。Pytest是一个可以自动查找到你编写的用例并运行后输出结果的测试框架。

- Pytest有什么特点
- pytest是一个命令行工具
- pytest可以扩展第三方插件
- pytest易于持续集成和应用于web自动化测试
- pytest编写用例简单，并具有很强的可读性
- pytest可以直接采用assert进行断言，不必采用self.assertEqual()等
- pytest可以运行unittest编写的用例
- pytest可以运行以test或test开头或结尾的包、文件和方法


## Pytest的简单示例
```
# test_simple.py
import requests

def test_one():
    r = requests.get('https://api.github.com/events')
    assert r.status_code == 200
运行测试用例可以直接在命令行中执行该py文件 pytest test_simple.py

(python_interface_base) F:\python_interface_test\python_interface_test\test_requests>pytest test_simple.py
============================= test session starts =============================
platform win32 -- Python 3.6.4, pytest-3.4.2, py-1.5.2, pluggy-0.6.0
rootdir: F:\python_interface_test\python_interface_test\test_requests, inifile:
collected 1 item

test_simple.py .                                                         [100%]

========================== 1 passed in 3.26 seconds ===========================
```
运行py文件中的单个用例
```
# test_simple.py
import requests

def test_one():
    r = requests.get('https://api.github.com/events')
    assert r.status_code == 200

def test_two():
    r = requests.get('https://api.github.com/events')
    assert r.encoding == 'utf'
运行py文件中的单个用例时，可以采用命令pytest test_simple.py::test_two

(python_interface_base) F:\python_interface_test\python_interface_test\test_requests>pytest test_simple.py::test_two
============================= test session starts =============================
platform win32 -- Python 3.6.4, pytest-3.4.2, py-1.5.2, pluggy-0.6.0
rootdir: F:\python_interface_test\python_interface_test\test_requests, inifile:
collected 1 item

test_simple.py F                                                         [100%]

================================== FAILURES ===================================
__________________________________ test_two ___________________________________

    def test_two():
        r = requests.get('https://api.github.com/events')
>       assert r.encoding == 'utf'
E       AssertionError: assert 'utf-8' == 'utf'
E         - utf-8
E         ?    --
E         + utf

test_simple.py:9: AssertionError
========================== 1 failed in 1.56 seconds ==========================
```
由于断言失败，从结果中可以看到失败的具体原因。
