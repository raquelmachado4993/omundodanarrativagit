//desabilitar colar no textarea
$(document).ready(function() {

$("#note").bind('paste', function(e) {
    e.preventDefault();
});


    // Initialize a new plugin instance for all
    // e.g. $('input[type="range"]') elements.
    $('input[type="range"]').rangeslider();

    // Destroy all plugin instances created from the
    // e.g. $('input[type="range"]') elements.
    $('input[type="range"]').rangeslider('destroy');

    // Update all rangeslider instances for all
    // e.g. $('input[type="range"]') elements.
    // Usefull if you changed some attributes e.g. `min` or `max` etc.
    $('input[type="range"]').rangeslider('update', true);

    $(document).ready(function(){
    $("#enviar").hide();  
    $("#imageURL").on("change", function(){
        $("#enviar").show();  
    })
});
