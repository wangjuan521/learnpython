#coding=utf-8
#@time   :2021/6/8  17:32
#@Author :wangjuan
import pytest
@pytest.mark.webui
def test_01():
    print('web01')
@pytest.mark.webui
def test_02():
    print('web02')
@pytest.mark.interface
def test_03():
    print('web03')
@pytest.mark.interface
def test_04():
    print('web04')
if __name__ == '__main__':
    pytest.main(['-s', 'test_casedemo.py', '-m webui']);