#coding=utf-8
#@time   :2021/4/29  17:25
#@Author :wangjuan
import tkinter as tk
import tkinter.messagebox as messbox
from tkinter import *
import Base.LoginBasePage as basepage
import Utlis.UrlTool as urltool
import Utlis.HttpTools as httptool
import kuaifuwang.GetCookie as coookie
import Utlis.checkexpress as expresstool
import Data.QueryAccountDB as databse
import Data.GetData as userinfo
import json
font=("黑体",13,'bold')
class Forgetpwd():
    def __init__(self,master):
        self.master = master;
        self.forgetpwdface = tk.Frame(self.master);
        # 定义输入框输入账号的变量
        self.accounttext = tk.StringVar()
        # 定义输入框输入密码的变量
        self.passwdtext = tk.StringVar();
        self.forgetpwdface.pack();
        self.labelsetlayout();
        self.entrysetlayout();
        self.buttonsetlayout();
    # 标签的布局
    def labelsetlayout(self):
        # 账号标签
        AccountLabel = tk.Label(self.forgetpwdface,text="请输入找回密码的账号",font=font);
        AccountLabel.grid(row=0,column=0,sticky=E,pady=50);
        # 密码标签
        findpwdLabel = tk.Label(self.forgetpwdface, text="请输入要重置的密码", font=font);
        findpwdLabel.grid(row=1, column=0, sticky=E);
    # 输入框的布局
    def entrysetlayout(self):
        # 输入账号输入框
        self.AccountEntry = tk.Entry(self.forgetpwdface,textvariable = self.accounttext,
                       validate="key");
        self.AccountEntry.grid(row=0,column=1,sticky=W);
        # 输入密码的输入框
        self.passwdEntry = tk.Entry(self.forgetpwdface,textvariable = self.passwdtext,
                       validate="key");
        self.passwdEntry.grid(row=1,column=1,sticky=W);

    #按钮的布局
    def buttonsetlayout(self):
        # 忘记找回密码
        forgetbtn = tk.Button(self.forgetpwdface,text="忘记密码",bg="#1798FC",fg="white",
                             command=self.forgetpwd);
        forgetbtn.grid(row=2,column=1,sticky=E,pady = 30)
        # 返回密码
        backbtn = tk.Button(self.forgetpwdface,text="返回主界面",bg="#1798FC",fg="white",
                             command=self.back);
        backbtn.grid(row=2,column=1,sticky=W)

    def forgetpwd(self):
        if self.accounttext.get() =="":
            messbox.showerror("温馨提示","账号不能为空")
        elif self.passwdtext.get()=="":
            messbox.showerror("温馨提示","重置密码不能为空")
        else:
            if expresstool.checkmail(self.accounttext.get())==False:
                messbox.showerror("温馨提示","请输入正确的邮箱账号")
            else:
                if len(userinfo.GetuserData(self.accounttext.get()))==0:
                    messbox.showerror("温馨提示","账号不存在，请重新输入")
                    # 清空输入框的文本
                    self.AccountEntry.delete(0,'end')
                else:
                    mycookie = coookie.getCookie();
                    self.refindpasswd(mycookie);
    def back(self):
        self.forgetpwdface.destroy();
        basepage.initfacepage(self.master)
    def findpwdurl(self,mycookie):
        myhead = {}
        myhead['Accept'] = "*/*";
        myhead['Accept-Encoding'] = "zh-CN,zh;q=0.9";
        myhead['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                               "Chrome/89.0.4389.90 Safari/537.36"
        myhead['X-Requested-With'] = "XMLHttpRequest"
        myhead['Cookie'] = mycookie;
        data = {};
        data['controller'] = "fp_url";
        data['action'] = "getRegUrl"
        data['email'] = self.accounttext.get();
        res = httptool.Send_Get(url=urltool.findpwdurl,params=data,headers=myhead)
        print(res.text)
        return res.text
    def refindpasswd(self,mycookie):
        resurl = self.findpwdurl(mycookie);
        pattern = re.compile("&urlcode=(.*)&")
        # 获取code
        urlcode = pattern.findall(resurl)[0]
        # 获取修改方式
        mypattern = re.compile("&change_way=(.*)");
        changeway = mypattern.findall(resurl)[0];
        mytimepattern = re.compile("&time=(.*)&urlcode");
        # 获取timea
        mytime = mytimepattern.findall(resurl)[0];
        print(mytime)
        myhead = {};
        myhead['Accept'] = "*/*";
        myhead['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                               "Chrome/89.0.4389.90 Safari/537.36"
        myhead['X-Requested-With'] = "XMLHttpRequest"
        myhead['Cookie'] = mycookie;
        myhead['Referer'] = resurl;
        data = {};
        data['email'] = self.accounttext.get();
        data['pwd'] = self.passwdtext.get();
        data['time'] = mytime;
        data['urlcode'] = urlcode;
        data['change_way'] = changeway;
        res = httptool.Send_Post(url=urltool.refindpwdurl,data=data,header=myhead)
        print(res.text)
        if res.text =="﻿success":
            messbox._show(title="提示",message="密码找回成功")
        else:
            messbox.showerror(title="提示",message="密码找回失败")

