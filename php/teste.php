<?php
include_once("./funcoes.php");

$sql="select n.texto_narrativa ,pe.nome
from pessoa pe
inner join narrativa n on pe.cod_pessoa = n.id_usuario";

$retorno = buscar($sql);
//echo($sql);
while ($row  = mysqli_fetch_assoc($retorno)) {
    echo("<h2>".$row['nome']."</h2><br><br>");echo($row['texto_narrativa']);
}


?>