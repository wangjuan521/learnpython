#coding=utf-8
#@time   :2021/4/23  10:37
#@Author :wangjuan
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import string
# 实例化对象，创建窗口
window = tk.Tk();
# 设置窗口的标题
window.title("添加子账号");
# 设置窗口的大小
window.geometry('400x300');
# 主账号变量，用于接收entry输入框输入的值
mainaccount = tk.StringVar();
# 接收输入框输入的子账号前缀的变量
subprefix = tk.StringVar();
# 设置选择邮箱格式的文本变量
subEmail = tk.StringVar();
# 设置添加子账号的数量变量文本
subaccountNum = tk.StringVar();
# 设置布局,包括标签，输入框，下拉框等的布局
def settingLayout():
    LabelLayout();
    EntryLayout();
    choiceBoxLayout();
    AddButton();
# 界面所有标签的布局
def LabelLayout():
    # 主账号的标签
    MainAccLabel = tk.Label(window,text="请输入主账号",font=("黑体",13))\
                   .grid(row=0,column=0,ipady=10,sticky=E);
    # 要添加的子账号的前缀的标签
    subprefixLabel = tk.Label(window,text="请输入子账号的前缀",font=("黑体",13))\
                    .grid(row=1,column=0,sticky=E);
    # 子账号邮箱的格式标签
    subEmailLabel = tk.Label(window, text="请选择子账号的邮箱格式", font=("黑体", 13)) \
        .grid(row=2, column=0,sticky =E,ipady=10);
    # 显示子账号数量的标签
    subNumsLabel = tk.Label(window, text="要添加子账号的数量", font=("黑体", 13)) \
        .grid(row=3, column=0,sticky=E);

# 设置输入框的布局
def EntryLayout():
    # 主账号输入框，show=none显示成明文
    MainAccEntry = tk.Entry(window,show = None,textvariable = mainaccount,validate="key")\
                   .grid(row=0,column=1,sticky=W);
    # 子账号前缀输入框
    subprefixEntry = tk.Entry(window,textvariable = subprefix,validate="key")\
                   .grid(row=1,column=1,sticky=W);
# 邮箱格式下拉框点击事件
def click(*argvs):
    print('点击下拉框',subEmail.get());
# 选择下拉框布局
def choiceBoxLayout():
    subEmailBox = ttk.Combobox(window,textvariable = subEmail,width = 17);
    subEmailBox["values"] = ("@163.com","@126.com","@qq.com","@gmail.com",
                            "@sina.com","@linshiyouxiang.net");
    # 默认选择第一个
    subEmailBox.current(0);
    # 点击绑定事件
    subEmailBox.bind("<<ComboboxSelected>>",click)  # 绑定事件,(下拉列表框被选中时，绑定click()函数)
    subEmailBox.grid(row=2,column=1,sticky = W);
    # 添加子账号数量的下拉框
    subaccNumBox = Spinbox(window, from_=1, to=200, textvariable = subaccountNum,
                           validate="key",width =18)\
                   .grid(row=3,column=1,sticky = W)
# 按钮的布局
def AddButton():
    addbtn = tk.Button(window,text="添加",bg = "#1798FC",fg="white",width =6,
            command = addaccount)\
             .grid(row=4,column = 1,sticky = E,pady=10);
# 添加子账号的事件
def addaccount():
#   获取主账号
    if mainaccount.get()=="":
        messagebox.showwarning("温馨提示","主账号不可为空")
    elif subprefix.get()=="":
        messagebox.showwarning("温馨提示", "子账号前缀不可为空")
    else:
        print("添加子账号")


if __name__ == '__main__':
    settingLayout();
    # 主窗口循环显示
    window.mainloop()
