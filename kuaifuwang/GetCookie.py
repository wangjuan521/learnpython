#coding=utf-8
#@time   :2021/4/23  9:49
#@Author :wangjuan
import requests
import Utlis.UrlTool as urltool
import Utlis.HttpTools as Httptool
import time
import Utlis.Md5Tool as md5tools
import json
import re
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
        return cookies,sessionID,res;
# 客服系统登录
def kfxtLogin(account,pwd):
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
    mydata = {"xajax":"check_login","xajaxr":mytime,"xajaxargs[]":[account,md5tools.GetMd5Str(pwd),"0","1"]}
    res = Httptool.Send_Post(url=urltool.kfxtloginurl,data=mydata,header=myhead)
    return res;
def getkfxtcookie(account,pwd):
    url = "http://saas7.71baomu.com/?"
    # url = "http://fsaas.71baomu.com/?token="+getToken(kfxtLogin(account,pwd))
    print(url)
    data = {};
    data['token'] = getToken(kfxtLogin(account,pwd));
    res = requests.get(url=url, params=data);
    print(res.cookies)
    cookies = "";
    for key, value in res.cookies.items():
        print(key, value);
        cookies += key + "=" + value + ";"
    print(cookies)
    return cookies;

def getToken(res):
    # 编写符合格式的正则表达式
    tokenpattern = re.compile(r"'201', '', '(.*)' ,");
    # 获取 token
    mytoken = tokenpattern.findall(res.text)[0];
    print(mytoken);
    return mytoken;

if __name__ == '__main__':
    getkfxtcookie("zc@163.com","abcdefg1234")
    # test = getkfwlogincookie("exr@126.com", "abcdefg1")
    # getyunweicookie();
    # getCookie();




