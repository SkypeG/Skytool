import json
import requests

iprequest = requests.get(f"http://ip-api.com/json/")
if iprequest.status_code == 200:
	ipdata = json.loads(iprequest.text)
if ipdata["status"] == "success":
    print("Query :", ipdata["query"])