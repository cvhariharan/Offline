<?php
$dbhost = 'localhost';
$dbuser = 'root';
$dbpass = 'admin';
$link = mysqli_connect($dbhost,$dbuser,$dbpass);
/*if (!$link) {
    echo "Error: Unable to connect to MySQL." . PHP_EOL;
    echo "Debugging errno: " . mysqli_connect_errno() . PHP_EOL;
    echo "Debugging error: " . mysqli_connect_error() . PHP_EOL;
    exit;
}*/
mysqli_select_db($link,'Offline');
?>
