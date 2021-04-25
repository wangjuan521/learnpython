#coding=utf-8
#@time   :2021/4/23  9:49
#@Author :wangjuan
import requests
import Utlis.UrlTool as urltool
import Utlis.HttpTools as Httptool

def getCookie():
    # url = "http://www.71baomu.com/Cloud_Manage/?controller=index&action=login";
    myhead = {};
    myhead['Host '] = "www.71baomu.com";
    myhead['Accept'] = "application/json, text/javascript, */*; q=0.01";
    myhead['X-Requested-With'] = "XMLHttpRequest";
    myhead['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 ";
    myhead['Content-Type'] ="application/x-www-form-urlencoded";
    myhead['Connection'] ="keep-alive";
    data = {};
    data['info[login_name]'] = "admin";
    data['info[login_pwd]'] = "abcdefg1";
    # res = requests.post(url=loginurl,data=data,headers=myhead)
    res= Httptool.Send_Post(url=urltool.loginurl,data=data,header=myhead)
    # print('====返回原始响应体===',res.raw)
    # print('====返回请求响应体===', res.content)
    # print('=====返回响应header===',res.headers)
    # print('====返回json===',res.json())
    # print(res.cookies)
    mycookie = requests.utils.dict_from_cookiejar(res.cookies)
    # print(mycookie);
    cookies= "";
    for key,value in mycookie.items():
        print(key,value);
        cookies+=key+"="+value+";"
    print(cookies)
    return cookies
if __name__ == '__main__':
    getCookie();
