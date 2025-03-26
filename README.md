O projeto consiste no desenvolvimento de uma aplicação integrada entre frontend e backend para consulta de operadoras ativas. O objetivo é criar uma interface amigável e funcional que permita aos usuários visualizar informações importantes, como nome fantasia, CNPJ e razão social das operadoras registradas.

Principais Componentes do Projeto:

Backend (Flask):

Desenvolvido em Python com Flask, o backend é responsável por acessar o banco de dados e fornecer os dados das operadoras através de um endpoint RESTful (/api/operadoras).

Suporte a CORS foi configurado para permitir o consumo da API a partir de aplicações externas.

A estrutura do backend garante o retorno dos dados no formato JSON, otimizando o consumo pelo frontend.

Frontend (Vue.js):

Utilizando Vue.js, o frontend oferece uma interface moderna e responsiva para exibir as informações das operadoras.

O layout foi projetado com uma abordagem intuitiva, utilizando botões para interação e apresentação dos dados em cartões estilizados.

O Axios é utilizado para conectar a aplicação ao backend, permitindo chamadas HTTP eficientes.

Banco de Dados:

Os dados das operadoras são armazenados em uma tabela chamada operadoras_ativas, contendo informações como nome fantasia, CNPJ e razão social.

Consultas SQL são otimizadas para retornar apenas os registros relevantes, limitando a quantidade de resultados.

Objetivos do Projeto:

Demonstrar a integração entre uma API RESTful e uma interface de usuário.

Facilitar a consulta e visualização de dados em tempo real.

Fornecer um exemplo funcional de uma aplicação completa para aprendizado ou demonstração.

Tecnologias Utilizadas:

Frontend: Vue.js, HTML, CSS e JavaScript (Axios para requisições HTTP).

Backend: Python, Flask e Flask-CORS.

Banco de Dados: PostgreSQL para armazenamento e gerenciamento de dados.

EndFragment
## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```
