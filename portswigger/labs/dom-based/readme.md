DOM-based vulnerabilities:

	DOM - Document Object Model
		is a web brower's hierarchical representation of the elements on the page.		
	
it arises when a websire contains js that takes an attacker-controllable value, known as a source, and passes it into a dangerous function, known as a sink.

sources can be from: 
	Reflected data
	Stored data
	Web Messages

DOM based reflected and stored xss are coverd in xss labs

Web Messages:

If a page handles incoming web messages in an unsafe way, for example, by not verifiying the origin of incoming messages correctly in the event listener, properties and that are called by the event listener can potentially become the sinks.

```//js
<script>
window.addEventListener('message', function(e){
    eval(e.data);
    });
</script>

This is vulnerable because an attacker could inject a JavaScript payload by constructing the following iframe:

<iframe src="//vulnerable-website" onload="this.contentWindow.postMessage('alert(1)','*')">
```
As the event listener does not verify the origin of the message and the postMessage() methods specifies the targetorigin as * the event listener accepts the payload and passes it to a sink, which in this is eval() function.

it requires a iframe to pass the message to the sink, unlike the query taken from url or anyother parameters

Sometimes the verification step can flawed which can be bypassed

using indexOf(), startsWith(), endsWith() functions to check the origin, is bad practice and can be bypassed

```//js
<iframe src="https://ac5d1f6a1f0d75458098a1a4003f00d7.web-security-academy.net/" onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:alert(document.cookie)\"}","*")'>```


DOM clobbering

	when you have a html injection but xss is not possible, you can overwrite global variable, which is then used by the application in unsafe way

	The term clobbering comes the fact that you are "clobbering" comes from the fact that you are "clobering" a global variable or property of an object and overwirting it with a DOM node or HTML collection instead

	Eg: 

		window.defaultAvatar is used in dengerous manner
	let defaultAvatar = window.defaultAvatar || {avatar: '/resources/images/avatarDefault.svg'}
	this if we add a a tage with class="defaultAvatar", the next time it will take our value as the src

<form onclick=alert(1)><input id=attributes>Click me 

this will clober the attributes object, thus allowing any attributes in form 

You can check that the attributes property of a DOM node is actually a instance of namednodemap. this ensures that the property is a attributes property and not a clobbered HTML elment


Other important functions to look out for, if user controlled values are passed to it without sanitization

Javascript injection

eval()
Function() constructor
setTimeout()
setInterval()
setImmediate()
execCommand()
execScript()
msSetImmediate()
range.createContextualFragment()
crypto.generateCRMFRequest()

Domain manipulation

document.domain()

Web message

postMessage()

Ajax request header mainpulation

XMLHttpRequest.setRequestHeader()
XMLHttpRequest.open()
XMLHttpRequest.send()
jQuery.globalEval()
$.globalEval()

DOM-based local file path mainpulation

FileReader.readAsArrayBuffer()
FileReader.readAsBinaryString()
FileReader.readAsDataURL()
FileReader.readAsText()
FileReader.readAsFile()
FileReader.root.getFile()
FileReader.root.getFile()

Client-side SQL injection

executeSql()

DOM-based HTML5 storage (if the attacker controlled item is stored temp and then if it retired this might lead to a vulnerabilitiy)

sessionStorage.setItem()
localStorage.setItem()

XPath injection

document.evaluate()
someDOMElement.evaluate() 

Json injection

JSON.parse()
jQuery.parseJSON()
$.parseJSON()

DOM-data manipulation

scriptElement.src
scriptElement.text
scriptElement.textContent
scriptElement.innerText
someDOMElement.setAttribute()
someDOMElement.search
someDOMElement.text
someDOMElement.textContent
someDOMElement.innerText
someDOMElement.outerText
someDOMElement.value
someDOMElement.name
someDOMElement.target
someDOMElement.method
someDOMElement.type
someDOMElement.backgroundImage
someDOMElement.cssText
someDOMElement.codebase
document.title
document.implementation.createHTMLDocument()
history.pushState()
history.replaceState() 

DOS 

requestFileSystem()
RegExp()







