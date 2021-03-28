<?php

require_once('vendor/autoload.php');

class Blog {
    public $user;
    public $desc;
    public $twig;

    public function __construct($user, $desc) {
        $this->user = $user;
        $this->desc = $desc;
    }

    public function __toString() {
        return $this->twig->render('index', ['user' => $this->user]);
    }

    public function __wakeup() {
	    echo "wakes up"."\n";
        $loader = new Twig_Loader_Array([
            'index' => $this->desc,
	]);
	print_r($loader);
	$this->twig = new Twig_Environment($loader);
	#echo serialize($this->twig)."\n";
    }

    public function __sleep() {
        return ["user", "desc"];
    }
}

$first = new Blog("test","{{ user }}");
$test = serialize($first);
unserialize($test);
echo $test."\n";
?>
