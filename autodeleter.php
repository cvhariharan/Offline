<?php
require "database.php";
$i=0;
$result = mysqli_query($link, "SELECT * FROM files WHERE 1");
$ip_list = Array();
while($row = mysqli_fetch_array($result))
{
    if(!in_array($row['ip'],$ip_list))
    {
      $ip_list[$i] = $row['ip'];
      $host = $row['ip'];
      $port = $row['port'];
    $status = getStatus($host,$port);
    echo $host.$port."<br>";
    if($status != '200')
      {
        echo "Offline";
      $sql = mysqli_query($link,"DELETE * FROM files WHERE ip = \"$host\"");
    }
    else {
      echo "Online";
    }
    $i++;
  }
}

function getStatus($ip, $port)
{
	/*$socket = @fsockopen($ip, $port, $errorNo, $errorStr, 2);
	if (!$socket) return false;
	else return true;*/
  $curl = curl_init("http://$ip:$port");
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
$result = curl_exec($curl);
$info = curl_getinfo($curl);
print_r($info);
return $info['http_code'];
}

?>
