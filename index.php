<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<title>registro</title>
	<link rel="stylesheet" type="text/css" href="miestilo.css">
</head>
<body>
	<?php
	$servername = "localhost";
	$username = "game";
	$password = "game";
	$bdjuego = "juego";

	// Create connection
	$conn = new mysqli($servername, $username, $password, $bdjuego);

	// Check connection
	if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
	}
	//echo "Connected successfully";

	//$sql = "USE juego";
	//if (mysqli_query($conn, $sql)) {
	   // echo "Ingreso a la base de datos";
	//} else {
	  //  echo "Error creating database: " . mysqli_error($conn);
//}

if ($_POST) {
	$usuario = $_POST["usuario"];
	$contraseña = $_POST["contraseña"];
	$nombreJuego = $_POST["nombreJuego"];

	$sql = "INSERT INTO persona VALUES ('$usuario', '$contraseña')";
	$sql = "INSERT INTO puntaje VALUES ('$usuario', '$nombreJuego',0)";
	//$sql2 = "INSERT INTO puntaje VALUES ('$usuario')"
	if ($conn->query($sql) === TRUE) {
	    echo "Se a registrado correctamente :D";
	} else {
	    echo "Error: " . $sql . "<br>" . $conn->error;
	}
}

$sql = "SELECT usuario, nombreJuego, puntaje FROM puntaje";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "Usuario: " . $row["usuario"]. "<br> nombre del Juego: " . $row["nombreJuego"]. " puntaje: ". $row["puntaje"]. "<br>";
    }
} else {
    echo "0 results";
}

// Cerrando la conexión
$conn->close();

	?>

	<div id="registro">
	<h1> <font color="white">Registro por Primera vez :)</font> </h1>
	<form action="index.php" method="post">
		<table>
			<tr>
				<h1>Los juegos que tenemos son :D</h1>
				<h2><a href="naves/naves-javascript.html"> naves </a></h2>
				<h2><a href="starfox/starfox.html"/> starfox </a></h2>
				<h2><a href="juegoa.html"/> Caballo ajedrez </a></h2>
		<P>
			<h3> <font color="white">UNETE PARA GUARDAR TUS PUNTAJES EN GAMESLAND</font></h3>
				<tr>
		 	 <td>Usuario:</td>
		 	 <td><input type="text" name="usuario" placeholder="Escribe Tu usuario" required></td>
		 	 </tr>
			 <tr>
			 <td>contraseña:</td>
			 <td><input type="password" name="contraseña" placeholder="Escribe Tu contraseña" required></td>
			 </tr>
			 <tr>
			<td>nombre del juego:</td>
			<td><input type="text" name="nombreJuego" placeholder="nombre del juego" required></td>
			</tr>
			 <tr>
				<td>&nbsp;</td>
				<td><input id="boton" type="submit" name="boton" value="Registrar"></td>
				</tr>
			</table>
	</FORM>
	<form action="inicio.php" method="post">
		<table>
		<tr>
	 <td>Usuario:</td>
	 <td><input type="text" name="usuario" placeholder="Escribe Tu usuario" required></td>
	 </tr>
	 <tr>
	 <td>contraseña:</td>
	 <td><input type="password" name="contraseña" placeholder="Escribe Tu contraseña" required></td>
	 </tr>
	 <tr>
		<td>&nbsp;</td>
		<td><input id="boton" type="submit" name="boton" value="iniciar sesión"></td>
		</tr>
		</table>
	</form>
</div>
</body>

</html>
