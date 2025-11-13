import json

print("=== Leitura e Escrita de Arquivo JSON ===")

dados = {
    "nome": "João",
    "idade": 28,
    "cidade": "Curitiba"
}

arquivo = "dados.json"

try:
    # Salva os dados no arquivo JSON
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print("Arquivo JSON salvo com sucesso!")

    # Lê novamente o arquivo e exibe os dados
    with open(arquivo, "r", encoding="utf-8") as f:
        dados_lidos = json.load(f)
        print("Dados lidos do arquivo:")
        print(dados_lidos)

except Exception as e:
    print("Falha ao salvar ou ler o arquivo:", e)
