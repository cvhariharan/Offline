<?php
$json_data = $_POST['list'];
str_replace("[","",$json_data);
str_replace("]","",$json_data);
str_replace("'","",$json_data);
$files = explode(",",$json_data);
echo "<pre>";
print_r($files);
echo "</pre>";
?>
