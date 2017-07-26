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
$delete = "DELETE FROM files WHERE ip = \"$ipaddr\"";
$del_result = mysqli_query($link,$delete);
foreach ($files as $file)
{
  $file_split = explode(":",$file);
  $hash =  $file_split[1];
  $loc = $file_split[0];
  $name_ = explode("/",$file_split[0])
  $name = $name_(count($name_)-1)
  $sql = "INSERT INTO `files`(`name`, `location`, `ip`, `username`, `server_user`, `server_pass`, `port`,`hash`) VALUES (\"$name\",\"$loc\",\"$ipaddr\",\"$username\",\"$server_user\",\"$server_pass\",\"$port\",\"$hash\")";
  $result = mysqli_query($link,$sql);
}
?>
