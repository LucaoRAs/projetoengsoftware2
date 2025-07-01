"""
Configuração para testes unitários
"""

import sys
import os

# Adicionar o diretório pai ao path para importar os módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configurações de teste
TEST_CONFIG = {
    'TESTING': True,
    'DEBUG': False,
    'WTF_CSRF_ENABLED': False
} 