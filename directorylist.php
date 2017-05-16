<?php

set_time_limit(0);
$host = "127.0.0.1";
$port = 6666;
$fp = fopen("ips.txt","w");
while(1)
{
require "database.php";
$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Could not create socket\n");
$result = socket_bind($socket,$host,$port) or die("Could not bind\n");
if (!socket_set_option($socket, SOL_SOCKET, SO_REUSEADDR, 1)) {
    echo socket_strerror(socket_last_error($socket));
    exit;
}

$result = socket_listen($socket,5) or die("Could not set up socket
listenern");
$spawn = socket_accept($socket) or die("Could not accept incoming
connectionn");
$i=0;
$input = socket_read($spawn,4096);
socket_getpeername($spawn,$ip);
echo $ip;
//$input = trim($input);
socket_write($spawn,$input,strlen($input));
fwrite($fp,"$ip\n",strlen($ip));
$names = explode("\n",$input);
$sql = "";
foreach($names as $name)
$sql .= "INSERT INTO files (filename,ip) VALUES (\"$name\",\"$ip\");";
$resu = mysqli_multi_query($link,$sql);
echo "<pre>";
print_r($names);
echo "</pre>";
socket_close($spawn);
socket_close($socket);
mysqli_close($link);
}
/*$client = stream_socket_client("tcp://127.0.0.1:4666",$errno,$errmsg);
if($client === false)
{
	die("Couldn't connect! $errmsg");
}
echo stream_get_contents($client);
fclose($client);*/

?>