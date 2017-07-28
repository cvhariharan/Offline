<?php

$d = file_get_contents("php://input");
$json = json_decode($d, true);
$user_data = $json["me"];
$name = $user_data["name"];
$username = $user_data["username"];
$port = $user_data["port"];
$server_user = $user_data["server_user"];
$server_pass = $user_data["server_pass"];

?>
