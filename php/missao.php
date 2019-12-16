<?php
include_once("funcoes.php");

function validaMissao($missao){
    $missao=$missao;

        if(empty($missao->pessoa)){
            return null;
        }
        if(empty($missao->recursospersonagem)){
            $missao->recursospersonagem="não preenchido";
        }
        if(empty($missao->duracaomissao)){
            $missao->duracaomissao="não preenchido";
        }
        if(empty($missao->importanciamissao)){
            $missao->importanciamissao="não preenchido";
        }
        if(empty($missao->prejuizomissao)){
            $missao->prejuizomissao="não preenchido";
        }
        if(empty($missao->demaisinfomissao)){
            $missao->demaisinfomissao="não preenchido";
        }
        if(empty($missao->finalfeliz)){
            $missao->finalfeliz="não preenchido";
        }
        if(empty($missao->facilidade)){
            $missao->facilidade="não preenchido";
        }
        if(empty($missao->aventura)){
            $missao->aventura="não preenchido";
        }
        if(empty($missao->perigo)){
            $missao->perigo="não preenchido";
        }
        if(empty($missao->tipomissao)){
            $missao->tipomissao="não preenchido";
        } 
        if(empty($missao->tempo)){
            $missao->tempo="";
        }     
    return $missao;

}



function cadMissao(){
    if(empty($_POST['jsonmissao'])){die;}
        $missao = json_decode($_POST['jsonmissao']);
        $tipo="false";
        $url="";
        $missao = validaMissao($missao);

        $sql="select cod_pessoa from credenciais 
        where credencial='".$missao->pessoa."'
        and DATE_FORMAT(data_espiracao,'%Y-%m-%d') = CURRENT_DATE()";
        //echo($sql);
        $retorno  = buscar($sql);
        while ($row  = mysqli_fetch_assoc($retorno)) {
                if(!empty($row['cod_pessoa'])){
                    $Sql1="INSERT INTO missao (id_usuario , recursospersonagem , duracaomissao , importanciamissao , prejuizomissao , demaisinfomissao , finalfeliz , facilidade , aventura , perigo , biscoito,tempo_gasto";
                    $Sql2=") VALUES(".$row['cod_pessoa'].", 
                            '".($missao->recursospersonagem)."',
                            '".($missao->duracaomissao)."',
                            '".($missao->importanciamissao)."',
                            '".($missao->prejuizomissao)."',
                            '".($missao->demaisinfomissao)."',
                            '".($missao->finalfeliz)."',
                            '".($missao->facilidade)."',
                            '".($missao->aventura)."',
                            '".($missao->perigo)."',
                            '".($missao->tipomissao)."',
                            '".($missao->tempo)."'";
                          //  echo('aqui');
                            $Sql= $Sql1.$Sql2.");";
                        if(inserir($Sql)){
                        $tipo="true";
                        $url="./paginadeselecao.html";
                        
                    }
                }
            }
        // resposta da informação
        $resp = array('tipo'=> $tipo,'url'=>$url); 
        $json = json_encode($resp);
        echo($json);
        
}
?>