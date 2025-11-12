'''1 - Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.'''

import random   # Importa o módulo 'random', usado para gerar escolhas aleatórias.
import string   # Importa o módulo 'string', que contém conjuntos prontos de caracteres (letras, dígitos, símbolos).

print("=== Gerador de Senhas ===")

# Solicita ao usuário o tamanho desejado da senha.
tamanho = int(input("Digite o tamanho da senha: "))

# Aqui criamos uma sequência de caracteres possíveis para a senha.
# string.ascii_letters → contém todas as letras (maiúsculas e minúsculas).
# string.digits → contém os números de 0 a 9.
# string.punctuation → contém os símbolos de pontuação (!, @, #, $, %, etc).
# O operador '+' junta todos esses conjuntos em uma única sequência de caracteres possíveis.
caracteres = string.ascii_letters + string.digits + string.punctuation

# Agora geramos a senha.
# random.choice(caracteres) → escolhe aleatoriamente um caractere da sequência 'caracteres'.
# for _ in range(tamanho) → repete o processo de escolha 'tamanho' vezes (o "_" é usado quando não precisamos do índice).
# "".join(...) → junta todos os caracteres escolhidos em uma única string (sem espaço entre eles).
senha = "".join(random.choice(caracteres) for _ in range(tamanho))

# Exibe a senha gerada.
print("Senha gerada:", senha)
