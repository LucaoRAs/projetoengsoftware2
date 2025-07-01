import unittest
import sys
import os

# Adicionar o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.exame import Exame

class TestExameModel(unittest.TestCase):
    """Testes unitários para o modelo Exame"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        pass
    
    def tearDown(self):
        """Limpeza após cada teste"""
        pass
    
    def test_listar_exames(self):
        """Testa se o método listar_exames retorna uma lista"""
        resultado = Exame.listar_exames()
        self.assertIsInstance(resultado, list)
    
    def test_buscar_por_nome_paciente(self):
        """Testa se o método buscar_por_nome_paciente retorna uma lista"""
        resultado = Exame.buscar_por_nome_paciente("NomeInexistente")
        self.assertIsInstance(resultado, list)
    
    def test_buscar_exame_por_id(self):
        """Testa se o método buscar_exame_por_id retorna None ou tupla para ID inválido"""
        resultado = Exame.buscar_exame_por_id(-1)  # ID improvável
        self.assertTrue(resultado is None or isinstance(resultado, tuple))
    
    def test_buscar_por_nome_paciente_string_vazia(self):
        """Testa o comportamento com string vazia"""
        resultado = Exame.buscar_por_nome_paciente("")
        self.assertIsInstance(resultado, list)
    
    def test_buscar_por_nome_paciente_none(self):
        """Testa o comportamento com None"""
        resultado = Exame.buscar_por_nome_paciente(None)
        self.assertIsInstance(resultado, list)

if __name__ == '__main__':
    unittest.main() 