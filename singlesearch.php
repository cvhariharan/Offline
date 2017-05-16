<?php
require "database.php";
set_time_limit(0);
$host = "127.0.0.1";
$port = 6555;
//$users = fopen("available.txt","w");
while(1)
{
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
socket_getpeername($spawn,$ip);
$input = socket_read($spawn,1024)  or die("Could not read inputn");

				$input = trim($input);
				//$tags = explode("++",$input);
				//$username = trim($tags[0]);
				//$passw = trim(crypt(md5(trim($tags[1])),md5(trim($tags[1]))));
				//$done = "1";
				//$notdone = "0";
				if($input != NULL)
				{
				$sql = "SELECT * FROM files WHERE MATCH (filename) AGAINST (\"$input\")";
				$result = mysqli_query($link,$sql);
				if($result != NULL)
				{
				while($row = mysqli_fetch_assoc($result))
				{
					socket_write($spawn,$row['id'],strlen($row['id']));
					socket_write($spawn,"        ");
					socket_write($spawn,$row['filename'],strlen($row['filename']));
					socket_write($spawn,"\n");
				}
				}
				}


if(!empty($row))
{
	mysqli_query($link,"INSERT INTO users (ip) VALUES (\"$ip\") WHERE username=\"$username\" AND passw=\"$passw\"");
	socket_write($spawn,$done,strlen($done));
unset($username);
unset($password);
}
else
	socket_write($spawn,$notdone,strlen($notdone));

socket_close($spawn);
socket_close($socket);
}
?>