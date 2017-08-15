<html>
<head>
	<title>Login</title>
</head>
<body>
	<form method = "POST" action = "">
<input type="text" name="username" placeholder="Username">
<input type="password" name="passw" placeholder="Password">
<input type="submit" name="submit">
	</form>
</body>
</html>
<?php
set_time_limit(0);
$current_file = __FILE__;
require "analytics.php";
require "database.php";
session_start();
if(isset($_POST['username']) && isset($_POST['passw']))
{
$username = $_POST['username'];
$passw = $_POST['passw'];
}
//$ipaddr = $_SERVER['REMOTE_ADDR'];
if(isset($_POST['username']) && isset($_POST['passw']))
{
$password = trim(crypt(md5($passw),md5($passw)));
$result = mysqli_query($link,"SELECT * FROM users WHERE username = \"$username\" AND passw = \"$password\"");
$row = mysqli_fetch_array($result);
if($row['username'] == $username)
{
	//$ipinsert = "UPDATE users SET ip=\"$ipaddr\" WHERE username=\"$username\" AND passw=\"$password\"";
	//$result_ip = mysqli_query($link,$ipinsert);
  $_SESSION['login'] = 5;
  $_SESSION['username'] = $username;
	echo "Logged in successfully!<br><a href=\"search.php\">Search</a><br>";
	exit;
}
}
?>
