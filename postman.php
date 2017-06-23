<?php
require "database.php";
session_start();
if(isset($_SESSION['login']) && $_SESSION['login']==5)
{
$hash = $_GET['hash'];
echo $hash;
$hash = str_replace("\r\n","",$hash);
$sql = "SELECT * FROM files WHERE hash LIKE  \"$hash%\""; //Changed the operator to LIKE as the hash format is not know.
$client = $_SESSION['username'];
$result = mysqli_query($link,$sql);
$row = mysqli_fetch_array($result);
$name = $row['name'];
$server = $row['ip'];
$port = $row['port'];
$user = $row['server_user'];
$pass = $row['server_pass'];
$location = $row['location'];
$servername = $row['username'];
/*while($row = mysqli_fetch_array($result))
{
  $servername = $servername." ".$row['username'];
}*/
header("Content-type: text/plain");
header("Content-Disposition: attachment; filename=$name.hv");
$content = "Name:$name\r\nLocation:$location\r\nServer:$server\r\nPort:$port\r\nUsername:$user\r\nPassword:$pass\r\nHash:$hash\r\nServername:$servername\r\n";
$iv = "1234567812345678";
$password = random_string();
$encrypted = openssl_encrypt($content,'AES-256-CBC',$password);
$encrypted = substr_replace($encrypted,$password,23,0);
echo ($encrypted);
}
else
{
echo "<a href=\"login.php\">Login</a>";
}
function random_string($length = 32)
{
    return substr(str_shuffle(str_repeat($x='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', ceil($length/strlen($x)) )),1,$length);
}
?>
