<?php
set_time_limit(0);
// open a server on port 
$server = stream_socket_server("tcp://127.0.0.1:6666", $errno, $errorMessage);
 
if ($server === false) 
{
    die("Could not bind to socket: $errorMessage");
}
 
$client_socks = array();
while(true)
{
    //prepare readable sockets
    $read_socks = $client_socks;
    $read_socks[] = $server;
     
    //start reading and use a large timeout
    if(!stream_select ( $read_socks, $write, $except, 300000 ))
    {
        die('something went wrong while selecting');
    }
     
    //new client
    if(in_array($server, $read_socks))
    {
        $new_client = stream_socket_accept($server);
         
        if ($new_client) 
        {
            //print remote client information, ip and port number
            echo 'Connection accepted from ' . stream_socket_get_name($new_client, true) . "n";
             
            $client_socks[] = $new_client;
            echo "Now there are total ". count($client_socks) . " clients.n";
        }
         
        //delete the server socket from the read sockets
        unset($read_socks[ array_search($server, $read_socks) ]);
    }
     
    //message from existing client
    foreach($read_socks as $sock)
    {
        $data = fread($sock, 4096);
        if(!$data)
        {
            unset($client_socks[ array_search($sock, $client_socks) ]);
            @fclose($sock);
            echo "A client disconnected. Now there are total ". count($client_socks) . " clients.n";
            continue;
        }
        //send the message back to client
        fwrite($sock, $data);
    }
}
?>