#coding=utf-8
#@time   :2021/5/6  13:12
#@Author :wangjuan
import tkinter as tk
from tkinter import *
import Base.LoginBasePage as basepage
import kuaifuwang.GetCookie as cookies
import Utlis.HttpTools as httptool
import Utlis.UrlTool as urltools
import re
import tkinter.messagebox as messbox
import Utlis.Md5Tool as MD5tools
font=("黑体",13,'bold')
class kfwModitypwd():
    def __init__(self,master):
        self.master = master;
        self.kfwModtityInterface = tk.Frame(self.master);
        self.kfwModtityInterface.pack();
        # 定义输入框账号的变量
        self.accountText = tk.StringVar();
        # 定义输入框密码的变量
        self.pwdText = tk.StringVar();
        # 定义输入框原密码的变量
        self.beforePwdText = tk.StringVar();
        # 定义输入框修改密码的变量
        self.newPwdText = tk.StringVar();
        # 标签的布局
        self.labelsetlayout();
        # 输入框的布局
        self.entrysetlayout();
        # 按钮的布局
        self.buttonsetlayout();
    # 各个标签的布局
    def labelsetlayout(self):
        # 账号标签
        AccountLabel = tk.Label(self.kfwModtityInterface, text="请输入登录账号", font=font);
        AccountLabel.grid(row=0, column=0, sticky=E, pady=20);
        # 密码标签
        pwdLabel = tk.Label(self.kfwModtityInterface, text="请输入账号密码", font=font);
        pwdLabel.grid(row=1, column=0, sticky=E);
        # 原密码标签
        beforepwdlabel = tk.Label(self.kfwModtityInterface,text = "请输入原密码",font=font)
        beforepwdlabel.grid(row=2, column=0, sticky=E,pady=20);
        # 新密码标签
        newpwdlabel = tk.Label(self.kfwModtityInterface, text="请输入新密码", font=font)
        newpwdlabel.grid(row=3, column=0, sticky=E);
    # 输入框的布局
    def entrysetlayout(self):
        # 输入账号输入框
        self.AccountEntry = tk.Entry(self.kfwModtityInterface, textvariable=self.accountText,
                                     validate="key");
        self.AccountEntry.grid(row=0, column=1, sticky=W);
        # 输入密码的输入框
        self.passwdEntry = tk.Entry(self.kfwModtityInterface, textvariable=self.pwdText,
                                    validate="key");
        self.passwdEntry.grid(row=1, column=1, sticky=W);
        # 输入原密码输入框
        self.beforepwdEntry = tk.Entry(self.kfwModtityInterface, textvariable=self.beforePwdText,
                                     validate="key");
        self.beforepwdEntry.grid(row=2, column=1, sticky=W);
        # 输入新密码的输入框
        self.newpwdEntry = tk.Entry(self.kfwModtityInterface, textvariable=self.newPwdText,
                                    validate="key");
        self.newpwdEntry.grid(row=3, column=1, sticky=W);
    # 按钮的布局
    def buttonsetlayout(self):
        # 个人信息修改密码
        moditypwdbtn = tk.Button(self.kfwModtityInterface, text="修改密码", bg="#1798FC", fg="white",
                              command=self.moditypwd);
        moditypwdbtn.grid(row=4, column=1, sticky=E, pady=30)
        # 返回密码
        backbtn = tk.Button(self.kfwModtityInterface, text="返回主界面", bg="#1798FC", fg="white",
                            command=self.back);
        backbtn.grid(row=4, column=1, sticky = W,padx = 5)
    def moditypwd(self):
        if self.accountText.get()=="":
            messbox.showerror(title="温馨提示",message="登录账号不可为空")
        elif self.pwdText.get()=="":
            messbox.showerror(title="温馨提示",message="登录密码不可为空")
        else:
            c= cookies.getkfwlogincookie(self.accountText.get(),self.pwdText.get());
            print('====ccccc==',c)
            if c ==None:
                print('账户或密码有误')
            else:
                myhead = {};
                myhead['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8";
                myhead['X-Requested-With'] = "XMLHttpRequest";
                myhead['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
                myhead['Cookie'] = c[0];
                mydata = {};
                mydata['old'] = self.beforePwdText.get();
                mydata['pwd'] = self.newPwdText.get();
                # 获取到sessionid后要 MD5加密
                mydata['token'] = MD5tools.GetMd5Str(c[1])
                res = httptool.Send_Post(url=urltools.kfwmodityuserpwd,data=mydata,header=myhead)
                print('请求的参数是',mydata)
                resstr = res.text;
                patternmsg = '\"msg\":\"(.*)\"'
                msg = re.findall(patternmsg,resstr)[0]
                # 将 unicode 转中文
                msgstr = msg.encode().decode("unicode_escape");
                patternstatus = '\"status\":\"(.*?)\"'
                statusstr = re.findall(patternstatus,res.text)[0]
                print("我要把你打印出来", msgstr,statusstr)
                if statusstr == "error":
                    messbox.showerror("温馨提示",message=msgstr)
                else:
                    messbox.showinfo(message=msgstr)
    def back(self):
        self.kfwModtityInterface.destroy();
        basepage.initfacepage(self.master)






