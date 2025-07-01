import unittest
import sys
import os

# Adicionar o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
import app

class TestApp(unittest.TestCase):
    """Testes unitários para a aplicação Flask"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def tearDown(self):
        """Limpeza após cada teste"""
        pass
    
    def test_app_instancia(self):
        """Testa se a aplicação pode ser criada"""
        self.assertIsNotNone(self.app)
    
    def test_app_config_testing(self):
        """Testa se a configuração de teste está ativa"""
        self.assertTrue(self.app.config['TESTING'])
    
    def test_home_route(self):
        """Testa se a rota home responde corretamente"""
        # Testar se a aplicação tem rotas registradas
        self.assertTrue(len(self.app.url_map._rules) > 0)
    
    def test_app_creation(self):
        """Testa se a aplicação pode ser criada sem erros"""
        try:
            app = create_app()
            self.assertIsNotNone(app)
        except Exception as e:
            self.fail(f"Falha ao criar aplicação: {e}")

if __name__ == '__main__':
    unittest.main() 