import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.exame import Exame


def test_listar_exames():
    resultado = Exame.listar_exames()
    assert isinstance(resultado, list)


def test_buscar_por_nome_paciente():
    resultado = Exame.buscar_por_nome_paciente("NomeInexistente")
    assert isinstance(resultado, list)


def test_buscar_exame_por_id():
    resultado = Exame.buscar_exame_por_id(-1)  # ID improvável
    assert resultado is None or isinstance(resultado, tuple)
