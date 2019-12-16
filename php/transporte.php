<?php
include_once("funcoes.php");

function validatransporte($transporte){
    $transporte=$transporte;

        if(empty($transporte->pessoa)){
            return null;
        }
        if(empty($transporte->nometransporte)){
            $transporte->nometransporte="não preenchido";
        }
        if(empty($transporte->caractransp)){
            $transporte->caractransp="não preenchido";
        }
        if(empty($transporte->captransp)){
            $transporte->captransp="não preenchido";
        }
        if(empty($transporte->caracmisttransp)){
            $transporte->caractransp="não preenchido";
        }
        if(empty($transporte->histotransp)){
            $transporte->histotransp="não preenchido";
        }
        if(empty($transporte->objtransporte)){
            $transporte->objtransporte="não preenchido";
        }   
        if(empty($transporte->tempo)){
            $transporte->tempo="";
        }

    return $transporte;

}



function cadtransporte(){
    if(empty($_POST['jsontransporte'])){die;}

        $transporte = json_decode($_POST['jsontransporte']);
        $tipo="false";
        $url="";
        $transporte = validatransporte($transporte);

        $sql="select cod_pessoa from credenciais 
        where credencial='".$transporte->pessoa."'
        and DATE_FORMAT(data_espiracao,'%Y-%m-%d') = CURRENT_DATE()";
      //  echo($sql);
        $retorno  = buscar($sql);
        while ($row  = mysqli_fetch_assoc($retorno)) {
                if(!empty($row['cod_pessoa'])){
                    $Sql1="INSERT INTO transporte(id_pessoa,nometransporte,caracteristica_transp,capacidade_transp,caracteristica_mistica_transp,historia_transp,objtransporte,tempo_gasto";
                    
                    $Sql2=") VALUES(".$row['cod_pessoa'].",
                            '".($transporte->nometransporte)."',
                            '".($transporte->caractransp)."',
                            '".($transporte->captransp)."',
                            '".($transporte->caracmisttransp)."',
                            '".($transporte->histotransp)."',
                            '".($transporte->objtransporte)."',
                            '".($transporte->tempo)."'";

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