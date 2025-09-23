import os

for arquivo is os.listdir("."):
    if arquivo.endswitch(".txt"):
    nome_novo = "backup_" + arquivo
    os.rename(arquivo, nome_novo):
    print(f"{arquivo} -> {nome_novo}")