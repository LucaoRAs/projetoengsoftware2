
# Sistema de Cadastro de Exames 🩺

Este repositório contém um sistema web para cadastro, agendamento e gerenciamento de exames médicos. O projeto foi desenvolvido como parte da disciplina de **Engenharia de Software II**, do curso de **Sistemas de Informação** da **Faculdade Libertas – Faculdades Integradas de São Sebastião do Paraíso (MG), Brasil**.

## 👨‍💻 Integrantes do Projeto

- **Lucas Rafael Avelino de Souza**
- **Thiago Francisco dos Reis Marcolino**
- **Cristian Biasi**

## 🎯 Objetivo

Criar um sistema simples e funcional que permita:

- Gerenciar exames médicos.
- Realizar cadastros, alterações, exclusões e visualizações (CRUD).
- Agendar exames por data e hora.
- Autenticar usuários com sistema de login.

## ⚙️ Funcionalidades

- Login e autenticação de usuários.
- Cadastro de novos exames.
- Agendamento com data e hora.
- Listagem de exames cadastrados.
- Edição e exclusão de registros.

## 🛠️ Tecnologias Utilizadas

- **Back-end:** Python com Flask
- **Banco de Dados:** MySQL
- **Front-end:** HTML, CSS, JavaScript e Bootstrap
- **Ambiente Virtual:** venv (Python)

## ▶️ Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/LucaoRAs/engenhariadesoftwareII.git
   ```

2. **Acesse o diretório:**
   ```bash
   cd engenhariadesoftwareII
   ```

3. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # No Windows
   ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure o banco de dados MySQL:**
   - Crie o banco e ajuste as credenciais no arquivo de configuração do Flask.

6. **Execute a aplicação:**
   ```bash
   flask run
   ```

7. **Acesse pelo navegador:**
   ```
   http://localhost:5000
   ```

## 📄 Licença

Este projeto é acadêmico e não possui fins comerciais.
