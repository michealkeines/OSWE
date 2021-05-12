we need to reset the admin password

looking at the code, the reset password hash is created using

createPasswordReset(username, "webgoat") // username=admin, key=webgoat

i ran the PasswordResetLink.java class to create the hash, which was

java -classpath .:/run_dir/junit-4.12.jar:target/dependency/\* Main admin webgoat
Generation password reset link for admin
Created password reset link: a081235eff82092a319374c24aaa757

i tried this hash but this didnot work, not sure why

then i checked the actualy comparsion

link.equals(SolutionConstants.ADMIN_PASSWORD_LINK) // String ADMIN_PASSWORD_LINK = "375afe1104f4a487a73823c50a9292a2"

still not user how we are supposed to get his hash


