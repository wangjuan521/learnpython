#coding=utf-8
#@time   :2021/5/11  13:27
#@Author :wangjuan
import tkinter as tk
from tkinter import *
import Base.LoginBasePage as basepage
import tkinter.messagebox as messbox
import kuaifuwang.GetCookie as getcookie
import re
# 字体的属性,设置成全局变量
font=("黑体",13,'bold')
class KFxtLogin():
    def __init__(self,master):
        self.master = master;
        self.kfxtlogininterface = tk.Frame(self.master);
        self.kfxtlogininterface.pack();
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
        AccountLabel = tk.Label(self.kfxtlogininterface, text="请输入登录账号", font=font);
        AccountLabel.grid(row=0, column=0, sticky=E, pady=20);
        # 密码标签
        pwdLabel = tk.Label(self.kfxtlogininterface, text="请输入账号密码", font=font);
        pwdLabel.grid(row=1, column=0, sticky=E);
    # 输入框的布局
    def entrysetlayout(self):
        # 输入账号输入框
        self.AccountEntry = tk.Entry(self.kfxtlogininterface, textvariable=self.accountText,
                                     validate="key");
        self.AccountEntry.grid(row=0, column=1, sticky=W);
        # 输入密码的输入框
        self.passwdEntry = tk.Entry(self.kfxtlogininterface, textvariable=self.pwdText,
                                    validate="key");
        self.passwdEntry.grid(row=1, column=1, sticky=W);
    # 按钮的布局
    def buttonsetlayout(self):
        # 个人信息修改密码
        kfxtloginbtn = tk.Button(self.kfxtlogininterface, text="登录", bg="#1798FC", fg="white",
                                 command=self.kfxtlogin);
        kfxtloginbtn.grid(row=4, column=1, sticky=E, pady=20, padx=15, ipadx=5)
        # 返回密码
        backbtn = tk.Button(self.kfxtlogininterface, text="返回主界面", bg="#1798FC", fg="white",
                            command=self.back);
        backbtn.grid(row=4, column=1, sticky=E, padx=80)
    # 多行文本框控件，打印登录信息
    def textsetLayout(self):
        self.showtext = tk.Text(self.kfxtlogininterface, height=10)
        self.showtext.grid(row=3, columnspan=2, sticky=W, padx=15, pady=10);

    def kfxtlogin(self):
        # 获取输入的账号
        Account = self.accountText.get();
        # 获取输入的密码
        pwd = self.pwdText.get();
        if Account == "":
            messbox.showerror(title="温馨提示",message="账号不可为空")
        elif pwd == "":
            messbox.showerror(title="温馨提示",message="密码不可为空")
        else:
            res= getcookie.kfxtLogin(Account,pwd);
            self.showtext.insert(END,res.text+"\n")
            # pattern = "bglogin((.*?),)"
            pattern = "\'(.*?)\',"
            statuscode = re.findall(pattern,res.text)[0]
            print('状态吗',statuscode,type(statuscode))
            if statuscode=='201':
                messbox.showinfo(title="温馨提示",message="登录成功")
                self.showtext.insert(END,"状态码是"+statuscode+"登录成功"+"\n")
            elif statuscode=='404' or statuscode=='406':
                messbox.showerror(title="温馨提示", message="账号或密码有误")
                self.showtext.insert(END, "状态码是" + statuscode + "登录失败，账号或密码有误" + "\n")
            elif statuscode=='500' or statuscode=='502':
                messbox.showerror(title="温馨提示", message="网络繁忙，请稍后重试")
                self.showtext.insert(END, "状态码是" + statuscode + "登录失败，网络繁忙" + "\n")
            else:
                messbox.showerror(title="温馨提示",message="登录失败")
                self.showtext.insert(END,"状态码是"+statuscode+"登录失败"+"\n")
    # def requestlogin(self,account,pwd):
    def back(self):
        self.kfxtlogininterface.destroy();
        basepage.initfacepage(self.master)
