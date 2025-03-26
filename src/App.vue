<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import BuscaOperadora from "./components/BuscaOperadora.vue";


</script>

<!--<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
      </div>
      </header>
      
      <main>
        <TheWelcome />
        </main>
        </template> -->


        <template>
          <div id="app">
            <h1>Lista de Operadoras</h1>
            <button @click="buscarOperadoras">Buscar Operadoras</button>
            <ul v-if="operadoras.length">
              <li v-for="operadora in operadoras" :key="operadora.cnpj">
                <strong>Nome Fantasia:</strong> {{ operadora.nome_fantasia }}<br>
                <strong>CNPJ:</strong> {{ operadora.cnpj }}<br>
                <strong>Razão Social:</strong> {{ operadora.razao_social }}
              </li>
            </ul>
            <p v-else>Clique no botão para carregar as operadoras.</p>
          </div>
        </template>
        
        <script>
        import axios from 'axios';
        
        export default {
          data() {
            return {
              operadoras: [] // Armazena os dados recebidos da API
            };
          },
          methods: {
            async buscarOperadoras() {
              try {
                console.log('Buscando operadoras...');
                const response = await axios.get('http://127.0.0.1:5000/api/operadoras');
                this.operadoras = response.data; // Salva os dados no estado
                console.log('Dados recebidos:', this.operadoras);
              } catch (error) {
                console.error('Erro ao buscar dados da API:', error);
                alert('Não foi possível carregar as operadoras.');
              }
            }
          }
        };
        </script>
        
        <style>
        #app {
          font-family: Avenir, Helvetica, Arial, sans-serif;
          text-align: center;
          margin-top: 20px;
        }
        </style>
        

<style scoped>
/* Estilo global */
body {
  margin: 0;
  font-family: 'Roboto', sans-serif;
  background-color: #f4f4f9; /* Fundo claro */
  color: #333; /* Texto padrão */
}

/* Estilo do container principal */
#app {
  text-align: center;
  margin: 20px auto;
}

h1 {
  font-size: 2.5rem;
  color: #4CAF50;
  margin-bottom: 10px;
}

button {
  background-color: #4CAF50;
  color: white;
  font-size: 1rem;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #45a049;
}

/* Lista de operadoras */
.operadoras-list {
  list-style-type: none;
  padding: 0;
  margin: 20px auto;
  max-width: 600px;
}

.operadoras-list li {
  background-color: white;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;
  text-align: left;
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}

.operadoras-list li:hover {
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.15);
  transform: translateY(-3px);
}

strong {
  font-size: 1.2rem;
  color: #4CAF50;
}

.no-data {
  font-size: 1rem;
  color: #888;
}

</style>
