(function ($) {
  $(function () {
    // set active radio to address bar
    $(document).on('click', '.tabs .tabs-nav label', function () {
      var hash = '#' + $(this).attr('for');
      window.history.replaceState('', '', hash);
    });
    // select active radio based on hash
    $(document.location.hash).prop('checked', true);
  });
})(window.Zepto || window.jQuery);


function cadescola() {
  //   nome_escola
  // bairro_escola
  // cep_escola
  // tipo_escola

  var texto = ('<br><br><form>');
  texto += ('<BR><label for="">Nome Escola</label> <input type="text" id="nomeesco" value="" required/><br>');
  texto += ('<BR><label for="">Bairro Escola</label> <input type="text" id="bairroesco" value="" /><br>');
  texto += ('<BR><label for="">CEP Escola</label> <input type="text" id="cepesco" value="" pattern="[0-9]+$" /><br>');
  texto += ('<BR>Tipo de Escola: <BR><BR> Publica   <input type="radio" id="tipo_escola" value="Publica"/> Particular  <input type="radio" name="tipo_escola" value="particular" />');

  texto += ('<br><BR><input type="button" onclick="cad_escola();" name="submit" value="Enviar" />');
  texto += ('</form>');
  document.getElementById("divaparece").innerHTML = texto;

}

function cad_escola() {
  if (($('#nomeesco').val())) {
    // alert("ENTREI");
    var Escola = new Object();
    Escola.nomeesco = $('#nomeesco').val();
    Escola.bairroesco = $('#bairroesco').val();
    Escola.cepesco = $('#cepesco').val();
    Escola.tipo_escola = $('#tipo_escola').val();
    var opcao = "cadEscola";
    var jsonEscola = JSON.stringify(Escola);
    $.post('./php/servlet.php', { jsonEscola: jsonEscola, opcao: opcao }, function (responseText) {
      //alert(responseText);
      var obj = JSON.parse(responseText);
      if (obj.tipo == "true") {
        alert("cadastro da escola feito com sucesso!");
        window.location.href = "./analise.html";

      } else {
        alert("falha no cadastro da escola");
        location.href = obj.url;
      }
    });
  } else {
    alert("preencha os campos");
  }
}

function cadturma() {
  var opcao = "carregaEscola";
  $.post('./php/servlet.php', { opcao: opcao }, function (responseText) {
    //alert(responseText);
    var obj = JSON.parse(responseText);
    if (obj) {
      var texto = ('<br><br><form> <select id="colegios"><option value="-">Selecione</option>');
      for (var key in obj) {
        texto += ('<option value="' + obj[key].id_escola + '">' + obj[key].escola + '</option>');
      }
      texto += ('</select><BR><BR><label for="">Identificador da turma </label> <input type="text" id="descturma" value="" required/><br>');
      texto += ('<BR><BR><label for="">Serie da turma </label> <input type="text" id="seriturma" value="" required/><br>');
      texto += ('<BR><BR><label for="">Descrição da turma </label> <input type="text" id="descturma2" value="" required/><br>');
      texto += ('<br><BR><input type="button" onclick="cad_turma();" name="submit" value="Enviar" />');
      texto += ('</form>');
      document.getElementById("divaparece").innerHTML = texto;
    } else {
      window.location.href = "./500.html";
    }
  });
}

function cad_turma() {
  if (($('#descturma').val()) && ($('#colegios').val() != '-')) {
    //  alert("ENTREI");

    var Escola = new Object();
    Escola.id = $('#colegios').val();
    Escola.turma = $('#descturma').val();
    Escola.seriturma = $('#seriturma').val();
    Escola.descturma = $('#descturma2').val();
    Escola.pessoa = sessionStorage.getItem("pessoa");
    var opcao = "cadTurma";
    var jsonEscola = JSON.stringify(Escola);
    $.post('./php/servlet.php', { jsonEscola: jsonEscola, opcao: opcao }, function (responseText) {
     // alert(responseText);
      var obj = JSON.parse(responseText);
      if (obj.tipo == "true") {
        alert("cadastro da escola feito com sucesso!");
        window.location.href = "./analise.html";

      } else {
        alert("falha no cadastro da escola");
        location.href = obj.url;
      }
    });
  } else {
    alert("preencha os campos");

  }
}
function mudancaModo() {
  var opcao = "buscaTurma";
  $.post('./php/servlet.php', {
    pessoa: sessionStorage.getItem("pessoa"),
    opcao: opcao
  }, function (responseText) {
    // alert(responseText);
    var obj = JSON.parse(responseText);
    if (obj) {
      var texto = ('<br><br><form> <select id="turmas"><option value="-">Selecione</option>');
      for (var key in obj) {
        texto += ('<option value="' + obj[key].cod_turma + '">' + obj[key].turma + '</option>');
      }
      texto += ('</select><br><br><label for="">versão completa </label></label><input type="radio" id="tipojogo" name="tipojogo" value="false" checked/><br>');
      texto += ('<label for="">somente texto </label><input type="radio" id="tipojogo" name="tipojogo" value="true" /><BR><BR>');
      texto += ('<input type="button" onclick="modTipoAplicacao();" name="submit" value="Enviar" />');
      texto += ('</form>');
      document.getElementById("divaparece").innerHTML = texto;

    } else {
      alert("falha no cadastro da escola");
      location.href = obj.url;
    }
  });
}

function modTipoAplicacao() {
  var radioValue = $("input[name='tipojogo']:checked").val();
  var turmas = $('#turmas').val();
  //alert("aqui o " + turmas);
  if (turmas != "-") {
    var opcao = "modTipoAplicacao";
    $.post('./php/servlet.php', {
      pessoa: sessionStorage.getItem("pessoa"),
      ativo: radioValue,
      turmas: turmas,
      opcao: opcao
    }, function (responseText) {
     // alert(responseText);
      if(responseText=="true"){
        alert("Mudança feita com sucesso!!"); window.location.href = "./analise.html";
      }else{ alert("Problema na modificação da turma "); window.location.href = "./analise.html";}
    });
  }else{
    alert("Selecione uma turma");
  }
}


