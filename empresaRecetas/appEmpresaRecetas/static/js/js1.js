
document.addEventListener("DOMContentLoaded", function() {
    alert("Bienvenido a nuestra web Gestor de Recetas");
});


document.addEventListener("DOMContentLoaded", function() {
    var botonForm = document.getElementById("irFormulario");

    botonForm.addEventListener("click", function() {
        window.location.href = "{% url 'registrar' %}";
    });
});