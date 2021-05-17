#coding=utf-8
#@time   :2021/4/28  15:37
#@Author :wangjuan
import tkinter as tk
import kuaifuwang.Addsub as addsubaccount
import kuaifuwang.Resetpwd as resetpwd
import kuaifuwang.Forgetpwd as forgetpwd
import kuaifuwang.ModityPwd as modity
import kuaifuwang.KfwLogin as kfwlogin
import kuaifuwang.kfwpwdreset as pwdreset
import kfxt.kfxtlogin as KFlogin
import kfxt.ghglresetpwd as KFxtresetpwd
from tkinter import *
# 创建基准界面的窗口
class basewindow():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('快服网单点登录相关功能')
        self.root.geometry("%dx%d+%d+%d" % (wwidth, wwheight, (screenw - wwidth) / 2, (screenh - wwheight) / 2));
        initfacepage(self.root)
class initfacepage():
    def __init__(self, master):
        self.master = master
        # 基准界面initface
        self.Addsubface = tk.Frame(self.master, )
        self.Addsubface.pack()
        # 添加子账号的按钮
        Addbtn = tk.Button(self.Addsubface, text='快服网添加子账号',
                command=self.add)
        Addbtn.grid(row=0,column=0,pady=20,sticky=E,padx=10);
        # 重置账号密码的按钮
        Resetpwdbtn = tk.Button(self.Addsubface, text='快服网后台重置密码',
                       command=self.resetpwd)
        Resetpwdbtn.grid(row=0,column=1,sticky = W)
        # 忘记密码的按钮
        Forgetpwdbtn = tk.Button(self.Addsubface, text='快服网后台忘记密码',
                       command=self.forgetpwd)
        Forgetpwdbtn.grid(row=1, column=0,pady=20,sticky=E,padx=10)
        #  快服网登录的按钮
        loginbtn = tk.Button(self.Addsubface, text='快服网商城登录接口',
                                 command=self.login)
        loginbtn.grid(row=1, column=1,sticky=W)
    #    快服网我的快服修改个人密码
        Moditypwdbtn = tk.Button(self.Addsubface, text='我的快服修改个人密码',
                             command=self.moditypwd)
        Moditypwdbtn.grid(row=2, column=0,pady=20,sticky=E,padx=10)
    # 快服网工号管理重置密码
        kfwpwdresetbtn = tk.Button(self.Addsubface, text='我的快服工号管理密码重置',
                             command=self.pwdreset)
        kfwpwdresetbtn.grid(row=2, column=1,sticky=W);
    # 客服系统登录接口
        kfxtloginbtn = tk.Button(self.Addsubface, text='saas客服系统登录接口',
                             command=self.kfxtlogin)
        kfxtloginbtn.grid(row=3, column=0,pady = 20,sticky=E,padx=10);
    # 客服系统工号管理密码重置
        kfxtghglbtn = tk.Button(self.Addsubface, text='客服系统工号管理密码重置',
                             command=self.kfxtghglresetpwd)
        kfxtghglbtn.grid(row=3,column=1,sticky=W);
    # 添加账号的点击事件
    def add(self):
        self.Addsubface.destroy()
        addsubaccount.addsubaccount(self.master)
    # 重置密码的点击事件
    def resetpwd(self):
        self.Addsubface.destroy();
        resetpwd.resetpwd(self.master)
    # 找回密码的点击事件
    def forgetpwd(self):
        self.Addsubface.destroy();
        forgetpwd.Forgetpwd(self.master)
    # 快服网登录点击事件
    def login(self):
        self.Addsubface.destroy();
        kfwlogin.kfwLoginPage(self.master);
#     快服网修改密码的点击事件
    def moditypwd(self):
        self.Addsubface.destroy();
        modity.kfwModitypwd(self.master);
#     快服网密码重置的点击事件
    def pwdreset(self):
        self.Addsubface.destroy();
        pwdreset.kfwpwdReset(self.master)
#     客服系统登录的点击事件
    def kfxtlogin(self):
        self.Addsubface.destroy();
        KFlogin.KFxtLogin(self.master);
        print('客服系统的登录')
    def kfxtghglresetpwd(self):
        self.Addsubface.destroy();
        KFxtresetpwd.KFXTpwdReset(self.master);
        print('客服系统工号管理密码重置')
if __name__ == '__main__':
    root = tk.Tk()
    # 窗口的宽度
    wwidth = 600;
    # 窗口的高度
    wwheight = 400;
    # 获得屏幕的高度
    screenh = root.winfo_screenheight();
    # 获得屏幕的宽度
    screenw = root.winfo_screenwidth();
    basewindow(root)
    root.mainloop()