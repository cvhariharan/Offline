<html>
  <body>
    <form enctype="multipart/form-data" action="" method="POST">
     
      Choose a file to upload: <input name="uploadedfile" type="file" /><br />
      <input type="submit" value="Upload File" />
    </form>
  </body>
</html>
<?php
/*session_start();
$_SESSION['login'] = 1;
$login = $_SESSION['login'];
$name = $_POST['name'];
$category = $_POST['category'];
$os = $_POST['os'];
if(isset($_FILES['uploaded']))
{
	$filesize = $_FILES['uploaded']['size'];
	$tmplocation = $_FILES['uploaded']['tmp_name'];
	$filetype = $_FILES['uploaded']['type'];
	if($category == "Movies")
	{
		if()
	}
}
if($login==1)
{
	if(!isset($name) && !isset($category))
	{
	echo <<<EOD
	<form method = "POST" action = "">
	<input type="text" name = "name" placeholder="Please write the correct name" required>
	<select name="category"><h3>Choose the category</h3>
	<option value="Movies">Movie</option>
	<option value="Games">Game</option>
	<option value="Softwares">Software</option>
	<option value="TVshows">TV Show</option>
	</select>
	<input type="submit" name="submit">
	</form>
EOD;
	}
	else
	{
		if(!isset($os))
		{
		if($category == "Games" || $category == "Softwares")
		{
			echo <<<EOD
	<form method = "POST" action = "">
	<select name="os"><h3>Select the OS</h3>
	<option value="Windows64">Windows 64-bit</option>
	<option value="Windows32">Windows 32-bit</option>
	<option value="Linux64">Linux 64-bit</option>
	<option value="Linux32">Linux 32-bit</option>
	<option value="MacOs">MacOs</option>
	</select>
	<input type="submit" name="submit">
	</form>
EOD;
		}
	}
	echo <<<EOD
	<form method = "POST" action = "">
	<input type="file" name="uploaded">
	<input type="submit" name="submit">
	</form>
EOD;
	}
	
}*/
$ftp_server = "ftp://localhost/";
$ftp_username   = "offline";
$ftp_password   =  "";

// setup of connection
$conn_id = ftp_connect($ftp_server) or die("could not connect to $ftp_server");

// login
if (@ftp_login($conn_id, $ftp_username, $ftp_password))
{
  echo "conectd as $ftp_username@$ftp_server\n";
}
else
{
  echo "could not connect as $ftp_username\n";
}

$file = $_FILES["uploadedfile"]["name"];
$remote_file_path = $_FILES['uploadedfile']['tmp_name'];
ftp_put($conn_id, $remote_file_path, $_FILES["uploadedfile"]["tmp_name"],
        FTP_ASCII);
ftp_close($conn_id);
echo "\n\nconnection closed";
?>