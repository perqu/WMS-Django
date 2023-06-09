var loginBtn = document.getElementById("login-button");
var loginWindow = document.getElementById("login-window");
var closeBtn = document.getElementsByClassName("close")[0];

loginBtn.onclick = function() {
    loginWindow.style.display = "block";
}

closeBtn.onclick = function() {
    loginWindow.style.display = "none";
}
/*
window.onclick = function(event) {
    if (event.target == loginWindow) {
        loginWindow.style.display = "none";
    }
}
*/