<?php
set_time_limit(0);
require "database.php";
session_start();
$_SESSION['login'] = 5;
$username = $_POST['username'];
$passw = $_POST['passw'];
$ipaddr = $_POST['ipaddr'];
if(isset($_POST['username']) && isset($_POST['passw']))
{
$password = trim(crypt(md5($passw),md5($passw)));
$result = mysqli_query($link,"SELECT * FROM users WHERE username = \"$username\" AND passw = \"$password\"");
$row = mysqli_fetch_array($result);
if($row['username'] == $username)
{
	$ipinsert = "UPDATE users SET ip=\"$ipaddr\" WHERE username=\"$username\" AND passw=\"$password\"";
	$result_ip = mysqli_query($link,$ipinsert);
	echo "1";
	exit;
}
}
?>
