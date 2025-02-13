import os
import geopandas as gpd
import matplotlib.pyplot as plt

def exibir_mosaico(mosaico_path, titulo):
    """Exibe o mosaico gerado"""
    if os.path.exists(mosaico_path):
        gdf = gpd.read_file(mosaico_path)
        gdf.plot(figsize=(10, 10), edgecolor="black", alpha=0.7)
        plt.title(titulo)
        plt.show()
