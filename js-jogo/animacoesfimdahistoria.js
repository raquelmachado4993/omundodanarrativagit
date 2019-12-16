var div = document.getElementById('modaltexto');
var texto = 'Hoje está um lindo dia!';
var ponteiro =-1;
var sol = 'O dia está lindo hoje!';

split = function (element) {
    words = $(element).text().split('');
    for (i in words) {
      words[i] = '<span>' + words[i] + '</span>';
    }
    text = words.join('');
    $(element).html(text);
  };
  
  textify = function(element,method,delay) {
    split(element);
    $(element + ' span').css('opacity','0')
    $(element + ' span').css('position','relative');
    in_speed = 10;
    count = 0;
    setTimeout(function(){
      count = 0;
      $(element + ' span').each(function () {
        if(method == 'fade'){
          $(this).delay(0 + in_speed * count).animate({ opacity: '1' }, 200);
        } else if(method == 'bounce'){
          $(this).delay(0 + in_speed * count).animate({ opacity: '1','top':'-4px'}, 220,'easeOutCubic');
          $(this).delay(0 + in_speed * count/4).animate({ opacity: '1','top':'0px'}, 220);
        }
        count++;
      });
    },delay);
  };
  




  var vetorjson  = [ 
    {"imagem": "./borboletas/NatePedrinho2.png","texto": "Você conseguiu, terráqueo! Conseguiu libertar uma linda borboleta-narrativa."},
    {"imagem": "./borboletas/NatePedrinho2.png","texto": "Você conseguiu, terráqueo! Conseguiu libertar uma linda borboleta-narrativa."},
    {"imagem": "./borboletas/NatePedrinho2.png","texto": "NAT: A metamorfose de suas ideias e o seu cuidado no processo trouxeram ao mundo um presente incrível: o seu texto!"},
    {"imagem": "./fim.html", texto: "proximo"}];

function lagartarandomica() {
    x = Math.random() *7;
    y = Math.round(x);
    //    alert("aqui");
    numero=y+1;
    fundo=  "./borboletas/borboleta"+numero+".png";
    $(document).ready(function() {
      document.getElementsByClassName("Imglagarta")[0].src = fundo;
  });
}


document.getElementById("ImgLagarta").innerHTML = lagartarandomica();

