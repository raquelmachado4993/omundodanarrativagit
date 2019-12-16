$(".js-open-modal").click(function () {
  $(".modal").addClass("visible");
});

$(".js-close-modal").click(function () {
  $(".modal").removeClass("visible");
});

$(document).click(function (event) {
  //if you click on anything except the modal itself or the "open modal" link, close the modal
  if (!$(event.target).closest(".modal,.js-open-modal").length) {
    $("body").find(".modal").removeClass("visible");
  }
});


function trocacena(fundo) {
  $(document).ready(function () {
    document.getElementsByClassName("myImg")[0].src = fundo;
  });
}
function proximapagina(pagina) {
  // alert(pagina);
  window.location.href = pagina;
}

function escrever(str, el) {
  el.innerHTML = "" + str;

}


function voltar() {
  ponteiro--;
  if (ponteiro < 0) {
    //  alert(ponteiro);
    ponteiro = 0;
  }
  if (vetorjson[ponteiro].texto == 'voltar') {
    //  alert("aqui");
    proximapagina(vetorjson[ponteiro].imagem);
  }
  trocacena(vetorjson[ponteiro].imagem);
  if ((vetorjson[ponteiro].texto != 'nada') || (vetorjson[ponteiro].texto != 'voltar')) {
    escrever(vetorjson[ponteiro].texto, div);
  }
  if (vetorjson[ponteiro].texto == 'nada') {
    $(".modal").removeClass("visible");
    setTimeout(voltar, 1000);
  } else {
    $(".modal").addClass("visible");
  }
}

function proximo() {
  if (ponteiro < 0) {
    // alert(ponteiro);
    ponteiro = 0;
  }
  if (vetorjson.length != ponteiro) {
    ponteiro++;
    trocacena(vetorjson[ponteiro].imagem);
    if (vetorjson[ponteiro].texto == 'proximo') {

      proximapagina(vetorjson[ponteiro].imagem);
    }
    if ((vetorjson[ponteiro].texto != 'nada') || (vetorjson[ponteiro].texto != 'voltar')) {
      escrever(vetorjson[ponteiro].texto, div);
    }
    if (vetorjson[ponteiro].texto == 'nada') {
      $(".modal").removeClass("visible");
      setTimeout(proximo, 1000);
    } else {
      $(".modal").addClass("visible");
    }

  }
}
