# processamento.py

import os
import geopandas as gpd
import pandas as pd
from config import CRS_ALVO, PASTA_SAIDA

def buscar_shapefiles(pasta_estado):
    """Busca shapefiles dentro da estrutura de diretórios do estado."""
    shapefiles = []
    for root, _, files in os.walk(pasta_estado):
        for file in files:
            if file.endswith(".shp"):
                shapefiles.append(os.path.join(root, file))
    return shapefiles

def mosaicar_shapefiles(nome_mosaico, pastas):
    """Mosaica os arquivos vetoriais Shapefile em um único conjunto."""
    print(f"🔄 Iniciando mosaico: {nome_mosaico}...")
    shapefiles = [shp for pasta in pastas for shp in buscar_shapefiles(pasta)]
    
    if not shapefiles:
        print(f"⚠ Nenhum arquivo Shapefile encontrado para {nome_mosaico}. Pulando mosaico.")
        return None

    gdfs = []
    for shp in shapefiles:
        # Mostra apenas o nome (ou caminho) do arquivo em processamento
        print(f"📂 Acessando arquivo: {os.path.basename(shp)}")

        gdf = gpd.read_file(shp)
        gdf = gdf[gdf.geometry.type.isin(["Polygon", "MultiPolygon"])]
        if gdf.empty:
            continue

        if gdf.crs is None:
            print(f"⚠ Aviso: CRS indefinido em {shp}. Pulando este arquivo.")
            continue

        # Converte silenciosamente para CRS_ALVO
        if gdf.crs.to_string() != CRS_ALVO:
            # (sem printar nada de 'convertendo')
            gdf = gdf.to_crs(CRS_ALVO)

        gdfs.append(gdf)

    if not gdfs:
        print(f"⚠ Nenhuma geometria POLYGON válida encontrada. Pulando mosaico.")
        return None

    # Concatena tudo num único GeoDataFrame
    mosaico = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True), crs=CRS_ALVO)

    output_shp = os.path.join(PASTA_SAIDA, f"{nome_mosaico}_mosaico.shp")
    mosaico.to_file(output_shp)

    print(f"✅ Mosaico salvo em {output_shp}")
    return output_shp
