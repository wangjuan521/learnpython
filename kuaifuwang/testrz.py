#coding=utf-8
#@time   :2021/5/19  14:40
#@Author :wangjuan
import kuaifuwang.GetCookie as cookietool
import requests
import Utlis.Md5Tool as md5tools
import pytest
import json
# 写一个简单的测试用例,以 test 开头
def test_01():
    mycookie = cookietool.getkfwlogincookie("zc@163.com","abcdefg1234")
    print("====打印一下COOkie和sessionid",mycookie[0])
    # 加密sessionid
    mysessionid = md5tools.GetMd5Str(mycookie[1])
    print("======打印一下加密后的sessionid===",mysessionid)
    url = "http://www.71baomu.com/?controller=ghpay&money=3000&com_id=107442&recharge_type=withdraw&recharge_act_id=0&attach=myrecharge|zc@163.com|107442|zc@163.com&token="+mysessionid
    myheader = {}
    myheader['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    myheader['X-Requested-With'] = "XMLHttpRequest"
    myheader['Origin'] = "http://www.71baomu.com"
    myheader['Referer'] = "http://www.71baomu.com/?controller=myrecharge"
    myheader['Cookie'] = mycookie[0];
    myheader['Proxy-Connection'] = "keep-alive"
    mydata = {};
    res = requests.post(url=url,data=None,headers=myheader)
    print(res.text)
if __name__ == '__main__':
    pytest.main();