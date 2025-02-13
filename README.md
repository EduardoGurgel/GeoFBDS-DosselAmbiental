# 🗺️ GeoFBDS-DosselAmbiental - Download e Processamento de Dados Geoespaciais

Este projeto realiza o **download automático de shapefiles dos estados brasileiros**, extrai e processa os arquivos, criando **mosaicos geográficos** padronizados no sistema de coordenadas.
### 📺 Demonstração do Projeto

📌
---



## 🚀 **Instalação e Configuração**

### 1️⃣ Criar e ativar um ambiente virtual (VENV)

Antes de instalar as dependências, é recomendado criar um **ambiente virtual** para isolar o projeto:

```sh
# Criar um ambiente virtual
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Linux/macOS
source venv/bin/activate
```

### 2️⃣ Instalar dependências
Após ativar o ambiente virtual, instale as dependências com:

```sh
pip install -r requirements.txt
```

### ▶️ Como Rodar o Programa
Execute o script principal main.py e siga as opções do menu:
```sh
python main.py
```

### Tecnologias Utilizadas
- Python 3.12+
- GeoPandas (Processamento de shapefiles)
- Matplotlib (Visualização)
- Requests (Download de arquivos)
- tqdm (Barra de progresso)
