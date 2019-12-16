var applied = localStorage.getItem("applied") == "true";
if (applied){
	var timeInMs = Date.now();
	var url_css = "wp-content/themes/ufsm/css/contraste.css?Ver="+timeInMs;
	var lnk = document.createElement('link');
	lnk.setAttribute('type', "text/css" );
	lnk.setAttribute('rel', "stylesheet" );
	lnk.setAttribute('id', "contraste" );
	lnk.setAttribute('href', url_css );  
  jQuery('body').addClass('contraste');
	document.getElementsByTagName("head").item(0).appendChild(lnk);
	// jQuery(".brasaoUFSM").attr('src', '/wp-content/themes/ufsm/images/brasao_branco.png');
} else {
	if(jQuery("body").hasClass("contraste")){
		jQuery('body').removeClass('contraste');
        jQuery("#contraste").remove();
				// jQuery(".brasaoUFSM").attr('src', '/wp-content/themes/ufsm/images/brasao_ufsm.png');
	}
}

function contraste(){
	if(!applied){
		var timeInMs = Date.now();
		var url_css = "wp-content/themes/ufsm/css/contraste.css?Ver="+timeInMs;
		var lnk = document.createElement('link');
		lnk.setAttribute('type', "text/css" );
		lnk.setAttribute('rel', "stylesheet" );
		lnk.setAttribute('id', "contraste" );
		lnk.setAttribute('href', url_css );  
        jQuery('body').addClass('contraste');
		document.getElementsByTagName("head").item(0).appendChild(lnk);
		// jQuery(".brasaoUFSM").attr('src', '/wp-content/themes/ufsm/images/brasao_branco.png');
		applied = true;
	} else { 
		if(jQuery("body").hasClass("contraste")){
			jQuery('body').removeClass('contraste');
					jQuery("#contraste").remove();
					// jQuery(".brasaoUFSM").attr('src', '/wp-content/themes/ufsm/images/brasao_ufsm.png');
		}
		applied = false;
	}
	localStorage.setItem("applied", applied);
}



