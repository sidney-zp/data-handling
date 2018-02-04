#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from config.config import *
from ftplib import FTP            #加载ftp模块

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class DownloadFile(object):
    def __init__(self,starttime):
        self.IP = FTP_IP
        self.username = USERNAME
        self.password = PASSWORD
        self.starttime = starttime

    def save_file(self):
        os.mkdir(base_dir + "/log/data/" + self.starttime)
        ftp=FTP()                         #设置变量
        #ftp.set_debuglevel(2)             #打开调试级别2，显示详细信息
        ftp.connect(self.IP,21)          #连接的ftp sever和端口
        ftp.login(self.username,self.password)      #连接的用户名，密码

        if ftp.cwd(FTP_TARGET_DIR + self.starttime + "/"):    #进入远程目录
            #print(ftp.nlst())
            #downloadlist = ftp.nlst()               
            bufsize=1024                      #设置的缓冲区大小
            
            for filename in ftp.nlst():
                if ELEMENT_1 in filename and ELEMENT_2 in filename:           #需要下载的文件

                    file_handle=open(base_dir + "/log/data/" + self.starttime + "/" + filename,"wb").write #以写模式在本地打开文件
                    #file_handle=open(filename,"wb").write
                    ftp.retrbinary("RETR "+filename,file_handle,bufsize) #接收服务器上文件并写入本地文件
        #            ftp.set_debuglevel(0)             #关闭调试模式
                    print(filename + " 已经下载完成！")

            ftp.cwd("/")
        print("您想要的文件已经全部下载完成！")
        ftp.quit()                        #退出ftp



 

    
