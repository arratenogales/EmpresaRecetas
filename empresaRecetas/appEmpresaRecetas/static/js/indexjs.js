function agregarComentario() {
    var correo = document.getElementById('correoq').value;
    var comentario = document.getElementById('comentarioq').value;

    if (correo.trim() === '' || comentario.trim() === '') {
      alert('Por favor, ingrese tanto el correo como el comentario.');
      return;
    }

    var nuevoComentario = document.createElement('p');
    nuevoComentario.innerHTML = '<strong>' + correo + ':</strong> ' + comentario +'<em> (Este comentario esta aun pendiente de revisar y aceptar por el sistema)</em> ';

    document.getElementById('comentarios2').appendChild(nuevoComentario);
    document.getElementById('correoq').value = '';
    document.getElementById('comentarioq').value = '';
    
    nuevocom={
      correo:correo,comentario:comentario
    }
    
    
  }

  
