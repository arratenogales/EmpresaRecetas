document.addEventListener('DOMContentLoaded', function() {
  alert("Bienvenido a nuestra web Gestor de Recetas");

  var thumbs = document.querySelectorAll('#thumbs img');

  var recetaElement = document.getElementById('receta');
  
  thumbs.forEach(function(thumb) {
    thumb.addEventListener('click', function() {
      var variable= document.getElementById('imagen-seleccionada').src;
      var variable2= document.getElementById('imagen-seleccionada').alt;
      document.getElementById('imagen-seleccionada').src = this.src;
      recetaElement.textContent = this.alt;
      this.src=variable;

      document.getElementById('imagen-seleccionada').alt=this.alt;
      this.alt=variable2;
      
    });
  });
});




