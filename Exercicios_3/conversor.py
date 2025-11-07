'''# Conversor de Temperatura

# Solicita os dados ao usuário
temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

# Converte a temperatura para Celsius primeiro
if origem == "C":
    temp_c = temperatura
elif origem == "F":
    temp_c = (temperatura - 32) * 5/9
elif origem == "K":
    temp_c = temperatura - 273.15
else:
    print("Unidade de origem inválida!")
    exit()

# Converte de Celsius para a unidade de destino
if destino == "C":
    resultado = temp_c
elif destino == "F":
    resultado = temp_c * 9/5 + 32
elif destino == "K":
    resultado = temp_c + 273.15
else:
    print("Unidade de destino inválida!")
    exit()

# Exibe o resultado
print(f"{temperatura}°{origem} equivalem a {resultado:.2f}°{destino}")'''

# Conversor de Temperatura

# Solicita os dados ao usuário
temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

# Verifica se as unidades são válidas
unidades_validas = ["C", "F", "K"]

if origem not in unidades_validas or destino not in unidades_validas:
    print("Unidade inválida! Use apenas C, F ou K.")
else:
    # Converte a temperatura para Celsius primeiro
    if origem == "C":
        temp_c = temperatura
    elif origem == "F":
        temp_c = (temperatura - 32) * 5/9
    elif origem == "K":
        temp_c = temperatura - 273.15

    # Converte de Celsius para a unidade de destino
    if destino == "C":
        resultado = temp_c
    elif destino == "F":
        resultado = temp_c * 9/5 + 32
    elif destino == "K":
        resultado = temp_c + 273.15

    # Exibe o resultado
    print(f"{temperatura}°{origem} equivalem a {resultado:.2f}°{destino}")