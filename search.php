<html>
<head>
 <title>Offl!ne</title>
 <link href="index.css" rel="stylesheet">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<center><form method="POST" action "">
<div class="heading"><label>Offl!ne</label></div>
<input type="text" name="query" required>

</form></center>
<?php
$current_file = __FILE__;
require "analytics.php";
require 'database.php';
session_start();
if(isset($_SESSION['login']) && $_SESSION['login']==5)
{
$query = $_POST['query'];
$ipaddr = $_SERVER['REMOTE_ADDR'];
$sql = "SELECT * FROM files WHERE MATCH (name,location) AGAINST(\"$query\") ORDER BY MATCH (name) AGAINST('$query') DESC";
$result = mysqli_query($link,$sql);
while($row = mysqli_fetch_array($result))
{
  $name = $row['name'];
  $hash = $row['hash'];
  $host = $row['username'];
  echo "<div class=\"links\"><a href=\"http://192.168.0.8/Offline/postman.php?hash=$hash\">$name</a></div><br>";
}
}
else
{
  echo "<a href=\"login.php\">Login</a>";
}
?>
</body>
</html>
