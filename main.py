from config import ESTADOS
from download import iniciar_download, extrair_tar
from processamento import mosaicar_shapefiles
from visualizacao import exibir_mosaico

def main():
    print("Escolha uma opção:")
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

    mosaicos_gerados = {}

    for estado in estados_para_baixar:
        tar_file = iniciar_download(estado)
        if tar_file:
            mosaicos_gerados[estado] = extrair_tar(tar_file)

    for estado in estados_para_baixar:
        mosaico_path = mosaicar_shapefiles(estado, [mosaicos_gerados[estado]])
        if mosaico_path and input(f"Deseja abrir o mosaico do estado {estado}? (S/N): ").strip().lower() == "s":
            exibir_mosaico(mosaico_path, f"{estado} (Mosaico)")

if __name__ == "__main__":
    main()
