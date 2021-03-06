<!DOCTYPE html PUBLIC>
<html>
<head>
<meta charset="UTF-8" />
<title>Game</title>
<link rel="stylesheet" type="text/css" href="style.css">

</head>

<body class="gamesTemplate">
	<?php
	$servername = "localhost";
	$username = "game";
	$password = "game";

	// Create connection
	$conn = new mysqli($servername, $username, $password);

	// Check connection
	if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
	}
	//echo "Connected successfully";

	$sql = "USE juego";
	if (mysqli_query($conn, $sql)) {
	   // echo "Ingreso a la base de datos";
	} else {
	    echo "Error creating database: " . mysqli_error($conn);
}

$conn->close();

	?>
	
<div id="container">
	<div id="header"><br />Juega y gana!!</div>
	<div id="menu">
		<ul>
			<li><a href="index.html">Inicio</a></li>
			<li><a href="juegoa.html">Juego A</a></li>
			<li><a href="naves/naves-javascript.html">Juego B</a></li>
			<li><a href="starfox/starfox.html">Juego C</a></li>
		</ul>
	</div>
	<div id="sidebar1">
		<div class="boxed_title">
			<h2 class="title">Modelos 2</h2>
		</div>

		<div class="boxed_title">
			<h2 class="title">2017</h2>
			<div class="boxed_content">
				<p>Este espacio corresponde a un proyecto que consiste en la integracion de 3 juegos diferentes desarrollados en javascript con diferentes paradigmas de programacion </p>
			</div>
		</div>
	</div>
	<div id="mainContent"><div class="inner_copy"></div>
		<div class="banner"></div>
		<div class="contents">
			<h1 class="title">Bienvenidos a este espacio</h1>
			<img src="images/intro_img.jpg" alt="image1" width="150" height="120" class="fltlft" />
			<p>Somos un grupo de 3 estudiantes de ingenieria con el fin de desarrollar juegos desarrollados en javascript, esto hace parte de un proyecto de la materia de modelos de programacion 2 dirigido por el profesor Alejandro Daza

			</p><br />
			<h2 class="title">Galeria de Juegos</h2>
			<div class="featured">
				<div class="featured_caption"><img src="images/image2.jpg" alt="image2" width="163" height="118"/><br/>
				<a href="juegoa.html">Juego A </a>
				</div>
				<div class="featured_caption"><img src="images/image3.jpg" alt="image2" width="163" height="118" /><br />
					<a href="naves/naves-javascript.html"> Juego B </a>
				</div>
				<div class="featured_caption"><img src="images/image1.jpg" alt="image2" width="159" height="118" /><br/>
					<a href="starfox/starfox.html"/> Juego C </a>

			</div>

		</div>

	</div>
	<div class="clearfloat"></div>
	<div id="footer">
		<center>
			<div class="fleft">Universidad Distrital Francisco Jose de Caldas</div>
			<div class="fright">Camilo Rozo Andres Acosta Wilmer Pachon</a></div>

			</div class="fclear"></div>
		</center>
	</div>

</div>
</body>
</html>
