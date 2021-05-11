if (!"Larry".equals(username_login)) {
            return failed(this).feedback("user.not.larry").feedbackArgs(username_login).build();

	    //Larry should be the username or it will not get to the sql statement
PreparedStatement statement = connection.prepareStatement("select password from challenge_users where userid = '" + username_login + "' and password = '" + password_login + "'");
            ResultSet resultSet = statement.executeQuery();

password=' or 1=1-- - // always return true, Thus bypassed the login

