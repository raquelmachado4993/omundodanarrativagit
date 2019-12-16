var cenariocadastrada = sessionStorage.getItem("cenariocadastrada");
var missaocadastrada = sessionStorage.getItem("missaocadastrada");
var objcadastrada = sessionStorage.getItem("objcadastrada");
var perscadastrada = sessionStorage.getItem("perscadastrada");
var transpcadastrada = sessionStorage.getItem("transpcadastrada");

if (((!cenariocadastrada)||(!missaocadastrada)||(!objcadastrada)||(!perscadastrada)||(!transpcadastrada))){
    alert("voce ainda não pode acessar essa pagina");
    window.location.href = "./paginadeselecao.html";
}else{
    alert("parabens pelo progresso!"); 
}