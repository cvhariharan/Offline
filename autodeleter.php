<?php
require "database.php";
$dir = getcwd();
require("$dir/Requests/library/Requests.php");
/*$i=0;
$result = mysqli_query($link, "SELECT * FROM files WHERE 1");
$ip_list = Array();
while($row = mysqli_fetch_array($result))
{
    if(!in_array($row['ip'],$ip_list))
    {
      $ip_list[$i] = $row['ip'];
      $host = $row['ip'];
      $port = $row['port'];
      $username = $row['server_user'];
      $password = $row['server_pass'];
    $status = checkOnline("http://$username:$password@$host:$port");
    echo $host.":".$port." ".$status."<br>";
    if(!$status)
      {
        echo "Offline";
      $sql = mysqli_query($link,"DELETE * FROM files WHERE ip = \"$host\"");
    }
    else {
      echo "Online";
    }http://hGkjab:7G03jkA9@192.168.0.8:6472/status.html
    $i++;
  }
}*/
$url = "http://hGkjab:7G03jkA9@192.168.0.8:6472/status.html";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
//curl_setopt($ch, CURLOPT_PROXY, $proxy); // $proxy is ip of proxy server
//curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
//curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
//curl_setopt($ch, CURLOPT_TIMEOUT, 10);
$httpCode = curl_getinfo($ch , CURLINFO_HTTP_CODE); // this results 0 every time
$response = curl_exec($ch);
if ($response === false) $response = curl_error($ch);
echo stripslashes($response);
curl_close($ch);
?>
