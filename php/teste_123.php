<?php
include_once("funcoes.php");
$sql="select pe.cod_pessoa ,Nome,tipo,login,senha,acesso_jogo,permissao_acesso_admin from pessoa pe
inner join permissao_acesso pa on pa.id_pessoa=pe.cod_pessoa
left outer join info_aluno ia on pe.cod_pessoa = ia.cod_pessoa
left outer join Turma tu on ia.Turma_cod_turma = tu.cod_turma
where pe.cod_pessoa  not in  (1,2,4); ";
$retorno = buscar("$sql");

// echo($sql);
while ($row = mysqli_fetch_assoc($retorno)) {
    $senha='12345';     
$tx = substr(trim($row['Nome']), 0, 4);
$senha = hash('sha256', $senha . $tx);

inserir("update pessoa set senha='".$senha."'  where cod_pessoa=".$row['cod_pessoa'].";");
//echo("update pessoa set senha='".$senha."'  where cod_pessoa=".$row['cod_pessoa']."; <br>");

}
?>