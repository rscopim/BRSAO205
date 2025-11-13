'''3 -  Crie um programa que leia um arquivo CSV informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.'''

import csv

print("=== Leitor de Arquivo CSV ===")

arquivo = input("Digite o nome do arquivo CSV para leitura: ")

try:
    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.reader(f)
        for linha in leitor:
            print(linha)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception as e:
    print("Falha ao ler o arquivo:", e)
