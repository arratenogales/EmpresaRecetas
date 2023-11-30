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
    
    if (correo && comentario) {
      const nuevoComentario = new ComentarioModelo(correo, comentario);
      
    }
  }

