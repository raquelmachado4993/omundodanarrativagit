function voltaanterios(){
    location.href="./paginadeselecaonarrativa.html";
}

function salvatecla(){

        var DateObj = new Date (Date.now());
        var pessoa = sessionStorage.getItem("pessoa");
        var narrativa = new Object();
        narrativa.millisec = DateObj.getMilliseconds();
        narrativa.Seconds =  DateObj.getSeconds();
        narrativa.minute =  DateObj.getMinutes();
        narrativa.hora =  DateObj.getHours();

        document.onkeypress = function(evt) {
                evt = evt || window.event;
                var charCode = evt.keyCode || evt.which;
                var charStr = String.fromCharCode(charCode);
                narrativa.letra=charStr;               
                var opcao = "cadFluxoNarrativa";
                var jsonnarrativa = JSON.stringify(narrativa);
                $.post('./php/servlet.php',{jsonnarrativa:jsonnarrativa,pessoa:pessoa,opcao:opcao},function(responseText) {
                        //alert(responseText);
                });
        };

        
        

}

function criarnarrativa(){
 
    var narrativa = new Object();
    narrativa.txnarrativa = $('#txnarrativa').val();
    narrativa.pessoa = sessionStorage.getItem("pessoa");
    narrativa.tempo = recupera();
     var opcao = "cadNarrativa";
     var jsonnarrativa = JSON.stringify(narrativa);
     $.post('./php/servlet.php',{jsonnarrativa:jsonnarrativa,opcao:opcao},function(responseText) {
            //alert(responseText);
            var obj = JSON.parse(responseText);
            if(obj.tipo == "true"){
                    alert("PARABÉNS! Sua narrativa foi criada com sucesso!"); 
                    if(!sessionStorage.getItem("narrativacadastrada")){
                            numero =parseInt(sessionStorage.getItem("percentualPessoa"));
                            numero=numero+1;
                            sessionStorage.setItem("percentualPessoa",numero);
                            sessionStorage.setItem("narrativacadastrada",true);
                    }       
                    location.href="./fimdahistoria.html";
                    //location.href="./index.html";
            }else{
                    location.href="./404.html";
            }
            });

}



function objeto(){
        window.open("./rascunho_objeto.html",'_blank');

}
function cenario(){
        window.open("./rascunho_cenario.html",'_blank');


}
function personagem(){
        window.open("./rascunho_personagem.html",'_blank');


}
function transporte(){
        window.open("./rascunho_transporte.html",'_blank');
      
}
function missao(){
        window.open("./rascunho_missao.html",'_blank');

}