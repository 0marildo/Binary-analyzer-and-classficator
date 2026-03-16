import pytest
from unittest.mock import patch

# ─── Happy Path ──────────────────────────────────────────────

def test_analyze_aceita_arquivo_bin_valido(client, valid_bin_file):
    # Mocka o process_binary_file pra não depender do core funcionando
    # Isso é um unit test — testa SÓ a rota, não o processamento
    with patch("backend.api.routes.api.process_binary_file") as mock_process:
        mock_process.return_value = {
            "num_blocks": 10,
            "clusters": [0, 1, 0, 1, 0],
            "plot": "base64string",
            "summary": {"header": 2, "raw_data": 3, "offset": 5}
        }  # ajuste pro seu AnalyseResponse

        filename, content, content_type = valid_bin_file
        response = client.post(
            "/api/v1/analyze",
            files={"file": (filename, content, content_type)}
        )

    assert response.status_code == 200

# ─── Validação de extensão ───────────────────────────────────

def test_analyze_rejeita_arquivo_txt(client):
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("malware.txt", b"conteudo", "text/plain")}
    )
    assert response.status_code == 400
    assert "bin" in response.json()["detail"].lower()

def test_analyze_rejeita_arquivo_pdf(client):
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("documento.pdf", b"%PDF-1.4", "application/pdf")}
    )
    assert response.status_code == 400

def test_analyze_rejeita_arquivo_sem_extensao(client):
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("arquivo", b"\x00\x01", "application/octet-stream")}
    )
    assert response.status_code == 400

# ─── Edge cases de arquivo ───────────────────────────────────

def test_analyze_rejeita_arquivo_vazio(client, empty_bin_file):
    with patch("backend.api.routes.api.process_binary_file") as mock_process:
        mock_process.side_effect = ValueError("Arquivo vazio")

        filename, content, content_type = empty_bin_file
        response = client.post(
            "/api/v1/analyze",
            files={"file": (filename, content, content_type)}
        )

    assert response.status_code == 500

def test_analyze_retorna_500_quando_processamento_falha(client, valid_bin_file):
    # Simula o core explodindo — garante que a rota trata o erro corretamente
    with patch("backend.api.routes.api.process_binary_file") as mock_process:
        mock_process.side_effect = Exception("Erro interno no processamento")

        filename, content, content_type = valid_bin_file
        response = client.post(
            "/api/v1/analyze",
            files={"file": (filename, content, content_type)}
        )

    assert response.status_code == 500

# ─── Edge case de nome de arquivo ────────────────────────────

def test_analyze_rejeita_nome_com_bin_no_meio(client):
    # "relatorio.bin.exe" não deve passar — termina em .exe
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("virus.bin.exe", b"\x00\x01", "application/octet-stream")}
    )
    assert response.status_code == 400




