#coding=utf-8
#@time   :2021/6/22  18:20
#@Author :wangjuan
'''
测试账户加入黑名单
'''
import pytest
import time
import Utlis.HttpTools as Httptool
import Utlis.UrlTool as urltool
import Utlis.Md5Tool as md5tools
import re
import kuaifuwang.ReadUsers as Readuser
readdata = Readuser.readuser()
@pytest.mark.parametrize('myuser',readdata)
def test_kfxtlogin(myuser):
    myhead = {}
    myhead['Connection'] = "keep-alive";
    myhead['Referer'] = "https://open.71baomu.com/";
    myhead['Method'] = "POST / HTTP/1.1";
    myhead['Accept'] = '*/*';
    myhead['Accept-Language'] = "zh-CN,zh;q=0.9";
    myhead['Origin'] = "http://open.71baomu.com";
    myhead['Content-Type'] = "application/x-www-form-urlencoded";
    myhead['Accept-Encoding'] = "gzip, deflate, br";
    myhead['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36";
    myhead['Content-Length'] = "152";
    myhead['Host'] = "open.71baomu.com";
    mytime = str(int(time.time()));
    mydata = {"xajax": "check_login", "xajaxr": mytime, "xajaxargs[]": [myuser[0], md5tools.GetMd5Str(myuser[1]), "0", "1"]}
    res = Httptool.Send_Post(url=urltool.kfxtloginurl, data=mydata, header=myhead)
    print(res.text)
    pattern = "\'(.*?)\',"
    statuscode = re.findall(pattern, res.text)[0]
    print('状态码', statuscode)
    assert statuscode == '201'
if __name__ == '__main__':
    pytest.main(['-v','-s'])
