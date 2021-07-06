#coding=utf-8
#@time   :2021/6/7  16:56
#@Author :wangjuan
'''
这是 pytest的 setup 和 teardown的配置文件，注意文件名称一定是 conftest，不能是其他的
scope 函数定义的几种等级，(默认是function等级)
session：在本次session中只执行一次
module:再模块级别中执行一次
class:在类级别中只执行一次
function：函数级，每个测试函数都会执行一次固件
'''
import pytest
# 定义一个基本的setup 和 teardown
# 预置函数，比如有些数据需要关联数据，比如某个接口请求需要一个token，那么我们可以使用预置函数，先获取token，然后执行用例
@pytest.fixture(scope='module')
def XuZhu():
    print('虚竹生命了，但是很强')
    return "我是王娟"
