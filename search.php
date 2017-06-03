<form method="POST" action "">
<input type="text" name="query" placeholder="Search" required>
<input type="submit" name="submit">
</form>

<?php
require 'database.php';
session_start();
if(isset($_SESSION['login']) && $_SESSION['login']==5)
{
$query = $_POST['query'];
$ipaddr = $_SERVER['REMOTE_ADDR'];
$sql = "SELECT * FROM files WHERE MATCH (name,location) AGAINST(\"$query\") ORDER BY MATCH (name) AGAINST('$query') DESC";
$result = mysqli_query($link,$sql);
/*$row = mysqli_fetch_array($result);
print_r($row);*/
if(!empty($row))
{
while($row = mysqli_fetch_array($result))
{
  $name = $row['name'];
  $hash = $row['hash'];
  $host = $row['username'];
  echo "From: $host <a href=\"http://192.168.0.8/Offline/postman.php?hash=$hash\">$name</a> <br>";
}
}
}
else {
  echo "<a href=\"login.php\">Login</a>";
}
 ?>
