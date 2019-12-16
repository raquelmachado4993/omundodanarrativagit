<?php
include_once("funcoes.php");

function validaobjeto($objeto){
    $objeto=$objeto;

        if(empty($objeto->pessoa)){
            return null;
        }
        if(empty($objeto->nomeobj)){
            $objeto->nomeobj="não preenchido";
        }
        if(empty($objeto->serventiaobjeto)){
            $objeto->serventiaobjeto="não preenchido";
        }
        if(empty($objeto->funcaoobj)){
            $objeto->funcaoobj="não preenchido";
        }
        if(empty($objeto->materialobjeto)){
            $objeto->materialobjeto="não preenchido";
        }
        if(empty($objeto->historiaobjeto)){
            $objeto->historiaobjeto="não preenchido";
        }
        if(empty($objeto->comoobjchegaaoobjeto)){
            $objeto->comoobjchegaaoobjeto="não preenchido";
        }
        if(empty($objeto->pqobjeto)){
            $objeto->pqobjeto="não preenchido";
        }
        if(empty($objeto->objselecao)){
            $objeto->objselecao="não preenchido";
        }
        if(empty($objeto->tempo)){
            $objeto->tempo="não preenchido";
        }     
    return $objeto;

}



function cadobjeto(){
    if(empty($_POST['jsonobjeto'])){die;}

        $objeto = json_decode($_POST['jsonobjeto']);
        $tipo="false";
        $url="";
        $objeto = validaobjeto($objeto);

        $sql="select cod_pessoa from credenciais 
        where credencial='".$objeto->pessoa."'
        and DATE_FORMAT(data_espiracao,'%Y-%m-%d') = CURRENT_DATE()";
      //  echo($sql);
        $retorno  = buscar($sql);
        while ($row  = mysqli_fetch_assoc($retorno)) {
                if(!empty($row['cod_pessoa'])){
                    $Sql1="INSERT INTO objeto(id_pessoa,nomeobj,serventiaobjeto,funcaoobj,materialobjeto,historiaobjeto,comoobjchegaaopersonagem,pqobjeto,objselecao,tempo_gasto";
                    
                    $Sql2=") VALUES(".$row['cod_pessoa'].",
                            '".($objeto->nomeobj)."',
                            '".($objeto->serventiaobjeto)."',
                            '".($objeto->funcaoobj)."',
                            '".($objeto->materialobjeto)."',
                            '".($objeto->historiaobjeto)."',
                            '".($objeto->comoobjchegaaoobjeto)."',
                            '".($objeto->pqobjeto)."',
                            '".($objeto->objselecao)."',
                            '".($objeto->tempo)."'";

                            $Sql= $Sql1.$Sql2.");";
                        if(buscar($Sql)){
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