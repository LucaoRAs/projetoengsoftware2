import pytest
from app import create_app
from app.controllers.controller_exame import listar_exames

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_listar_exames_diretamente(client):
    # Aqui a função do controller depende do request.args, então criamos um contexto simulado
    with client.application.test_request_context('/exames?busca='):
        resposta = listar_exames()
        assert isinstance(resposta, str)
        assert '<html' in resposta  # ou outra verificação de conteúdo HTML
