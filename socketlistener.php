<?php

// set some variables
$host = "127.0.0.1";
$port = 4444;

// don’t timeout!
set_time_limit(0);

// create socket
$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Could not create
socketn");

// bind socket to port
$result = socket_bind($socket, $host, $port) or die("Could not bind to
socketn");

// start listening for connections
$result = socket_listen($socket) or die("Could not set up socket
listenern");

// accept incoming connections
// spawn another socket to handle communication
$spawn = socket_accept($socket) or die("Could not accept incoming
connectionn");

// read client input
$input = socket_read($spawn, 1024) or die("Could not read inputn");

// clean up input string
$input = trim($input);
$output = "You Wrote: $input";
socket_write($spawn,$output, strlen ($output)) or die("Could not write
outputn");

// close sockets
socket_close($spawn);
socket_close($socket);
?>