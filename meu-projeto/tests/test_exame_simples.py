import unittest
import sys
import os

# Adicionar o diretório pai ao path para importar os módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.exame import Exame

class TestExameSimples(unittest.TestCase):
    def test_listar_exames(self):
        resultado = Exame.listar_exames()
        self.assertIsInstance(resultado, list)

    def test_buscar_por_nome_paciente(self):
        resultado = Exame.buscar_por_nome_paciente("NomeInexistente")
        self.assertIsInstance(resultado, list)

    def test_buscar_exame_por_id(self):
        resultado = Exame.buscar_exame_por_id(-1)  # ID improvável
        self.assertTrue(resultado is None or isinstance(resultado, tuple))

if __name__ == '__main__':
    unittest.main() 