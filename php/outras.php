<?php

function verificaEmail()
{
    $email = cuidado($_POST['email']);
    $sql = "select count(*) as soma from pessoa where email='" . $email . "';";
    $retorno  = buscar($sql);
    while ($row = mysqli_fetch_assoc($retorno)) {

        if ($row['soma'] == 1) {
            echo ("true");
        } else {
            echo ("false");
        }
    }
}
function verificalogin()
{
    $login = cuidado($_POST['login']);
    $sql = "select count(*) as soma from pessoa where login='" . $login . "';";
    $retorno  = buscar($sql);
    while ($row = mysqli_fetch_assoc($retorno)) {

        if ($row['soma'] == 1) {
            echo ("true");
        } else {
            echo ("false");
        }
    }
}

function jsonretorno1($tipo, $url)
{
    // header('Location: 404.html');
    $resp = array('tipo' => $tipo, 'url' => $url);
    $json = json_encode($resp);
    echo ($json);
}

function verificar_log()
{
    if (session_status() !== PHP_SESSION_ACTIVE) {
        session_start();
    }
    $url = "500.html";
    $tipo = "false";

    // echo("chegei na funcao");

    if (empty($_SESSION['usuario'])) {
        // echo("sessao vazia");
        $url = "login.html";
        $tipo = "false";
        jsonretorno1($tipo, $url);
        die;
    }
    if (empty($_POST['pessoa'])) {
        //echo("sem pessoa");
        $url = "login.html";
        $tipo = "false";
        jsonretorno1($tipo, $url);
        die;
    }
    $cod_pessoa = retorna_id_pessoa($_SESSION['usuario']);

    if (!$cod_pessoa) {
       // echo ("aesse o e codigo" . $cod_pessoa);
        $url = "login.html";
        $tipo = "false";
        jsonretorno1($tipo, $url);
        die;
    }

    $sql = "INSERT INTO log_jogo(id_pessoa,info_naveg,ip_naveg,pag_acessada)
    VALUES('" . $cod_pessoa . "','" . $_SERVER["HTTP_USER_AGENT"] . "',
    '" . $_SERVER["REMOTE_ADDR"] . "','" . $_SERVER["HTTP_REFERER"] . "');";
    inserir($sql);

    $usuario = $_SESSION['usuario'];
    $pessoa = cuidado($_POST['pessoa']);

    if ($usuario == $pessoa) {
        $sql = "select cod_pessoa from credenciais 
                where credencial='" . $usuario . "'
                and DATE_FORMAT(data_espiracao,'%Y-%m-%d') = CURRENT_DATE();";
        $retorno  = buscar($sql);
        while ($row  = mysqli_fetch_assoc($retorno)) {
            $cod_pessoa = $row['cod_pessoa'];
            if (empty($cod_pessoa)) {
                $url = "./login.html";
                $tipo = "false";
                jsonretorno1($tipo, $url);
                exit;
            } else {
                $url = "";
                $tipo = "true";
                jsonretorno1($tipo, $url);
                exit;
            }
        }if($tipo=="false"){
            $url = "login.html";
            jsonretorno1($tipo, $url);
            exit;
        }

    } else {
        $url = "login.html";
        $tipo = "false";
        jsonretorno1($tipo, $url);
        exit;
    }
}



function cadastrarUtilizacao()
{
    $obj = json_decode($_POST['jsonInfo']);

    $tipo =  cuidado($obj->tipo);
    $informacao =  cuidado($obj->informacao);
    $credencial =  cuidado($obj->senha);

    $cod_pessoa = retorna_id_pessoa($credencial);

    if (!$cod_pessoa) {
        echo ("erro");
        die;
    }

    $sql1 = ("insert into acoes(id_pessoa,tipo_acao,acao) 
            values ('" . $cod_pessoa . "','" . $tipo . "','" . $informacao . "');");

     //echo($sql1);       

    if (buscar($sql1)) {
        $url = "";
        $tipo = "true";
        jsonretorno1($tipo, $url);            
    } else {
        $url = "500.html";
        $tipo = "false";
        jsonretorno1($tipo, $url);
        die;
    }
}
function pgerro()
{
    # code...
    echo $_SERVER["REMOTE_ADDR"];
    echo $_SERVER['HTTP_USER_AGENT'];
    echo ('Location: ../500.html');
    header("Location: ../500.html");
}

function iniciojogo()
{
    $_SESSION['usuario'];
}

?>