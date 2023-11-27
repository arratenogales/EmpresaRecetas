document.addEventListener('DOMContentLoaded', function() {
    alert("Bienvenido a nuestra web Gestor de Recetas");
    var thumbs = document.querySelectorAll('#thumbs img');
    thumbs.forEach(function(thumb) {
      thumb.addEventListener('click', function() {
        variable= document.getElementById('imagen-seleccionada').src;
        document.getElementById('imagen-seleccionada').src = this.src;
        this.src=variable;
      });
    });
  });




