﻿//Variaveis do canvas

var c;
var ctx;

//Variaveis do Jogador 

var img_player;
var player_x;
var player_y;
var player_width;
var player_height;
var gravity;

//Variaveis do Inseticida

var img_inseticida;
var inseticida_x;
var inseticida_y;
var inseticida_width;
var inseticida_height;
var inseticida_speed;
var criar;
var inseticida_count;

//Variaveis do Estado do Jogo
var comecou = false;
var estajogando;
var ponto = 0;

//Jogo rodando 

if (comecou == false) {
    comecar();
} 
var nextInterval = setInterval(Draw, 10);
var nextUpdate = setInterval(Update, 1);

//inicio do jogo
function comecar() {
  
    	
  	//VariaveisdoCanvas
    c = document.getElementById("screen");
    ctx = c.getContext("2d");
    c.width = 960;
    c.height = 720;
    offset_x = 32;
    offset_y = c.height - 128;

  	//Sobre o jogador
    img_player = new Image();
    img_player.src = "./images/lagarta2.png";
    player_x = 300;
    player_y = offset_y;
    player_width = 64;
    player_height = 64;
    gravity = 2;

  	//Sobre o inseticida
    img_inseticida = new Image();
    img_inseticida.src = "./images/inseticida2.png";
    criar = true;
    inseticida_count = 0;

	//Estado
    comecou = true;
    estajogando = false;
  	//ponto = 0;
}

//Atualizar frames
function Update() {
    Input();

    if (estajogando) {
        if (criar == true) {
            criarinseticida();
        }

        if (inseticida_count > 0) {
            CollisionHandling();
        }
    }
}

//Funcao para desenhar 
function Draw() {
  
  	//Background
    ctx.fillStyle = "lightblue";
    ctx.fillRect(0, 0, c.width, c.height);
    ctx.fillStyle = "green";
    ctx.fillRect(0, c.height - 64, c.width, c.height);

  	//Jogador
    ctx.drawImage(img_player, player_x, player_y);
  
  	//pontuacao
  	ctx.font = "24px VT323";
	//ctx.fillText("ponto: " + ponto,10, 30); nao quero mostrar a pontuacao

  	
    if (estajogando) {
        if (inseticida_count > 0) {
      
          	//Move inseticida
          	inseticida_x -= inseticida_speed;
          	//Draw inseticida
            ctx.drawImage(img_inseticida, inseticida_x, inseticida_y);
        }

        if (player_y < offset_y) {
          //gravidade
          player_y += gravity;
        }

        if (inseticida_x < -64) {
          	//criar inseticida
            criar = true;
        }
      //Add ponto
      ponto += 1;

    }
	if (ponto == 4000) { 
	alert("Que legal! Você ajudou sua lagarta a chegar ao campo de morangos!");
	window.location.href = "morangos.html";
} 

}


//Input
function Input() {
    window.onkeydown = function(e) {
        var keyCode = e.keycode ? e.keycode : e.which;

        switch (keyCode) {
            case 32:
            
            	if (estajogando == false)
                {
                  //Inicia o jogo
                  estajogando = true;
									ponto = 0;
                }
            	else
                {
                if (player_y == offset_y) {
                  //Pula
                  player_y -= 150;
                }
                }
                break;
            default:
                break;
        }
    }
}

//criar inseticidas
function criarinseticida() {
    inseticida_x = c.width;
    inseticida_y = offset_y;
    inseticida_width = 64;
    inseticida_height = 64;
    inseticida_speed = 3;
    inseticida_count += 1;
    if (inseticida_count > 0) {
        criar = false;
    }
}

//Verificar as colisoes
function CollisionHandling() {
    if (player_x < inseticida_x && player_x + player_width > inseticida_x) {
        if (player_y + player_height > inseticida_y) {
          	//Restart the game
            Start();
        }
    }
}