<?php
function random_string($length)
{
    return substr(str_shuffle(str_repeat($x='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', ceil($length/strlen($x)) )),1,$length);
}
$server_user = random_string(6);
$server_pass = random_string(8);
$port = rand(6000,7500);
$localhost = "10.10.6.9";
header("Content-type: text/plain");
header("Content-Disposition: attachment; filename=sr.conf");
$content = "Username:$server_user\nPassword:$server_pass\nPort:$port\nLocalhost:$localhost\n";
echo $content;
?>
