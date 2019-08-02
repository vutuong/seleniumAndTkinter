from selenium import webdriver
import pandas
# import pyexcel as p
import datetime
import time
import math 
import argparse
import datetime
from tkinter import *
from functools import partial
import tkinter as tk
from tkinter import messagebox
def selenium(worker):
    your_url  = "http://yourweb/Dashboard/Dashboard/"
    PROXY = "proxy.name.vn:80" # IP:PORT or HOST:PORT
    path = r"C:/Users/TuongVX/Desktop/chromedriver" # goi path nay den noi chua file chromedriver
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--proxy-server=%s' % PROXY) # co the window khong can proxy nay, cai nay dung trong server centos.
    username = "user"
    passwword = "passwword"
    chrome = webdriver.Chrome(executable_path= path, chrome_options=chrome_options)
    chrome.get("http://yourweb.com") 
    elem = chrome.find_element_by_id('User')
    elem.send_keys(username)
    elem = chrome.find_element_by_id('Pass')
    elem.send_keys(passwword)
    chrome.find_element_by_id('btnLogIn').click()
    count = 0
    while True:
        if count >= len(worker):
            count = 0
        chrome.get("http://yourweb/Dashboard/Dashboard/")

        table = chrome.find_elements_by_css_selector("#SupportNew table tbody tr td:nth-child(3) a")
        list_link_ticket = [link.get_attribute("href") for link in table]
        if len(list_link_ticket) ==0:
            print("Hiện chưa có Ticket!")
            # sys.exit()
        for link in list_link_ticket:
            option_worker = []
            option_position = []
            chrome.get(link)
            # chrome.find_element_by_xpath('//*[@id=\"fTicketStatus\"]/option[2]').click()
            # option = chrome.find_elements_by_css_selector('#fProcessStaff > option')
            # for i in range(len(option)):
            #   option_worker.append(option[i].text)
            # print(option_worker)
            # for i in range(len(option_worker)):
            #   for j in range(len(list(worker.keys()))):
            #       if option_worker[i] == list(worker.keys())[j]:
            #           option_position.append(i+1)
            # print(option_position)
            # xpath_worker = '//*[@id=\"fProcessStaff\"]/option[' + str(option_position[count])+ ']'
            chrome.find_element_by_xpath("//select[@name=\'fProcessStaff\']/option[text()=\'" + str(list(worker.keys())[count]) + "\']").click()
            # chrome.find_element_by_xpath(xpath_worker).click()
            # chrome.find_element_by_xpath('//*[@id=\"btnCreate\"]').click() #fProcessStaff > option:nth-child(2)
        time.sleep(5)
        count = count + 1
        # chrome.find_element_by_xpath('//*[@id=\"fProcessStaff\"]/option[21]').click()
        # chrome.find_element_by_xpath('//*[@id=\"btnCreate\"]').click() #fProcessStaff > option:nth-child(2)
    chrome.close()
worker = {"Tạ Thanh Sơn":0, "Lê Văn Tuấn Anh":0, "Đỗ Văn Thuật":0} # tam thoi dung list nay de test cac nhan su dang truc 
# selenium(worker)

def action(var):
    worker = {}
    clicked_items = var.curselection()
    # print(clicked_items)
    for item in clicked_items:
        # print(var.get(item))
        worker[var.get(item)] = 0
    print(worker)
    selenium(worker)
    # return worker
    # messagebox.showinfo("data","You Selected " + x)
def GUI():
    arg = []
    worker = ['Bùi Thanh Sinh', 'Cao Thanh Lâm', 'Đỗ Như Ngọc', 'Đỗ Thị Thanh Thu', 'Đỗ Văn Thuật',\
    'Đồng Xuân Huy', 'Dương Đức Nhân ', 'Dương Thị Bích', 'Dương Thị Mỹ', 'Hoàng Đình Duy', 'Hoàng Tuấn Đạt',\
    'Huỳnh Hoàng Tiến Đạt', 'Lê Đình Tùng', 'Lê Mai Châu Giang', 'Lê Minh Cảnh', 'Lê Như Ý', 'Lê Quốc Dương',\
    'Lê Tuấn Anh', 'Lê Văn Mạnh', 'Lê Văn Tuấn Anh', 'Lê Vũ Hoàng', 'Mai Thị Minh Trang', 'Ngô Minh Hưng',\
    'Ngô Thị Khả Anh', 'Nguyễn Châu Long', 'Nguyễn Công Nguyên', 'Nguyễn Đức Việt', 'Nguyễn Duy Định', \
    'Nguyễn Gia Thuận', 'Nguyễn Hoàng Anh', 'Nguyễn Hoàng Sơn', 'Nguyễn Hoàng Trung', 'Nguyễn Hữu Hiệp', \
    'Nguyễn Minh Đức', 'Nguyễn Minh Tuấn', 'Nguyễn Ngọc Hoài Ân (MR)', 'Nguyễn Ngọc Minh Thư', 'Nguyễn Ngọc Sang', \
    'Nguyễn Thị Bảo Hà', 'Nguyễn Thị Hải Hiền', 'Nguyễn Thị Linh', 'Nguyễn Trần Thạch Tiến', 'Nguyễn Tùng Lâm', \
    'Nguyễn Văn Khang', 'Phạm Thao Thức', 'Phạm Thị Hoa', 'Phạm Văn Quyền ', 'Phan Khánh Toàn', 'Phan Văn Minh Tuấn', \
    'Tạ Thanh Sơn', 'Thái Văn Nghĩa', 'Trần Quốc Tùng', 'Trần Thị Dung', 'Trịnh Đức Cương', 'Trương Ngọc Trung', \
    'Trương Tiến Thành', 'Võ Minh Pháp', 'Vũ Minh Tuấn', 'Vũ Ngọc Hội', 'Vũ Thị Thủy', 'Vương Chí Lộc']
    arg.append(worker)
    root = Tk()
    root.geometry("300x300")
    root.title('TOOL TAKE TICKET')
    # root.state('zoomed')
    root['bg'] = '#CAFF33'
    frame = Frame(root)
    frame.pack()
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(frame, width=30, height=15, selectmode=MULTIPLE)
    for i in worker:
        listbox.insert(END, i)
    # attach listbox to scrollbar
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.pack()

    # Checkbutton.pack(side = LEFT, fill = BOTH)
    ok_button = Button(root,text="OK", command = partial(action, listbox), width=15)#.grid(column=0, row=len(worker), sticky=W)
    delete_button = Button(root,text="QUIT", command = root.destroy, width=15)#.grid(column=1, row=len(worker), sticky=W)
    ok_button.pack()
    delete_button.pack()
    root.mainloop()
GUI()


