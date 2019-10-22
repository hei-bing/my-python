#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by heibing on 2019/10/22

import os
from tkinter import *
from tkinter import messagebox

# host文件地址
HostAddress = "C:\Windows\System32\drivers\etc\hosts"


# 添加域名功能
def add_domain():
    new_domain = content.get()
    with open(HostAddress, 'a', encoding='utf-8') as fp:
        fp.write(new_domain + '\n')
    messagebox.showinfo(title="状态信息", message="添加域名" + new_domain + "成功！")


# 删除域名功能
def del_domain():
    deldomain = content.get()
    with open(HostAddress, 'r', encoding='utf-8') as fp:
        for item in fp.readlines():
            if deldomain != item.split()[1]:
                with open(HostAddress + 'tmp', 'a', encoding='utf-8') as fw:
                    fw.write(item.strip() + '\n')
    os.remove(HostAddress)
    os.rename(HostAddress + 'tmp', HostAddress)
    messagebox.showinfo(title="状态信息", message="删除域名" + deldomain + "成功！")

def OpenHost():  # 打开host文件
    os.system("notepad " + HostAddress)


# 构建UI界面
soft = Tk()
soft.title("Windows之hosts文件管理")
# 设置界面的大小和显示位置
soft.geometry("350x200+800+400")
soft.resizable(0, 0)
text1 = Label(soft, text="请输入IP和域名：", compound="center").grid(row=0, column=0, columnspan=2, padx=0, pady=0)
content = StringVar()
content.set('')
text2 = Entry(soft, textvariable=content, width=30).grid(row=1, column=0, columnspan=2, padx=5, pady=0)
button1 = Button(soft, text="添加域名解析", command=add_domain, width=20).grid(row=2, column=0, padx=5, pady=10)
button2 = Button(soft, text="删除域名解析", command=del_domain, width=20).grid(row=2, column=1, padx=5, pady=10)
button3 = Button(soft, text="查看hosts文件", command=OpenHost, compound="center", width=20).grid(row=3, column=0, padx=5, pady=10)
soft.mainloop()
