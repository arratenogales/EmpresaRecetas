new Vue({
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
        },
        {
          name: 'Ane San Juan',
          email: 'ane@gmail.com',
          phone: '622-699-847'
        },
        {
          name: 'Aitziber Luis',
          email: 'aitziber@gmail.com',
          phone: '658-636-219'
        },
        {
          name: 'Marina Villanueva',
          email: 'marina@gmail.com',
          phone: '615-893-861'
        }
      ] 
    },
    computed: {
      contactCount() {
        return this.contactos.length;
      }
    },
    /* */ 
    firestore: {
      contactos: db.collection('contactos'),
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
      changeState: function (newState) {
        this.state = newState;
      },

      removeContact: function(contact) {
        const index = this.contactos.indexOf(contact);
        if (index !== -1) {
          this.contactos.splice(index, 1);
        }      
      }
    }
  });