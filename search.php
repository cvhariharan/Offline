<form method="POST" action "">
<input type="text" name="query" placeholder="Search" required>
<input type="submit" name="submit">
</form>

<?php
require 'database.php';
$query = $_POST['query'];
$ipaddr = $_SERVER['REMOTE_ADDR'];
$sql = "SELECT * FROM files WHERE MATCH (name,location) AGAINST(\"$query\") AND ip != \"$ipaddr\" ORDER BY MATCH (name) AGAINST('$query') DESC";
$result = mysqli_query($link,$sql);
/*$row = mysqli_fetch_array($result);
print_r($row);*/
while($row = mysqli_fetch_array($result))
{
  $name = $row['name'];
  $hash = $row['hash'];
  echo "<a href=\"http://192.168.0.8/Offline/postman.php?hash=$hash\">$name</a> <br>";
}
 ?>
