#coding=utf-8
#@time   :2021/5/10  9:58
#@Author :wangjuan
import tkinter as tk
from tkinter import *
import Base.LoginBasePage as basepage
from tkinter import messagebox as messbox
import kuaifuwang.GetCookie as cookies
import Utlis.checkexpress as checkmailtool
import Data.GetData as getdata
import Utlis.HttpTools as httptool
import Utlis.UrlTool as urltool
import Data.QueryAccountDB as querydb
import re
font=("黑体",13,'bold')
class kfwpwdReset():
    def __init__(self,master):
        self.master = master;
        self.kfwpassword = tk.Frame(self.master);
        self.kfwpassword.pack();
        # 定义输入框账号的变量
        self.accountText = tk.StringVar();
        # 定义输入框密码的变量
        self.pwdText = tk.StringVar();
        # 定义输入框重置账号的变量
        self.subAccount = tk.StringVar();
        # 定义输入框要重置的密码
        self.resetpwdText = tk.StringVar();
        # 标签的布局
        self.labelsetlayout();
        # 输入框的布局
        self.entrysetlayout();
        # 按钮的布局
        self.buttonsetlayout();
    # 各个标签的布局
    def labelsetlayout(self):
        # 账号标签
        AccountLabel = tk.Label(self.kfwpassword, text="请输入主账号邮箱", font=font);
        AccountLabel.grid(row=0, column=0, sticky=E, pady=20);
        # 密码标签
        pwdLabel = tk.Label(self.kfwpassword, text="请输入主账号密码", font=font);
        pwdLabel.grid(row=1, column=0, sticky=E);
        #重置密码子账号的标签
        subaccountlabel = tk.Label(self.kfwpassword, text="请输入重置密码的子账号", font=font);
        subaccountlabel.grid(row=2, column=0, sticky=E,pady=20);
        #要重置密码的标签
        resetpwdlabel = tk.Label(self.kfwpassword, text="请输入要重置的密码", font=font);
        resetpwdlabel.grid(row=3, column=0, sticky=E);
    # 输入框的布局
    def entrysetlayout(self):
        # 输入账号输入框
        self.AccountEntry = tk.Entry(self.kfwpassword, textvariable=self.accountText,
                                     validate="key");
        self.AccountEntry.grid(row=0, column=1, sticky=W);
        # 输入密码的输入框
        self.passwdEntry = tk.Entry(self.kfwpassword, textvariable=self.pwdText,
                                    validate="key");
        self.passwdEntry.grid(row=1, column=1, sticky=W);
       # 重置密码子账号的输入框
        self.resetsubaccountEntry = tk.Entry(self.kfwpassword, textvariable=self.subAccount,
                                    validate="key");
        self.resetsubaccountEntry.grid(row=2, column=1, sticky=W);
       # 要重置的密码
        self.restpwdEntry = tk.Entry(self.kfwpassword, textvariable=self.resetpwdText,
                                    validate="key");
        self.restpwdEntry.grid(row=3, column=1, sticky=W);


    # 按钮的布局
    def buttonsetlayout(self):
        # 个人信息修改密码
        moditypwdbtn = tk.Button(self.kfwpassword, text="登录", bg="#1798FC", fg="white",
                                 command=self.moditypwd);
        moditypwdbtn.grid(row=4, column=1, sticky=E, pady=30,ipadx=5)
        # 返回密码
        backbtn = tk.Button(self.kfwpassword, text="返回主界面", bg="#1798FC", fg="white",
                            command=self.back);
        backbtn.grid(row=4, column=1, sticky=W,ipadx = 10)

    def moditypwd(self):
        # 获取输入的用户名
        Account = self.accountText.get();
        # 获取输入的密码
        password = self.pwdText.get();
        # 获取输入的子账号
        subAccount = self.subAccount.get();
        # 获取要重置的密码
        resetpwd = self.resetpwdText.get();
        if Account == "" or Account.isspace():
            messbox.showerror(title="温馨提示",message="主账号不可为空")
        elif password == "" or password.isspace():
            messbox.showerror(title="温馨提示",message="主账号密码不可为空")
        elif subAccount == "" or subAccount.isspace():
            messbox.showerror(title="温馨提示",message="子账号不可为空")
        else:
            c = cookies.getkfwlogincookie(self.accountText.get(), self.pwdText.get());
            if c == None:
                print('===获取不到缓存')
            else:
                if checkmailtool.checkmail(subAccount)==False:
                    messbox.showerror(title="温馨提示",message="您输入的子账号邮箱格式不正确")
                else:
                    if len(getdata.GetuserData(subAccount))==0:
                        messbox.showerror(title="温馨提示",message="子账号不存在")
                    else:
                        print('=====准备开始=====')
                        self.RequestWorkPwd(c,subAccount,resetpwd);

    def back(self):
        self.kfwpassword.destroy();
        basepage.initfacepage(self.master)
    def RequestWorkPwd(self,mycookie,subaccount,password):
        id6d = getdata.getidid(getdata.GetuserData(subaccount));
        print('===id6d的类型===',type(id6d))
        myid = querydb.querytable(str(id6d))
        print("====p===",myid)
        myhead = {};
        myhead['Accept'] = "application/json, text/javascript, */*; q=0.01";
        myhead['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8";
        myhead['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        myhead['X-Requested-With'] = "XMLHttpRequest"
        myhead['Cookie'] = mycookie[0];
        data = {};
        data['sub_account'] = subaccount;
        data['id'] = myid;
        data['password'] = password;
        res = httptool.Send_Post(url=urltool.resetworkpwdurl,data=data,header=myhead)
        print(res.text)
        # 将 unicode 转中文
        patternstatus = '\"status\":\"(.*?)\"'
        statusstr = re.findall(patternstatus, res.text)[0]

        patternmsg = '\"msg\":\"(.*)\"'
        msg = re.findall(patternmsg,res.text)[0]
        # 将 unicode 转中文
        msgstr = msg.encode().decode("unicode_escape");
        if statusstr == "success":
            messbox.showinfo(title="温馨提示",message="工号密码重置成功")
        else:
            messbox.showerror(title="温馨提示",message= msgstr)
