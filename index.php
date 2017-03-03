<?php
$dir = getcwd();
echo $dir."<br>";
chdir("$dir/Movies/");
//$dir = getcwd();
//echo $dir."<br>";
$movies = scandir($dir."/Movies/",1); 
foreach($movies as $movie)
{
	if($movie != "." && $movie != "..")
	{
		$loc = "$dir\Movies\\".$movie;
	echo "<a href=\"/Movies/$movie\">$movie</a></br>";
	}
}
?>