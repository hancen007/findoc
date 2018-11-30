# -*- coding: utf-8 -*-
# @File  : test_assert_raises.py
# @Author: 岑苏岸
# @Date  : 2018/10/9
# @Desc  :



import sys
sys.path.append(".")
import requests
import pytest
import is_leap_year

class TestAssert():
    # 对一个判断是否是闰年的方法进行测试
    def test_exception_typeerror(self):
        with pytest.raises(TypeError):
            is_leap_year.is_leap_year('ss')

    def test_true(self):
        assert is_leap_year.is_leap_year(400) == True