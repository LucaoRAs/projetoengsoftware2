# Testes Unitários

Esta pasta contém todos os testes unitários do projeto.

## Estrutura

- `test_models.py` - Testes para os modelos da aplicação
- `test_app.py` - Testes para a aplicação Flask
- `test_exame_simples.py` - Testes simples do modelo Exame
- `run_tests.py` - Script para executar todos os testes
- `conftest.py` - Configuração para testes
- `__init__.py` - Torna a pasta um pacote Python

## Como executar os testes

### Executar todos os testes:
```bash
python tests/run_tests.py
```

### Executar um arquivo de teste específico:
```bash
python tests/test_models.py
python tests/test_app.py
python tests/test_exame_simples.py
```

## Exemplo de teste

```python
import unittest

class TestExemplo(unittest.TestCase):
    def setUp(self):
        """Configuração inicial"""
        pass
    
    def test_metodo_exemplo(self):
        """Testa se o método funciona corretamente"""
        resultado = funcao_teste()
        self.assertIsInstance(resultado, list)
```

## Cobertura de testes

Os testes cobrem:
- ✅ Modelos (Exame)
- ✅ Rotas principais da aplicação Flask
- ✅ Casos de borda e valores inválidos

