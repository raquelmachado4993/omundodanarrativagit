<?php
include_once("funcoes.php");
//var_dump($_POST);

$imgagem = $_FILES['file']['tmp_name']; 
$pessoa = $_POST['usuario'];
$tipo = $_POST['tipo'];
$imgagem = $_POST['file'];
$image = addslashes($imgagem);

$sql="select cod_pessoa from credenciais 
where credencial='".$pessoa."'
and DATE_FORMAT(data_espiracao,'%Y-%m-%d') = CURRENT_DATE()";
//  echo($sql);

$retorno  = buscar($sql);
while ($row  = mysqli_fetch_assoc($retorno)) {
        if(!empty($row['cod_pessoa'])){
            $Sql1="INSERT INTO omundo88_jogonarrativa.imagens (imagem, local_imagem, id_pessoa";
            $Sql2=") VALUES ('".$image."' , '".$tipo."',".$row['cod_pessoa']." );";

                    $Sql= $Sql1.$Sql2.");";
                if(buscar($Sql)){
                    echo("imagem viada com sucesso!");
                }else{
                    echo("problema ao carregar imagem!");
                }

            }
        }

?>