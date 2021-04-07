OAuth as a way of sharing access to specific data between applications. 

Client application: The website or web application that wants to access the user's data

Resource owner: The user whose data the client application wants to access

OAuth service provider: The website or application that controls the user's data and access to it. They support OAuth by providing an API for interacting with both of these grant types involve the following stages.

there are differnet flows and grant types, like authorization code, implicit etc,

Grant type are often referred to as "OAuth flows"

Process:
	The client application requests access to a subset of the user's data, specifying which grant type they want to use and what kind of access they want.

	The user is prompted to log in to the OAuthe service and explicitly give their consent for the requested access.

	The client application receives a unique access token that proves they have permission from the user to access the requested data. Exactly how this happens varies signigicantly depending on the grant type.

	The client application uses this access token to mkae API calls fetching the relevent data from the resource server.


OAuth scopes:
	The client application has to specify which data it wants to access and what kind of operations it wants to perform.
	scope paramter is used to specify this

	eg:
		scope=contacts
		scope=https://server/auth/scopes/user/contacts

	this implementation is unique to each oAuth service

Authorization grant type uses a series of browser based HTTP request that initiate the flow, 
	
	->once the user explicity accepts the access request. 
	
	->the Oauth service sends a authorization grant code to the /callback of client application

	->with the authorization code  the client application can request for access token to /token in oauth server

	-> no with access token the client application can get data from the info endpoint

only difference in implicit grant type is, the oauth server send the access token as soon as the user explicity grans permission to access the data

In Oauth authentication the client application follows the same process and get the username and a token, where that unique token is uses a that's users password

Recon:
	besides looking for the oauth service used

	try the 
	
	    /.well-known/oauth-authorization-server
	    /.well-known/openid-configuration

	in those endpoints, exposing information regarding the implementation

Two possible attack surface

	vulneabilites in the implemenation or configuration of client application

	vulenerabilities in the implemenation or configuration of oAuth service

https://acdc1f2d1fc63516809c0e0d02ee00ae.web-security-academy.net/auth?client_id=baym9u22tgksmylbqdvne&redirect_uri=https://ac2a1fcf1fca354280fa0eb501a800d7.web-security-academy.net/exploit&response_type=code&scope=openid%20profile%20email


