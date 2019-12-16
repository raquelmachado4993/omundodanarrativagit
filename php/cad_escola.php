<?php
include_once("funcoes.php");

function cadEscola()
{
    $tipo = "false";
    $url = "./500.html";
    $obj = json_decode($_POST['jsonEscola']);

    $nomeesco = '';
    $bairroesco =  '';
    $cepesco =  '';
    $tipo_escola =  '';


    $nomeesco .=  cuidado($obj->nomeesco);
    $bairroesco .=  cuidado($obj->bairroesco);
    $cepesco .=  cuidado($obj->cepesco);
    $tipo_escola .=  cuidado($obj->tipo_escola);

    $cepesco  = str_replace("-", "", $cepesco);
    $cepesco = preg_replace("/[^0-9]/", "", $cepesco);


    // var_dump($obj);
    $sql = 'insert into escola(nome_escola,bairro_escola,cep_escola,tipo_escola) 
    values ("' . $nomeesco . '","' . $bairroesco . '","' . $cepesco . '","' . $tipo_escola . '");';
    if (inserir($sql)) {
        $tipo = ("true");
        $url = './analise.html';
    } else {
        $tipo = ("false");
    }
    $resp = array('tipo' => $tipo, 'url' => $url);
    $json = json_encode($resp);
    echo ($json);
}

function cadTurma()
{
    $tipo = "false";
    $url = "./500.html";
    $obj = json_decode($_POST['jsonEscola']);
    $id = '';
    $turma =  '';
    $seriturma =  '';
    $descturma =  '';
    $pessoa =  '';

    $id .=  cuidado($obj->id);
    $turma .=  cuidado($obj->turma);
    $seriturma .=  cuidado($obj->seriturma);
    $descturma .=  cuidado($obj->descturma);
    $pessoa .=  cuidado($obj->pessoa);

    $sql = "select cod_pessoa from credenciais 
    where credencial='" . $obj->pessoa . "'
    and DATE_FORMAT(data_espiracao,'%Y-%m-%d') = CURRENT_DATE()";
    $retorno  = buscar($sql);
    while ($row  = mysqli_fetch_assoc($retorno)) {
        if (!empty($row['cod_pessoa'])) {
            $sql2 = ("insert into Turma(ano_turma,identificacao_turma,
                    cod_professor,cod_escola)
                    values('" . $seriturma . "','" . $descturma . "','" . $row['cod_pessoa'] . "','" . $id . "');");

                  //  echo($sql2);
            if (inserir($sql2)) {
                echo("funcionou");
                $tipo = ("true");
                $url = '../analise.html';
            } else {
                $tipo = ("false");
            }
        }
    }
        $resp = array('tipo' => $tipo, 'url' => $url);
        $json = json_encode($resp);
        echo ($json);
    
}
