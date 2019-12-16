<?php
include_once("funcoes.php");

function validacenario($cenario){
    $cenario=$cenario;

        if(empty($cenario->pessoa)){
            return null;
        }
        if(empty($cenario->nomecenario)){
            $cenario->nomecenario="não preenchido";
        }
        if(empty($cenario->explicacenario)){
            $cenario->explicacenario="não preenchido";
        }
        if(empty($cenario->localizacaodocenario)){
            $cenario->localizacaodocenario="não preenchido";
        }
        if(empty($cenario->caracteristicasfisicascenario)){
            $cenario->caracteristicasfisicascenario="não preenchido";
        }
        if(empty($cenario->historiacenario)){
            $cenario->historiacenario="não preenchido";
        }
        if(empty($cenario->outrasinfocenario)){
            $cenario->outrasinfocenario="não preenchido";
        }
        if(empty($cenario->motivoescolhacenario)){
            $cenario->motivoescolhacenario="não preenchido";
        }

        if(empty($cenario->objcenario)){
            $cenario->objcenario="não preenchido";
        } 
        if(empty($cenario->tempo)){
            $cenario->tempo="";
        }
  
    return $cenario;

}



function cadcenario(){
    if(empty($_POST['jsoncenario'])){die;}

        $cenario = json_decode($_POST['jsoncenario']);
        $tipo="false";
        $url="";
        $cenario = validacenario($cenario);

        $sql="select cod_pessoa from credenciais 
        where credencial='".$cenario->pessoa."'
        and DATE_FORMAT(data_espiracao,'%Y-%m-%d') = CURRENT_DATE()";
      //  echo($sql);
        $retorno  = buscar($sql);
        while ($row  = mysqli_fetch_assoc($retorno)) {
                if(!empty($row['cod_pessoa'])){
                    $Sql1="INSERT INTO cenario
                    (id_pessoa, nome_cenario, explica_cenario, localizacao_do_cenario, caracteristicas_fisicas_cenario, caracteristicas_misticas_cenario, historia_cenario, outras_info_cenario, motivo_escolha_cenario,objcenario,tempo_gasto";
                    
                    $Sql2=") VALUES(".$row['cod_pessoa'].",
                            '".($cenario->nomecenario)."',
                            '".($cenario->explicacenario)."',
                            '".($cenario->localizacaodocenario)."',
                            '".($cenario->caracteristicasfisicascenario)."',
                            '".($cenario->caracteristicasmisticascenario)."',
                            '".($cenario->historiacenario)."',
                            '".($cenario->outrasinfocenario)."',
                            '".($cenario->motivoescolhacenario)."',
                            '".($cenario->objcenario)."',
                            '".($cenario->tempo)."'";

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