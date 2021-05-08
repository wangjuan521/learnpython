#coding=utf-8
#@time   :2021/4/23  9:49
#@Author :wangjuan
import requests
import Utlis.UrlTool as urltool
import Utlis.HttpTools as Httptool
import time
import Utlis.Md5Tool as md5tools
import json
import tkinter.messagebox as messbox

def getCookie():
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
    time.sleep(5);
    mycookie = requests.utils.dict_from_cookiejar(res.cookies)
    # print(mycookie);
    cookies= "";
    for key,value in mycookie.items():
        print(key,value);
        cookies+=key+"="+value+";"
    print(cookies)
    return cookies

def getyunweicookie():
    myhead={};
    myhead['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36";
    myhead['X-Requested-With'] = "XMLHttpRequest"
    myhead['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8";
    myhead['Accept'] = "application/json, text/javascript, */*; q=0.01"
    mydata = {};
    mydata['username'] ="wangjuan";
    mydata['password'] = "123456";
    mydata['checked'] = "false";
    res = Httptool.Send_Post(url=urltool.yunweiloginurl,data=mydata,header=myhead)
    print(res.text,res.cookies)
    time.sleep(1)
    mycookie = requests.utils.dict_from_cookiejar(res.cookies)
    # print(mycookie);
    cookies = "";
    for key, value in mycookie.items():
        print(key, value);
        cookies += key + "=" + value + ";"
    print(cookies)
    return cookies
# 获取快服网登录的cookie
def getkfwlogincookie(account,pwd):
    myhead = {};
    myhead['Accept'] = "application/json, text/javascript, */*; q=0.01";
    myhead['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8";
    myhead['X-Requested-With'] = "XMLHttpRequest";
    myhead['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    mydata = {};
    mydata['username'] = account
    mydata['password'] = md5tools.GetMd5Str(pwd)
    mydata['mem_pwd'] = 1;
    res = Httptool.Send_Post(url=urltool.kuaifuwanglogin,data=mydata,header=myhead)
    resdic = json.loads(res.text)
    print('====打印请求的参数====',mydata)
    print(type(resdic),resdic)
    if resdic['status'] != 201:
        print(resdic['data']['msg'])
        messbox.showerror("温馨提示",message=resdic['data']['msg'])
        return None;
    else:
        # 将cookie转换成字典
        mycookie = requests.utils.dict_from_cookiejar(res.cookies)
        sessionID = mycookie['CLOUDSESSID']
        print('==我是sessionid==',sessionID);
        cookies = "";
        for key, value in mycookie.items():
            print(key, value);
            cookies += key + "=" + value + ";"
        print(cookies)
        messbox.showinfo(title="温馨提示",message="登录成功")
        return cookies,sessionID;

if __name__ == '__main__':
    test = getkfwlogincookie("exr@126.com", "abcdefg1")
    # getyunweicookie();
    # getCookie();




