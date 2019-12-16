if (sessionStorage.getItem("transporte")=="coringa"){
    //  document.getElementById("botaodeimagem").style.display="block";
 }else{
     document.getElementById("imagemtransporte").innerHTML += '<img class="Imgtransporte" width=100%” height=”100%” src="'+sessionStorage.getItem("imagem_transporte")+'">';
 }
 function criartransporte(){
 
    var transporte = new Object();
    transporte.nometransporte = $('#nometransporte').val();
    transporte.caractransp = $('#caractransp').val();
    transporte.captransp = $('#captransp').val();
    transporte.caracmisttransp = $('#caracmisttransp').val();
    transporte.histotransp = $('#histotransp').val();
    transporte.pessoa = sessionStorage.getItem("pessoa");
    transporte.objtransporte = sessionStorage.getItem("transporte");
    transporte.tempo = recupera();
     var opcao = "cadTransporte";
     var jsontransporte = JSON.stringify(transporte);
     $.post('./php/servlet.php',{jsontransporte:jsontransporte,opcao:opcao},function(responseText) {
            //alert(responseText);
            var obj = JSON.parse(responseText);
            if(obj.tipo == "true"){
                    alert("parabéns o transporte foi criado com sucesso!"); 
                    if(!sessionStorage.getItem("transpcadastrada")){
                            numero =parseInt(sessionStorage.getItem("percentualPessoa"));
                            numero=numero+1;
                            sessionStorage.setItem("percentualPessoa",numero);
                            sessionStorage.setItem("transpcadastrada",true);
                    }       
                    location.href=obj.url;
            }else{
                    location.href="./404.html";
            }
            });

}