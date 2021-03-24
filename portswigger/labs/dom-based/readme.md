DOM-based vulnerabilities:

	DOM - Document Object Model
		is a web brower's hierarchical representation of the elements on the page.		
	
it arises when a websire contains js that takes an attacker-controllable value, known as a source, and passes it into a dangerous function, known as a sink.

DOM based reflected and stored xss are coverd in xss labs

If a page handles incoming web messages in an unsafe way, for example, by not verifiying the origin of incoming messages correctly in the event listener, properties and that are called by the event listener can potentially become the sinks.

```
//js
 <script>
window.addEventListener('message', function(e){
    eval(e.data);
    });
</script>

This is vulnerable because an attacker could inject a JavaScript payload by constructing the following iframe:

<iframe src="//vulnerable-website" onload="this.contentWindow.postMessage('alert(1)','*')"> ```

