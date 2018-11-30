# -*- coding: utf-8 -*-
# @File  : test_simple.py
# @Author: 岑苏岸
# @Date  : 2018/10/9
# @Desc  :




import requests

def test_one():
    r = requests.get('https://api.github.com/events')
    assert r.status_code == 200

def test_two():
    r = requests.get('https://api.github.com/events')
    assert r.encoding == 'utf'