<?php

require "dbConfig.php";
  
// Connect Helper
$conn = mysqli_connect($dbhost, $dbuser, $dbpassword, $dbname);//

if (mysqli_connect_errno()) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
    exit;
}

echo "Connected!";
?>
