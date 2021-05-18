#coding=utf-8
#@time   :2021/4/29  11:19
#@Author :wangjuan
import tkinter as tk
import tkinter.messagebox as messbox
from tkinter import *
import Base.LoginBasePage as basepage
import Utlis.UrlTool as urltool
import Utlis.HttpTools as httptool
import kuaifuwang.GetCookie as coookie
import Data.GetData as userinfo
import json
import Utlis.checkexpress as expresstool
font=("黑体",13,'bold')
class resetpwd():
    def __init__(self,master):
        self.master = master;
        self.resetpwdface = tk.Frame(self.master);
        # 定义输入框输入账号的变量
        self.accounttext = tk.StringVar()
        self.resetpwdface.pack();
        self.labelsetlayout();
        self.entrysetlayout();
        self.buttonsetlayout();
    # 标签的布局
    def labelsetlayout(self):
        # 账号的标签
        AccountLabel = tk.Label(self.resetpwdface,text="请输入重置密码的邮箱账号",font=font);
        AccountLabel.grid(row=0,column=0,sticky=E,pady=100);

        tipsLabel = tk.Label(self.resetpwdface,text="（重置后的密码是abcdefg）");
        tipsLabel.grid(row=0,column=2)

    # 输入框的布局
    def entrysetlayout(self):
        # 输入账号输入框
        self.AccountEntry = tk.Entry(self.resetpwdface,textvariable = self.accounttext,
                       validate="key");
        self.AccountEntry.grid(row=0,column=1,sticky=W);
    #按钮的布局
    def buttonsetlayout(self):
        # 重置密码
        resetbtn = tk.Button(self.resetpwdface,text="重置密码",bg="#1798FC",fg="white",
                             command=self.resetpwd);
        resetbtn.grid(row=1,column=2,sticky=E)
        # 返回密码
        backbtn = tk.Button(self.resetpwdface,text="返回主界面",bg="#1798FC",fg="white",
                             command=self.back);
        backbtn.grid(row=1,column=2,sticky=W)
    # 点击重置密码按钮的事件
    def resetpwd(self):
        if self.accounttext.get() =="" or self.accounttext.get().isspace():
            messbox.showerror("温馨提示","邮箱账号不能为空")
        else:
            Account = self.accounttext.get();
            if expresstool.checkmail(Account)==False:
                messbox.showerror("温馨提示","请输入正确格式的邮箱账号")
            else:
                if len(userinfo.GetuserData(self.accounttext.get()))==0:
                    messbox.showerror("温馨提示","账号不存在，请重新输入")
                    # 清空输入框的文本
                    self.AccountEntry.delete(0,'end')
                else:
                    self.Requestresetpwd();
    # 请求重置密码的接口
    def Requestresetpwd(self):
        headers = {};
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        headers['Cookie'] = coookie.getCookie();
        headers['X-Requested-With'] = "XMLHttpRequest";
        headers['Accept'] = "application/json, text/javascript, */*; q=0.01"
        headers['Content-Type'] = "application/x-www-form-urlencoded";
        mydata = {};
        mydata['reset_pwd[company_id]'] = userinfo.getComid(userinfo.GetuserData(self.accounttext.get()));
        mydata['reset_pwd[master_account]'] = self.accounttext.get();
        res = httptool.Send_Post(url=urltool.ResetpwdUrl, data=mydata, header=headers)
        res_dic = json.loads(res.text)
        print("-----------------", type(res_dic), res_dic)
        if res_dic['status'] == "success":
            messbox.showinfo(title="温馨提示", message="密码重置成功")
        else:
            messbox.showerror(title="温馨提示", message="密码重置失败")
    def back(self):
        self.resetpwdface.destroy();
        basepage.initfacepage(self.master)