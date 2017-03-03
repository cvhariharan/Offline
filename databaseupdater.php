<html>
<head>
<title>
Offline
</title>
</head>

<body>
<?php
set_time_limit(0);
require "database.php";
$dir = getcwd();
$movies = scandir($dir."/Movies/",1); //Descending order so that the dots are in the end
$games = scandir($dir."/Games/",1);
$softwares = scandir($dir."/Softwares/",1);
$tvshows = scandir($dir."/Tvshows/",1);
$select = mysqli_query($link,"SELECT * FROM movies WHERE 1=1");
$i=0;
while($res = mysqli_fetch_array($select))
{
	$selectresult[$i] = $res;
	$i++;
}
print_r($selectresult);
foreach($movies as $movie)
{
	if($movie != "." && $movie != "..")
	{
		$flag = 0;
		foreach($selectresult as $entry)
		{
			if(in_array($movie,$entry))
		{
			$flag = 1;
			break;
			
		}
		}
		if($flag==0)
		{
			$fullname = explode(".",$movie);
			$fullname[count($fullname)-1] = "";
			$name = implode(" ",$fullname); //The name of the movie without extensions
			$name1 = str_replace(' ','%20',$name);
			$data = file_get_contents("http://www.omdbapi.com/?t=$name1&&tomatoes=true");
			$obj = json_decode($data);
			$id = $obj->imdbID;
			$posterdata = file_get_contents("https://api.themoviedb.org/3/find/$id?external_source=imdb_id&api_key=93631a4df04f817768febdf9bf8ad2a1");
			$post = json_decode($posterdata,true);
			//print_r($post);
			$imgurl = $post['movie_results'][0]['poster_path'];
			$director = $obj->Director;
			$title = $obj->Title;
			$date = $obj->Released;
			$reviewt = $obj->tomatoConsensus;
			$posra = $obj->tomatoFresh;
			$negra = $obj->tomatoRotten;
			$poster = $obj->Poster;
			$plot = $obj->Plot;
			$imdbrating = $obj->imdbRating;
			$genre = $obj->Genre;
			
			$image = file_get_contents("http://image.tmdb.org/t/p/w500/$imgurl");
			$saveimg = fopen("$id.jpg","w");
			$img = $id."jpg";
			fwrite($saveimg,$image);
			fclose($saveimg);
			$add = mysqli_query($link,"INSERT INTO movies (name,filename,director,plot,released,imdb,genre,poster) VALUES (\"$name\",\"$movie\",\"$director\",\"$plot\",\"$date\",\"$imdbrating\",\"$genre\",\"$img\")");
		}
		echo "$movie</br>";
	}
}

?>
</body>
</html>