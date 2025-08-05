import os
import shutil

caminho_origem = input("Por favor, cole aqui o caminho completo da pasta que você quer organizar e pressione Enter: ")

categorias = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documentos': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx'],
    'Vídeos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Músicas': ['.mp3', '.wav', '.aac'],
    'Compactados': ['.zip', '.rar', '.7z']
}

for nome_arquivo in os.listdir(caminho_origem):
    if os.path.isdir(os.path.join(caminho_origem, nome_arquivo)):
        continue
    extensao = os.path.splitext(nome_arquivo)[1].lower()

    pasta_destino = 'Outros' # Se categoria não for encontrada, será criada uma pasta com este nome.
    for categoria, extensoes in categorias.items():
        if extensao in extensoes:
            pasta_destino = categoria
            break

    caminho_destino_pasta = os.path.join(caminho_origem, pasta_destino)
    os.makedirs(caminho_destino_pasta, exist_ok=True)
    caminho_origem_arquivo = os.path.join(caminho_origem, nome_arquivo)
    shutil.move(caminho_origem_arquivo, caminho_destino_pasta)

    print(f"Moveu '{nome_arquivo}' para a pasta '{pasta_destino}'")

print("\nOrganização concluída!")
input("\nPressione Enter para sair...")