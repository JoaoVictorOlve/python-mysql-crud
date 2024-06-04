import os
import time
from db import listar_produtos, adicionar_produto, remover_produto, alterar_produto, efetuar_cadastro

while True:
    os.system('cls')
    print("""=========================
|ADEMILSON SUPERMERCADOS|
=========================""")
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    os.system('cls')

    if nome and senha:
        if efetuar_cadastro(nome, senha):
            time.sleep(3)
            break
    else:
        print("Nome ou senha inválidos!")
    time.sleep(3)

while True:
    os.system('cls')
    print("""=========================
|ADEMILSON SUPERMERCADOS|
=========================""")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar estoque de produto")
    print("4 - Remover produto")
    print("5 - Sair")
    opcao = input("Opção: ")

    if opcao == '1':
        os.system('cls')
        adicionar_produto()
        time.sleep(3)

    elif opcao == '2':
        os.system('cls')
        listar_produtos()
    
    elif opcao == '3':
        os.system('cls')
        while True:
            os.system('cls')
            try:
                id = int(input("Informe o id do produto: "))
                alterar_produto(id)
                break    
            except:
                print("ID inválido!")
                time.sleep(3)

    elif opcao == '4':
        while True:
            os.system('cls')
            try:
                id = int(input("Informe o id do produto: "))
                remover_produto(id)
                break    
            except:
                print("ID inválido!")
                time.sleep(3)

    elif opcao == '5':
        os.system('cls')
        print("""=========================
|ADEMILSON SUPERMERCADOS|
=========================""")
        print("Saindo do sistema, até mais!")
        time.sleep(3)
        break
    else:
        os.system('cls')
        print("Opção inválida!")
        time.sleep(3)