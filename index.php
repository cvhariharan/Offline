 <html>
<head>
  <title>Offl!ne</title>
  <link href="index.css" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
<div class="navbar">
  <?php
  session_start();
  $current_file = __FILE__;
  require "analytics.php";
  if(isset($_SESSION['username']))
  {
  $username = $_SESSION['username'];
  $logged = "<ul align=\"right\">
    <li><a href=\"logout.php\">Hello $username! Logout?</a></li>
  </ul>";
  }
  
  $not_logged = "<ul align=\"right\">
    <li><a href=\"login.php\">Login</a></li>
    <li><a href=\"signup.php\">Signup</a></li>
    <li><a href=\"sr_generator.php\">SR Generator</a></li>
    <li><a href=\"How-To.pdf\">How To Use?</a></li>
    <li><a href=\"Offline_Windows10_64bit.zip\">Download</a></li>
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
<p>Offl!ne.</p></div>
<div id="search_box">
<form method="POST" action="search.php">
<center><input type="text" name="query"></center>
</form>
</div>
</body>
</html>
