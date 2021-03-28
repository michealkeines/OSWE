Serialization:
	process of converting complex data structures such as objects and their fields into a flatter format that can be sent and received as a sequential stream of bytes 

Desrialization:
	process of restoring this byte stream to a fully functional replica of the original object, in the exact state as when it was serialized.

common terms, marshalling in ruby, pickling in python

It is even possible to replace the seialized object with an object of entirely different class. objects of any class that is available to the website will be deserialized and instantiated, regardless of which class was expected for this reason insecure deserailization is sometimes known as an "object injection"

PHP format:

$user->name = "carlos";
$user->admin = true;

O:4:"user":2:{s:4:"name":s:6:"carlos";s:5:"admin":b:1;}

O:4:"user" -> name of class 4 chars "user"
2 -> object has two attributes
s:4:"name" -> string 4 chars "name"

serialize() and unserialize() are the functions used

java format:

it uses binary data, but mostly its starts with aced or rO0 in base64

any class that implements the interface java.io.serializable can be seriablized, its uses readObject() methods

tampering objects to elevate privilege

lose comparisions arise logic flaws

5 == "5" php converst the string to int if the first char is number

0 == "any string here" but it should not start with a number thus the integer coneversionn makes that string into 0

thus if the password doesnt have a number in the intial character, if we pass 0 that check will pass
if("password" == 0)
its true

Magic methods are like automatic methods that are called when a event occurs

like whe object of a class is getting instantiated, it called the respective
constructor methods to initialize stuff

php its __construct();
python its __init__();

__destuct function unlinks the file so
we create a object of the class

O:14:"CustomTemplate":2:{s:18:"template_file_path";s:23:"/home/carlos/morale.txt";s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";} 

 had two private variable so we create object of CustomeTemplate with two attributes

Gadget Chains:

	A Gadget is a snippet of code that exsist in the application that can help an attacker to achieve a particular goal. An individual gadget may not directly do anything harmfull with user input, however, the attaker's goal might simply be to invoke method that will pass their input into another gadget. By channing muliple gadgets together in this way, an attaker can potentially pas  their input into a dangerous sink

Custom Chains:
	find a class with magic funtion and see what it does with the input, keep goidn down the call till it reaches a good sink or a dead end

__sleep() is called when you serialize() an object and __wakeup() after you unserialize() it.

__get($variablethatisundefined) is called when the member of object is not defined, thus when 
$desc = $desc->$default_desc is called from the default_map object, the get is called and it take the default_desc_html = "<our playload>"

PHAR deserialization:
	PHP provides several url-style wrappers that you can use for handling, different protocols, when accessing file paths, one of these is the phar:// wrapper, which provides a stream interface for accessing php archive files(.phar)

PHar manifest files contain serialized metadata, if you perform any filesystem operations on a phar:// stream, this metadata is implicitly deserialized.

any fucntions like, include(), fopen(), file_exists() is enough to read the phar stream, thus invoking the deserialization

step:
	upload a file with phar code in it, 
	open the file in any endpoint that uses these funtions with phar://, thus invoking the serialze function to read the manifest of the file, which is the where we injected our exploit object.


also, if nothing works try memory corruption, as seiralize is not developed to take huge input, just smash its stack
