<?php

include('logfile.php');

class ReadFile
{
	public function __toString()
	{
		return file_get_contents($this->filename);
	}
}

class User
{
	public $username = "test";
	public $isAdmin;

	public function PrintData()
	{
		if ($this->isAdmin)
		{
			echo $this->username. " is an admin\n";
		}
		else
		{
			echo $this->username. " is not an admin\n";
		}
	}
}

$obj = unserialize($_POST['data']);
$obj->PrintData();
?>
