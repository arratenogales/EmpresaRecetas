

document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("irFormulario");

    form.addEventListener("click", function() {
        window.location.href = "/registrar/";
    });
});


document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("registro");

    form.addEventListener("submit", function() {
        var aceptar = form.elements["Accept"].checked;

        if (!aceptar) {
            alert("Debes aceptar las condiciones para registrarte.");
            return false; 
        }

        return true; 
    });
});