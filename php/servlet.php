<?php
include_once("funcoes.php");
include_once("outras.php");
error_reporting(E_ALL); ini_set('display_errors', TRUE);  ini_set('display_startup_errors', TRUE);

$opcao = $_POST{'opcao'};
// echo($opcao);
switch ($opcao) {
    case "verifica_email":
        verificaEmail();
        break;
    case "verifica_login":
        verificalogin();
        break;
    case "logado":
        verificar_log();
        break;
    case "salvaprogresso":
        cadastrarUtilizacao();
        break;
    case "cadPersonagem":
        include_once("./personagem.php");
        cadPersonagem();
        break;
    case "cadTransporte":
        include_once("./transporte.php");
        cadTransporte();
        break;
    case "cadObjeto":
        include_once("./objeto.php");
        cadObjeto();
        break;
        case "cadFluxoNarrativa":
        include_once("./narrativa.php");
        cadFluxoNarrativa();
    case "cadNarrativa":
        include_once("./narrativa.php");
        cadNarrativa();
        break;
    case "cadMissao":
        include_once("./missao.php");
        cadMissao();
        break;
    case "cadCenario":
        include_once("./cenario.php");
        cadCenario();
        break;
    case "cadUsu":
        include_once("./login.php");
        loginentrada();
        break;
    case "cadEscola":
    // echo("aqui no servlet ");
        include_once("./cad_escola.php");
        cadEscola();
        break;
        case "cadTurma":
        // echo("aqui no servlet ");
            include_once("./cad_escola.php");
            cadTurma();
            break;
        case "carregaEscola":
    // echo("aqui no servlet ");
        include_once("./carregaEscola.php");
        carregaEscola();
        break;
        case "buscaTurma":
        include_once("./carregaEscola.php");
        buscaTurma();
        break;
        case "modTipoAplicacao":
            include_once("./carregaEscola.php");
            modTipoAplicacao();
            break;
        case "carregaturma":
            include_once("./carregaEscola.php");
            carregaTurma();
            break;

    default:
        echo ("deu ruim!!!");
        pgerro();
        break;
}
