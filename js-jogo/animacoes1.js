var div = document.getElementById('modaltexto');
var texto = 'Hoje está um lindo dia!';
var ponteiro = -1;
var sol = 'O dia está lindo hoje!';

split = function (element) {
    words = $(element).text().split('');
    for (i in words) {
        words[i] = '<span>' + words[i] + '</span>';
    }
    text = words.join('');
    $(element).html(text);
};

textify = function (element, method, delay) {
    split(element);
    $(element + ' span').css('opacity', '0')
    $(element + ' span').css('position', 'relative');
    in_speed = 10;
    count = 0;
    setTimeout(function () {
        count = 0;
        $(element + ' span').each(function () {
            if (method == 'fade') {
                $(this).delay(0 + in_speed * count).animate({ opacity: '1' }, 200);
            } else if (method == 'bounce') {
                $(this).delay(0 + in_speed * count).animate({ opacity: '1', 'top': '-4px' }, 220, 'easeOutCubic');
                $(this).delay(0 + in_speed * count / 4).animate({ opacity: '1', 'top': '0px' }, 220);
            }
            count++;
        });
    }, delay);
};





var vetorjson = [
    { "imagem": "./inicio.html", "texto": "voltar" },
    { "imagem": "./fundos/pedrinho_no_mundo_da_narrativa.png", "texto": "Era uma vez um menino chamado Pedrinho." },
    { "imagem": "./fundos/criancasbrincandocompedrinho.png", "texto": "Pedrinho era uma criança feliz e adorava brincar com seus amigos." },
    { "imagem": "./fundos/escola1.png", "texto": "Mas Pedrinho não gostava da aula de Português. A professora, tia Fátima, vivia pedindo para que as crianças escrevessem textos, mas Pedrinho nunca entendia muito bem o motivo." },
    { "imagem": "./fundos/semideia.png", "texto": "Pedrinho também não tinha ideias sobre o que escrever e sempre criava textos pequenos. Quando conseguia escrever cinco linhas, era muito!" },
    { "imagem": "./fundos/escola2.png", "texto": "Mas a professora não entendia. Sempre brigava, dizia que precisava escrever mais e até passava textos como dever de casa" },
    { "imagem": "./fundos/escola2.png", "texto": "PEDRINHO: Ah, não! Escrever texto é coisa de outro mundo, professora!" },
    { "imagem": "./fundos/escola2.png", "texto": "PROFESSORA: Que isso, Pedrinho! Escrever textos é a coisa mais legal do mundo!" },
    { "imagem": "./fundos/escola2.png", "texto": "PEDRINHO: Só se for do seu mundo..." },
    { "imagem": "./fundos/natnoquartodopedrinho.png", "texto": "Quando terminou a aula, Pedrinho foi para casa e ao invés de fazer o dever, foi brincar. De repente, surge uma coisa sinistra no seu quarto!" },
    { "imagem": "./fundos/natnoquartodopedrinho.png", "texto": "PEDRINHO: Oi! Quem é você?" },
    { "imagem": "./fundos/natnoquartodopedrinho.png", "texto": "NAT: Oi, Terráqueo! Meu nome é Nat. Eu vim te buscar!" },
    { "imagem": "./fundos/pedrinhoassustadonanave.png", "texto": "PEDRINHO: Socorro!" },
    { "imagem": "./fundos/pedrinhoassustadonanave.png", "texto": "NAT: Fique calmo, Terráqueo!" },
    { "imagem": "./fundos/pedrinhoassustadonanave.png", "texto": "PEDRINHO: Para onde você está me levando?" },
    { "imagem": "./fundos/pedrinhoassustadonanave.png", "texto": "NAT: Estou levando você para conhecer um mundo maravilhoso! Lá existem muitas possibilidades e muitas coisas incríveis podem acontecer!" },
    { "imagem": "./fundos/pedrinhoassustadonanave.png", "texto": "NAT: Mas fique tranquilo! Nesse mundo, todos somos realeza e temos o poder de escolher o que vai acontecer!" },
    { "imagem": "./fundos/pedrinonanave1.png", "texto": "nada" },
    { "imagem": "./fundos/pedrinhonanave2.png", "texto": "nada" },
    { "imagem": "./fundos/pedrinhonanave3.png", "texto": "nada" },
    { "imagem": "./fundos/pedrinhonanave4.png", "texto": "nada" },
    { "imagem": "./fundos/chegouemkidzr.png", texto: "NAT: Chegamos!" },
    { "imagem": "./fundos/chegouemkidzr2.png", texto: "NAT: Fique à vontade para conhecer!" },
    { "imagem": "./fundos/pedrinhoindignadosozinhoemkidzr.png", texto: "PEDRINHO: Espere! Não me deixe aqui sozinho!" },
    { "imagem": "./fundos/pedrinho-esquerda.png", texto: "Pedrinho foi caminhando e observando as particularidades daquele lugar." },
    { "imagem": "./fundos/pedrinho-esquerda.png", texto: "Lá, existiam plantas em formatos diferentes, animais coloridos e MUITAS lagartas!" },
    { "imagem": "./fundos/pedrinhorecebeofertadeajuda.png", texto: "PÁSSARO AMARELO: Olá, Terráqueo! Precisa de ajuda?" },
    { "imagem": "./fundos/pedrinhorecebeofertadeajuda.png", texto: "PEDRINHO: Uau! Um pássaro falante! Eu preciso de ajuda sim. Eu estou meio perdido por aqui e tem um monte de lagartas me seguindo!" },
    { "imagem": "./fundos/pedrinhorecebeofertadeajuda.png", texto: "PÁSSARO AMARELO: As lagartas são metáforas da natureza" },
    { "imagem": "./fundos/pedrinhorecebeofertadeajuda.png", texto: "PEDRINHO: E o que isso significa de verdade?" },
    { "imagem": "./fundos/pedrinhorecebeofertadeajuda.png", texto: "PÁSSARO AMARELO: Significa que a inspiração é viva e pode estar em toda parte: na rua, na escola, no espaço ou até mesmo na orelha de sua avó!" },
    { "imagem": "./fundos/pedrinhorecebeofertadeajuda.png", texto: "PÁSSARO AMARELO: Veja ao redor quantas lagartas, isto é, quantas ideias estão por aí esperando serem encontradas!" },
    { "imagem": "./fundos/lagartasqueimandopedrinho.png", texto: "PEDRINHO: Mas elas estão me queimando!" },
    { "imagem": "./fundos/lagartasqueimandopedrinho.png", texto: "PÁSSARO AMARELO: Sim! Precisamos cuidar das lagartas para que as borboletas voem narrativas!" },
    { "imagem": "./fundos/lagartasqueimandopedrinho.png", texto: "PÁSSARO AMARELO: Quando a gente encontra uma inspiração e não cuida dela, ela morre. E nunca voa pelo mundo... a chama do arrependimento pode arder em sua alma para sempre! É melhor cuidar antes que isso aconteça!" },
    { "imagem": "./fundos/pedrinhoescolheulagarta2.png", texto: "PEDRINHO: Tudo bem! Acho que posso cuidar desta aqui!" },
    { "imagem": "./fundos/passarovaiembora2.png", texto: "PÁSSARO AMARELO: Muito bem! Parece que esta lagarta se transformará em uma bela narrativa! Boa sorte, Pedrinho!" },
    { "imagem": "./fundos/passarovaiembora2.png", texto: "PEDRINHO: Espere, não vai embora! Eu não sei cuidar de uma lagarta!" },
    { "imagem": "./fundos/passarovaiembora2.png", texto: "PÁSSARO AMARELO: Eu preciso ir! Tenho muitas canções para cantar. Alimente sua lagarta com o melhor de sua imaginação!" },
    { "imagem": "./paginadeselecao.html", texto: "proximo" }

]

    ;


function funcaosol() {


    var txtTitulo = 'Está um dia lindo hoje!';
    var txt1 = document.getElementById("nat");

    txt1.innerHTML += txtTitulo + "</u>";


    // document.getElementById("nat").innerHTML = '<h1>Está um lindo dia hoje!</h1>';
}

// function myFunction() {
//     document.getElementById("nat").reset();
//   }

function funcaonuvem() {

    var txtTitulo = 'Essas nuvens são de algodão doce! É melhor deixá-las para sobremesa!';

    var txt1 = document.getElementById("nat");
    txt1.innerHTML += txtTitulo + "</u>";

    // document.getElementById("nat").innerHTML = '<h1>Está um lindo dia hoje!</h1>';
}

function funcaoarvore() {

    var txtTitulo = 'Sua lagarta não pode comer sozinha uma árvore inteira!';
    var txt1 = document.getElementById("nat");
    txt1.innerHTML += txtTitulo + "</u>";


    // document.getElementById("nat").innerHTML = '<h1>Está um lindo dia hoje!</h1>';
}

function funcaogirassol() {

    document.getElementById("nat").innerHTML = 'Que Girassol lindo!';
}


function funcaopedra() {
    document.getElementById("nat").innerHTML = 'No meio do caminho tinha uma pedra. Tinha uma pedra no meio do caminho...';
}

function funcaocerca() {
    document.getElementById("nat").innerHTML = 'Cuidado para não se machucar na cerca!';
}

function funcaojanela() {
    document.getElementById("nat").innerHTML = 'Você está bisbilhotando pela janela?';
}

function funcaotorademadeira() {
    document.getElementById("nat").innerHTML = 'Essas toras de madeira estão muito pesadas! Acho que não vai dar pra carregá-las!';
}

function funcaolaranjeira() {
    document.getElementById("nat").innerHTML = 'Que bonita esta árvore!';
}

function funcaomacieira() {
    document.getElementById("nat").innerHTML = 'Essas frutas estão suculentas. Aposto que sua lagarta ia adorar comer várias. Como você pode fazer para carregar?';
}

function funcaoporta() {
    document.getElementById("nat").innerHTML = 'Você entrou na casa de algum alien';
    salvaprogresso('navegacao', 'entrou na porta');
    location.href = "./casa.html";

}

function funcaosofa() {
    document.getElementById("nat").innerHTML = 'O alien dono da casa disse que não pode emprestar o sofá hoje. Talvez amanhã de tarde...';
}

function funcaobanco() {
    document.getElementById("nat").innerHTML = 'O dono da casa vai precisar usar o banquinho e não vai poder emprestar';
}

function funcaolustre() {
    document.getElementById("nat").innerHTML = 'O dono da casa disse que pode emprestar o lustre.';
}

function funcaoabajour() {
    document.getElementById("nat").innerHTML = 'Para que você precisa de um abajour?';
}

function funcaovela() {
    document.getElementById("nat").innerHTML = 'O dono da casa disse que você pode levar a vela';
}

function funcaolivro() {
    document.getElementById("nat").innerHTML = 'Você pegou um livro emprestado';
}

function funcaoquadro() {
    document.getElementById("nat").innerHTML = 'O dono da casa te emprestou um quadro. Será que vai caber na nave quando você for voltar pra Terra?';
}

function funcaocesta() {
    salvaprogresso('progresso', 'pegou a cesta');
    document.getElementById("nat").innerHTML = 'Que legal. Você pegou uma cesta emprestada!';
    document.getElementById("nat").innerHTML += '<input type="image" vspace="200" onclick=\'fasefrutas();\' src="./botoes/escolher.png">';

}

function fasefrutas() {
    sessionStorage.setItem('cesta', 'true');
    window.location.href = "./frutas.html";
}

function funcaotapete() {
    document.getElementById("nat").innerHTML = 'Você pegou um tapete emprestado.';
}

function funcaoplanta() {
    document.getElementById("nat").innerHTML = 'Você pegou um vaso de planta emprestado.';
}

function funcaocortina() {
    document.getElementById("nat").innerHTML = 'Você pegou uma cortina emprestada.';
}

function funcaomoinho() {
    document.getElementById("nat").innerHTML = 'Você entrou no moinho';
}

function funcaovaca1() {
    var audio = new Audio('./sounds/vaca.mp3');
    audio.play();
    document.getElementById("nat").innerHTML = 'Sua lagarta tem intolerância à lactose!';
    document.getElementById("nat").innerHTML = 'Melhor deixar as vacas em paz!';

}

function funcaovaca2() {
    var audio = new Audio('./sounds/vaca.mp3');
    audio.play();
    var texto = "Essa vaca fez um grande salto sob a lua.";
    texto += "O que você acha que aconteceu quando a vaca saltou sob a lua?";
    texto += '<br><input type="text" id="imputvaca"  name="imputvaca" required>';
    texto += "<input type=\"image\"   class=\"js-open-modal\" id=\"botao2\"  src=\"./botoes/botaoavancar2.png\" width=\”5px\” height=\”5px\” onclick='finalvaca();'/>";
    document.getElementById("nat").innerHTML = texto;

}
function finalvaca() {
    var textovaca = $('#imputvaca').val();
    if (textovaca == "") {
        alert("voce tem que preencher o texto!!");
    } else {
        sessionStorage.setItem("textovaca", textovaca);
        salvaprogresso("resposta_vaca",textovaca);
        $(".modal").removeClass("visible");
        alert("A vaca ficou muito famosa no Youtube.");
    }


}


function funcaoabelha() {
    var audio = new Audio('./sounds/abelha.mp3');
    audio.play();
    document.getElementById("nat").innerHTML = 'A abelha está indo fazer a polinização. É melhor não atrapalhá-la!';

}

function ancinho() {
    document.getElementById("nat").innerHTML = 'O nome desse negócio é Ancinho! Ele serve para coletar folhas soltas e para nivelar um solo que foi cavado.';

}

function regador1() {
    document.getElementById("nat").innerHTML = 'O regador está sem água.';

}

function regador2() {
    document.getElementById("nat").innerHTML = 'Ué, cadê a água?';

}

function caramujo() {
    document.getElementById("nat").innerHTML = 'Você já viu um caracol andar tão rápido?';

}

function arvorezinha1() {
    document.getElementById("nat").innerHTML = 'Já dizia Kalil Gibran: "Árvores são poemas que a terra escreve para o céu."';

}

function arvorezinha2() {
    document.getElementById("nat").innerHTML = 'Segue teu destino, rega tuas plantas, ama as tuas rosas. O resto é sombra de árvores alheias...';

}

function arvorezinha3() {
    document.getElementById("nat").innerHTML = 'As maiores árvores um dia foram apenas sementes...';

}

function arvorezinha4() {
    document.getElementById("nat").innerHTML = 'Devíamos plantar mais árvores!';

}


function arvoremaca1() {
    document.getElementById("nat").innerHTML = 'A lagarta parece estar mais a fim de comer couves agora';

}

function arvoremaca2() {
    document.getElementById("nat").innerHTML = 'Que interessante! Milhões viram a maçã cair mas Newton foi quem perguntou porquê.';

}

function legume1() {
    document.getElementById("nat").innerHTML = 'Isso que é alimentação saudável!';

}

function legume2() {
    document.getElementById("nat").innerHTML = 'Parece que sua lagarta está de olho nas couves';

}

function legume3() {
    document.getElementById("nat").innerHTML = '...';

}

function legume4() {
    document.getElementById("nat").innerHTML = '...';

}

function legume5() {
    document.getElementById("nat").innerHTML = '...';

}

function flor1() {
    document.getElementById("nat").innerHTML = 'É realmente um absurdo eu não poder ser a guardiã do poço!';

}

function flor2() {
    document.getElementById("nat").innerHTML = 'Eu sou uma linda e exótica flor, mas não posso te ajudar.';

}

function flor3() {
    document.getElementById("nat").innerHTML = 'Você está gastando a minha beleza. Com licença! Deixe-me em paz!';

}

function flor4() {
    document.getElementById("nat").innerHTML = 'Estou muito ocupada agora exalando meu perfume. Volte mais tarde!';

}

function flor5() {
    document.getElementById("nat").innerHTML = 'Você está gastando a minha beleza. Com licença! Deixe-me em paz! Arrume outra flor para importunar!';

}

function cocofeliz() {
    document.getElementById("nat").innerHTML = 'Belo adubo!';

}

function couve1() {
    document.getElementById("nat").innerHTML = 'Eu estou precisando de água para fazer a fotossíntese e terminar de me desenvolver!';

}

function couve2() {
    document.getElementById("nat").innerHTML = 'O que a couve perguntou pro Terráqueo perdido? Oi, Terráqueo, quecouve? hahaha';

}

function couve3() {
    document.getElementById("nat").innerHTML = 'Quando eu crescer vou ser a couve mais bonita que você já viu!';

}

function couve4() {
    document.getElementById("nat").innerHTML = 'Oi, meu nome é Brassica e o seu?';

}

function couve5() {
    document.getElementById("nat").innerHTML = 'Me respeite! Eu sou do reino Plantae!';

}

function couve6() {
    document.getElementById("nat").innerHTML = 'É verdade, o nabo e a mostarda são meus primos!';

}

function couve7() {
    document.getElementById("nat").innerHTML = 'Eu sou muito rica, meu bem! Vitamina C é o que não me falta!';

}

function couve8() {
    document.getElementById("nat").innerHTML = 'Eu sou muito rica, meu bem! Vitamina A é o que não me falta!';

}

function couve9() {
    document.getElementById("nat").innerHTML = 'Me respeite! Eu sou do reino Plantae!';

}

function couve10() {
    document.getElementById("nat").innerHTML = 'Olá, muito prazer! Meu nome é Brassica olerácea.';

}

function couve10() {
    document.getElementById("nat").innerHTML = 'Senhor, desculpe-me, hoje não estou a fim de papo!';

}

function couve11() {
    document.getElementById("nat").innerHTML = 'Nossa, está muito quente hoje!';

}

function couve12() {
    document.getElementById("nat").innerHTML = 'Estou precisando dar um UP na minha clorofila!';

}

function couve13() {
    document.getElementById("nat").innerHTML = 'Estou com muita sede...';

}

function couve14() {
    document.getElementById("nat").innerHTML = 'Vá importunar outra couve!';

}

function couve15() {
    document.getElementById("nat").innerHTML = 'Sem água não vai rolar minha fotossíntese hoje...';

}

function couve16() {
    document.getElementById("nat").innerHTML = 'Eu estou morrendo de vontade de incorporar água em meus tecidos!';

}

function couve17() {
    document.getElementById("nat").innerHTML = 'Estou precisando dar um UP na minha clorofila!';

}

function couve18() {
    document.getElementById("nat").innerHTML = 'Minhas organelas hoje estão confusas';

}

function couve19() {
    document.getElementById("nat").innerHTML = 'Ei, Terráqueo, você tem água aí?';

}

function couve20() {
    document.getElementById("nat").innerHTML = 'Por favor, traga-nos água!';

}

function couve21() {
    document.getElementById("nat").innerHTML = 'Olá, muito prazer! Meu nome é Brassica olerácea Junior.';

}

function couve22() {
    document.getElementById("nat").innerHTML = 'Eu sou a mais bonita das couves desse mundo!';

}

function couve23() {
    document.getElementById("nat").innerHTML = 'Estou ansiosa para terminar minha fotossíntese!';

}

function couve24() {
    document.getElementById("nat").innerHTML = 'Eu sou muito rica, meu bem! Vitamina K é o que não me falta!';

}

function couve25() {
    document.getElementById("nat").innerHTML = 'Que horas eu vou poder começar a transformar energia?';

}

function couve26() {
    document.getElementById("nat").innerHTML = 'Vá importunar outra couve! Era só o que me faltava... sem água e sem sossego!';

}

function balde() {
    document.getElementById("nat").innerHTML = 'Você conseguiu um balde, mas ele está vazio. Onde podemos buscar água para regar as plantas?';
    sessionStorage.setItem("balde", "true");
}

function arvore1() {
    document.getElementById("nat").innerHTML = 'Vovó Árvore está muito ocupada hoje';

}

function arvore2() {
    document.getElementById("nat").innerHTML = 'O Árvore Junior não está autorizado a falar com desconhecidos';

}

function arvore3() {
    document.getElementById("nat").innerHTML = 'O seu Árvore falou que o espantalho sabe como conseguir água';

}

function arvore4() {
    document.getElementById("nat").innerHTML = 'Dona Árvore disse que o espantalho sabe como conseguir água';

}

function arvore5() {
    document.getElementById("nat").innerHTML = 'O Árvore Junior não está autorizado a falar com desconhecidos';

}

function arvore6() {
    document.getElementById("nat").innerHTML = 'A senhorita árvore falou que não é difícil conseguir água, basta encontrar o poço';

}

function enxada() {
    document.getElementById("nat").innerHTML = 'Você encontrou uma enxada.';

}

function funcaochapeudejardinagem() {
    document.getElementById("nat").innerHTML = 'Você encontrou os chapéus de jardinagem.';

}

function funcaochapeudejardinagem() {
    document.getElementById("nat").innerHTML = 'Você encontrou os chapéus de jardinagem.';

}

function funcaobotasdejardinagem() {
    document.getElementById("nat").innerHTML = 'Você encontrou as botas de jardinagem.';

}

function couveflor1() {
    document.getElementById("nat").innerHTML = 'Sua lagarta prefere couve a couve-flor';

}

function couveflor2() {
    document.getElementById("nat").innerHTML = 'As folhas de couve já foram colhidas por aqui, só sobrou a inflorescência';

}

function couveflor3() {
    document.getElementById("nat").innerHTML = 'Estou com sede!';

}

function couveflor4() {
    document.getElementById("nat").innerHTML = 'As folhas de couve já foram colhidas por aqui, só sobrou a inflorescência';

}

function couveflor5() {
    document.getElementById("nat").innerHTML = 'A Flor guardiã do poço sabe onde encontrar água!';

}

function couveflor6() {
    document.getElementById("nat").innerHTML = 'Sua lagarta prefere couve a couve-flor';

}

function couveflor7() {
    document.getElementById("nat").innerHTML = 'As folhas de couve já foram colhidas por aqui, só sobrou a inflorescência';

}

function couveflor8() {
    document.getElementById("nat").innerHTML = 'Que couve-flor mais simpática!';

}

function couveflor9() {
    document.getElementById("nat").innerHTML = 'As folhas de couve já foram colhidas por aqui, só sobrou a inflorescência';

}

function couveflor10() {
    document.getElementById("nat").innerHTML = 'As folhas de couve já foram colhidas por aqui, só sobrou a inflorescência';

}

function alface1() {
    document.getElementById("nat").innerHTML = 'A alface está bem bonita.';

}

function alface2() {
    document.getElementById("nat").innerHTML = 'Muito prazer em conhecê-lo, meu nome é Lactuca!';

}

function alface3() {
    document.getElementById("nat").innerHTML = 'Muito prazer em conhecê-lo. Pode me chamar de alface-repolhuda!';

}

function alface4() {
    document.getElementById("nat").innerHTML = 'A alface está bem bonita.';

}

function alface5() {
    document.getElementById("nat").innerHTML = 'Sua lagarta prefere couve a alface!';

}

function alface6() {
    document.getElementById("nat").innerHTML = 'Tenho vitaminas, proteínas e minerais! Sou ótima!';

}

function alface7() {
    document.getElementById("nat").innerHTML = 'Eu sou a mais bela alface desta plantação!';

}

function alface8() {
    document.getElementById("nat").innerHTML = 'A alface está bem bonita.';
}

function plantacarnivora() {
    sessionStorage.setItem("plantacarnivora", "true");
    if (sessionStorage.getItem("balde") !== null && sessionStorage.getItem("espantalho") !== null) {
        // espantalho e balde ativos
        // alert("espantalho e balde ativos");
        textofala4();
    }
    if (sessionStorage.getItem("balde") === null && sessionStorage.getItem("espantalho") !== null) {
        //espantalho sem balde
        // alert("espantalho sem balde");
        textofala3();
    }
    if (sessionStorage.getItem("balde") !== null && sessionStorage.getItem("espantalho") === null) {
        //sem espantalho com balde
        // alert("sem espantalho com balde");
        textofala4();
    }
    if (sessionStorage.getItem("balde") === null && sessionStorage.getItem("espantalho") === null) {
        // alert("sem espantalho sem balde");
        textofala1();
        //sem espantalho sem balde
    }


}

function espantalho() {
    sessionStorage.setItem("espantalho", "true");
    //||sessionStorage.getItem("espantalho")=='true'
    if (sessionStorage.getItem("plantacarnivora") !== null) {
        txespantalho2();
    } else {
        txespantalho();
    }
}
var ponteiro1 = -1;
var vetortexto1 = [{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Olá, Terráqueo, muito prazer! Meu nome é Dioneia." },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Estou muito feliz por você ter me procurado. Significa que você é uma pessoa que não liga para estereótipos." },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Algumas pessoas têm medo de mim. Acham que sou malvada e que como pessoas, mas isso não é verdade." },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Eu sou uma planta carinhosa, gentil e sou a guardiã do poço. " },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: E justamente sou a guardiã do poço para confundir pessoas que nunca se aproximariam de mim por medo. " },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Você pensou de um jeito diferente, por isso, te mostrarei onde está o poço para que você termine de regar as couves para sua lagarta." },
{ "texto": "trocatexto", "valor": "PEDRINHO: Legal, Dioneia. Valeu mesmo!" },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Você precisa de um balde para pegar água do poço." },
{ "texto": "proximo", "valor": "./fasecenarios.html" }
];


var ponteiro2 = -1;
var vetortexto2 = [{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Olá, Terráqueo, muito prazer! Meu nome é Dioneia." },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Estou muito feliz por você ter me procurado. Significa que você é uma pessoa que não liga para estereótipos." },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Algumas pessoas têm medo de mim. Acham que sou malvada e que como pessoas, mas isso não é verdade." },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Eu sou uma planta carinhosa, gentil e sou a guardiã do poço. " },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: E justamente sou a guardiã do poço para confundir pessoas que nunca se aproximariam de mim por medo. " },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Você pensou de um jeito diferente, por isso, te mostrarei onde está o poço para que você termine de regar as couves para sua lagarta." },
{ "texto": "trocatexto", "valor": "PEDRINHO: Legal, Dioneia. Valeu mesmo!" },
{ "texto": "proximo", "valor": "./fasecenarios.html" }
];




var ponteiro3 = -1;
var vetortexto3 = [{ "texto": "trocatexto", "valor": "ESPANTALHO: Fala aí, Terráqueo. Beleza?" },
{ "texto": "trocatexto", "valor": "PEDRINHO: Olá, espantalho! Você pode me falar então onde eu consigo água? Preciso regar as couves." },
{ "texto": "trocatexto", "valor": "ESPANTALHO: Oh! É claro! Existe um grande poço com muita água, você pode ir lá buscar." },
{ "texto": "trocatexto", "valor": "PEDRINHO: Não vi nenhum poço por aqui. Onde ele está? " },
{ "texto": "trocatexto", "valor": "ESPANTALHO: Está sob os cuidados da guardiã da horta." },
{ "texto": "trocatexto", "valor": "PEDRINHO: E quem é a guardiã da horta?" },
{ "texto": "trocatexto", "valor": "ESPANTALHO: A Flor mais antiga, poderosa e gentil da horta. Ela é uma fofa e cuida de todos nós com muito amor. Sempre nos protege dos invasores hostis. É uma planta exuberante, de uma beleza estonteante!" },
{ "texto": "trocatexto", "valor": "PEDRINHO: Valeu, espantalho! Vou procurar essa Flor!" },
{ "texto": "proximo", "valor": "./fasecenarios.html" }
];







var ponteiro4 = -1;
var vetortexto4 = [{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Você chegou até aqui e você está com um balde!" },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Vou te mostrar onde está o poço para que você regue as couves e alimente sua lagarta." },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Veja!" },
{ "texto": "trocaimagem", "valor": "./fundos/plantacarnivoracompoco.png" },
{ "texto": "trocatexto", "valor": "PLANTA CARNÍVORA: Legal. A água que você pegou no poço foi essencial para o desenvolvimento das couves." },
{ "texto": "trocatexto", "valor": "PLANTA CARNIVORA: Elas cresceram rápido e estão bem verdinhas. Sua lagarta vai adorar escolher uma para se alimentar." },
{ "texto": "proximo", "valor": "./couves.html" }
];



function textofala1() {
    if (vetortexto1.length > ponteiro1) {
        ponteiro1++;
        if (vetortexto1[ponteiro1].texto == 'proximo') {
            proximapagina(vetortexto1[ponteiro1].valor);
        }
        if (vetortexto1[ponteiro1].texto == 'trocaimagem') {
            trocacena(vetortexto1[ponteiro1].valor);
            document.getElementById("nat").innerHTML = "";
        }
        if (vetortexto1[ponteiro1].texto == 'trocatexto') {
            document.getElementById("nat").innerHTML = vetortexto1[ponteiro1].valor;
            document.getElementById("nat").innerHTML += "<input type=\"image\"   class=\"js-open-modal\" id=\"botao2\"  src=\"./botoes/botaoavancar2.png\" width=\”5px\” height=\”5px\” onclick='textofala1();'/>";
        }
    }
}

function textofala2() {
    if (vetortexto2.length > ponteiro2) {
        ponteiro2++;
        if (vetortexto2[ponteiro2].texto == 'proximo') {
            proximapagina(vetortexto2[ponteiro2].valor);
        }
        if (vetortexto2[ponteiro2].texto == 'trocaimagem') {
            trocacena(vetortexto2[ponteiro2].valor);
            document.getElementById("nat").innerHTML = "";
        }
        if (vetortexto2[ponteiro2].texto == 'trocatexto') {
            document.getElementById("nat").innerHTML = vetortexto2[ponteiro2].valor;
            document.getElementById("nat").innerHTML += "<input type=\"image\"   class=\"js-open-modal\" id=\"botao2\"  src=\"./botoes/botaoavancar2.png\" width=\”5px\” height=\”5px\” onclick='textofala2();'/>";
        }
    }
}

function textofala3() {
    if (vetortexto3.length > ponteiro3) {
        ponteiro3++;
        if (vetortexto3[ponteiro3].texto == 'proximo') {
            proximapagina(vetortexto3[ponteiro3].valor);
        }
        if (vetortexto3[ponteiro3].texto == 'trocaimagem') {
            trocacena(vetortexto3[ponteiro3].valor);
            document.getElementById("nat").innerHTML = "";
        }
        if (vetortexto3[ponteiro3].texto == 'trocatexto') {
            document.getElementById("nat").innerHTML = vetortexto3[ponteiro3].valor;
            document.getElementById("nat").innerHTML += "<input type=\"image\"   class=\"js-open-modal\" id=\"botao2\"  src=\"./botoes/botaoavancar2.png\" width=\”5px\” height=\”5px\” onclick='textofala3();'/>";
        }
    }
}

function textofala4() {
    if (vetortexto4.length > ponteiro4) {
        ponteiro4++;
        if (vetortexto4[ponteiro4].texto == 'proximo') {
            proximapagina(vetortexto4[ponteiro4].valor);
        }
        if (vetortexto4[ponteiro4].texto == 'trocaimagem') {
            trocacena(vetortexto4[ponteiro4].valor);
            document.getElementById("nat").innerHTML = "";
            textofala4();
        }
        if (vetortexto4[ponteiro4].texto == 'trocatexto') {
            document.getElementById("nat").innerHTML = vetortexto4[ponteiro4].valor;
            document.getElementById("nat").innerHTML += "<input type=\"image\"   class=\"js-open-modal\" id=\"botao2\"  src=\"./botoes/botaoavancar2.png\" width=\”5px\” height=\”5px\” onclick='textofala4();'/>";
        }
    }
}




var pestantalho = -1;
var vestantalho = [{ "texto": "trocatexto", "valor": "ESPANTALHO: Fala aí, Terráqueo. Beleza?" },
{ "texto": "trocatexto", "valor": "PEDRINHO: Olá, espantalho! Você pode me falar então onde eu consigo água? Preciso regar as couves." },
{ "texto": "trocatexto", "valor": "ESPANTALHO: Oh! É claro! Existe um grande poço com muita água, você pode ir lá buscar." },
{ "texto": "trocatexto", "valor": "PEDRINHO: Não vi nenhum poço por aqui. Onde ele está? " },
{ "texto": "trocatexto", "valor": "ESPANTALHO: Está sob os cuidados da guardiã da horta." },
{ "texto": "trocatexto", "valor": "PEDRINHO: E quem é a guardiã da horta?" },
{ "texto": "trocatexto", "valor": "ESPANTALHO: A Flor mais antiga, poderosa e gentil da horta. Ela é uma fofa e cuida de todos nós com muito amor. Sempre nos protege dos invasores hostis. É uma planta exuberante, de uma beleza estonteante!" },
{ "texto": "trocatexto", "valor": "PEDRINHO: Valeu, espantalho! Vou procurar essa Flor!" },
{ "texto": "nada", "valor": "" }
];

function txespantalho() {
    if (vestantalho.length > pestantalho) {
        pestantalho++;
        if (vestantalho[pestantalho].texto == 'trocaimagem') {
            trocacena(vestantalho[pestantalho].valor);
            document.getElementById("nat").innerHTML = "";
        }
        if (vestantalho[pestantalho].texto == 'trocatexto') {
            document.getElementById("nat").innerHTML = vestantalho[pestantalho].valor;
            document.getElementById("nat").innerHTML += "<input type=\"image\"   class=\"js-open-modal\" id=\"botao2\"  src=\"./botoes/botaoavancar2.png\" width=\”5px\” height=\”5px\” onclick='txespantalho();'/>";
        }
    }
}

var pestantalho2 = -1;
var vestantalho2 = [{ "texto": "trocatexto", "valor": "ESPANTALHO: Fala aí, Terráqueo. Beleza?" },
{ "texto": "trocatexto", "valor": "PEDRINHO: Oi, espantalho. Estou com dificuldade de conseguir água pra regar as couves." },
{ "texto": "trocatexto", "valor": "ESPANTALHO: Eu vi você falando com a Dioneia. Ela deve ter falado sobre o poço." },
{ "texto": "trocatexto", "valor": "PEDRINHO: Sim, mas eu preciso de um balde pra pegar a água. " },
{ "texto": "trocatexto", "valor": "ESPANTALHO: Eu vi um balde pertinho das couves. Vai lá buscar!" },
{ "texto": "trocatexto", "valor": "PEDRINHO: Valeu, espantalho. Já estou indo!" },
{ "texto": "nada", "valor": "" }
];

function txespantalho2() {
    if (vestantalho2.length > pestantalho2) {
        pestantalho2++;
        if (vestantalho2[pestantalho2].texto == 'trocaimagem') {
            trocacena(vetortexto2[pestantalho].valor);
            document.getElementById("nat").innerHTML = "";
        }
        if (vestantalho2[pestantalho2].texto == 'trocatexto') {
            document.getElementById("nat").innerHTML = vestantalho2[pestantalho2].valor;
            document.getElementById("nat").innerHTML += "<input type=\"image\"   class=\"js-open-modal\" id=\"botao2\"  src=\"./botoes/botaoavancar2.png\" width=\”5px\” height=\”5px\” onclick='txespantalho2();'/>";
        }
    }
}
