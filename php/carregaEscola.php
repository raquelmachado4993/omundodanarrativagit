<?php

function carregaEscola(){
    $dbdata = array();
    $sql = "select id_escola,CONCAT(nome_escola,' - ',bairro_escola ) AS 'escola' from   escola;";
    $retorno  = buscar($sql);
    while ( $row = $retorno->fetch_assoc())  {
        $dbdata[]=$row;
      }
    echo json_encode($dbdata);
}

function carregaTurma(){
    $dbdata = array();
    $escola = cuidado($_POST['escola']);
    $sql = "select  cod_turma  , CONCAT(ano_turma,'  - Professor - ',Nome ) AS 'turma'
    from Turma tu inner join pessoa pe on tu.cod_professor=pe.cod_pessoa
     where cod_escola='".$escola."';";
     //echo($sql);
    $retorno  = buscar($sql);
    while ( $row = $retorno->fetch_assoc())  {
        $dbdata[]=$row;
      }
    echo json_encode($dbdata);
    }

    function buscaTurma(){
      $dbdata = array();
      $pessoa = cuidado($_POST['pessoa']);
      $sql = "select  cod_turma  , CONCAT(ano_turma,'  - Professor - ',Nome ) AS 'turma'
      from Turma tu inner join pessoa pe on tu.cod_professor=pe.cod_pessoa
        inner join credenciais c on pe.cod_pessoa = c.cod_pessoa
        where c.credencial='".$pessoa."';";
       //echo($sql);
      $retorno  = buscar($sql);
      while ( $row = $retorno->fetch_assoc())  {
          $dbdata[]=$row;
        }
      echo json_encode($dbdata);
      }


      function modTipoAplicacao(){
        $dbdata = array();
        $pessoa = cuidado($_POST['pessoa']);
        $ativo = cuidado($_POST['ativo']);
        $turmas = cuidado($_POST['turmas']);
        
            
        $sql = "update Turma t set t.acesso_jogo=".$ativo." where cod_turma='".$turmas."' and   t.cod_professor in (select cod_pessoa from credenciais  where credencial ='".$pessoa."');";
        //echo($sql); 
        if(buscar($sql)){echo("true");}else{ echo("false");}
      }


/*
    ano_turma

    cod_escola
    cod_professor
    identificacao_turma
    trabalha_Professor_cod_professor
    trabalha_escola_id_escola
    
    
    
    
     \
                        <select  name="escola" id="escola" onblur="" required> \
                        <option value="selecione">selecione</option> \
                        </select><label class="ali"> Ano/turma </label> \
                        <select  name="anoturma" id="anoturma" onblur="" required></select>
    
    
    
    
        //\
        //<select  name="escola" id="escola" onblur="" required> \
        //<option value="selecione">selecione</option> \
        //</select><label class="ali"> Ano/turma </label> \
        //<select  name="anoturma" id="anoturma" onblur="" required></select>
    

*/

?>