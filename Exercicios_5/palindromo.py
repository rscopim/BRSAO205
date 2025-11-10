'''2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.'''

def palindromo(texto):
    texto_limpo = "".join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]
frase = input("Digite uma frase: ")
resultado = palindromo(frase)
if resultado:
    print("Sim")
else:
    print("Não")

# Verificador de Palavras Palindromo

def eh_palindromo(texto: str) -> bool:
    """
    Verifica se uma palavra ou frase é um palíndromo,
    ignorando espaços, acentos, pontuação e maiúsculas/minúsculas.
    """
    # Remove espaços e pontuações
    texto_limpo = "".join(char.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]


# Programa principal
frase = input("Digite uma palavra ou frase: ")

if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")