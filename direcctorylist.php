<?php
require "database.php";
$json_data = $_POST['list'];
$username = $_POST['username'];
$ipaddr = $_POST['ipaddr'];
$location = $_POST['location'];
$json_data = str_replace(array('\'','[',']'), '', $json_data);
$files = explode(",",$json_data);
echo "<pre>";
print_r($files);
echo "</pre>";
foreach ($files as $file)
{
  $sql = "INSERT INTO files (name,location,ip,username) VALUES (\"$file\",\"$location\",\"$ipaddr\",\"$username\")";
  $result = mysqli_query($link,$sql);
}
?>
