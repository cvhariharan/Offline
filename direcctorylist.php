<?php
set_time_limit(0);
require "database.php";
$json_data = $_POST['list'];
$username = $_POST['username'];
$ipaddr = $_POST['ipaddr'];
$location = $_POST['location'];
$server_user = $_POST['server_user'];
$server_pass = $_POST['server_pass'];
$port = $_POST['port'];
$json_data = str_replace(array('\'','[',']'), '', $json_data);
$files = explode(",",$json_data);
echo "<pre>";
print_r($files);
echo "</pre>";
foreach ($files as $file)
{
  $file_split = explode(":",$file);
  $hash =  $file_split[1];
  $name = $file_split[0];
  $sql = "INSERT INTO `files`(`name`, `location`, `ip`, `username`, `server_user`, `server_pass`, `port`,`hash`) VALUES (\"$name\",\"$location\",\"$ipaddr\",\"$username\",\"$server_user\",\"$server_pass\",\"$port\",\"$hash\")";
  $result = mysqli_query($link,$sql);
}
?>
