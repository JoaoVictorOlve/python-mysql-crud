from create_db import mycursor, mydb
import os
import time

def efetuar_cadastro(nome, senha):
    mycursor.execute(f"SELECT * FROM users WHERE name = '{nome}' and where password = '{senha}' ")
    produto = mycursor.fetchone()
    if not produto:
        print("Usuário ou senha inválidos!")
        return False
    else:
        print("Cadastro efetuado!")
        return True

def adicionar_produto():
    while True:
        os.system('cls')
        descricao = input("Descrição do produto: ")
        if descricao == '':
            print("Descrição inválida!")
            time.sleep(3)
        else:
            break

    while True:
        os.system('cls')
        try:
            quantidade = int(input("Quantidade do produto: "))
            break
        except:
            print("Quantidade inválida!")
            time.sleep(3)

    while True:
        os.system('cls')
        try:
            preco = float(input("Preco do produto: "))
            break
        except:
            print("Preço inválido!")
            time.sleep(3)

    try:
        mycursor.execute(f"INSERT INTO produtos (descricao, qtd, preco) VALUES ('{descricao}', {quantidade}, {preco})")
        mydb.commit()
        print("Produto adicionado com sucesso!")
    except:
        print("Um erro ocorreu e não foi possível adicionar produto!")

def listar_produtos():
    mycursor.execute("SELECT * FROM produtos")
    produtos_result = mycursor.fetchall()
    if not produtos_result:
        print("Lista de produtos está vazia!")
    else:
        for produto in produtos_result:
            print(f"ID: {produto[0]} | Descrição: {produto[1]} | Qtd: {produto[2]} | Preço: R${produto[3]}")
        input("Pressione Enter para voltar")

def alterar_produto(id):
    mycursor.execute(f"SELECT * FROM produtos WHERE ID = {id}")
    produto = mycursor.fetchone()
    if not produto:
        print("ID de produto não existe!")
        time.sleep(3)
    else:
        print(f"ID: {produto[0]} | Descrição: {produto[1]} | Qtd: {produto[2]} | Preço: R${produto[3]}")

        while True:
            print("O que deseja alterar do produto?")
            print("1 - Descrição")
            print("2 - Quantidade")
            print("3 - Preço")

            opcao = input("Opção: ")
            if opcao == '1':
                while True:
                    os.system('cls')
                    descricao = input("Nova descrição do produto: ")
                    if descricao == '':
                        print("Descrição inválida!")
                        time.sleep(3)
                    else:
                        try:
                            mycursor.execute(f"UPDATE produtos SET descricao = '{descricao}' WHERE id = {id} ")
                            mydb.commit()
                            print("Descrição atualizada com sucesso!")
                            time.sleep(3)
                            break
                        except:
                            print("Algum erro aconteceu e não foi possível atualizar descrição do produto")
                            time.sleep(3)
                            break
                break
            
            if opcao == '2':
                while True:
                    os.system('cls')
                    try:
                        quantidade = int(input("Quantidade do produto: "))
                        break
                    except:
                        print("Quantidade inválida!")
                        time.sleep(3)
                
                try:
                    mycursor.execute(f"UPDATE produtos SET qtd = {quantidade} WHERE id = {id} ")
                    mydb.commit()
                    print("Quantidade atualizada com sucesso!")
                    time.sleep(3)
                except:
                    print("Algum erro aconteceu e não foi possível atualizar quantidade do produto")
                    time.sleep(3)
                break

            if opcao == '3':
                while True:
                    os.system('cls')
                    try:
                        preco = float(input("Preço do produto: "))
                        break
                    except:
                        print("Preço inválido!")
                        time.sleep(3)
                
                try:
                    mycursor.execute(f"UPDATE produtos SET preco = {preco} WHERE id = {id} ")
                    mydb.commit()
                    print("Preço atualizado com sucesso!")
                    time.sleep(3)
                except:
                    print("Algum erro aconteceu e não foi possível atualizar preço do produto")
                    time.sleep(3)
                break
            

            time.sleep(3)

def remover_produto(id):
    mycursor.execute(f"SELECT * FROM produtos WHERE ID = {id}")
    produto = mycursor.fetchone()
    if not produto:
        print("ID de produto não existe!")
        time.sleep(3)
    else:
        print(f"ID: {produto[0]} | Descrição: {produto[1]} | Qtd: {produto[2]} | Preço: R${produto[3]}")
        while True:
            opcao = input("Deseja remover produto do estoque? (S/N) ")
            if opcao == 'S':
                try:
                    mycursor.execute(f"DELETE FROM produtos WHERE ID = {id}")
                    mydb.commit()
                    print("Produto removido com sucesso!")
                except:
                    print("Algum erro aconteceu e não foi possível remover produto")
                time.sleep(3)
                break
            if opcao == 'N':
                break
            else:
                print("Opção inválida!")
                time.sleep(3)