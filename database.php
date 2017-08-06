<?php
/*Testing server configurations*/
$dbhost = 'localhost';
$dbuser = 'root';
$dbpass = '';
$link = mysqli_connect($dbhost,$dbuser,$dbpass);
mysqli_select_db($link,'Offline');
?>
