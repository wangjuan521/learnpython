#coding=utf-8
#@time   :2021/6/3  13:43
#@Author :wangjuan
'''
客服系统官网登录的接口
'''
import tkinter as tk
from tkinter import *
import Base.LoginBasePage as basepage
import tkinter.messagebox as messbox
import Utlis.HttpTools as httptool
import Utlis.UrlTool as urltool
import kfxt.kfxtResetPwd as kfxtResetPwd
import time
import requests
font=("黑体",13,'bold')
class kfxtWebLogin():
    def __init__(self,master):
        self.master = master;
        self.kfxtweblogininterface = tk.Frame(self.master);
        self.kfxtweblogininterface.pack();
        # 定义输入框账号的变量
        self.accountText = tk.StringVar();
        # 定义输入框密码的变量
        self.pwdText = tk.StringVar();
        # 标签的布局
        self.labelsetlayout();
        # 输入框的布局
        self.entrysetlayout();
        # 按钮的布局
        self.buttonsetlayout();
        # 多行文本的布局
        self.textsetLayout();
    # 各个标签的布局
    def labelsetlayout(self):
        # 账号标签
        AccountLabel = tk.Label(self.kfxtweblogininterface, text="请输入登录邮箱账号", font=font);
        AccountLabel.grid(row=0, column=0, sticky=E, pady=20);
        # 密码标签
        pwdLabel = tk.Label(self.kfxtweblogininterface, text="请输入账号密码", font=font);
        pwdLabel.grid(row=1, column=0, sticky=E);
    # 输入框的布局
    def entrysetlayout(self):
        # 输入账号输入框
        self.AccountEntry = tk.Entry(self.kfxtweblogininterface, textvariable=self.accountText,
                                     validate="key");
        self.AccountEntry.grid(row=0, column=1, sticky=W);
        # 输入密码的输入框
        self.passwdEntry = tk.Entry(self.kfxtweblogininterface, textvariable=self.pwdText,
                                    validate="key");
        self.passwdEntry.grid(row=1, column=1, sticky=W);
    # 按钮的布局
    def buttonsetlayout(self):
        # 个人信息修改密码
        moditypwdbtn = tk.Button(self.kfxtweblogininterface, text="登录", bg="#1798FC", fg="white",
                                 command=self.login);
        moditypwdbtn.grid(row=4, column=1, sticky=E, pady=20,padx=15,ipadx=5)
        # 返回密码
        backbtn = tk.Button(self.kfxtweblogininterface, text="返回主界面", bg="#1798FC", fg="white",
                            command=self.back);
        backbtn.grid(row=4, column=1, sticky=E,padx=80)
    # 多行文本框控件，打印登录信息
    def textsetLayout(self):
        self.showtext = tk.Text(self.kfxtweblogininterface, height=10)
        self.showtext.grid(row=3, columnspan=2, sticky=W, padx=15, pady=10);
    def login(self):
        if not self.accountText.get() or self.accountText.get().isspace():
            messbox.showwarning(title="温馨提示",message="邮箱账号不可为空")
        elif self.pwdText.get()=="" or self.pwdText.get().isspace():
            messbox.showwarning(title="温馨提示",message="账号密码不可为空")
        else:
            res= self.requestlogin(self.accountText.get(),self.pwdText.get())
            resjson = res.json()
            statuscode = resjson['status']
            statusText = resjson['msg']
            # 获取cookie
            cookies = "";
            mycookies = requests.utils.dict_from_cookiejar(res.cookies)
            for key,value in mycookies.items():
                cookies += key + "=" + value + ";"
            print(cookies,res.cookies)
            if statuscode=="1" and statusText == "重置密码登录，请尽快修改":
                urlcode = resjson['urlcode']
                self.showtext.insert(END, resjson['msg'] + "\n")
                self.kfxtweblogininterface.destroy();
                kfxtResetPwd.ResetPassword(self.master,self.accountText.get(),self.pwdText.get(),"客服系统官网",urlcode,cookies)
            else:
                self.showtext.insert(END,resjson['msg'] + "\n")
    def back(self):
        self.kfxtweblogininterface.destroy();
        basepage.initfacepage(self.master)
    # 请求登录的接口
    def requestlogin(self,account,pwd):
        myhead = {};
        myhead['Host'] = "kf.71baomu.com"
        myhead['Origi'] = "https://kf.71baomu.com"
        myhead['Referer'] = "https://kf.71baomu.com/login/guide?url=http://kf.71baomu.com"
        myhead['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        myhead['X-Requested-With'] = "XMLHttpRequest"
        mydata = {};
        mydata['account'] = account;
        mydata['flag'] = ""
        mydata['password'] = pwd;
        mydata['relogin'] = "true"
        res = httptool.Send_Post(url=urltool.kfxtWebUrl,data=mydata,header=myhead)
        self.showtext.insert(END, str(res.json()) + "\n")
        print(res.json())
        return res
