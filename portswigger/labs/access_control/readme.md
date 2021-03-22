Access control or Authorization 
	it is the appliction of constraints on who or what can perform attempted actions or access resources that they have requested.

Authentication: identifies the user and confirms that they are who they say they are.

Session managment: identifies which subsequent HTTP requests are being mage by that same user.

Access control: determines whether the user is allowed to carry out the action that they are attempting to perform

Access control security models:

	Programmatic access control:
		a matrix of user privileges is stored and are appllied programmatically with reference to this matrix
		eg: roles, groups, users 
	
	Discretionary access control:
		Owners of resources have the ability to assign or delegate access to users, consequently this model can become very complex to design and manage

	Mandatory access control:
		it is a centrally controlled system of access in which access to some object by a subject is constrained. unlike DAC the users or owners of resources have no capability to delegate or modify access for their resources.

	Role-based access control:
		named roles are defined to which access privileges are assigned, user can then be assigned to single or multiple roles.

from an user's perspective in web applications:
	Vertical access controls:
		diffrent types of users ahave access to different application functions, thus it can be more fine-graned to enforce business policies such duties and least privileges
	
	POST /my-account/change-email the backend also updated any parameter we pass to it, instead of just updating the email

{
"email":"test@test.conm","roleid":2
} 
	/admin panels resistricted from outside traffic can be bypassed by expicit headers repective to the rules used.

	x-forwarded-host, x-original-url 

	if a functionality is blocked based on methods, some other method can be used to get the same function working

	post was blocked in /admin-roles for all users but not get request

	GET /admin-roles?username=wiener&action=upgrade
	thus a attacker can send this request to get admin privileges


thus a attacker can esculate your privaleges to admin

	Horizontal access control:
		different users have access to a subset of resources of the same type, like paid and free users

	user --> /myaccount?name=wiener
	other --> /myaccount?name=carlos
	thus the attacker was able to read other user account details
	
		using unpredictable values to identify users might not work well, as those values could be disclosed in someother places, which then can be used to access the users information

	user --> /my-account?id=464dd36c-b7a0-4ea3-a899-e84a3f393c6a
	found the carlos id from one of his post

	thus i was able to use that get carlos account

	redirects sometimes reveal extra information in the 302 response, which might contain sentive data

IDOR leads to both horizontal and vertical privilage esculation

	Context-dependent access control:
		it prevents a user from performing actions in the wrong order, like modifiying the shoppin cart after the payment is done.

Multi-step process makes an assumptions that all checks are made in previous steps

step1--->step2--->step3--->done
yes	  yes      no

the attacker can send the request directly to step3 and elevate his/her/their privilages

some make assumptions based on the referer header, which could be manipulated by the attacker to elevate his privilages

GET /admin-roles?username=wiener&action=upgrade HTTP/1.1

Referer: https://ac091f391e7e810f808d15b1004e009c.web-security-academy.net/admin

as the reference header matches the attacker will be able to get admin rights


location based access control can be bypassed using vpns, proxies or client side manipulation



	

