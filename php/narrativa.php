<?php
include_once("funcoes.php");

function validanarrativa($narrativa){
    $narrativa=$narrativa;

        if(empty($narrativa->pessoa)){
            return null;
        }
        if(empty($narrativa->txnarrativa)){
            $narrativa->nomeobj="não preenchido";
        }
        if(empty($narrativa->tempo)){
            $narrativa->tempo="tempo com problema";
        }     
    return $narrativa;

}



function cadNarrativa(){
    if(empty($_POST['jsonnarrativa'])){die;}

        $narrativa = json_decode($_POST['jsonnarrativa']);
        $tipo="false";
        $url="";
        $narrativa = validanarrativa($narrativa);

        $sql="select cod_pessoa from credenciais 
        where credencial='".$narrativa->pessoa."'
        and DATE_FORMAT(data_espiracao,'%Y-%m-%d') = CURRENT_DATE()";
      //  echo($sql);
        $retorno  = buscar($sql);
        while ($row  = mysqli_fetch_assoc($retorno)) {
                if(!empty($row['cod_pessoa'])){
                    $Sql1="INSERT INTO narrativa (id_usuario,texto_narrativa,tempo_gasto";
                    $Sql2=") VALUES(".$row['cod_pessoa'].",
                            '".($narrativa->txnarrativa)."',
                            '".($narrativa->tempo)."'";

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

function cadFluxoNarrativa(){
     $jsonnarrativa = cuidado2($_POST['jsonnarrativa']);
     $pessoa = cuidado($_POST['pessoa']);

     $Sql="insert into fluxoTexto(validador,fluxoTexto) 
     values ('".$pessoa."','".$jsonnarrativa."') ;";
  // echo(inserir($Sql));
     if(!inserir($Sql)){
        $tipo="erro";
        $url="./500.html";
    }
//    $resp = array('tipo'=> $tipo,'url'=>$url); 
//    $json = json_encode($resp);
//    echo($json);
}


?>