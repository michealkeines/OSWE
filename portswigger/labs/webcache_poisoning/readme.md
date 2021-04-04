Webcache Poisoning

	an attacker exploits the behaviour of a webserver and cache so that a harmfull HTTP response is served to other users

	The attacker need to find a bad response in the site either a openreirect,xss and then poison the cache so that other users get the malicious request


If a server had to send a new reposnse to every single HTTP request separately, this would likey overload the server, resulting in latency issues and a poor user experience, especially during busy periods. Caching is primarly a means to reduce such issues

The cache sits between the server and the user, where it saves the responses to particular requests, usaully for a fixed amout of time. if another user then sends an equivalent request, the cache simply serves a copy of the cached response directly to the user, without any intraction from the backend, this greatly eases the load on the server by reducing the number of duplicate requests it had to handle.

cache key is made with request line and host header, other attribute falls under unkeyed

As poisoned cache is more a means of distrubution than a standalone attack

An attack can usually be scripted in such a way that it repoisons the cache indefinitly

Exploit:

	identify unkeyed inputs that are supported by the server, by adding random inputs to requests and observing it has any change

	Once you have a unkeyed input being refected in the response, you can poison that request
	
	vary header show what is header based this cache is getting hit

Cache key flaws:
	identify a suitable cache oracle, i.e find a page or endlpoint that provides feedback about the cache's behavior, this needs to be cachable and must indicate in some way whether you received a cached respone or a response directly from the server.
	a http header explicitly tells you whether you got a cache hit
	observable changes in dynamic content
	distint repsonse times

	investigate whether the cache performs any additional processing of your input when generating the cache key, like is anything being excluded from a keyed component when its added to the cache key

	get / http/1.1			http/1.1 302
	host: test.com    ---->		location: https://test.com/en

then if we send 

	get / http/1.1			http/1.1 302
	host: test.com:1337 ---> 	location: https://test.com:1337/en

then again if we make the first request we will get the cached response with port, thus the cache is take host header as a key and removing the port, thus even requests with or withour port numbers get the same cache hit

	if a unkeyed parameter is dynamically added to the page, ti can lead to cache posison, making refective xss more severe

parameter cloaking

	/?actuam=test?exculeded_param=payload

	/js/geolocate.js?callback=setCountryCookie&utm_content=te;callback=%3balert(1)%3b%2f%2f

	if the backend prases diffrently that cache server, we send fake params with diffrent delimiters, ';' in case of ruby make it take diffrent payload

	X-HTTP-Method-Override: POST

	to force the backend to use post parm while the cache server uses the valid parm

normalized cache keys

	when the delimeter for cache is not properly escaped we will be able to inser our own key inside it

Internal cache poisoning:
	different stack have internal cache which are tailored uniquely thus they would just have a cache for certain file that is loaded in every request

	finding frament of requests getting loaded into a page is the important part of exploiting this 
