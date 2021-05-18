#coding=utf-8
#@time   :2021/5/7  12:54
#@Author :wangjuan
import tkinter as tk  # 使用Tkinter前需要先导入

# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
#
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
#
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
#
# # 第4步，在图形界面上创建一个标签label用以显示并放置
# var1 = tk.StringVar()  # 创建变量，用var1用来接收鼠标点击具体选项的内容
# l = tk.Label(window, bg='green', fg='yellow', font=('Arial', 12), width=10, textvariable=var1)
# l.pack()
#
#
# # 第6步，创建一个方法用于按钮的点击事件
# def print_selection():
#     value = lb.get(lb.curselection())  # 获取当前选中的文本
#     var1.set(value)  # 为label设置值
#
#
# # 第5步，创建一个按钮并放置，点击按钮调用print_selection函数
# b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
# b1.pack()
#
# # 第7步，创建Listbox并为其添加内容
# var2 = tk.StringVar()
# var2.set((1, 2, 3, 4))  # 为变量var2设置值
# # 创建Listbox
# lb = tk.Listbox(window, listvariable=var2)  # 将var2的值赋给Listbox
# # 创建一个list并将值循环添加到Listbox控件中
# list_items = [11, 22, 33, 44]
# for item in list_items:
#     lb.insert('end', item)  # 从最后一个位置开始加入值
# lb.insert(1, 'first')  # 在第一个位置加入'first'字符
# lb.insert(2, 'second')  # 在第二个位置加入'second'字符
# lb.delete(2)  # 删除第二个位置的字符
# lb.pack()

# from tkinter import *
# root = Tk()
# theLB = Listbox(root,selectmode=MULTIPLE,height=11)#height=11设置listbox组件的高度，默认是10行。
# theLB.pack()
# for item in['公鸡','母鸡','小鸡','火鸡','战斗机',]:
#     theLB.insert(END,item)  #END表示每插入一个都是在最后一个位置
# theButton = Button(root,text='删除',\
#                    command=lambda x=theLB:x.delete(ACTIVE))
# theButton.pack()
# # 第8步，主窗口循环显示
# root.mainloop()
# import json
# import requests
# import kuaifuwang.GetCookie as mycookie
# myurl = "http://saas7.71baomu.com/Number/reset_password?module=worker&arg=p10011920_10102164"
# myheader = {}
# myheader['Content-Type'] = "application/json;charset=UTF-8"
# myheader['Cookie'] = mycookie.getkfxtcookie("zc@163.com","abcdefg1234")
# myheader['Host'] = "saas7.71baomu.com"
# myheader['Origin'] = "http://saas7.71baomu.com"
# # myheader['Referer'] = "http://saas7.71baomu.com/?token=36933B2F327FC182AE9613213AD1534D432894AC2B525C2AFD46DACD0B348850D7FF12F34DEA9D7B446BA10F016CCF9D0C7A2CBEA94B6612AF03DD313E591935&time=1621232663&sign=0ee86acd52f8b718167b7437343350bf"
# myheader['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
# mydata = {}
# mydata['account'] = "22_twm@163.com"
# mydata['id6d'] = 10209547;
# mydata['password'] = "KF123456"
# res = requests.post(url=myurl,data=json.dumps(mydata),headers=myheader)
# print(res.text)
import re
def check(str):
    my_re = re.compile(r'[A-Za-z]', re.S)
    res = re.findall(my_re, str)
    if len(res):
        print('包含英文字符')
    else:
        print('不包含英文字符')
if __name__ == '__main__':
    str = '你好123hello'
    check(str)

