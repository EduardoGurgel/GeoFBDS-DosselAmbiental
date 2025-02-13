import os

# URL base do GEO.FBDS
BASE_URL = "https://www.geo.fbds.org.br"

# Pastas de destino
PASTA_DESTINO = "downloads"
PASTA_SAIDA = "mosaico"
os.makedirs(PASTA_DESTINO, exist_ok=True)
os.makedirs(PASTA_SAIDA, exist_ok=True)

# Lista de estados disponíveis
ESTADOS = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]

# CRS alvo para padronização
CRS_ALVO = "EPSG:4326"  # WGS 84

# Cabeçalhos básicos para evitar bloqueios do servidor
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
    "Accept": "*/*",
    "Origin": BASE_URL,
    "Referer": BASE_URL,
    "Content-Type": "application/x-www-form-urlencoded",
}
