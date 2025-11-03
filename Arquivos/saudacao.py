'''print("olá, mundo")

idade = 20 #variavel
if idade >= 18: # estrutura de controle
    print("Você é adulto")

print(20 +5)
print("20" + "5")

idade = 25 # int - inteiro
nome = "Ricardo" # str - string
altura = 1.70 # float
verfa = True # bool

idade = int("25") 

#LISTA
nome = ["Maria", 3, "Carol"]
idade = [1, 2, 3]
print(nome[1])
print(nome)
print(idade)

#Tupla
numero = (10, 20)

#Dicionario
aluno = {
    "nome": "Ricardo",
    "idade": 47,
    "curso": "AWS"
}
print(aluno)

def dobro(x):
    return x * 2
print(dobro(5))

def soma(a, b, c):
    return a + b+ c
print(soma(1, 2, 3))

def lista_nomes():
    return[]

def matriz():
    return[[1, 2], [3, 4]]

matriz = [[1, 2], [3, 4]]

vetor = [10, 20, 30, 40]

idade = 10 #variavel
if idade >= 18: # estrutura de controle
    print("Você é adulto")
else:
    print("Menor de idade")

opcao = 2
acao = {
    1: "Iniciar",
    2: "Parar",
    3: "Reinciar"
}
print(acao.get(acao, "OK"))'''

for i in range(5):
    print("Conte", i)

contador = 0
while contador < 5:
    print("contar", contador)
    contador += 1