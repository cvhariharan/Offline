<?php
error_reporting(~E_NOTICE);
set_time_limit (0);
require "database.php";
$address = "127.0.0.1";
$port = 6555;
$max_clients = 1000;
 
if(!($sock = socket_create(AF_INET, SOCK_STREAM, 0)))
{
    $errorcode = socket_last_error();
    $errormsg = socket_strerror($errorcode);
     
    die("Couldn't create socket: [$errorcode] $errormsg \n");
}
 
echo "Socket created \n";
 
// Bind the source address
if( !socket_bind($sock, $address , $port) )
{
    $errorcode = socket_last_error();
    $errormsg = socket_strerror($errorcode);
     
    die("Could not bind socket : [$errorcode] $errormsg \n");
}
 
echo "Socket bind OK \n";
 
if(!socket_listen ($sock , 10))
{
    $errorcode = socket_last_error();
    $errormsg = socket_strerror($errorcode);
     
    die("Could not listen on socket : [$errorcode] $errormsg \n");
}
 
echo "Socket listen OK \n";
 
echo "Waiting for incoming connections... \n";
 
//array of client sockets
$client_socks = array();
 
//array of sockets to read
$read = array();
 
//start loop to listen for incoming connections and process existing connections
while (true) 
{
    //prepare array of readable client sockets
    $read = array();
     
    //first socket is the master socket
    $read[0] = $sock;
     
    //now add the existing client sockets
    for ($i = 0; $i < $max_clients; $i++)
    {
        if($client_socks[$i] != null)
        {
            $read[$i+1] = $client_socks[$i];
        }
    }
     
    //now call select - blocking call
    if(socket_select($read , $write , $except , null) === false)
    {
        $errorcode = socket_last_error();
        $errormsg = socket_strerror($errorcode);
     
        die("Could not listen on socket : [$errorcode] $errormsg \n");
    }
     
    //if ready contains the master socket, then a new connection has come in
    if (in_array($sock, $read)) 
    {
        for ($i = 0; $i < $max_clients; $i++)
        {
            if ($client_socks[$i] == null) 
            {
                $client_socks[$i] = socket_accept($sock);
                 
                //display information about the client who is connected
                
                 
                //Send Welcome message to client
                /*$message = "Welcome to php socket server version 1.0 \n";
                $message .= "Enter a message and press enter, and i shall reply back \n";
				socket_write($client_socks[$i] , $address);
                socket_write($client_socks[$i] , $message);*/
                break;
            }
        }
    }
 
    //check each client if they send any data
    for ($i = 0; $i < $max_clients; $i++)
    {
        if (in_array($client_socks[$i] , $read))
        {
				$input = socket_read($client_socks[$i],1024)  or die("Could not read inputn");

				$input = trim($input);
				//$tags = explode("++",$input);
				//$username = trim($tags[0]);
				//$passw = trim(crypt(md5(trim($tags[1])),md5(trim($tags[1]))));
				//$done = "1";
				//$notdone = "0";
				$sql = "SELECT * FROM files WHERE MATCH (filename) AGAINST (\"$input\")";
				$result = mysqli_query($link,$sql);
				if($result != NULL)
				{
				while($row = mysqli_fetch_assoc($result))
				{
					socket_write($client_socks[$i],$row['filename'],strlen($row['filename']));
					socket_write($client_socks[$i],"\n");
				}
				}
            if ($input == null) 
            {
                //zero length string meaning disconnected, remove and close the socket
                unset($client_socks[$i]);
                socket_close($client_socks[$i]);
            }
			/*if(!empty($row))
		{
			foreach($rows as $data)
	socket_write($client_socks[$i],$out,strlen($done));
	unset($username);
	unset($password);
		}*/
/*else
	socket_write($client_socks[$i],$notdone,strlen($notdone));*/
            /*$n = trim($input);
 
            $output = "OK ... $input";
             
            echo "Sending output to client \n";
             
            //send response to client
            socket_write($client_socks[$i] , $output);*/
        }
    }
}
?>