<?php
include_once("funcoes.php");
if (!(isset($_SESSION['id_unidade'])||(isset($_SESSION['id_usuario'])))){
    if (strpos($_SERVER['SCRIPT_NAME'], "autenticacao.php")===false){
        echo('<META HTTP-EQUIV="Refresh" CONTENT="0; URL=./login.php">');
    }  
}
?>