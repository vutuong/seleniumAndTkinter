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
    
    PROXY = "proxy.fpt.vn:80" # IP:PORT or HOST:PORT
    path = r"C:/Users/TuongVX/Desktop/chromedriver" # goi path nay den noi chua file chromedriver
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--proxy-server=%s' % PROXY) # co the window khong can proxy nay, cai nay dung trong server centos.
    username = "user"
    passwword = "password"
    chrome = webdriver.Chrome(executable_path= path, chrome_options=chrome_options)
    chrome.get("http://ticket.fpt.net") 
    elem = chrome.find_element_by_id('User')
    elem.send_keys(username)
    elem = chrome.find_element_by_id('Pass')
    elem.send_keys(passwword)
    chrome.find_element_by_id('btnLogIn').click()
    count = 0
    while True:
        chrome.get("http://ticket.fpt.net/Dashboard/Dashboard/")

        table = chrome.find_elements_by_css_selector("#SupportNew table tbody tr td:nth-child(3) a")
        list_link_ticket = [link.get_attribute("href") for link in table]
        if len(list_link_ticket) ==0:
            print("Hiện chưa có Ticket!")
            # sys.exit()
        for link in list_link_ticket:
            option_worker = []
            option_position = []
            chrome.get(link)
            if count >= len(worker):
                count = 0
            chrome.find_element_by_xpath('//*[@id=\"fTicketStatus\"]/option[2]').click()
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
            count = count + 1
            # chrome.find_element_by_xpath(xpath_worker).click()
            # chrome.find_element_by_xpath('//*[@id=\"btnCreate\"]').click() #fProcessStaff > option:nth-child(2)
        time.sleep(5)
        # chrome.find_element_by_xpath('//*[@id=\"fProcessStaff\"]/option[21]').click()
        # chrome.find_element_by_xpath('//*[@id=\"btnCreate\"]').click() #fProcessStaff > option:nth-child(2)
    chrome.close()
worker = {"worker1":0, "worker2":0, "worker3":0} # tam thoi dung list nay de test cac nhan su dang truc 
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
    worker = ['worker1', 'worker2', 'worker3']
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
