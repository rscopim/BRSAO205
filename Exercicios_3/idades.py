def classificar_idade():
    """
    Solicita a idade do usuário e a classifica em categorias.
    """
    # 1. Solicita a entrada do usuário
    while True:
        try:
            idade_str = input("Por favor, digite sua idade: ")
            idade = int(idade_str)
            
            # Validação básica para idades não negativas
            if idade < 0:
                print("Idade não pode ser um número negativo. Tente novamente.")
                continue
            
            break # Sai do loop se a idade for um inteiro positivo ou zero
            
        except ValueError:
            print(f"Entrada inválida. '{idade_str}' não é um número inteiro. Tente novamente.")
            
    # 2. Classifica a idade usando condicionais
    if 0 <= idade <= 12:
        categoria = "Criança"
    elif 13 <= idade <= 17:
        categoria = "Adolescente"
    elif 18 <= idade <= 59:
        categoria = "Adulto"
    # A última condição pega todos os valores restantes (60 ou mais)
    elif idade >= 60:
        categoria = "Idoso"
    else:
        # Esta linha só seria alcançada se a validação acima falhasse (ex: idade negativa),
        # mas mantemos por segurança.
        categoria = "Idade fora do intervalo de classificação (erro interno)."

    # 3. Exibe o resultado
    print(f"\n--- Resultado da Classificação ---")
    print(f"Sua idade é: {idade} anos.")
    print(f"Sua categoria é: **{categoria}**.")

# Executa a função principal
classificar_idade()