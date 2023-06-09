document.getElementById("login-window").addEventListener("submit", function(event) {
    event.preventDefault();
    var form = this.querySelector("form");
    var formData = new FormData(form);
    var xhr = new XMLHttpRequest();
    xhr.open(form.method, form.action);
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    xhr.onload = function() {
        if (xhr.status === 200) {
            var redirectUrl = xhr.getResponseHeader("X-Redirect");  // Odczytanie nagłówka "X-Redirect" z przekierowaniem
            if (redirectUrl) {
                window.location.href = redirectUrl;  // Przekierowanie na poprzednią stronę
            } else {
                window.location.reload();
            }
        } 
        else {
            loginWindow.style.display = "block";
            var loginContent = document.getElementById("login-content");
            loginContent.style.height = "430px"
            var errorContainer = document.getElementById("error-container");
            errorContainer.style.display = "block"
            errorContainer.textContent = "Nieprawidłowa nazwa uzytkownika lub haslo.";
        }
    };
    xhr.send(formData);
  });