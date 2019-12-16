$(".js-open-modal").click(function(){
  $(".modal").addClass("visible");
});

$(".js-open-modal2").click(function(){
  $(".modal2").addClass("visible");
});

$(".js-close-modal").click(function(){
  $(".modal").removeClass("visible");
  $(".modal2").removeClass("visible");
});



var div = document.getElementById('modaltexto');
var texto = 'texto';

/*
var parouno = sessionStorage.getItem("parouno");
if (!parouno){
  ponteiro=sessionStorage.getItem('parouno');

}else{
  
}
*/
var ponteiro =-1;

voltar();
  var vetorimagem  = [ 
    {"imagem": "ambulancia"},
    {"imagem": "carroconversivel"},
    {"imagem": "helicoptero"},
    {"imagem": "patinete"},
    {"imagem": "aviao"},
    {"imagem": "carrodapolicia"},
    {"imagem": "lancha"},
    {"imagem": "patins"},
    {"imagem": "balao"},
    {"imagem": "carrodobombeiro"},
    {"imagem": "limusine"},
    {"imagem": "submarino"},
    {"imagem": "bicicleta"},
    {"imagem": "carro"},
    {"imagem": "motoca"},
    {"imagem": "taxi"},
    {"imagem": "caminhaodecarga"},
    {"imagem": "foguete"},
    {"imagem": "navio"},
    {"imagem": "teleferico"},
    {"imagem": "caminhaosemcarga"},
    {"imagem": "onibusescolar"},
    {"imagem": "trator"},
    {"imagem": "caravela"},
    {"imagem": "guindaste"},
    {"imagem": "onibus"},
    {"imagem": "trem"},
    {"imagem": "cavaloalado"},
    {"imagem": "caminhando"},
    {"imagem": "naveespacial"},
    {"imagem": "barco"},
    {"imagem": "teletransporte"},
    {"imagem": "elevador"},
    {"imagem": "naviopirata"},
    {"imagem": "skate"},
    {"imagem": "fusca"}
    
  ];
  x = Math.random() *36;
y = Math.round(x);
//    alert("aqui");
numero=y+1;
randomico=vetorimagem[numero].imagem;
sessionStorage.setItem('transporte', randomico); 
sessionStorage.setItem('imagem_transporte', "./meiosdetransporte/"+randomico+".png");
salvaprogresso("escolheu_opcao_transporte",randomico); 


var vetorjson  = [ 
  {"imagem": "./paginadeselecao.html", "texto": "voltar"},
  {"imagem": "./fundos/aldeia.png", "texto": "Pedrinho seguiu outro caminho e avistou uma grande aldeia com muitas ocas."},
  {"imagem": "./fundos/alienindios.png","texto": "E nas ocas havia muitos alienindios!"},
  {"imagem": "./fundos/historiadopaje.png","texto": "O pajé alien estava contando belas histórias para as crianças alienígenas."},
  {"imagem": "./fundos/aliensucupira.png","texto": "A que Pedrinho mais gostou foi a de um alienígena anão com cabelo vermelho e os pés virados, que assombrava as crianças na mata."},
  {"imagem": "./fundos/pajealienconvidouprapassaranoite.png","texto": "Pedrinho foi convidado pelo pajé-alien a passar a noite na aldeia. Ele e sua lagarta foram muito bem acolhidos."},
  {"imagem": "./fundos/pedrinhoqueriadormir.png","texto": "Pedrinho dormia muito bem até que sua lagarta começou a roncar."},
  {"imagem": "./fundos/anoiteceu-alienindios.png","texto": "Depois de acordar com o barulho do ronco, Pedrinho não conseguiu dormir de novo e resolveu dar uma volta na beira do lago para ver as estrelas."},
  {"imagem": "./fundos/lagartaepedrinho.png","texto": "Depois de muito contemplar as estrelas, Pedrinho se deu conta de que sua lagarta também tinha acordado e já estava bem ali ao seu lado. Ela ficou encantada com as estrelas."},
  {"imagem": "./fundos/pow.png","texto": "De repente, Pedrinho caiu no chão."},
  {"imagem": "./fundos/pedrinho_atingido.png","texto": "Ele foi atingido por uma estrela que caiu bem na sua cabeça!" }, 
  {"imagem": "./fundos/fundoestrelascadentes.png","texto": "PEDRINHO: Ué!"},
  {"imagem": "./fundos/fundoestrelascadentes.png","texto": "A estrela cadente trouxe uma inspiração <br> <input class=\"js-open-modal2\"  type=\"image\"  id=\"botaoescolha\"  src=\"./botoes/botaomostrar.png\" width=\”5px\” height=\”5px\” onclick='escolharandomica();'/>"},
  {"imagem": "./fundos/fundoestrelascadentes.png","texto": "PEDRINHO: Acabei de ganhar uma ideia de transporte: "+randomico+" "+"!"},
  {"imagem": "./fundos/lagartafeliz.png","texto": "Pedrinho olhou pra sua lagarta e não entendeu o que aconteceu!"},
  {"imagem": "./fundos/lagartafeliz.png","texto": "Pedrinho ficou muito preocupado e decidiu buscar ajuda para sua lagarta. Ela estava vomitando arco-íris..."},
  {"imagem": "./fundos/lagartafeliz.png","texto": "O que Pedrinho deve fazer? <br> <input class=\"js-open-modal\"  type=\"image\"  id=\"botaoperguntar\"  src=\"./botoes/perguntar.png\" width=\”5px\” height=\”5px\” onclick='proximo();'/>   <input class=\"js-open-modal2\"  type=\"image\"  id=\"botaopesquisar\"  src=\"./botoes/pesquisar.png\" width=\”5px\” height=\”5px\” onclick='pgbusca();'/>           "},
  {"imagem": "./fundos/pajealienexplicando.png","texto": "PAJÉ ALIEN: Pedrinho, uma pessoa saudável é aquela que tem completude em todo o seu ser. É preciso cuidar e alimentar o corpo, mas também é necessário cuidar e alimentar a mente."},
  {"imagem": "./fundos/pajealienexplicando2.png","texto": "PAJÉ ALIEN: A contemplação da natureza e a meditação sob as estrelas cadentes alimentou a mente e sua consciência se expandiu." },
  {"imagem": "./fundos/pajealienexplicando2.png","texto": "PAJÉ ALIEN: Vá em frente e complete essa ideia!" },
  {"imagem": "./cadastro_transporte.html", texto: "proximo"}
];

function voltar(){
  var parouno = sessionStorage.getItem("parouno");
  // alert(parouno);
 // if (!parouno){
  //alert("voltei");
 ///   ponteiro=sessionStorage.getItem('parouno');
 //   ponteiro+=1;
 //   proximo();
 //   sessionStorage.removeItem('parouno');
//}
}

function pgbusca(){
  sessionStorage.removeItem('parouno');
  sessionStorage.setItem('parouno',ponteiro);
  window.location.href = "./paginadepesquisa.html"; 
  
}

function fechamodal(){
  $(".modal2").removeClass("visible");
}

function escolharandomica() {
  $(".modal2").addClass("visible"); 
  document.getElementById("modalescolha").innerHTML += '<img class="Imgpersonagem" src="./meiosdetransporte/'+randomico+'.png">';     
}
  // document.getElementById("modalescolha").innerHTML = '<h1>testando pra ver se funciona<br>smosmsosmosmosmosmsomso<br>ssaamoamsoasmaosmao</h1>';
    

