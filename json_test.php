<?php
$d = file_get_contents("php://input");
$j = json_decode($d,true);
//$d = fread($jd,filesize("files.json"));
//$data = json_decode(trim($d),true);
foreach(array_keys($j) as $arr)
{
  echo $arr;
}
?>
