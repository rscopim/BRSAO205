'''Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

temperatura = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Unidade para conversão (C, F, K): ").upper()

if origem == "C":
    celsius = temperatura
elif origem == "F":
    celsius = (temperatura - 32) * 5/9
elif origem == "K":
    celsius = temperatura - 273.15
else:
    print("Invalido")

