# visualizacao.py

import os
import folium
import geopandas as gpd
import matplotlib.pyplot as plt

def exibir_mosaico(mosaico_path, titulo):
    """Exibe o mosaico gerado com matplotlib"""
    if os.path.exists(mosaico_path):
        gdf = gpd.read_file(mosaico_path)
        gdf.plot(figsize=(10, 10), edgecolor="black", alpha=0.7)
        plt.title(titulo)
        plt.show()
    else:
        print(f"❌ Arquivo não encontrado: {mosaico_path}")

def exibir_mosaico_folium(mosaico_path, titulo="Mapa Interativo"):
    """
    Lê o shapefile do mosaico e gera um mapa interativo em HTML usando Folium.
    """
    if not os.path.exists(mosaico_path):
        print(f"❌ Arquivo não encontrado: {mosaico_path}")
        return

    # Lê o arquivo shapefile do mosaico
    gdf = gpd.read_file(mosaico_path)
    
    # Para garantir que o Folium renderize bem
    if gdf.crs is None or gdf.crs.to_string() != "EPSG:4326":
        gdf = gdf.to_crs(epsg=4326)

    # Calcula o centro do mapa 
    bounds = gdf.total_bounds  # [minX, minY, maxX, maxY]
    center_lat = (bounds[1] + bounds[3]) / 2
    center_lon = (bounds[0] + bounds[2]) / 2

    # Cria o mapa
    m = folium.Map(location=[center_lat, center_lon], zoom_start=6)

    # Converte cada feature do GeoDataFrame para GeoJson e adiciona no mapa
    folium.GeoJson(
        data=gdf,
        name=titulo,
        style_function=lambda x: {"fillColor": "#228B22", "color": "black", "weight": 1, "fillOpacity": 0.5}
    ).add_to(m)

    folium.LayerControl().add_to(m)

    # Salva em um HTML
    saida_html = f"{titulo.lower().replace(' ', '_')}.html"
    m.save(saida_html)

    print(f"✅ Mapa interativo gerado: {saida_html} (abra no seu navegador)")

def exibir_mosaico_folium_em_memoria(gdf, titulo="Mapa Interativo"):
    """
    Gera um mapa interativo em memória a partir de um GeoDataFrame (sem precisar salvar Shapefile).
    """
    if gdf.crs is None or gdf.crs.to_string() != "EPSG:4326":
        gdf = gdf.to_crs(epsg=4326)

    bounds = gdf.total_bounds
    center_lat = (bounds[1] + bounds[3]) / 2
    center_lon = (bounds[0] + bounds[2]) / 2

    m = folium.Map(location=[center_lat, center_lon], zoom_start=6)

    folium.GeoJson(
        data=gdf,
        name=titulo,
        style_function=lambda x: {"fillColor": "#FF4500", "color": "black", "weight": 1, "fillOpacity": 0.5}
    ).add_to(m)

    folium.LayerControl().add_to(m)

    saida_html = f"{titulo.lower().replace(' ', '_')}_memoria.html"
    m.save(saida_html)

    print(f"✅ Mapa com DF e AC em memória gerado: {saida_html} (abra no seu navegador)")
