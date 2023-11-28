


document.addEventListener("DOMContentLoaded", function() {
    var formulario = document.getElementById('irFormulario');

    var aceptar = document.getElementById('accept');
    var enviarBoton = document.getElementById('btnRegis');

    if (enviarBoton && aceptar) {
        enviarBoton.disabled = !aceptar.checked;

        aceptar.addEventListener('change', function() {
            enviarBoton.disabled = !aceptar.checked;
        });

        enviarBoton.addEventListener('click', function() {
            alert("Pregunta enviada.");

        });
    }
});

