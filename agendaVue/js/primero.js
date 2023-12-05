var appVue = new Vue({
    el: '#app-1',
    data: {
      state: 'default',
      header: 'AgendaVue',
      nuevoContacto: {
        name: '',
        email: '',
        phone: ''
      },
      contactos: [
        {
          name: 'Arrate Nogales',
          email: 'arrate@gmail.com',
          phone: '678-456-213'
        }
      ] 
    },
    computed: {
      contactCount() {
        return this.contactos.length;
      }
    },
    methods: {
      aniadirContacto: function (contact) {
        console.log('Añadiendo contacto:', contact);
    
        this.contactos.push({
          name: contact.name,
          email: contact.email,
          phone: contact.phone
        });
        this.nuevoContacto = { name: '', email: '', phone: '' };
      },

      removeContact: function(contact) {
        const index = this.contactos.indexOf(contact);
        if (index !== -1) {
          this.contactos.splice(index, 1);
        }      
      }
    }
  });
  