#coding=utf-8
#@time   :2021/6/23  15:30
#@Author :wangjuan
import tkinter as tk
from tkinter import *
import kfxt.kfxtlogin as kfxt
import kfxt.kfxtweblogin as weblogin
import tkinter.messagebox as messbox
import Utlis.UrlTool as urltool
import Utlis.HttpTools as httptool
import time
import re
class ResetPassword():
    def __init__(self,master,userAccount,OldPwd,producttype,urlcode,mycookie):
        self.master = master
        self.account = userAccount;
        self.oldpwd = OldPwd;
        self.product = producttype
        self.urlcode = urlcode
        self.cookie = mycookie
        self.ResetPwdInterFace = tk.Frame(self.master)
        self.ResetPwdInterFace.pack()
        self.font = ("黑体",13,'bold')
        # 定义输入框账号的变量
        self.pwdText = tk.StringVar();
        # 定义输入框密码的变量
        self.confirmpwdText = tk.StringVar();
        # 标签的布局
        self.labelsetlayout();
        # 输入框的布局
        self.entrysetlayout();
        # 按钮的布局
        self.buttonsetlayout();
    # 各个标签的布局
    def labelsetlayout(self):
        resetpwdtitle = tk.Label(self.ResetPwdInterFace, text="重置密码登录，请尽快修改", font = ("黑体",16,'bold') );
        resetpwdtitle.grid(row=0, column=0, sticky=E, pady=20,padx =80);

        pwderrorText = tk.Label(self.ResetPwdInterFace, text="8-20位，需包含英文和数字，不能有符号和空格", font = ("宋体",10,'italic'));
        pwderrorText.grid(row=2, column=0, sticky=E, pady=20,padx =80);
        pwderrorText['fg'] = "grey"
    # 输入框的布局
    def entrysetlayout(self):
        # 输入账号输入框
        self.newpwdEntry = tk.Entry(self.ResetPwdInterFace, textvariable=self.pwdText,
                                     validate="key");
        self.newpwdEntry.grid(row=1
                              , column=0, sticky= 'ew',padx=80);
        # 输入框内插入默认文本
        self.newpwdEntry.insert(0, "新密码")
        # 设置placeholder颜色为灰色
        self.newpwdEntry['fg'] = "grey"
        # 绑定鼠标键入的事件
        self.newpwdEntry.bind("<FocusIn>", self.foc_in)
        # 绑定鼠标键出的事件
        self.newpwdEntry.bind("<FocusOut>", self.foc_out)
        # self.AccountEntry.grid_columnconfigure(1,weight=1)
        # 输入密码的输入框
        self.passwdEntry = tk.Entry(self.ResetPwdInterFace, textvariable=self.confirmpwdText,
                                    validate="key");
        self.passwdEntry.grid(row=3, column=0, sticky= 'ew',padx=80);
        # 输入框内插入默认文本
        self.passwdEntry.insert(0, "请再次确认密码")
        # 设置placeholder颜色为灰色
        self.passwdEntry['fg'] = "grey"
        # 绑定鼠标键入的事件
        self.passwdEntry.bind("<FocusIn>", self.newfoc_in)
        # 绑定鼠标键出的事件
        self.passwdEntry.bind("<FocusOut>", self.newfoc_out)
        # self.passwdEntry.grid_columnconfigure(2,weight=1)
    # 鼠标键入事件
    def newfoc_in(self, *args):
        self.passwdEntry.delete('0', 'end')
        self.passwdEntry['fg'] = 'black';

    # 鼠标键出事件
    def newfoc_out(self, *args):
        if not self.passwdEntry.get():
            # 输入框内插入默认文本
            self.passwdEntry.insert(0, "请再次确认密码")
            # 设置placeholder颜色为灰色
            self.passwdEntry['fg'] = "grey"
    # 鼠标键入事件
    def foc_in(self,*args):
        self.newpwdEntry.delete('0', 'end')
        self.newpwdEntry['fg'] = 'black';
    # 鼠标键出事件
    def foc_out(self,*args):
        if not self.newpwdEntry.get():
            # 输入框内插入默认文本
            self.newpwdEntry.insert(0, "新密码")
            # 设置placeholder颜色为灰色
            self.newpwdEntry['fg'] = "grey"
    def buttonsetlayout(self):
        # 重置密码
        kfxtrestpwd = tk.Button(self.ResetPwdInterFace, text="密码重置", bg="#1798FC", fg="white",
                                 command=self.kfxtresetpwd);
        kfxtrestpwd.grid(row=5, column=0, sticky='E', pady=30,ipadx = 5)
        # 返回密码
        backbtn = tk.Button(self.ResetPwdInterFace, text="返回上一界面", bg="#1798FC", fg="white",
                            command=self.back);
        backbtn.grid(row=5, column=0, sticky='E',padx=80)
    def kfxtresetpwd(self):
        # 新密码
        newpwd = self.pwdText.get();
        # 确认密码
        confirmpwd = self.confirmpwdText.get();
        if newpwd == "" or  newpwd.isspace() or newpwd =="新密码":
            messbox.showerror(title="温馨提示", message="新密码不可为空");
        elif confirmpwd=="" or confirmpwd.isspace() or confirmpwd=="请再次确认密码":
            messbox.showerror(title="温馨提示", message="确认密码不可为空");
        else:
            if newpwd==confirmpwd:
                if self.product == "客服系统网页":
                    self.ResetPwd(newpwd)
                elif self.product ==  "客服系统官网":
                    self.WebsistModitypwd(newpwd,self.cookie)
                else:
                    pass
            else:
                messbox.showerror(title="温馨提示", message="两次密码不一致");
    def back(self):
        if self.product == "客服系统网页":
            self.ResetPwdInterFace.destroy();
            kfxt.KFxtLogin(self.master)
        elif self.product == "客服系统官网":
            self.ResetPwdInterFace.destroy();
            weblogin.kfxtWebLogin(self.master)
    # 客服系统网页端修改密码
    def ResetPwd(self,newpwd):
        mytime = str(int(round(time.time())*1000));
        data = {"xajax":"restall_pwd","xajaxr":mytime,
                "xajaxargs[]":[self.account,newpwd,self.oldpwd]};
        res = httptool.Send_Post(url=urltool.restall_pwdurl,data=data)
        print(data)
        print(res.text)
        try:
            pattern = "\'(.*?)\'"
            statustext = re.findall(pattern, res.text)[1]
            print(statustext)
            messbox.showinfo(title="温馨提示",message=statustext)
        except Exception as e:
            print('异常信息是',e)
            messbox.showinfo(title="温馨提示", message="密码修改失败")
        else:
            pass
    # 客服系统官网修改密码
    def WebsistModitypwd(self,newpwd,mycookie):
        print('mycookie',mycookie)
        myhead = {}
        myhead['Host'] = "kf.71baomu.com"
        myhead['Connection'] = "keep-alive"
        myhead['Content-Length'] = "108"
        myhead['sec-ch-ua'] = "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"
        myhead['Accept'] = "*/*"
        myhead['X-CSRF-TOKEN'] = "wOZI2VPE6RHihOgbziaHuXZGnCmgHgPEyYT4SgwP"
        myhead['X-Requested-With'] = "XMLHttpRequest"
        myhead['sec-ch-ua-mobile'] = "?0"
        myhead['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        myhead['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
        myhead['Origin'] = "https://kf.71baomu.com"
        myhead['Sec-Fetch-Site'] = "same-origin"
        myhead['Sec-Fetch-Mode'] = "cors"
        myhead['Sec-Fetch-Dest'] = "empty"
        myhead['Referer'] = "https://kf.71baomu.com/login/guide?url=http://kf.71baomu.com"
        myhead['Accept-Encoding'] = "gzip, deflate, br"
        myhead['Accept-Language'] = "zh-CN,zh;q=0.9"
        myhead['Cookie'] = "53equipment_id=02447f3ae75331001206188f4305983e; _ga=GA1.2.1545582004.1624526999; _gid=GA1.2.2002512153.1624526999; XSRF-TOKEN=eyJpdiI6Inp3RWpJNHR1WWljczNYY3o2RzNQSEE9PSIsInZhbHVlIjoid3ExYXRtbXU1NkdkSlFJd2lTSXJNV2tSMUFKN2VSbXREV1lhc2RzRjh3RXNBR3dtQzcwdDBnU3c3YlVsbGV4YSIsIm1hYyI6ImY2MTY0Zjk3ZDlmMmYyOTgwZGExNDAyMmQwNzEyNmM5NzJhNmI0M2NkODQ5NGJmNzMxYTY1NWFlZmQxODY2ZjEifQ%3D%3D; laravel_session=eyJpdiI6IlFlSHlVMUJnTUtBcjBEdXdcL3pyWVFBPT0iLCJ2YWx1ZSI6IlNZNW1xT0FZZjFCclRQSDkyajFhVXpnWEJuN1RtRVJ4YlNTM052dU1teElCNVwva01MbkE4OHFOYW1tVVFndWJFIiwibWFjIjoiOWMwNzhkMjhkYjVmMzg2ZmU4M2Q0MWQxNjZjYzIyNDNkM2YwNjI1MWY1OTFmNjJmMWE5MDU2ZTA1NTRhOWFkZSJ9"
        myhead['Cookie'] = mycookie;
        mydata = {}
        mydata['account'] = self.account;
        mydata['change_way'] = "expire_change"
        mydata['password'] = newpwd;
        mydata['urlcode'] = self.urlcode;
        res = httptool.Send_Post(url=urltool.kfrestall_pwd,data=mydata,header=myhead)
        print(mydata)
        resjson = res.json()
        print(resjson)
        messbox.showinfo(title="温馨提示",message=resjson['msg'])





