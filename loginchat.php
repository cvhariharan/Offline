<center><table><form method="POST" action="">
<tr><td><input type="text" name="username" placeholder="Username" required></td></tr>
<tr><td><input type="password" name="passw" placeholder="Password" required></td></tr>
<tr><td><input type="submit" name="submit"></td></tr>
</form></table></center>
<?php
require "database.php";
$username = $_POST["username"];
$password = $_POST["passw"];
$passw = crypt(md5($password),md5($password));
$sql = "SELECT * FROM users WHERE username=\"$username\" AND passw=\"$passw\"";
$result = mysqli_query($link,$sql);
$row = mysqli_fetch_array($result);
print_r($row);
if(!empty($row))
{
	session_start();
	$_SESSION['username'] = $username;
	$_SESSION['id'] = $row['id'];
	$_SESSION['login'] = 5;
	echo "Logged in!";
}
else
	echo "Not such account exists.<br><a href=\"chatindex.php\">Login</a>";
?>