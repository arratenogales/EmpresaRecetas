function agregarComentario() {
    var correo = document.getElementById('correo').value;
    var comentario = document.getElementById('comentario').value;

    if (correo.trim() === '' || comentario.trim() === '') {
      alert('Por favor, ingrese tanto el correo como el comentario.');
      return;
    }

    var nuevoComentario = document.createElement('p');
    nuevoComentario.innerHTML = '<strong>' + correo + ':</strong> ' + comentario +'<em> (Este comentario esta aun pendiente de revisar y aceptar por el sistema)</em> ';

    document.getElementById('comentarios').appendChild(nuevoComentario);
    document.getElementById('correo').value = '';
    document.getElementById('comentario').value = '';
  }


function toggleComentarios() {
    var comentariosDiv = document.getElementById("comentarios2");
    var boton = document.getElementById("comentarios2");

    if (comentariosDiv.style.display === "none") {
      comentariosDiv.style.display = "block";
      boton.textContent = "Ocultar Comentarios";
    } else {
      comentariosDiv.style.display = "none";
      boton.textContent = "Mostrar Comentarios";
    }
  }