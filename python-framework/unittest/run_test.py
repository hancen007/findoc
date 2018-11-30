
import time, sys,os

from HTMLTestRunner_PY3 import HTMLTestRunner
import unittest

# 指定测试用例为当前文件夹下的 test_case 目录
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')


if __name__ == "__main__":

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='报告详细如下: ')
    runner.run(discover)
    fp.close()
