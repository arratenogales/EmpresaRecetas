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
    
    nuevocom={
      correo:correo,comentario:comentario
    }
    
    fetch('/agregar_comentario/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(nuevocom)
  })
  .then(response => response.json())
  .then(data => {
      alert(data.mensaje);
  })
  .catch(error => {
      console.error('Error:', error);
  });
  }

  
  
  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

