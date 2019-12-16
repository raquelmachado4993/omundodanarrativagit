$(document).ready(function (c) {
	$('.alert-close').on('click', function (c) {
		$('.message').fadeOut('slow', function (c) {
			$('.message').remove();
		});
	});
});


function voltar() {
	sessionStorage.clear();
	location.href = "index.html";
}
function entrar() {
	sessionStorage.clear();
//	alert("Sistema temporariamente indisponível. Tente novamente mais tarde.");
	// assim funciona muito SVGFEFuncBElement, seria legal usar isso para tudo


	if (($('#login').val()) || ($('#senha').val())) {
	//alert("aqui");
		var Login = new Object();
		Login.login = $('#login').val();
		Login.senha = $('#senha').val();
		var opcao = "cadUsu";
		var jsonLogin = JSON.stringify(Login);
		$.post('./php/servlet.php', { jsonLogin: jsonLogin, opcao: opcao }, function (responseText) {
		//	alert(responseText);
			var obj = JSON.parse(responseText);
			if (obj.tipo != "true") {
				alert("Falha na autenticação. Favor conferir suas credenciais.");
				location.href = obj.url;
			} else {
				sessionStorage.setItem("pessoa", obj.pessoa);
				location.href = obj.url;
			}
		});
	} else {
		alert("preencha os campos");
	}


}