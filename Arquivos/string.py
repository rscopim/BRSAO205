'''myString = "Isso é um string"
print(myString)
print(type(myString))
print(myString + " é do tipo de dado " + str(type(myString)))


# Concatenação de string
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)'''

name = input("Qual é o seu nome? ")
color = input("Qual sua cor favorita? ")
animal = input("Qual seu animal favorito? ")
print("{}, você gosta da cor {} e do animal {}!".format(name, color, animal))

# Explicação do código Python

# A primeira linha, `name = input("Qual é o seu nome? ")`, solicita ao usuário que digite seu nome.
# A função `input()` exibe a mensagem "Qual é o seu nome? " na tela e aguarda a entrada do usuário.
# O valor que o usuário digita é então armazenado na variável chamada `name`.

# A segunda linha, `color = input("Qual sua cor favorita? ")`, funciona da mesma forma que a anterior.
# Ela pede ao usuário para digitar sua cor favorita e armazena a resposta na variável `color`.

# A terceira linha, `animal = input("Qual seu animal favorito? ")`, repete o processo.
# Ela pede ao usuário para digitar seu animal favorito e armazena a resposta na variável `animal`.

# A quarta linha, `print("{}, você gosta da cor {} e do animal {}!".format(name, color, animal))`, 
# é onde a mágica acontece. A função `print()` exibe uma mensagem na tela.
# A string `"{}, você gosta da cor {} e do animal {}!"` é um modelo de texto.
# Os pares de chaves `{}` são espaços reservados para valores que serão inseridos mais tarde.

# A função `.format(name, color, animal)` é o que preenche esses espaços.
# Ela pega os valores das variáveis `name`, `color` e `animal` e os insere na string na ordem em que aparecem.
# Por exemplo, o valor de `name` entra no primeiro `{}`.
# O valor de `color` entra no segundo `{}`.
# O valor de `animal` entra no terceiro `{}`.
# O resultado final é uma frase completa e personalizada, como por exemplo:
# "João, você gosta da cor azul e do animal cachorro!".

