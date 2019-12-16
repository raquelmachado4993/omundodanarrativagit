<?php
include_once("funcoes.php");


function controle_usuario($cod_pessoa, $chave){
    $chave = cuidado($chave);
    $cod_pessoa = cuidado($cod_pessoa);
    $usuario = credencial_usuario($cod_pessoa, $chave);
    // /echo($usuario);
    if($usuario){
        return  inserir("insert into credenciais(cod_pessoa, credencial) value (" . $cod_pessoa . ",'" . $chave . "');");
    }else{
        return $usuario;
    }
    }

function credencial_usuario($cod_pessoa, $chave)
{
    //$cod_pessoa = cuidado($cod_pessoa);
    $sql = ("select c.credencial,p.* from credenciais c inner join pessoa  p on c.cod_pessoa = p.cod_pessoa
    where p.cod_pessoa=" . $cod_pessoa . " and  credencial='".$chave."'and 
    DATE_FORMAT(data_espiracao,'%Y-%m-%d') = CURRENT_DATE();");
   // echo($sql);
     while ($row = mysqli_fetch_assoc(buscar($sql))) {
        return false;
    }
    return true;
}

function loginentrada()
{
    $tipo = "false";
    $url = "./500.html";
    $pessoa = null;
    try {
        if (!empty($_POST['jsonLogin'])) {

            $obj = json_decode($_POST['jsonLogin']);
        } else {
            echo ("problema no json");
            die;
        }

        $login =  cuidado($obj->login);
        $senha =  cuidado($obj->senha);

        $sql="select pe.cod_pessoa ,Nome,tipo,login,senha,acesso_jogo,permissao_acesso_admin from pessoa pe
                inner join permissao_acesso pa on pa.id_pessoa=pe.cod_pessoa
                left outer join info_aluno ia on pe.cod_pessoa = ia.cod_pessoa
                left outer join Turma tu on ia.Turma_cod_turma = tu.cod_turma
                where login ='". $login ."'; ";
        $retorno = buscar("$sql");

       // echo($sql);
        while ($row = mysqli_fetch_assoc($retorno)) {

            $tx = substr(trim($row['Nome']), 0, 4);
            $senha = hash('sha256', $senha . $tx);
            if (($login == $row['login']) && ($row['senha'] == $senha)) {
                 //echo($row['login']);
                if (session_status() !== PHP_SESSION_ACTIVE) {
                    session_start();
                } else {
                    session_destroy();
                    session_start();
                }
                $pessoa = hash('sha512', $row['cod_pessoa'] . $row['Nome'] . $row['tipo'] . _FATOR_CALCULO.data_corrente().hora_corrente());
                //  echo($row['permissao_acesso_admin']);
                if ($row['permissao_acesso_admin']) {
                  //  echo("aqui");
                    $url = "./analise.html";
                } else {
                       // var_dump($row['acesso_jogo']);
                        if (empty($row['acesso_jogo'])) {
                            $url = "./inicio.html";
                        }else{
                            $url = "./narrativa.html";
                        }
                }
                $_SESSION['usuario'] = $pessoa;
                $_SESSION['id_usuario'] = $row['cod_pessoa'];
                if ((controle_usuario($row['cod_pessoa'], $pessoa))) {
                   // echo("aqui");
                    $tipo = "true";
                }
            } else {
                $tipo = "false";
                $url = "./login.html";
            }
        }
    } catch (Exception $e) {
        echo ($e->getMessage());
        $sql = "INSERT INTO log_erro(agente_erro,remote_erro,arquivo_erro,cod_erro)
    VALUES('" . $_SERVER["HTTP_USER_AGENT"] . "',
    '" . $_SERVER["REMOTE_ADDR"] . "',
    '" . $_SERVER["HTTP_REFERER"] . "  " . $obj . "',
    '" . $e->getMessage() . "');";
        inserir($sql);
    } finally {
        $resp = array('tipo' => $tipo, 'pessoa' => $pessoa, 'url' => $url);
        $json = json_encode($resp);
        echo ($json);
    }
}
