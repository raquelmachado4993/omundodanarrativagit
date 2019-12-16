function funcao1() {
    //confirm("Eu sou um alert!");

    document.getElementById("nat").innerHTML = '<h1>testando pra ver se funciona<br>smosmsosmosmosmosmsomso<br>ssaamoamsoasmaosmao</h1>';
    document.getElementById("nat").innerHTML += '<img class="myImg" src="personagens/imagem-pirata.png">';
    document.getElementById("nat").innerHTML += '<button type="button">volta</button>';
    document.getElementById("nat").innerHTML += '<button type="button">escolher</button>';
}

function verifica_genero() {
    var genero = $('#genero').val();
    if (genero == "selecione") {
        //s alert("selecione seu genero!");
        document.getElementById("cgenero").style.visibility = "visible";
    } else {
        document.getElementById("cgenero").style.visibility = "hidden";
    }
}


function showAluno() {
    var texto = '';

    var opcao = "carregaEscola";
    $.post('./php/servlet.php', { opcao: opcao }, function (responseText) {
        //alert(responseText);
        var obj = JSON.parse(responseText);
        if (obj) {
            texto += '<label class="ali"> genero </label>  \
                    <select  name="genero" id="genero" onblur="verifica_genero()" required	> \
                    <option value="selecione">selecione</option> \
                    <option value="masculino">masculino</option> \
                    <option value="feminino">feminino</option> \
                    <option value="outros">outros</option> </select>  \
                    <div style="visibility: hidden;" id="cgenero"><font  color="red"> selecione um genero </font></div><br><br> \
                    <label class="ali"> Data de nascimento </label> <input type="date" name="datanascimento" value=""/><br> \
                    <br><br><label class="ali"> Escola </label>';
            texto += ('<select id="colegios" onclick="bussala();"><option value="-">Selecione</option>');
            for (var key in obj) {
                texto += ('<option value="' + obj[key].id_escola + '">' + obj[key].escola + '</option>');
            }
            texto += '</select><br> <br>';
            texto +='<div id="divSala"></div>';
            document.getElementById("divOutros").innerHTML = texto;
        }
    });

}


function bussala(){
    var texto = '';
    var escola=$('#colegios').val();
    var opcao = "carregaturma";
    $.post('./php/servlet.php', { opcao: opcao,escola: escola }, function (responseText) {
        //alert(responseText);
        var obj = JSON.parse(responseText);
        if (obj) {
            texto = '<br><br><label class="ali"> turma </label>';
            texto += ('<select id="turmas" name="turmas" onblur=""><option value="-">Selecione</option>');
            for (var key in obj) {
                texto += ('<option value="' + obj[key].cod_turma + '">' + obj[key].turma + '</option>');
            }
            texto += '</select><br> <br>';
            document.getElementById("divSala").innerHTML = texto;
        }
    });

}

function showProfessor() {
    var texto = '<label class="ali"> Email </label>  \
    <input type="email" id="email" size="50" name="email" value="" onblur="validaEmail()" /><br> \
    <div style="visibility: hidden;" id="vmail"><font  color="red">email já cadastrado</font></div> \
    </br><br> <label class="ali"> Confirmação de Email </label> <input id="email2" type="email" name="email2" value="" size="50"  onblur="verifica_email()"/> \
    <div style="visibility: hidden;" id="cmail"><font  color="red">email nao confere</font></div><br><br>';
    document.getElementById("divOutros").innerHTML = texto;

}

function showOutro() {
    var texto = '';
    document.getElementById("divOutros").innerHTML = texto;

}




function validaEmail() {

    var email1 = $('#email').val();
    var opcao1 = "verifica_email";
    $.post('./php/servlet.php', { email: email1, opcao: opcao1 }, function (responseText) {

        if (responseText == "true") {
            document.getElementById("vmail").style.visibility = "visible";
        } else {
            document.getElementById("vmail").style.visibility = "hidden";
        }
    });
}


function validalogin() {

    var login1 = $('#login').val();
    var opcao1 = "verifica_login";
    $.post('./php/servlet.php', { login: login1, opcao: opcao1 }, function (responseText) {

        if (responseText == "true") {
            document.getElementById("vlogin").style.visibility = "visible";
        } else {
            document.getElementById("vlogin").style.visibility = "hidden";
        }
    });
}



function verifica_email() {
    if (($('#email').val()) != ($('#email2').val())) {
        document.getElementById("cmail").style.visibility = "visible";
    } else {
        document.getElementById("cmail").style.visibility = "hidden";
    }
}

function verifica_senha() {
    if (($('#senha').val()) != ($('#senha2').val())) {
        document.getElementById("csenha").style.visibility = "visible";
    } else {
        document.getElementById("csenha").style.visibility = "hidden";
    }
}

//showOutro();

// assim funciona muito SVGFEFuncBElement, seria legal usar isso para tudo
// var Aluno = new Object();
// Aluno.email = $('#email').val(); 
// var opcao1 = "cadUsu";
//  var jsonAluno1 = JSON.stringify(Aluno);
// $.post('./php/testes.php',{jsonAluno:jsonAluno1,opcao:opcao1},function(responseText) {
//                      alert(responseText);
//                  });