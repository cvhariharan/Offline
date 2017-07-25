<?php
require "database.php";
$user_agent = $_SERVER['HTTP_USER_AGENT'];
$ipaddr = $_SERVER['REMOTE_ADDR'];
$t = time();
$add = "INSERT INTO analytics (useragent,ip,page) VALUES (\"$user_agent\",\"$ipaddr\",\"$current_file\")";
$add_result = mysqli_query($link,$add);
?>
