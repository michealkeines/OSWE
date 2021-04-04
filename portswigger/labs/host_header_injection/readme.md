Host header Injection

	HTTP host header is a mandatory request header as of HTTP/1.1

	as several hosts are accesible with ip, host header lets the proxy to route the request to proper server

	Content delivery network, reverse proxies, load balancers user host header or some custom header to make this work

	Host header vulnerabilities typically arise due to the flawed assumpltion that the header is not user controllable

	if the manipulated host header is ignore that might mean that the server has a fall back host value that i being used when faced with a unknow host header

	if the host header is checked for certain valu, then check how the validation is done, there will be loopholes to bypass it, likeinjection in port number

	host:port
	
	if the host is greped for certain value, you will be able to register a arbitrary subdomain and bypass it

	poorly handled check can be bypassed using two host header

	supply absolute URL to trick the server

	GET https://evil/test HTTP/1.1
	host: good

	indented host header

	 host: value
	host: vlaue

	use custom headers to overirde host value

	X-host, X-Forwarded-Host

	custom proxy servers may consider test@private-interat/test as user@localhost
thus giving access to internal network


