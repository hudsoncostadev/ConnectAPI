<template>
  <div>
    <h1>Busca de Operadoras</h1>
    <button @click="buscarOperadoras">Buscar Operadoras</button>
    <ul v-if="operadoras.length">
      <li v-for="operadora in operadoras" :key="operadora.cnpj">
        <strong>Nome Fantasia:</strong> {{ operadora.nome_fantasia }}<br>
        <strong>CNPJ:</strong> {{ operadora.cnpj }}<br>
        <strong>Razão Social:</strong> {{ operadora.razao_social }}
      </li>
    </ul>
    <p v-if="!operadoras.length">Clique no botão para carregar as operadoras.</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      operadoras: [] // Lista para armazenar os dados da API
    }
  },
  methods: {
    async buscarOperadoras() {
      try {
        console.log('Enviando requisição para API...')
        const response = await axios.get('http://127.0.0.1:5000/api/operadoras');
        console.log('Resposta da API:', response.data);
        this.operadoras = response.data; // Armazenar os dados recebidos
      } catch (error) {
        console.error('Erro ao buscar operadoras:', error);
        alert('Erro ao carregar as operadoras.');
      }
    }
  }
}
</script>

<style>
h1 {
  font-family: Arial, sans-serif;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 10px 0;
}
</style>
