#coding=utf-8
#@time   :2021/5/13  15:42
#@Author :wangjuan
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Base.LoginBasePage as basepage
from tkinter import messagebox as messbox
import Data.GetData as userData
import requests
import json
import re
font=("黑体",13,'bold')
class Workresetpwd():
    def __init__(self,master,cookie,worklist,Arg,id6d):
        self.master = master;
        self.workresetpwdinterface = tk.Frame(self.master)
        self.workresetpwdinterface.pack();
        self.cookies = cookie;
        self.worklist = worklist;
        self.arg = Arg;
        self.id6d = id6d;
        # 定义输入框重置账号的变量
        self.subAccount = tk.StringVar();
        print('打印传过来的东西',self.cookies,self.worklist)
        # 定义输入框要重置的密码
        self.resetpwdText = tk.StringVar();
        # 标签的布局
        self.labelsetlayout();
        # 输入框的布局
        self.entrysetlayout();
        # 按钮的布局
        self.buttonsetlayout();
        # 选择下拉框的布局
        self.choiceBoxLayout();
  # 各个标签的布局
    def labelsetlayout(self):
        subaccountlabel = tk.Label(self.workresetpwdinterface, text="请选择重置密码的子账号", font=font);
        subaccountlabel.grid(row=0, column=0, sticky=E,pady=50);
        #要重置密码的标签
        resetpwdlabel = tk.Label(self.workresetpwdinterface, text="请输入要重置的密码", font=font);
        resetpwdlabel.grid(row=1, column=0, sticky=E);
    # 输入框的布局
    def entrysetlayout(self):
        self.restpwdEntry = tk.Entry(self.workresetpwdinterface, textvariable=self.resetpwdText,
                                     validate="key");
        self.restpwdEntry.grid(row=1, column=1, sticky=W);
    # 选择下拉框的布局
    def choiceBoxLayout(self):
        # self.list = ["请选择账号"];
        self.subEmailBox = ttk.Combobox(self.workresetpwdinterface, textvariable=self.subAccount, validate="key",width=17);
        self.subEmailBox["values"] = self.worklist;
        # 默认选择第一个
        self.subEmailBox.current(0);
        # 点击绑定事件
        self.subEmailBox.bind("<<ComboboxSelected>>", self.click)  # 绑定事件,(下拉列表框被选中时，绑定click()函数)
        self.subEmailBox.grid(row=0, column=1, sticky=W);
        # 邮箱格式下拉框点击事件
    def click(self, *argvs):
        print('点击下拉框', self.subAccount.get());

    # 按钮的布局
    def buttonsetlayout(self):
        # 个人信息修改密码
        moditypwdbtn = tk.Button(self.workresetpwdinterface, text="重置密码", bg="#1798FC", fg="white",
                                 command=self.moditypwd);
        moditypwdbtn.grid(row=2, column=1, sticky=E, pady=20, ipadx=5)
        # 返回密码
        backbtn = tk.Button(self.workresetpwdinterface, text="返回主界面", bg="#1798FC", fg="white",
                            command=self.back);
        backbtn.grid(row=2, column=1, sticky=W)
    def moditypwd(self):
        subEmail = self.subAccount.get();
        pwd = self.resetpwdText.get();
        print('打印下拉框内的值', subEmail)
        if subEmail == "请选择账号" or subEmail.isspace() or subEmail=="":
            messbox.showerror(title="温馨提示",message="请选择账号")
        elif pwd == "" or pwd.isspace():
            messbox.showerror(title="温馨提示",message="请输入要重置的密码")
        else:
            self.requestResetpwd(subEmail,pwd)
    def requestResetpwd(self,subEmail,pwd):
        print("重置密码的cookie",self.cookies)
        userid6d = userData.getidid(userData.GetuserData(subEmail))
        myurl = "http://saas7.71baomu.com/Number/reset_password?module=worker&arg=p"+self.arg+"_"+str(self.id6d)
        myheader = {}
        myheader['Content-Type'] = "application/json;charset=UTF-8"
        myheader['Cookie'] = self.cookies;
        myheader['Host'] = "saas7.71baomu.com"
        myheader['Origin'] = "http://saas7.71baomu.com"
        myheader['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        mydata = {}
        mydata['account'] = subEmail;
        mydata['id6d'] = userid6d;
        mydata['password'] = pwd;
        res = requests.post(url=myurl, data=json.dumps(mydata), headers=myheader)
        print(res.text)
        resstr = res.text;
        patternmsg = '\"msg\":\"(.*)\"'
        msg = re.findall(patternmsg, resstr)[0]
        # 将 unicode 转中文
        msgstr = msg.encode().decode("unicode_escape");
        patternstatus = '\"status\":\"(.*?)\"'
        statusstr = re.findall(patternstatus, res.text)[0]
        print("我要把你打印出来", msgstr, statusstr)
        if statusstr == "error":
            messbox.showerror("温馨提示", message=msgstr)
        else:
            messbox.showinfo(message=msgstr)



    def back(self):
        self.workresetpwdinterface.destroy();
        basepage.initfacepage(self.master)