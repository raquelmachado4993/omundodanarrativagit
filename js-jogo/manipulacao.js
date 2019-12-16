
function teste(){
    $.GET("/session-storage.php").success(function(response){
        sessionStorage.setItem("data", response);
    });
}