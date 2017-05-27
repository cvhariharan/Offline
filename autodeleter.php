<?php
require "database.php";
$i=0;
$result = mysqli_query($link, "SELECT ip FROM users WHERE 1");
while($row = mysqli_fetch_array($result))
{
    if(!in_array($row[0],$ip_list))
      $ip_list[$i] = $row[0];
    $status = GetServerStatus("http://$row[0]",8000);
    if($status == 'OFFLINE')
        $sql = mysqli_query($link,"DELETE * FROM files WHERE ip = \"$row[0]\"");
}

function GetServerStatus($site, $port)
{
$status = array("OFFLINE", "ONLINE");
$fp = @fsockopen($site, $port, $errno, $errstr, 2);
if (!$fp)
{
    return $status[0];
} else
  {
     return $status[1];
  }
}

?>
