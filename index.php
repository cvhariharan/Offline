 <html>
<head>
  <title>Offl!ne</title>
  <link href="https://fonts.googleapis.com/css?family=Luckiest+Guy" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Overpass" rel="stylesheet">
  <link href="index.css" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
<div class="navbar">
  <?php
  session_start();
  $username = $_SESSION['username'];
  $logged = "<ul align=\"right\">
    <li><a href=\"#\">Hello $username!</a></li>
  </ul>";
  $not_logged = "<ul align=\"right\">
    <li><a href=\"login.php\">Login</a></li>
    <li><a href=\"signup.php\">Signup</a></li>
  </ul>";
  if(isset($_SESSION['login']) && $_SESSION['login']==5)
  {
    echo $logged;
  }
  else {
    echo $not_logged;
  }
  ?>

</div>
<div class="offline">
<h2>Offl!ne.</h2></div>
<div id="search_box">
<form method="POST" action="search.php">
<center><input type="text" name="query"></center>
</form>
</div>
</body>
</html>
