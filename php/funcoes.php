<?php
ini_set('default_charset','utf-8');


//define ('_COM_MYSQL','192.168.1.64');

if(1){
    define ('_COM_MYSQL','192.168.1.64');
    define ('_PORT_MYSQL','3306');
    define ('_BANCO_MYSQL','jogonarrativa');
    define ('_USU_MYSQL','jogonarrativa');
    define ('_SENHA_MYSQL','jogonarrativa');
    error_reporting(E_ALL); ini_set('display_errors', TRUE);  ini_set('display_startup_errors', TRUE);
} else{
    define ('_COM_MYSQL','192.168.1.64');
    define ('_PORT_MYSQL','3306');
    define ('_BANCO_MYSQL','jogonarrativa');
    define ('_USU_MYSQL','jogonarrativa');
    define ('_SENHA_MYSQL','jogonarrativa');
}



define ('_FATOR_CALCULO','BoHonjtWn;Z2cuk');

function logI($texto){
    salvar("log_saida.log",data_corrente()." - ".$texto."\r\n\r\n");
}

function conexao (){
 //   $link = mysqli_connect(_COM_MYSQL, _USU_MYSQL, _SENHA_MYSQL, _BANCO_MYSQL);
 $link = mysqli_connect(_COM_MYSQL, _USU_MYSQL, _SENHA_MYSQL, _BANCO_MYSQL);
 mysqli_set_charset($link, "utf8");
    if (!$link) {
        echo "Error: Unable to connect to MySQL." . PHP_EOL;
        echo "Debugging errno: " . mysqli_connect_errno() . PHP_EOL;
        echo "Debugging error: " . mysqli_connect_error() . PHP_EOL;
    die();
    }
    return $link;
}

function buscar($sql){
   try{
    $con = conexao ();
    //$sql = mysqli_real_escape_string($con, $sql);
    $result = mysqli_query($con, $sql);
    if($result== TRUE){
      //  mysqli_close($con);
        return $result;
    }
    echo($sql);
    echo("erro ".mysqli_error($con));
    mysqli_close($con);  
    return null;
} catch (Exception $e) {
    echo($e->getMessage());
    $sql2="INSERT INTO log_erro(agente_erro,remote_erro,arquivo_erro,cod_erro)
    VALUES('".$_SERVER["HTTP_USER_AGENT"]."',
    '".$_SERVER["REMOTE_ADDR"]."',
    '".$_SERVER["HTTP_REFERER"]." erro no buscar com alguma sql "."',
    '".$e->getMessage()."');";
    inserir($sql2);   
}
}
function inserir($sql){
   try{
    $con = conexao ();
    $result = mysqli_query($con, $sql);
    if($result== TRUE){
        mysqli_close($con);
      // echo("aqui funcionou");
        return true;
    }  
   // echo(mysqli_error($con));
    mysqli_close($con);
    return false;
} catch (Exception $e) {
    echo($e);
    $sql="INSERT INTO log_erro(agente_erro,remote_erro,arquivo_erro,cod_erro)
    VALUES('".$_SERVER["HTTP_USER_AGENT"]."',
    '".$_SERVER["REMOTE_ADDR"]."',
    '".$_SERVER["HTTP_REFERER"]." erro no insert com alguma sql "."',
    '".$e."');";
   // echo($sql);
    inserir($sql);   
}
}

function deletar(){

}

function logar(){

}

function salvar($name, $text){
    $file = fopen($name, 'a+');
    fwrite($file, $text);
    fclose($file);
}

function conversao ($texto){
    $texto  = str_replace("'", "´", $texto);
    $texto  = str_replace(";", " ", $texto);
    $texto  = str_replace("--", " ", $texto);
    $texto  = str_replace("/", " ", $texto);
    $texto  = str_replace("&", "E", $texto);
    $texto  = str_replace("%", " ", $texto);
    $texto  = str_replace("", " ", $texto);
    return $texto;

}

function cuidado2($texto){
    $pos = strpos(strtoupper($texto), "INSERT");
    $pos = strpos(strtoupper($texto), "UPDATE");
    $pos = strpos(strtoupper($texto), "DELETE");
    $pos = strpos(strtoupper($texto), "DROP");
    $pos = strpos(strtoupper($texto), "INTO");
    $pos = strpos(strtoupper($texto), "VALUES");
    $pos = strpos(strtoupper($texto), "FROM");
    $pos = strpos(strtoupper($texto), "SELECT");
    $pos = strpos($texto, "&lt");
    $pos = strpos($texto, "&gt");
    $pos = strpos($texto, "&amp");
    $pos = strpos($texto, "&quot");
    $pos = strpos(strtoupper($texto), "SCRIPT");
    $pos = strpos(strtoupper($texto), "<");
    $pos = strpos(strtoupper($texto), ">");
    $pos = strpos(strtoupper($texto), "#");
    
    if ($pos === false) {
        $texto =conversao ($texto);
            return $texto;
    }else{    
        return "informação ilegam foi identificada";
            
        }

   }





function cuidado($texto){
    $texto=utf8_decode($texto);
    $pos = strpos(strtoupper($texto), "INSERT");
    $pos = strpos(strtoupper($texto), "UPDATE");
    $pos = strpos(strtoupper($texto), "DELETE");
    $pos = strpos(strtoupper($texto), "DROP");
    $pos = strpos(strtoupper($texto), "INTO");
    $pos = strpos(strtoupper($texto), "VALUES");
    $pos = strpos(strtoupper($texto), "FROM");
    $pos = strpos(strtoupper($texto), "SELECT");
    $pos = strpos($texto, "&lt");
    $pos = strpos($texto, "&gt");
    $pos = strpos($texto, "&amp");
    $pos = strpos($texto, "&quot");
    $pos = strpos(strtoupper($texto), "SCRIPT");
    $pos = strpos(strtoupper($texto), "<");
    $pos = strpos(strtoupper($texto), ">");
    $pos = strpos(strtoupper($texto), "#");
    
    if ($pos === false) {
        $texto =conversao ($texto);
            return $texto;
    }else{    
        return "informação ilegam foi identificada";
            
        }

   }
   function data_corrente(){
        date_default_timezone_set('America/Sao_Paulo');
    return  date('Y-m-d');
}
    function hora_corrente(){
        date_default_timezone_set('America/Sao_Paulo');
    return  date('H:i:s');
}

function retorna_id_pessoa($credencial){
    $id_pessoa='';
    $sql="select cod_pessoa from credenciais  
    where credencial='".$credencial."'
    and DATE_FORMAT(data_espiracao,'%Y-%m-%d') = CURRENT_DATE()";
    //echo($sql); 
    $retorno  = buscar($sql);
    while ($row = mysqli_fetch_assoc($retorno)) {
        $id_pessoa =$row['cod_pessoa'];
    }
    if($id_pessoa==''){
        return false;
    }else{
        return $id_pessoa; 
    }
}


?>