Server side request forgery allows attackers to induce the server side application to make HTTP requests to an arbitrary domain of the attacker's choosing

it often exploit trust relationships to escalate an attack from the vulnerable application and perform unauthorized actions. these trust relationships might exist in relation to the server itself or in relation to other backend systems within the same organization

stockApi=http://127.0.0.1/admin/delete?username=carlos

because its from an internal server all the access controls are bypassed

if the url is blacklisted:
    Using an alternative IP representation of 127.0.0.1, such as 2130706433, 017700000001, or 127.1.
    Registering your own domain name that resolves to 127.0.0.1. You can use spoofed.burpcollaborator.net for this purpose.
    Obfuscating blocked strings using URL encoding or case variation.
if the url is whitelisted:
 You can embed credentials in a URL before the hostname, using the @ character. For example: https://expected-host@evil-host.
You can use the # character to indicate a URL fragment. For example: https://evil-host#expected-host.
You can leverage the DNS naming hierarchy to place required input into a fully-qualified DNS name that you control. For example: https://expected-host.evil-host.
You can URL-encode characters to confuse the URL-parsing code. This is particularly useful if the code that implements the filter handles URL-encoded characters differently than the code that performs the back-end HTTP request. 

ssrf can be chained with openredirect to bypass restrictions

Blind SSRF vulnerabilities arise when an application can be induced to issue a back-end HTTP request to a supplied URL, but the response from the back-end request is not returned in the application's front-end response.

