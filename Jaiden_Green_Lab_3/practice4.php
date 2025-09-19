<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Multiplication Table</title>
  <style>
    table, td, th { border: 1px solid black; border-collapse: collapse; padding: 5px; }
    th { background-color: #ddd; }
  </style>
</head>
<body>
  <h2>Multiplication Table</h2>
  <form method="post">
    Enter a number: <input type="number" name="num">
    <input type="submit" value="Generate">
  </form>

  <?php
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $n = intval($_POST["num"]);
    echo "<table>";
    // header row
    echo "<tr><th>*</th>";
    for ($i=1; $i <= $n; $i++) {
      echo "<th>$i</th>";
    }
    echo "</tr>";
    // rows
    for ($i=1; $i <= $n; $i++) {
      echo "<tr><th>$i</th>";
      for ($j=1; $j <= $n; $j++) {
        echo "<td>".($i*$j)."</td>";
      }
      echo "</tr>";
    }
    echo "</table>";
  }
  ?>
</body>
</html>
