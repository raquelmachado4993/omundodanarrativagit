if ((sessionStorage.getItem("cenario")=="coringa" )|| (sessionStorage.getItem("cenario")=== null)){
        document.getElementById("imagemcenario").innerHTML += '<form id="formulario" method="post" enctype="multipart/form-data" action="upload.php">';
        document.getElementById("imagemcenario").innerHTML += '<input type="file" id="imagem" name="imagem" /></form>';
        document.getElementById("imagemcenario").innerHTML += '<br><button onclick="EnviaImg();">enviar</button>';

}else{
     document.getElementById("imagemcenario").innerHTML += '<img class="Imgcenario" width=100%” height=”100%” src="'+sessionStorage.getItem("imagem_couve")+'">';
 }
 function criarcenario(){
 
    var cenario = new Object();
    cenario.nomecenario = $('#nome_cenario').val();
    cenario.explicacenario = $('#explica_cenario').val();
    cenario.localizacaodocenario = $('#localizacaodocenario').val();
    cenario.caracteristicasfisicascenario = $('#caracteristicasfisicascenario').val();
    cenario.caracteristicasmisticascenario = $('#caracteristicasmisticascenario').val();
    cenario.historiacenario = $('#historiacenario').val();
    cenario.outrasinfocenario = $('#outrasinfocenario').val();
    cenario.motivoescolhacenario = $('#motivoescolhacenario').val();
    cenario.pessoa = sessionStorage.getItem("pessoa");
    cenario.objcenario = sessionStorage.getItem("couve");
    cenario.tempo = recupera();
     var opcao = "cadCenario";
     var jsoncenario = JSON.stringify(cenario);
     $.post('./php/servlet.php',{jsoncenario:jsoncenario,opcao:opcao},function(responseText) {
            //alert(responseText);
            var obj = JSON.parse(responseText);
            if(obj.tipo == "true"){
                    alert("parabéns o cenario foi criado com sucesso!"); 
                    if(!sessionStorage.getItem("cenariocadastrada")){
                            numero =parseInt(sessionStorage.getItem("percentualPessoa"));
                            numero=numero+1;
                            sessionStorage.setItem("percentualPessoa",numero);
                            sessionStorage.setItem("cenariocadastrada",true);
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
