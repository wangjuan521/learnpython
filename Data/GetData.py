#coding=utf-8
#@time   :2021/4/27  10:26
#@Author :wangjuan
import kuaifuwang.GetCookie as cookie
import Utlis.HttpTools as httptool
import Utlis.UrlTool as urltool
import json
import kuaifuwang.GetCookie as cookies
import tkinter.messagebox as messbox
# 请求账号信息的接口
def GetuserData(useremail):
    myhead = {};
    myhead['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36";
    myhead['X-Requested-With'] = "XMLHttpRequest"
    myhead['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8";
    myhead['Accept'] = "application/json, text/javascript, */*; q=0.01"
    myhead['Cookie'] = cookie.getyunweicookie();
    data = {};
    data['user_email'] = useremail;
    print("接收到的邮箱是",useremail)
    print("===打印data===",data)
    res = httptool.Send_Post(url=urltool.userinfourl,data=data,header=myhead)
    res_dic = json.loads(res.text)
    return res_dic
# 获取公司 id
def getComid(res_dic):
    companyid = res_dic['company_id']
    print(companyid)
    return companyid
# 获取 id6d
def getidid(res_dic):
    id6d = res_dic['id6d']
    print(id6d)
    return id6d
if __name__ == '__main__':
    GetuserData("1111")