<?php
include_once("funcoes.php");

function validapersonagem($personagem){
    $personagem=$personagem;

        if(empty($personagem->pessoa)){
            return null;
        }
        if(empty($personagem->nomedopersonagem)){
            $personagem->nomedopersonagem="não preenchido";
        }
        if(empty($personagem->idadedopersonagem)){
            $personagem->idadedopersonagem="não preenchido";
        }
        if(empty($personagem->ondemora)){
            $personagem->ondemora="não preenchido";
        }
        if(empty($personagem->melhoramigo)){
            $personagem->melhoramigo="não preenchido";
        }
        if(empty($personagem->inimigospersonagem)){
            $personagem->inimigospersonagem="não preenchido";
        }
        if(empty($personagem->caracteristicasfisicas)){
            $personagem->caracteristicasfisicas="não preenchido";
        }
        if(empty($personagem->caracteristicaspsicologicas)){
            $personagem->caracteristicaspsicologicas="não preenchido";
        }
        if(empty($personagem->caracteristicasmisticas)){
            $personagem->caracteristicasmisticas="não preenchido";
        }
        if(empty($personagem->demiasinfo)){
            $personagem->demiasinfo="não preenchido";
        }
        if(empty($personagem->inteligencia)){
            $personagem->inteligencia="não preenchido";
        }
        if(empty($personagem->forca)){
            $personagem->forca="não preenchido";
        }
        if(empty($personagem->criatividade)){
            $personagem->criatividade="não preenchido";
        }
        if(empty($personagem->Coragem)){
            $personagem->Coragem="não preenchido";
        }
        if(empty($personagem->tipoPersonagem)){
            $personagem->tipoPersonagem="não preenchido";
        }
        if(empty($personagem->id_imagem)){
            $personagem->id_imagem="";
        }
        if(empty($personagem->id_imagem)){
            $personagem->id_imagem="";
        }
        if(empty($personagem->tempo)){
            $personagem->tempo="";
        }
            
    return $personagem;

}



function cadPersonagem(){
    if(empty($_POST['jsonPersonagem'])){die;}

        $personagem = json_decode($_POST['jsonPersonagem']);
        $tipo="false";
        $url="";
        $personagem = validapersonagem($personagem);

        $sql="select cod_pessoa from credenciais 
        where credencial='".$personagem->pessoa."'
        and DATE_FORMAT(data_espiracao,'%Y-%m-%d') = CURRENT_DATE()";
      //  echo($sql);
        $retorno  = buscar($sql);
        while ($row  = mysqli_fetch_assoc($retorno)) {
                if(!empty($row['cod_pessoa'])){
                    $Sql1="INSERT INTO perssonagem( id_pessoa ,  nome ,  idade ,  onde_mora ,  melhore_amigos ,  inimigos ,  carac_fisio ,  carac_psico ,  carac_poderes ,  mais_info ,  inteligencia ,  forca ,  criatividade ,  coragem ,  tipo_personagem ,tempo_gasto ";
                    
                    $Sql2=") VALUES(".$row['cod_pessoa'].",
                            '".($personagem->nomedopersonagem)."',
                            '".($personagem->idadedopersonagem)."',
                            '".($personagem->ondemora)."',
                            '".($personagem->melhoramigo)."',
                            '".($personagem->inimigospersonagem)."',
                            '".($personagem->caracteristicasfisicas)."',
                            '".($personagem->caracteristicaspsicologicas)."',
                            '".($personagem->caracteristicasmisticas)."',
                            '".($personagem->demiasinfo)."',
                            '".($personagem->inteligencia)."',
                            '".($personagem->forca)."',
                            '".($personagem->criatividade)."',
                            '".($personagem->Coragem)."',
                            '".($personagem->tipoPersonagem)."',
                            '".($personagem->tempo)."'";

                            if(!isset($personagem->id_imagem)){
                                $Sql1.= ", id_imagem";
                                $Sql2.= ",'".($personagem->id_imagem)."'";
                            }
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