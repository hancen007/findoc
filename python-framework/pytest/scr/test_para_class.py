# -*- coding: utf-8 -*-
# @File  : test_para_class.py
# @Author: 岑苏岸
# @Date  : 2018/10/9
# @Desc  :

import sys
sys.path.append('.')
import is_leap_year
import pytest

class TestPara():

    # 参数传入year中
    @pytest.mark.parametrize('year, expected', [(1, False), (4, True)])
    def test_is_leap(self, year, expected):
        assert is_leap_year.is_leap_year(year) == expected







    @pytest.mark.parametrize('year, expected', [(0, ValueError), ('-4', TypeError), (-4, ValueError), ('ss', TypeError), (100, ValueError)])
    def test_is_typeerror(self, year,expected):
        if expected == ValueError:
            with pytest.raises(ValueError) as excinfo:
                is_leap_year.is_leap_year(year)
            assert excinfo.type == expected
        else:
            with pytest.raises(TypeError) as excinfo:
                is_leap_year.is_leap_year(year)
            assert excinfo.type == expected