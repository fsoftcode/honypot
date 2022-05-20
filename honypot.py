#!/usr/bin/env python3  
""" 
Copyright 2020-2021 AFacode
Auther  uri : http://afacode.com
Auther Email : fsoftcode@gmail.com
file: honeypot.py
Demo code.  No warranty of any kind.  Use at your own risk
"""
import sys
import socket 
import os
import time
import datetime
from ctypes import *
import appscript



banner = """
        \033[92m ################################################ \033[0m 
        \033[92m #              AFACODE honeypot                # \033[0m 
        \033[92m #                                              # \033[0m 
        \033[92m #      tools for detection scanning in network # \033[0m 
        \033[92m ################################################ \033[0m 
        \033[93m     usage : python3 honeypot.py  \033[0m 
        \033[94m        url auther afacode.com     \n  \033[0m 
"""
VERSION = '0.1'
welcome = b"Ubuntu 18.04.1 LTS\nserver login: \nubuntu >> "
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 


# read log file function        
def read_log(file):
    ofile = open(file,"r")
    #rfile = ofile.read()
    for i in ofile:
        print(i)
    ofile.close() 
    chose(IPAddr)  

# creat action on log file 
def log_file(add,d,port):
    file = open("LOG.txt","a")
    msg = "[ - ]  You have attack on address {} for port {} at {} \n\n ".format(add,port,d)
    file.write(msg)
    file.close()

# Start honypot detection scan
def honeypot(address,port):
    now = datetime.datetime.now()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((address,port))
    s.listen()
    print("\033[91m \033[1m [+] Start Listenng on Port {} ... \033[0m ".format(port))
    con,add = s.accept()
    con.setblocking(0)
    print('\033[33m  [!] I have One Attacking ... {}  [!] \n \033[0m'.format(add))
    os.system('afplay honypot.wav')    
    log_file(add,now,port)
    s.close()
    time.sleep(4)
    print("\033[92m \033[1m ******************************************************* \033[0m ".format(port))
    honeypot(address, port)

# choose menus function 
def chose(address,file="LOG.txt"):
    global port
    try:
        print("\033[94m << Chose on Menus  >> \n \033[0m")
        print("\033[95m [ 1 ] = honypot detection scan  \033[0m")
        print("\033[95m [ 2 ] = read log file   \033[0m")
        print("\033[95m [ 3 ] = Quit  \033[0m")
        chose = int(input(">>  "))
        if chose == 1:
            port = int(input("\033[92m  Enter port To Listen : \033[0m"))
            honeypot(address,port)
        elif chose == 2 :
            read_log(file)

        elif chose == 3:
            print("\003[92m  Good By \033[0m")
            sys.exit()
        else:
            print(" \033[91m [> Your choose out range try again !! <] \033[0m ")
    except KeyboardInterrupt:
        print("Quit !!")
        exit()        

if __name__ == '__main__': 
    os.system("clear" or "cls")
    print(banner)
    if os.geteuid() != 0:
        exit("\033[91m \033[1m  You need to have root privileges to run this script. \033[0m  \nPlease try again, this time using 'sudo'. Exiting. ")
    else:
        chose(IPAddr)
