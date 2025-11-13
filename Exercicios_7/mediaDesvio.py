'''1 -  Crie um programa que lê um arquivo CSV de logs de treinamento com a biblioteca pandas, calcule e exiba a média e o desvio padrão da coluna tempo_execucao, caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. '''

import pandas as pd

print("=== Análise de Logs de Treinamento ===")

arquivo = input("Digite o nome do arquivo CSV (ex: logs.csv): ")

try:
    # Lê o arquivo CSV em um DataFrame
    df = pd.read_csv(arquivo)
    
    # Calcula média e desvio padrão da coluna 'tempo_execucao'
    media = df["tempo_execucao"].mean()
    desvio = df["tempo_execucao"].std()
    
    print(f"Média do tempo de execução: {media:.2f}")
    print(f"Desvio padrão do tempo de execução: {desvio:.2f}")

except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception as e:
    print("Falha ao ler o arquivo:", e)
