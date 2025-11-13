import csv

print("=== Criador de Arquivo CSV ===")

# Dados de exemplo
pessoas = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 25, "São Paulo"],
    ["Bruno", 30, "Rio de Janeiro"],
    ["Carla", 22, "Belo Horizonte"]
]

arquivo = input("Digite o nome do arquivo CSV para salvar (ex: pessoas.csv): ")

try:
    # Abre o arquivo no modo de escrita e grava os dados em formato CSV
    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerows(pessoas)
    print("Arquivo salvo com sucesso!")

except Exception as e:
    print("Falha ao salvar o arquivo:", e)
