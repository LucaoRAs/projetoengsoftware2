import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.exame import Exame


def test_listar_exames():
    resultado = Exame.listar_exames()
    assert isinstance(resultado, list)


def test_buscar_por_nome_paciente():
    resultado = Exame.buscar_por_nome_paciente("NomeInexistente")
    assert isinstance(resultado, list)


def test_buscar_exame_por_id():
    resultado = Exame.buscar_exame_por_id(-1)
    assert resultado is None or isinstance(resultado, tuple)


def test_buscar_por_nome_paciente_string_vazia():
    resultado = Exame.buscar_por_nome_paciente("")
    assert isinstance(resultado, list)


def test_buscar_por_nome_paciente_none():
    resultado = Exame.buscar_por_nome_paciente(None)
    assert isinstance(resultado, list)
