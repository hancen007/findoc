# -*- coding: utf-8 -*-
# @File  : test_para.py
# @Author: 岑苏岸
# @Date  : 2018/10/9
# @Desc  :



import sys
sys.path.append('.')
import is_leap_year #测试数据

import pytest

class TestPara():
    def test_is_leap(self, is_leap_y):
        assert is_leap_year.is_leap_year(is_leap_y) == True

    def test_is_typeerror(self, is_type_error):
        with pytest.raises(TypeError):
            is_leap_year.is_leap_year(is_type_error)