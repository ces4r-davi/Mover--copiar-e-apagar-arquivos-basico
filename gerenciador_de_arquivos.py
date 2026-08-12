import os
import shutil

def criar_caminho(caminho_novo):
    try:
        os.mkdir(caminho_novo)
    except FileExistsError as e:
        print("O caminho que deseja criar ja existe")

def mover_arquivos(caminho_antigo, caminho_novo):
    for root, dirs, files in os.walk(caminho_antigo):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(caminho_novo, file)
            shutil.move(old_file_path, new_file_path)
            print(f"O arquivo {file} foi movido com sucesso!")

def copiar_arquivos(caminho_antigo, caminho_novo, extensao=None):
    for root, dirs, files in os.walk(caminho_antigo):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(caminho_novo, file)
            if extensao is not None:
                if file.endswith(extensao) in new_file_path:
                    shutil.copy(old_file_path, new_file_path)
                    print(f"O arquivo {file} foi copiado com sucesso!")
            else:
                shutil.copy(old_file_path, new_file_path)
                print(f"O arquivo {file} foi copiado com sucesso!")

def remover_arquivos(caminho):
    for root, dirs, files in os.walk(caminho):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
    

