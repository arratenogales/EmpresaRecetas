

document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("irFormulario");

    form.addEventListener("click", function() {
        window.location.href = "{% url 'registrar' %}";
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
    var form = document.getElementById("volver");

    form.addEventListener("click", function() {
        var url = form.dataset.url;
        window.location.href = url;
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

