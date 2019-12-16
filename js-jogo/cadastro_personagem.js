if ((sessionStorage.getItem("personagem")=="coringa")||(sessionStorage.getItem("cenario")=== null)){
        document.getElementById("imagemcenario").innerHTML += '<form id="formulario" method="post" enctype="multipart/form-data" action="upload.php">';
        document.getElementById("imagemcenario").innerHTML += '<input type="file" id="imagem" name="imagem" /></form>';
        document.getElementById("imagemcenario").innerHTML += '<br><button onclick="EnviaImg();">enviar</button>';

}else{
    document.getElementById("imagempersonagem").innerHTML += '<img class="imagempersonagem" src="'+sessionStorage.getItem("imagem")+'">';
}


function enviarimagem(){

}

function criarpersonagem(){

        var personagem = new Object();
        personagem.inteligencia = $('#inteligencia').val();
        personagem.forca = $('#forca').val();
        personagem.criatividade = $('#criatividade').val();
        personagem.Coragem = $('#Coragem').val();
        personagem.nomedopersonagem = $('#nomedopersonagem').val();
        personagem.idadedopersonagem = $('#idadedopersonagem').val();
        personagem.ondemora = $('#ondemora').val();
        personagem.melhoramigo = $('#melhoramigo').val();
        personagem.inimigospersonagem = $('#inimigospersonagem').val();
        personagem.caracteristicasfisicas = $('#caracteristicasfisicas').val();
        personagem.caracteristicaspsicologicas = $('#caracteristicaspsicologicas').val();
        personagem.caracteristicasmisticas = $('#caracteristicasmisticas').val();
        personagem.demiasinfo = $('#demiasinfo').val();
        personagem.pessoa = sessionStorage.getItem("pessoa");
        personagem.tipoPersonagem = sessionStorage.getItem("personagem");
        personagem.tempo = recupera();
        //personagem.tipoPersonagem = "";
         var opcao = "cadPersonagem";
         var jsonPersonagem = JSON.stringify(personagem);
         $.post('./php/servlet.php',{jsonPersonagem:jsonPersonagem,opcao:opcao},function(responseText) {
               //alert(responseText);
                var obj = JSON.parse(responseText);
                if(obj.tipo == "true"){
                        alert("parabéns o personagem foi criado com sucesso!"); 
                        if(!sessionStorage.getItem("perscadastrada")){
                                numero =parseInt(sessionStorage.getItem("percentualPessoa"));
                                numero=numero+1;
                                sessionStorage.setItem("percentualPessoa",numero);
                                sessionStorage.setItem("perscadastrada",true);
                        }       
                        location.href=obj.url;
                }else{
                        location.href="./404.html";
                }
                });

}

function EnviaImg(){
        alert("eu to aqui");

        var fd = new FormData();
        fd.append('file', $("#imagem"));
        fd.append('usuario',sessionStorage.getItem("pessoa"));
        fd.append('tipo',"cenario");
        // Envia O FormData através da requisição AJAX
        $.ajax({
                url: './php/carregaimg.php',
                data: fd,
                processData: false,
                contentType: false,
                type: 'POST',
                success: function(data) {
                    alert(data);
                }
            });

             alert("cheguei no final");
        }