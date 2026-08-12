import os
import shutil

caminho_antigo = r"C:\Users\davic\Downloads\testedeleitura"
caminho_novo = r"C:\Users\davic\Downloads\pastaparamover"

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print("O caminho que deseja criar ja existe")

for root, dirs, files in os.walk(caminho_antigo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        print(new_file_path)

        shutil.move(old_file_path, new_file_path)
        print(f"O arquivo {file} foi movido com sucesso!")