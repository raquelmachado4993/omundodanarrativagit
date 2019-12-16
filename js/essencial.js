var percentualPessoa = sessionStorage.getItem("percentualPessoa");
if (!percentualPessoa) {
  sessionStorage.setItem("percentualPessoa", 0);
}

$(document).ready(function(e) {
  $('img[usemap]').rwdImageMaps();
});



// alert('aqui');
verificarlog();

const sleep = (milliseconds) => {
  return new Promise(resolve => setTimeout(resolve, milliseconds))
}

function salvaprogresso(tipo,informacao) {
 

  var opcao = "salvaprogresso";
  var info = new Object();

  info.tipo = tipo;
  info.informacao = informacao;
  info.senha = sessionStorage.getItem("pessoa");
  var jsonInfo = JSON.stringify(info);
   //alert("aqui no salva progresso"); 
  $.post('./php/servlet.php', { jsonInfo: jsonInfo, opcao: opcao }, function (responseText) {
    // alert(responseText);
    tipo_rep='';
    var obj = JSON.parse(responseText);
    if (obj.tipo != "true") {
      location.href = obj.url;
      tipo_rep="false";
      location.href = "./500.html";
    } else {
      tipo_rep="true";
    }
  });
//  return tipo_rep;
}


function limpar() {
  sessionStorage.clear();
  location.href = "index.html";
}

function verificarlog() {
  var pessoa = sessionStorage.getItem("pessoa");
  var opcao = "logado";
  if (!pessoa) {
    alert("É necessário logar primeiro");
    window.location.href = "./login.html";
  }
  $.post("./php/servlet.php", { pessoa: pessoa, opcao: opcao }, function (responseText) {
    //alert(responseText);
    var obj = JSON.parse(responseText);
    if (obj.tipo != "true" || (obj.tipo === null)) {
      //alert(obj.tipo); 
      location.href = obj.url;
      location.href = "./login.html";
    }
  });
}

interval = setInterval("conta();", 1000);
function formatatempo(segs) {
  //function por Augusto Claro
  //augustoclaro1@hotmail.com
  //www.seven3d.com.br
  min = 0;
  hr = 0;
  /*
  if hr < 10 then hr = "0"&hr
  if min < 10 then min = "0"&min
  if segs < 10 then segs = "0"&segs
  */
  while (segs >= 60) {
    if (segs >= 60) {
      segs = segs - 60;
      min = min + 1;
    }
  }

  while (min >= 60) {
    if (min >= 60) {
      min = min - 60;
      hr = hr + 1;
    }
  }

  if (hr < 10) { hr = "0" + hr }
  if (min < 10) { min = "0" + min }
  if (segs < 10) { segs = "0" + segs }
  fin = hr + ":" + min + ":" + segs
  return fin;
}
var segundos = 0; //inicio do cronometro
function conta() {
  segundos++;
  document.getElementById("counter").innerHTML = formatatempo(segundos);
}



function recupera() {
  return formatatempo(segundos);
}



