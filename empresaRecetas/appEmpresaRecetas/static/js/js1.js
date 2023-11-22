

document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("irFormulario");

    form.addEventListener("click", function() {
        window.location.href = "/registrar/";
    });
});



document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("irDatos");

    form.addEventListener("click", function() {
        window.location.href = "/iniciar/";
    });
});



document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("irPortada");

    form.addEventListener("click", function() {
        window.location.href = "{% url 'portada' %}";
    });
});


document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("btnRegis");

    form.addEventListener("click", function() {
        window.location.href = "{% url 'portada' %}";

    });

});


document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("registro");

    form.addEventListener("submit", function() {
        var aceptar = form.elements["Accept"].checked;

        if (!aceptar) {
            alert("Debes aceptar las condiciones para registrarte.");

        }else{
            window.location.href = "{% url 'portada' %}";
        }
        


    });
});



alert("Datos incorrectos. Por favor, inténtelo de nuevo.");
window.location.href = "{% url 'iniciar_sesion' %}";