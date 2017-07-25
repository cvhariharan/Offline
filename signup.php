<center><table><form method="POST" action="">
<tr><td><input type="text" name="username" placeholder="Username" required></td></tr>
<tr><td><input type="password" name="passw" placeholder="Password" required></td></tr>
<tr><td><input type="password" name="passwr" placeholder="Retype Password" required></td></tr>
<tr><td><input type="submit" name="submit"></td></tr>
</form></table></center>

<?php
require "database.php";
$ipaddr = $_SERVER['REMOTE_ADDR'];
$username = $_POST["username"];
$pass = $_POST["passw"];
$pass1 = $_POST["passwr"];
//$ipaddr =  getHostByName(php_uname('n'));
$password = trim(crypt(md5($pass),md5($pass)));
$password1 = trim(crypt(md5($pass1),md5($pass1)));
$check = mysqli_query($link,"SELECT * FROM users WHERE username = \"$username\"");
$rowu = mysqli_fetch_array($check);
echo $ipaddr."<br>";
if(isset($_POST['username']) && isset($_POST['passw']))
{
if(empty($rowu['username']))
{
if($password==$password1)
{
//$server_user = random_string(6);
//$server_pass = random_string(8);
$sql = "INSERT INTO users (username,passw,ip) VALUES (\"$username\",\"$password\",\"$ipaddr\")";
$result = mysqli_query($link,$sql);
if($result)
{

	echo "Successfully signed up!Now login from the client on your pc.<a href=\"clienthelp.php\">How to use the client software?</a>";
}
else
{
	echo $result."<br>";
	echo "Some error in signing up! Try again later.";
}
}
else
	echo "Passwords don't match. Try again.";
}
else
	echo "Username not available. Sign up again with another username.";
}

/*function random_string($length = 32) 
{
    return substr(str_shuffle(str_repeat($x='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', ceil($length/strlen($x)) )),1,$length);
}*/

?>
