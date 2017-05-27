<?php
require "database.php";
$name = $_POST['name'];
$sql = "SELECT ip FROM users WHERE username = \"$name\"";
$result = mysqli_query($link,$sql);
$row = mysqli_fetch_array($result);
echo $row['ip'];
?>
