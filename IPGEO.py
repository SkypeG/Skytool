import json
import requests

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