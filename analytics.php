<?php
require "database.php";
$user_agent = $_SERVER['HTTP_USER_AGENT'];
$ipaddr = $_SERVER['REMOTE_ADDR'];
echo $user_agent."<br>".$ipaddr."<br>";
$t = time();
echo $t."<br>";
$add = "INSERT INTO analytics (useragent,ip) VALUES (\"$user_agent\",\"$ipaddr\")";
$add_result = mysqli_query($link,$add);
?>
