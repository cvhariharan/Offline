<?php
$stop_list = array(); //List of usernames whose client software has to be stopped.
$version = "1.0.0";
$client_version = $_GET["version"];
$username = $_GET["username"];
$message = "Welcome to Offline!:start";
$stop_message = "Download the latest version.:stop";
if (!in_array($username,$stop_list))
{
	echo $message;
}
else
	echo $stop_message;
?>
