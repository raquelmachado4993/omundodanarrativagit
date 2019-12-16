var div = document.getElementById('modaltexto');
var texto = 'texto';
var ponteiro =-1;

var vetorjson  = [ 
    {"imagem": "./fundos/fundoestrelascadentes.png","texto": "PEDRINHO: Acabei de ganhar uma ideia de transporte!" },   
  ];

var random_images_array = ["balao.png", "patinete.png", "ambulancia.png"];



  function transporteRandomico(imgAr, path) {
      path = path || 'meiosdetransporte'; // default path here
      var num = Math.floor( Math.random() * imgAr.length );
      var img = imgAr[ num ];
      var imgStr = '<img src="' + path + img + '" alt = "">';
      document.write(imgStr); document.close();
      document.getElementById("novomodal").src = random_images_array(imgStr);
   
  }

 









//   function transporte() {
//     alert("cheguei")
//     x = Math.random() *2;
//     y = Math.round(x);
//     //    alert("aqui");
//     fundo=  "";

//     switch(y) {
//         case 0:
//         document.getElementById("nat").innerHTML += '<img class="Imgpersonagem" src="./meiosdetransporte/balao.png">';
//           break;

//         case 1:
//         document.getElementById("nat").innerHTML += '<img class="Imgpersonagem" src="./meiosdetransporte/foguete.png">';
//           break;

//         case 2:
//         document.getElementById("nat").innerHTML += '<img class="Imgpersonagem" src="./meiosdetransporte/ambulancia.png">';
//         default:
//           // code block
//       }


//     $(document).ready(function() {
//       document.getElementsByClassName("nat")[0].src = fundo;
//   });
// }


   



//   {"imagem": "./fundos/lagartafeliz.png","texto": "Pedrinho olhou pra sua lagarta e não entendeu o que aconteceu!"},
//   {"imagem": "./fundos/lagartafeliz.png","texto": "Pedrinho ficou muito preocupado e decidiu buscar ajuda para sua lagarta. Ela estava vomitando arco-íris..."},
//   {"imagem": "./fundos/lagartafeliz.png","texto": "O que Pedrinho deve fazer?"},
//   {"imagem": "./fundos/pajealienexplicando.png","texto": "PAJÉ ALIEN: Pedrinho, uma pessoa saudável é aquela que tem completude em todo o seu ser. É preciso cuidar e alimentar o corpo, mas também é necessário cuidar e alimentar a mente."},
//   {"imagem": "./fundos/pajealienexplicando2.png","texto": "PAJÉ ALIEN: A contemplação da natureza e a meditação sob as estrelas cadentes alimentou a mente e sua consciência se expandiu." },
//   {"imagem": "./fundos/pajealienexplicando2.png","texto": "PAJÉ ALIEN: Quando a mente se abre, novas ideias surgem. Você alimentou sua lagarta e foi presenteado com uma nova ideia." }





