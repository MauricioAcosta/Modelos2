<html>
<head>
	<title>GAME OR DIE</title>
</head>
<body>
	<h1>GAME</h1>
  <?php
  // Conectando, seleccionando la base de datos
  $link = mysql_connect('localhost', 'game', 'game')
      or die('No se pudo conectar: ' . mysql_error());
  echo 'Connected successfully';
  mysql_select_db('juego') or die('No se pudo seleccionar la base de datos');

  // Realizar una consulta MySQL
  $query = 'SELECT * FROM persona';
  $result = mysql_query($query) or die('Consulta fallida: ' . mysql_error());

  // Imprimir los resultados en HTML
  echo "<table>\n";
  while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
      echo "\t<tr>\n";
      foreach ($line as $col_value) {
          echo "\t\t<td>$col_value</td>\n";
      }
      echo "\t</tr>\n";
  }
  echo "</table>\n";

  // Liberar resultados
  mysql_free_result($result);

  // Cerrar la conexión
  mysql_close($link);

?>

<form action="index.html" method="post">

<table width="400" border="0" cellspacing="0" cellpadding="0" align="center">

 <tr>
 <td>Usuario:</td>
 <td><input type="text" name="usuario" placeholder="Escribe Tu usuario" required></td>

 </tr>

 <tr>
 <td>contraseña:</td>
 <td><input type="text" name="contraseña" placeholder="Escribe Tu contraseña" required></td>

 </tr>

<tr>
 <td>&nbsp;</td>
 <td><input id="boton" type="submit" name="boton" value="Guardar"></td>
 </tr>
 </tr>
 <td>&nbsp;</td>
 </tr>
 </table>
</form>
</body>

</html>
