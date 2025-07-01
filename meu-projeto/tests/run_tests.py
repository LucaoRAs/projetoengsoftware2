#!/usr/bin/env python3
"""
Script para executar todos os testes unitários do projeto
"""

import unittest
import sys
import os

# Adicionar o diretório pai ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_all_tests():
    """Executa todos os testes unitários"""
    
    # Descobrir e carregar todos os testes
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Executar os testes
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Retornar código de saída baseado no resultado
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    print("Executando testes unitários...")
    print("=" * 50)
    
    exit_code = run_all_tests()
    
    print("=" * 50)
    if exit_code == 0:
        print("✅ Todos os testes passaram!")
    else:
        print("❌ Alguns testes falharam!")
    
    sys.exit(exit_code) 