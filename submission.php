<?php
include
$servername = "localhost";
$username = "sai";
$password = "1234";

// Creating the connection using mysqli
$conn = new mysqli($servername, $username, $password);

//to check wether the connection is established
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

// // for creating database
// $sql = "CREATE DATABASE myDB";
// if ($conn->query($sql) === TRUE) {
//   echo "Database created successfully";
// } else {
//   echo "Error creating database: " . $conn->error;
// }
// ?> 





<?php
  $Name= GET['tx1'];
  $TagNo=GET['txt'];
  $Gender=GET['gender1'];
  $DOB=GET['dat'];
  $Cattle=GET['img'];

  $sql = "INSERT INTO MyGuests (Name, Tagno ,gender,Date,Cattle)
VALUES ('$Name', '$TagNo', '$Gender','$DOB','$Cattle')";

if ($conn->query($sql) === TRUE) {
    echo "inserted  successfully";
  } else {
    echo "not inserted successfully";
  }
?>