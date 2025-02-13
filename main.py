import os
import geopandas as gpd
import pandas as pd  
from config import ESTADOS
from download import iniciar_download, extrair_tar
from processamento import mosaicar_shapefiles
from visualizacao import exibir_mosaico  

def main():
    print("1 - Baixar DF e AC para testes")
    print("2 - Baixar todos os estados (isso pode demorar muito)")
    print("3 - Digite um estado que deseja baixar (Ex: DF, GO, SP ...)")
    opcao = input("Digite 1, 2 ou 3: ").strip()

    if opcao == "1":
        estados_para_baixar = ["DF", "AC"]
    elif opcao == "2":
        estados_para_baixar = ESTADOS
    elif opcao == "3":
        estado_escolhido = input("Digite a sigla do estado: ").strip().upper()
        estados_para_baixar = [estado_escolhido] if estado_escolhido in ESTADOS else []
    else:
        print("❌ Opção inválida. Saindo...")
        return

    # Baixar e extrair cada estado
    mosaicos_gerados = {}
    for estado in estados_para_baixar:
        tar_file = iniciar_download(estado)
        if tar_file:
            mosaicos_gerados[estado] = extrair_tar(tar_file)

    # Criar o mosaico individual de cada estado
    caminhos_mosaico = {}
    for estado in estados_para_baixar:
        mosaico_path = mosaicar_shapefiles(estado, [mosaicos_gerados[estado]])
        if mosaico_path:
            caminhos_mosaico[estado] = mosaico_path


    if opcao == "1" and "DF" in caminhos_mosaico and "AC" in caminhos_mosaico:
        print("\nMesclando DF + AC em um único shapefile...")
        df_gdf = gpd.read_file(caminhos_mosaico["DF"])
        ac_gdf = gpd.read_file(caminhos_mosaico["AC"])

        df_ac_combinado = gpd.GeoDataFrame(
            pd.concat([df_gdf, ac_gdf], ignore_index=True),
            crs=df_gdf.crs
        )

        # Salva o shapefile combinado
        df_ac_mosaico_path = os.path.join("mosaico", "DF_AC_mosaico.shp")
        df_ac_combinado.to_file(df_ac_mosaico_path)

        print(f"\n✅ Shapefile mesclado disponível em: {df_ac_mosaico_path}")


        visualizar_combinado = input("Deseja visualizar o shapefile mesclado (DF + AC)? (S/N): ").strip().lower()
        if visualizar_combinado == "s":
            exibir_mosaico(df_ac_mosaico_path, "DF + AC (Mosaico Combinado)")


        visualizar_df = input("\nDeseja visualizar o mosaico individual do DF? (S/N): ").strip().lower()
        if visualizar_df == "s":
            exibir_mosaico(caminhos_mosaico["DF"], "Mosaico DF")

        visualizar_ac = input("\nDeseja visualizar o mosaico individual do AC? (S/N): ").strip().lower()
        if visualizar_ac == "s":
            exibir_mosaico(caminhos_mosaico["AC"], "Mosaico AC")


if __name__ == "__main__":
    main()
