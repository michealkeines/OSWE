the flaws are generally the result of failing to aniticipate unusual application states that may occur and consequently failing to handle them safely.

Excessive trust in client side validation

productId=1&redir=PRODUCT&quantity=1&price=<any price>

this is serious bad assumption

Failing to handle unconventional input

-> are there any limits that are imposed on the data
-> what happends when you reach those limits
-> is any transformation or normalization is being performed 

Eg:
	$transferAmount = $_POST['amount'];
	$currentBalance = $user->getBalance();
	
	if ($transferAmount <= $currentBalance) {
		// Complete the transfer
	} else {
		// insufficient funds
	}

here the attacker can just pass a negative value and bypass this check

if the site takes - values in quantities,

add 2 jackets --> 2 * 1000 = 2000
add -5 shirts --> 5 * 300  = -1500
add -4 socks -->  4 * 100 = -400

		total = 100

thus you can effectively get 2 jackets for 100 dollars because of negative values

productId=2&quantity=<-1 negative values>&redir=CART

if the interger value added is not properly evaluated, if we keep adding to it, it will get to negative value, thus we can update rest products to take the price to whatever we what

if the input is not properly validated, some backend might truncate after certain characters

<randomlongstring>what@admin.com.<valid id that passes the intial check>

on when its gets stored in backend rest of the chacter will get trunccated with crafted amount of random character in front

thus the email will be saved as <string>@admin.com, which then can be chained with other exploits

if the seurity measure are good at login and register and wasnt practiced in update page after user logs in, this could be a serious flaw,

user registers with proper email id
then user update his email id to subdmoin as admin and gets admin access, this is inconsistent security controls

 When probing for logic flaws, you should try removing each parameter in turn and observing what effect this has on the response. You should make sure to:

    Only remove one parameter at a time to ensure all relevant code paths are reached.
    Try deleting the name of the parameter as well as the value. The server will typically handle both cases differently.
    Follow multi-stage processes through to completion. Sometimes tampering with a parameter in one step will have an effect on another step further along in the workflow.

users won't follow the intended sequence
if a step authorized the indentiy even if the next step is still waiting, a attacker can just open and new tab and use that cookie to get access of the user

add something to your cart and make this request you will bypass the payment

GET /cart/order-confirmation?order-confirmation=true

if the attacker drops a request it defaults to admin account

You should pay particular attention to any situation where prices or other sensitive values are adjusted based on criteria determined by user actions. Try to understand what algorithms the application uses to make these adjustments and at what point these adjustments are made. This often involves manipulating the application so that it is in a state where the applied adjustments do not correspond to the original criteria intended by the developers.

the site checks if the coupon is applied based on the previously applied coupon, thus we can use two coupons alternatively to apply the same coupon


coupon reuse able flawed check lets us, add more credits

if a endpoint is encrypting user input and another endpoint decrypts user input then it can be used to create decrypt session and get structures of valid accounts

administrator:1614002661049 ---> admin with timestamp is encrypted as the keeplogged in cookies, as we can encrypt and decypt user input, we send this and get the valid decrypted token which can be used to get elevated privilages

Tx93EO5oeG9p7+T6zgfPYq2RwTkoD1DeUadN//3HAe0=









