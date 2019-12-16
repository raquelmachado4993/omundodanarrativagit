<?php
include_once("funcoes.php");

try{
$nome=cuidado($_POST['nome']);
$senha=cuidado($_POST['senha']);
$confsenha=cuidado($_POST['confirmar_senha']);
$tipo=cuidado($_POST['tipo']);
$login=cuidado($_POST['login']);




    if(($senha==$confsenha)){
        $tx = substr(trim($nome), 0, 4);
        $senha = hash('sha256',$senha.$tx);  
        $sql=("INSERT INTO pessoa(login, senha, Nome,tipo)
        VALUES ('".$login."', '".$senha."', '".$nome."','".$tipo."');");
       inserir($sql);
       // echo();
        $sql =("INSERT INTO permissao_acesso(id_pessoa,permissao_acesso_admin,permissao_jogar)
        VALUES((select cod_pessoa from pessoa where login like '".$login."'),false,true);");
        //echo(inserir($sql));
        inserir($sql);
        if($tipo=="professor"){
            $email=cuidado($_POST['email']);
            $confemail=cuidado($_POST['email2']);

            if($email==$confemail){
                $retorno=buscar("select * from pessoa where login like '".$login."' ; ");
                while ($row = mysqli_fetch_assoc($retorno)) {
                    $sql2=("INSERT INTO Professor(cod_pessoa,email)VALUES(".$row['cod_pessoa'].",'".$email."');");
                    //echo($sql2);
                   // echo();
                   inserir($sql2);
                }
            }

        }
        
        if($tipo=="aluno"){
           // echo($tipo);
            $genero=cuidado($_POST['genero']);
            $data_nascimento = cuidado($_POST['datanascimento']);
            $cod_turmas=cuidado($_POST['turmas']);
            //  ,Turma_cod_turma  ,".$cod_turma."
            $retorno=buscar("select * from pessoa where login like '".$login."' ; ");
            while ($row = mysqli_fetch_assoc($retorno)) {
                $sql2=("INSERT INTO info_aluno(sexo,cod_pessoa,data_nascimento,Turma_cod_turma)
                VALUES('".$genero."',".$row['cod_pessoa'].",'".$data_nascimento."','".$cod_turmas."');");
                //echo($sql2);
                inserir($sql2);
            }

        }
        echo("<br><br><h1>Usuario cadastrado com sucesso!</h1>");
    }else{
        echo("<br><br><h1>informações incorretas</h1>");
    }
    //echo('<META HTTP-EQUIV="Refresh" CONTENT="3; URL=../index.html">');

}catch (Exception $e) {
    //echo($e->getMessage());
    $sql="INSERT INTO log_erro(agente_erro,remote_erro,arquivo_erro,cod_erro)
    VALUES('".$_SERVER["HTTP_USER_AGENT"]."',
    '".$_SERVER["REMOTE_ADDR"]."',
    '".$_SERVER["HTTP_REFERER"]."  ".$obj."',
    '".$e->getMessage()."');";
    inserir($sql);   
}
  //var_dump( buscar("select count(*) from pessoa"));
?>