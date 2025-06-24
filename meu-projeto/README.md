# Sistema de Agendamento de Exames

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
    MYSQL_PORT = 3308         # Sua porta MySQL
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
│   │   └── controller_exame.py
│   │   
│   ├── models/
│   │   └── exame.py
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   └── extensions.py
├── logs/
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

## Funcionalidades

- Listar exames
- Criar novo exame
- Editar exame existente
- Deletar exame
- Buscar exame por ID
- Buscar exames por nome do paciente 