# Sistema de Agendamento de Exames

Sistema web desenvolvido em Flask para gerenciamento de exames médicos.

## Pré-requisitos

- Python 3.8+
- MySQL Server
- pip

## Instalação e Configuração

### 1. Configurar o Banco de Dados

1. Inicie o MySQL Server
2. Execute o script SQL para criar o banco e tabelas:
   ```sql
   -- Execute o arquivo bd.sql no seu MySQL
   ```

### 2. Configurar o Ambiente Python

1. Navegue até a pasta do projeto:
   ```bash
   cd meu-projeto
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Configurar as Variáveis de Banco

Edite o arquivo `config.py` com suas configurações de MySQL:
```python
class Config:
    MYSQL_HOST = 'localhost'  # Seu host MySQL
    MYSQL_USER = 'root'       # Seu usuário MySQL
    MYSQL_PASSWORD = 'root'   # Sua senha MySQL
    MYSQL_DB = 'banco_agenda_exames'
    MYSQL_PORT = 3306         # Sua porta MySQL
```

### 4. Executar a Aplicação

1. Certifique-se de que o ambiente virtual está ativado
2. Execute a aplicação:
   ```bash
   python app.py
   ```

3. Acesse a aplicação em: http://localhost:5000

## Estrutura do Projeto

```
meu-projeto/
├── app/
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── controller_exame.py
│   │   
│   ├── models/
│   │   ├── __init__.py
│   │   └── exame.py
│   │   
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   │   
│   ├── templates/
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── inicio.html
│   │   ├── novo_exame.html
│   │   └── editar_exame.html
│   │   
│   ├── __init__.py
│   └── extensions.py
├── logs/
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

## Funcionalidades

- **Login**: Tela de autenticação (simulada)
- **Dashboard**: Página inicial com opções de navegação
- **Listar Exames**: Visualização de todos os exames cadastrados
- **Buscar Exames**: Filtro por nome do paciente
- **Criar Exame**: Formulário para cadastro de novos exames
- **Editar Exame**: Modificação de exames existentes
- **Deletar Exame**: Remoção de exames com confirmação
- **Logout**: Encerramento da sessão

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Banco de Dados**: MySQL
- **Frontend**: HTML, CSS, JavaScript
- **Estilização**: CSS customizado com gradientes e animações

## Características do Design

- Interface moderna e responsiva
- Gradientes coloridos e animações suaves
- Design limpo e profissional
- Compatível com dispositivos móveis
- Feedback visual em interações

## Logs

O sistema gera logs de conexão com o banco de dados no diretório `logs/` em formato JSON. 

## Testes Unitários

Para executar testes unitários, salve o código abaixo como `test_exame_simples.py` na pasta do projeto e execute:

```
python test_exame_simples.py 