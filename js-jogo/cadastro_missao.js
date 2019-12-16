document.getElementById("imagembiscoito").innerHTML += '<img class="Imgmissao" width=100%” height=”100%” src="'+sessionStorage.getItem("imagem_biscoito")+'">';


function criarmissao(){

        //alert($('#recursos_personagem').val());
        var missao = new Object();
        missao.facilidade = $('#facilidade').val();
        missao.aventura = $('#aventura').val();
        missao.perigo = $('#perigo').val();
        missao.recursospersonagem = $('#recursos_personagem').val();
        missao.duracaomissao = $('#duracao_missao').val();
        missao.importanciamissao = $('#importancia_missao').val();
        missao.prejuizomissao = $('#prejuizo_missao').val();
        missao.demaisinfomissao = $('#demais_info_missao').val();
        missao.finalfeliz = $('#finalfeliz').val();
        missao.pessoa = sessionStorage.getItem("pessoa");
        missao.tipomissao = sessionStorage.getItem("biscoito");
        missao.tempo = recupera();
         var opcao = "cadMissao";
         var jsonmissao = JSON.stringify(missao);
         $.post('./php/servlet.php',{jsonmissao:jsonmissao,opcao:opcao},function(responseText) {
                //alert(responseText);
                var obj = JSON.parse(responseText);
                if(obj.tipo == "true"){
                        alert("parabéns o missao foi criado com sucesso!"); 
                        if(!sessionStorage.getItem("missaocadastrada")){
                                numero =parseInt(sessionStorage.getItem("percentualPessoa"));
                                numero=numero+1;
                                sessionStorage.setItem("percentualPessoa",numero);
                                sessionStorage.setItem("missaocadastrada",true); 
                        }
      
                        location.href=obj.url;
                }else{
                        location.href="./404.html";
                }
                });

}