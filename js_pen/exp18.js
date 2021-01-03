<script> 
	xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if(this.readyState == 4 && this.status ==200){
			document.getElementById('result').innerHTML = this.responseXML.getElementById('address').innerHTML;
		}
	};
	xhttp.open('GET','/lab/webapp/jfp/18/address',true);
	xhttp.responseType='document';
	xhttp.send();
</script>


things learned,
	we can parse xhttp request into differnt response type in this we used the responseXML to make the reponse into a htmldocument object
