var thumbs = document.querySelectorAll('#thumbs img');
  thumbs.forEach(function(thumb) {
    thumb.addEventListener('click', function() {
        alert("Bienvenido a nuestra web Gestor de Recetas");
        document.getElementById('imagen-seleccionada').src = this.src;
    });
  });



document.addEventListener("DOMContentLoaded", function() {
    alert("Bienvenido a nuestra web Gestor de Recetas");
});
