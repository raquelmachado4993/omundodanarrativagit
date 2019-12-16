if (sessionStorage.getItem("objeto")=="coringa"){
    //  document.getElementById("botaodeimagem").style.display="block";
 }else{
     document.getElementById("imagemcenario").innerHTML += '<img class="Imgobjeto" width=100%” height=”100%” src="'+sessionStorage.getItem("imagem_morango")+'">';
 }
  
 function criarobjeto(){
 
         var objeto = new Object();
         objeto.nomeobj = $('#nomeobj').val();
         objeto.serventiaobjeto = $('#serventiaobjeto').val();
         objeto.funcaoobj = $('#funcaoobj').val();
         objeto.materialobjeto = $('#materialobjeto').val();
         objeto.historiaobjeto = $('#historiaobjeto').val();
         objeto.comoobjchegaaoobjeto = $('#comoobjchegaaoobjeto').val();
         objeto.pqobjeto = $('#pqobjeto').val();
         objeto.pessoa = sessionStorage.getItem("pessoa");
         objeto.objselecao = sessionStorage.getItem("morango");
         objeto.tempo = recupera();
          var opcao = "cadObjeto";
          var jsonobjeto = JSON.stringify(objeto);
          $.post('./php/servlet.php',{jsonobjeto:jsonobjeto,opcao:opcao},function(responseText) {
                // alert(responseText);
                 var obj = JSON.parse(responseText);
                 if(obj.tipo == "true"){
                         alert("parabéns o objeto foi criado com sucesso!"); 
                         if(!sessionStorage.getItem("objcadastrada")){
                                 numero =parseInt(sessionStorage.getItem("percentualPessoa"));
                                 numero=numero+1;
                                 sessionStorage.setItem("percentualPessoa",numero);
                                 sessionStorage.setItem("objcadastrada",true);
                         }       
                         location.href=obj.url;
                 }else{
                         location.href="./404.html";
                 }
                 });
 
 }