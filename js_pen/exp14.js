var xhttp = XMLHttpRequest();
xhttp.onreadystatechange = function(){
	if (this.readyState == 4 && this.status == 200){
		document.getElementById('result').innerHTML = xhttp.responseText;
	}
}
xhttp.open('get','http://pentesteracademylab.appspot.com/lab/webapp/jfp/14/email?name=john',true);
xhttp.send();

things learned,

we can send date based on the information we have so far to any other server to get back and print the result in a seperate tag

