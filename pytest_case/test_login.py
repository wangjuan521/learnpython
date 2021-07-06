#coding=utf-8
#@time   :2021/6/7  15:58
#@Author :wangjuan
import pytest
from config.ReadYaml import *
class TestDemo:
    @pytest.mark.parametrize('users',readUser('./Data/testuser.yaml'))
    def test_demo1(self,users):
        print(readUser('./Data/testuser.yaml'))
        print(1111111111111,users)
    def test_demo2(self):
        print(222222222222)
    @pytest.mark.parametrize('userdata',readUser('./Data/user.yaml'))
    def test_read(self,userdata):
        print('读取yaml文件')
        print(userdata,type(userdata))
    # def setup_class(self):
    #     print('setup_class')
    # def teardown_class(self):
    #     print('teardown_class');
    # def setup_module(self):
    #     print('setup_module');
    # def teardown_module(self):
    #     print('teardown_module');
    # def setup_method(self):
    #     print('setup_module');
    # def teardown_method(self):
    #     print('teardown_module');
if __name__ == '__main__':
    pytest.main(['-v', '-s']);


