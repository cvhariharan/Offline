<?php
require "database.php";
set_time_limit(0);
$username = $_POST["username"];
$passw = $_POST["passw"];
$result = mysqli_query($link,"SELECT * FROM users WHERE username = \"$username\"");
$row = mysqli_fetch_array($result);
if(!empty($row['username']))
{
session_start();
$_SESSION['login'] = 5;
echo "Authenticated<br>";
}
?>