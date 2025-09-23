"""
Exemplo: explicação linha a linha dentro do próprio código.
Tudo o que explica cada linha está aqui, nos comentários abaixo.
"""

# Linha 1: exibe uma pergunta e guarda a resposta na variável 'name'
# input("Qual é o seu nome? ") -> mostra o texto entre aspas ao usuário no terminal/console
# quando o usuário digita algo e pressiona Enter, input() retorna esse texto como uma string (tipo str)
# o operador '=' atribui essa string à variável name
name = input("Qual é o seu nome? ")

# Linha 2: mesma ideia — pergunta e guarda na variável 'color'
# input sempre retorna texto; aqui guardamos a cor favorita informada pelo usuário
color = input("Qual sua cor favorita? ")

# Linha 3: pergunta e guarda na variável 'animal'
animal = input("Qual seu animal favorito? ")

# Linha 4: imprime uma frase usando formatação de string
# print(...) -> envia para a saída padrão (normalmente a tela/console) o que estiver dentro dos parênteses
# a string "{}, você gosta da cor {} e do animal {}!" contém três pares de chaves {} — são placeholders (marcadores)
# o método .format(name, color, animal) substitui cada {} pelo respectivo argumento, na ordem:
#   1º {}  <- name
#   2º {}  <- color
#   3º {}  <- animal
# Exemplo de funcionamento:
#   se o usuário informou name = "João", color = "verde", animal = "cachorro"
#   o print exibirá: "João, você gosta da cor verde e do animal cachorro!"
print("{}, você gosta da cor {} e do animal {}!".format(name, color, animal))

# Observações extras (comentadas dentro do código):
# - input() sempre retorna str em Python 3. Se você precisar de um número, converta:
#     idade = int(input("Quantos anos você tem? "))
# - .format() é uma forma de interpolar variáveis em strings. Alternativas:
#     - f-strings (Python 3.6+): print(f"{name}, você gosta da cor {color} e do animal {animal}!")
#     - placeholders nomeados: print("{n}, gosta de {c} e {a}".format(n=name, c=color, a=animal))
# - Para mostrar chaves literais na string (sem usar como placeholders) use '{{' e '}}':
#     print("Mostrando chaves: {{}}".format())
