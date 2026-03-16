import pytest
from fastapi.testclient import TestClient
from backend.main import app

@pytest.fixture
def client():
    # TestClient é o "navegador falso" que simula requisições
    # sem precisar subir um servidor de verdade
    return TestClient(app)

@pytest.fixture
def valid_bin_file():
    # Simula um arquivo .bin com bytes reais
    # Não precisamos de um arquivo real no disco
    return ("arquivo_teste.bin", b"\x00\x01\x02\x03\xFF", "application/octet-stream")

@pytest.fixture
def empty_bin_file():
    return ("arquivo_vazio.bin", b"", "application/octet-stream")