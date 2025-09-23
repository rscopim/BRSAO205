import os

for arquivo is os.listdir("."):
    if arquivo.endswitch(".txt"):
        nome_novo = "backup_" + arquivo
        os.rename(arquivo, nome_novo):
        print(f"{arquivo} -> {nome_novo}")

defnew_user():
    confirm= "N"
    whileconfirm!= "Y":
        username= input("Insira o nome do usuário a ser adicionado: ")
        print("Usar o nome de usuário '"+ username+ "'? (S/N)")
        confirm= input() .upper()
os.system("sudoadduser"+ username)