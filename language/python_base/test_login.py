import pytest

@pytest.mark.xfail
def test_03():
    print('test_03')
    
def test_fail():
    print('test_fail')
    assert 1 == 2

def test_error():
    print('test_error')
    error_func()

def error_func():
    

