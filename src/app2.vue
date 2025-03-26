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
