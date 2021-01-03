<script>
var url_string = window.location.href;
var url = new URL(url_string);
var csrf = url.searchParams.get("csrf_token");
console.log(csrf);
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function () { 
	if(this.readyState == 4 && this.status == 200){
	document.getElementById('result').innerHTML = this.responseText; 
	};
};
xhttp.open('get','/lab/webapp/jfp/16/email?name=john'+'&'+'csrf_token='+csrf);
xhttp.send();
</script>

things learned, 
we can take a parameter from the get resquest and use that dynamically for every request


