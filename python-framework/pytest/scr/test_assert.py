# -*- coding: utf-8 -*-
# @File  : test_assert.py
# @Author: 岑苏岸
# @Date  : 2018/10/9
# @Desc  :


import requests


class TestAssert():

    def test_assert(self):
        r = requests.get('http://www.baidu.com')
        assert r.status_code == 100, "返回200说明访问成功"