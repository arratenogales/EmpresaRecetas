/*
import Vue from 'vue';
import VueFire from 'vuefire';
import firebase from 'firebase/app';
import 'firebase/firestore';
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

Vue.use(VueFire);


// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCsf9zaLGWRe736BShZhykIAAB4Raspw34",
  authDomain: "agendaiw-844ec.firebaseapp.com",
  projectId: "agendaiw-844ec",
  storageBucket: "agendaiw-844ec.appspot.com",
  messagingSenderId: "326430926225",
  appId: "1:326430926225:web:0a7385f09590fd64d66630",
  measurementId: "G-ETLB3WD40V"
};

firebase.initializeApp(firebaseConfig);
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
// Obtiene una instancia de Firestore
const db = firebase.firestore();

// Agrega la instancia de Firestore a Vue como $firestore
Vue.prototype.$firestore = db;
*/
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
    /*
    firestore: {
      contactos: db.collection('contactos'),
    },*/
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
  