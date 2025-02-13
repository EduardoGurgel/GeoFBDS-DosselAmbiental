import os
import requests
import tarfile
from tqdm import tqdm
from config import BASE_URL, HEADERS, PASTA_DESTINO

def iniciar_download(estado):
    """Baixa o arquivo TAR do estado"""
    file_path = os.path.join(PASTA_DESTINO, f"{estado}.tar")
    if os.path.exists(file_path):
        print(f"📂 Arquivo {estado}.tar já baixado. Pulando download...")
        return file_path

    session = requests.Session()
    data = {
        "action": "download",
        "as": f"{estado}.tar",
        "type": "php-tar",
        "baseHref": "/",
        "hrefs": "",
        "hrefs[0]": f"/{estado}/",
    }

    print(f"⬇ Solicitando download para {estado}...")
    response = session.post(BASE_URL, headers=HEADERS, data=data, stream=True)

    if response.status_code == 200:
        total_size = int(response.headers.get("content-length", 0))
        with open(file_path, "wb") as file, tqdm(
            desc=f"{estado}.tar", total=total_size, unit="B", unit_scale=True, unit_divisor=1024
        ) as bar:
            for chunk in response.iter_content(1024):
                file.write(chunk)
                bar.update(len(chunk))

        print(f"✅ Download concluído: {file_path}")
        return file_path
    else:
        print(f"❌ Erro ao baixar {estado}.tar - Status: {response.status_code}")
        return None

def extrair_tar(file_path):
    """Extrai os arquivos TAR baixados"""
    extract_path = os.path.join(PASTA_DESTINO, os.path.splitext(os.path.basename(file_path))[0])
    if os.path.exists(extract_path):
        print(f"📂 Arquivos de {file_path} já extraídos. Pulando extração...")
        return extract_path

    with tarfile.open(file_path, "r") as tar:
        tar.extractall(PASTA_DESTINO)

    print(f"📂 Extração concluída: {extract_path}")
    return extract_path
