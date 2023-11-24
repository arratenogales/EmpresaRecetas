


document.addEventListener("DOMContentLoaded", function() {
    var formulario = document.getElementById('irFormulario');

    var aceptar = document.getElementById('Accept');
    var enviarBoton = document.getElementById('btnRegis');

    if (enviarBoton && aceptar) {
        enviarBoton.disabled = !aceptar.checked;

        aceptar.addEventListener('change', function() {
            enviarBoton.disabled = !aceptar.checked;
        });

        enviarBoton.addEventListener('click', function() {
            alert("Usuario registrado con éxito.");

        });
    }
});


document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("irDatos");

    form.addEventListener("click", function() {
        window.location.href = "/iniciar/";
    });
});