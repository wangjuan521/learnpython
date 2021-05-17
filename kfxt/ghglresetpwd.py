#coding=utf-8
#@time   :2021/5/12  14:07
#@Author :wangjuan
import tkinter as tk
from tkinter import *
import Base.LoginBasePage as basepage
from tkinter import ttk
from tkinter import messagebox as messbox
import kuaifuwang.GetCookie as cookies
import Data.GetData as getdata
import Utlis.HttpTools as httptool
import Utlis.UrlTool as urltool
import json
import re
import math
import kfxt.WorkPwdReset as workresetpwd
font=("黑体",13,'bold')
AccountList = ["请选择账号"];
class KFXTpwdReset():
    def __init__(self,master):
        self.master = master;
        self.kfxttpasreset = tk.Frame(self.master);
        self.kfxttpasreset.pack();
        # 定义输入框账号的变量
        self.accountText = tk.StringVar();
        # 定义输入框密码的变量
        self.pwdText = tk.StringVar();
        # 定义输入框重置账号的变量
        self.subAccount = tk.StringVar();
        # 标签的布局
        self.labelsetlayout();
        # 输入框的布局
        self.entrysetlayout();
        # 按钮的布局
        self.buttonsetlayout();
    # #     选择下拉框的布局
    #     self.choiceBoxLayout();
    # 各个标签的布局
    def labelsetlayout(self):
        # 账号标签
        AccountLabel = tk.Label(self.kfxttpasreset, text="请输入主账号", font=font);
        AccountLabel.grid(row=0, column=0, sticky=E, pady=50);
        # 密码标签
        pwdLabel = tk.Label(self.kfxttpasreset, text="请输入主账号密码", font=font);
        pwdLabel.grid(row=1, column=0, sticky=E);
    # 输入框的布局
    def entrysetlayout(self):
        # 输入账号输入框
        self.AccountEntry = tk.Entry(self.kfxttpasreset, textvariable=self.accountText,
                                     validate="key");
        self.AccountEntry.grid(row=0,column=1, sticky=E)
        # 输入密码的输入框
        self.passwdEntry = tk.Entry(self.kfxttpasreset, textvariable=self.pwdText,
                                    validate="key");
        self.passwdEntry.grid(row=1, column=1, sticky=W);

    # 选择下拉框的布局
    def choiceBoxLayout(self):
        self.list = ["请选择账号"];
        self.subEmailBox = ttk.Combobox(self.kfxttpasreset, textvariable=self.subAccount, width=17);
        self.subEmailBox["values"] = self.list;
        # 默认选择第一个
        self.subEmailBox.current(0);
        # 点击绑定事件
        self.subEmailBox.bind("<<ComboboxSelected>>", self.click)  # 绑定事件,(下拉列表框被选中时，绑定click()函数)
        self.subEmailBox.grid(row=2, column=1, sticky=W);
        # 邮箱格式下拉框点击事件

    def click(self, *argvs):
        print('点击下拉框', self.subAccount.get());

    # 按钮的布局
    def buttonsetlayout(self):
        # 个人信息修改密码
        moditypwdbtn = tk.Button(self.kfxttpasreset, text="登录并跳转", bg="#1798FC", fg="white",
                                 command=self.moditypwd);
        moditypwdbtn.grid(row=2, column=1, sticky=E, pady=20)
        # 返回密码
        backbtn = tk.Button(self.kfxttpasreset, text="返回主界面", bg="#1798FC", fg="white",
                            command=self.back);
        backbtn.grid(row=2, column=1, sticky=W)
    def moditypwd(self):
        print('密码重置')
        # 获取输入的账号
        Account = self.accountText.get();
        # 获取输入的密码
        pwd = self.pwdText.get();
        if Account == "":
            messbox.showerror(title="温馨提示", message="账号不可为空")
        elif pwd == "":
            messbox.showerror(title="温馨提示", message="密码不可为空")
        else:
            res = cookies.kfxtLogin(Account,pwd);
            # pattern = "bglogin((.*?),)"
            pattern = "\'(.*?)\',"
            statuscode = re.findall(pattern, res.text)[0]
            print('状态吗', statuscode, type(statuscode))
            if statuscode == '201':
                print('这里请求工号管理工号的请求')
                res = getdata.GetuserData(Account);
                comid = getdata.getComid(res)
                arg = "10" + str(comid)[2:]
                id6d = getdata.getidid(res)
                mycookie = cookies.getkfxtcookie(Account,pwd)
                self.kfxttpasreset.destroy();
                workresetpwd.Workresetpwd(self.master,mycookie,self.getWorker(Account,pwd,arg,id6d,mycookie),arg,id6d)
                # self.subEmailBox.config(values=self.getWorker(Account,pwd,arg,id6d,mycookie))
            elif statuscode == '404' or statuscode == '406':
                messbox.showerror(title="温馨提示", message="账号或密码有误")
            elif statuscode == '500' or statuscode == '502':
                messbox.showerror(title="温馨提示", message="网络繁忙，请稍后重试")
            else:
                messbox.showerror(title="温馨提示", message="登录失败")
    def back(self):
        self.kfxttpasreset.destroy();
        basepage.initfacepage(self.master)
    def getworkerpage(self,account,pwd,arg,id6d,mycookie):
        url = urltool.ghglworkurl+arg+"_"+str(id6d)
        myheader = {};
        myheader['Content-Type'] = "application/json"
        myheader['Host'] = "saas7.71baomu.com"
        myheader['Origin'] = "http://saas7.71baomu.com"
        myheader['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36";
        myheader['Cookie'] = mycookie;
        mydata = {};
        mydata['listrow'] = 50
        mydata['page'] = 1
        mydata['resign_type'] = 0
        mydata['search'] = {'group': -1, 'option': "worker_id", 'content': ""}
        mydata['timeSort'] = 0
        res = httptool.Send_Post(url=url,data=json.dumps(mydata),header=myheader)
       # 将请求数据转换成字典
        resdic = json.loads(res.text);
        worktotal = resdic['account']
        page = math.ceil(worktotal / 50);
        print(page)
        return page
    def getWorker(self,account,pwd,arg,id6d,mycookie):
        page = self.getworkerpage(account,pwd,arg,id6d,mycookie)
        url = urltool.ghglworkurl + arg + "_" + str(id6d)
        for i in range(page):
            print("进入第%d次循环"%(i+1))
            myheader = {};
            myheader['Content-Type'] = "application/json"
            myheader['Host'] = "saas7.71baomu.com"
            myheader['Origin'] = "http://saas7.71baomu.com"
            myheader['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36";
            myheader['Cookie'] = mycookie;
            mydata = {};
            mydata['listrow'] = 50
            mydata['page'] = i+1
            mydata['resign_type'] = 0
            mydata['search'] = {'group': -1, 'option': "worker_id", 'content': ""}
            mydata['timeSort'] = 0
            res = httptool.Send_Post(url=url, data=json.dumps(mydata), header=myheader)
            # 将请求数据转换成字典
            resdic = json.loads(res.text);
            numberlist = resdic['number_list'];
            for j in range(len(numberlist)):
                workaccount = numberlist[j]['account'];
                AccountList.append(workaccount)
        print("账号列表是",AccountList)
        return AccountList;







