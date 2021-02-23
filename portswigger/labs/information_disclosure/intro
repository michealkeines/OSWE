when a website unintentionally reveals sensitive information to its users. Depending on the context, websites may leak all kinds of information to potential attacker, including:

-> data about other users
-> sensitive commercial or business data
-> techincal details about the website and its infrastructure

techincal information can potentially be the starting for additional attack surface

eg:

	revealing the names of hidden directories or structure, directory listing
	access to source codes via backups
	verbose databse error messages
	hardcoding api keys, databases credentials on source code
	hinting existence or absence of resources, usernames via subtle difference in application behavior

how it arise?

-> failure to remove internal content from public content

-> insecure configuration of the website and related technologies

-> flawed design and behevior of the application

File for web crawlers:
	/robots.txt /sitemap.xml

Directory listings:
	Directory listings themselves are not necessarily a security vulnerability. however, if the website also fails to implement proper access control, leaking the existence and location of sensitve resources in this way clearly an issue

Developer comments:
	Although these comments are not visible on the rendered page, they can easily be accessed using burp or even your browser's built-in developer tools, occasionally, these comments contain information that is useful to an attacker. for example, they might hint at the esistence of hidden directories or provide clues about the application logic

Debugging data:
	many websites generate custom error messages and logs that contain large amounts of information about the application's behavior. while this information is useful during develpment, it is also extremely useful to an attacker.

-> values for key session varibales
-> hostnames and credentials from backend components
-> file and directory names on server 
-> keys used to encrypt data transmited via client

	Sometimes the debugging information may be stored in seperate file, if an attacker is able to access that file, it can be used as a usefull reference.

Source code disclosure via backup:
	obtaining source code access makes it much easier for an ttacker to understand the applications behavior, also text editors often generate temp files while the original file is being edited, these temp files can be accessed using (~) infront of the filename

Information disclosure due to insecure configuration:
	websites are sometimes vulnerable as a result of improper configuration, as vast varity of configuration options are not necessarily well understood by those implementing them, like enabling TRACE method might lead to information disclosure, such as the internal headers that may be appended to requests by reverse proxies

TRACE /admin ---> revealed the custom header that is used to ckeck if the request is from the internal network

TRACE /admin HTTP/1.1

X-Custom-IP-Authorization: 157.123.12.2

now the attacker can add this request to any request and get admin access

X-Custom-IP-Authorization: 127.0.0.1

Version control history:
	all websites are developed using some form of version control system, such as git etc. git stored all the information in .git folder, which is in some cases explosed thorough server, whicch can be used to retrive sensitve information to get better attack surface

git show fe5888800eb8b407bbb92c435ac1042c7b1c0861 
revealed the older peice of the file that is the admin password being updated







