function helper(){
	alert(document.cookie);
}
document.innerHTML = "wht";
document.getElementsByTagName('form')[0].setAttribute('onsubmit','return helper()');
