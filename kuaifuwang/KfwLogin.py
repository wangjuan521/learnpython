#coding=utf-8
#@time   :2021/5/8  15:35
#@Author :wangjuan
import tkinter as tk
from tkinter import *
import Base.LoginBasePage as basepage
import kuaifuwang.GetCookie as cookies
import Utlis.HttpTools as httptool
import Utlis.UrlTool as urltools
import re
import tkinter.messagebox as messbox
import json
import Utlis.Md5Tool as MD5tools
font=("黑体",13,'bold')
class kfwLoginPage():
    def __init__(self,master):
        self.master = master;
        self.kfwloginpageinterface = tk.Frame(self.master);
        self.kfwloginpageinterface.pack();
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
    # 各个标签的布局
    def labelsetlayout(self):
        # 账号标签
        AccountLabel = tk.Label(self.kfwloginpageinterface, text="请输入登录账号", font=font);
        AccountLabel.grid(row=0, column=0, sticky=E, pady=50);
        # 密码标签
        pwdLabel = tk.Label(self.kfwloginpageinterface, text="请输入账号密码", font=font);
        pwdLabel.grid(row=1, column=0, sticky=E);
    # 输入框的布局
    def entrysetlayout(self):
        # 输入账号输入框
        self.AccountEntry = tk.Entry(self.kfwloginpageinterface, textvariable=self.accountText,
                                     validate="key");
        self.AccountEntry.grid(row=0, column=1, sticky=W);
        # 输入密码的输入框
        self.passwdEntry = tk.Entry(self.kfwloginpageinterface, textvariable=self.pwdText,
                                    validate="key");
        self.passwdEntry.grid(row=1, column=1, sticky=W);

    # 按钮的布局
    def buttonsetlayout(self):
        # 个人信息修改密码
        moditypwdbtn = tk.Button(self.kfwloginpageinterface, text="登录", bg="#1798FC", fg="white",
                                 command=self.moditypwd);
        moditypwdbtn.grid(row=4, column=1, sticky=E, pady=30)
        # 返回密码
        backbtn = tk.Button(self.kfwloginpageinterface, text="返回主界面", bg="#1798FC", fg="white",
                            command=self.back);
        backbtn.grid(row=4, column=1, sticky=W,ipadx = 10)
    def moditypwd(self):
        c = cookies.getkfwlogincookie(self.accountText.get(), self.pwdText.get());

    def back(self):
        self.kfwloginpageinterface.destroy();
        basepage.initfacepage(self.master)