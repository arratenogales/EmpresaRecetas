


document.addEventListener("DOMContentLoaded", function() {
    var formulario = document.getElementById('miFormulario');

    var aceptar = document.getElementById('accept');
    var enviarBoton = document.getElementById('btnRegis');

    if (enviarBoton && aceptar) {
        enviarBoton.disabled = !aceptar.checked;

        aceptar.addEventListener('change', function() {
            enviarBoton.disabled = !aceptar.checked;
        });

        enviarBoton.addEventListener('click', function() {
            console.log("Botón de envío clicado");

            if (aceptar.checked) {
                console.log("Enviando formulario...");

                formulario.submit();
            } else {
                alert("Debes aceptar las condiciones para enviar el formulario.");
            }
        });
    }
});

