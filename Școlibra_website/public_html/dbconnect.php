<?php 
    $host='localhost';
    $username='id20929942_root';
    $pass='1234QWERasdf.';
    $dbname='id20929942_biblioteca'; 

    $con=mysqli_connect($host,$username,$pass) or die("Failed to connect to MySQL: " . mysql_error()); 
    $db=mysqli_select_db($con,$dbname) or die("Failed to connect to MySQL: " . mysql_error()); 
?>