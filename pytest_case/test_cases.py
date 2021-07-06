#coding=utf-8
#@time   :2021/6/7  14:23
#@Author :wangjuan
import Utlis.Md5Tool as md5tools
import pytest
import Utlis.UrlTool as urltool
import Utlis.HttpTools as Httptool
# 写一个简单的测试用例,以 test 开头
# 这里的XuZhu调用了conftest里面的预置函数
def test_01():
    print(1111)
# pytest环境下，对于参数化的处理是基于mark标记来实现的
'''
pytest 中的setup和teardown:一般可以通过一个配置文件直接进行管理：
配置文件命名一定要是conftest.py，这个是pytest的setup和teardown的配置文件
'''
# 定义一个全局变量 token
token = None;
@pytest.mark.parametrize(['user','pwd','statuscode'],[['zc@163.com','abcdefg','201'],['mymy@163.com','abcdefg1','201'],['mymy04@163.com','abcdefg1','406'],['mymy04@163.com','abcdefg1','406']])
def test_02(user,pwd,statuscode,XuZhu):
    print('----------------',XuZhu)
    print(user,pwd)
    myhead = {};
    myhead['Accept'] = "application/json, text/javascript, */*; q=0.01";
    myhead['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8";
    myhead['X-Requested-With'] = "XMLHttpRequest";
    myhead['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    mydata = {};
    mydata['username'] = user;
    mydata['password'] = md5tools.GetMd5Str(pwd)
    mydata['mem_pwd'] = 1;
    res = Httptool.Send_Post(url=urltool.kuaifuwanglogin, data=mydata, header=myhead)
    res_json = res.json();
    print(res_json['status'],type(res_json['status']))
    status = str(res_json['status']);
    # try:
    #     global token
    #     token=(res.json()['token'])
    # except:
    #     pass
    # 断言预期结果是否等于实际结果
    assert statuscode==status or statuscode=="403"
# # 前置与后置条件
# def setup_function():
#     print('前置条件')
# # 后置条件
# def teardown_function():
#     print('后置条件')
# 定义了一个模块级别的
# def setup_module():
#     print(' setup ')
# def teardown_module():
#     print('teardown')
# def setup_method():
#     print('setup_method')
# def teardown_method():
#     print('teardown_method')
if __name__ == '__main__':
    # pytest 默认不打印信息，如果需要打印，要添加 -s命令
    # -v 用于详细显示日志信息
    # -rA用于测试结果的简单统计
    pytest.main(['-v', '-s','-rA']);