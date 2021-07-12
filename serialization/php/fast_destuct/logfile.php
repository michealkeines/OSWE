<?php

class LogFile
{
        public function __destruct()
        {
                echo "Log File destruct \n";
                file_put_contents($this->filename,$this->username, FILE_APPEND);
        }
}

?>
