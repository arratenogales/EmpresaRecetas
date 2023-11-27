function agregarComentario() {
    var correo = document.getElementById('correo').value;
    var comentario = document.getElementById('comentario').value;

    if (correo.trim() === '' || comentario.trim() === '') {
      alert('Por favor, ingrese tanto el correo como el comentario.');
      return;
    }

    var nuevoComentario = document.createElement('p');
    nuevoComentario.innerHTML = '<strong>' + correo + ':</strong> ' + comentario;

  
    document.getElementById('comentarios').appendChild(nuevoComentario);

    document.getElementById('correo').value = '';
    document.getElementById('comentario').value = '';
  }