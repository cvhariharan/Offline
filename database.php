<?php
$dbhost = 'localhost';
$dbuser = 'root';
$dbpass = '';
$link = mysqli_connect($dbhost,$dbuser,$dbpass);
mysqli_select_db($link,'offline');
?>