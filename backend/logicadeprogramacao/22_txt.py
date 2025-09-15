def menu():
    while True:
        print("\n======== MENU DE OPÇÕES ========")
        print("1 - Cadastrar produtos")
        print("2 - Listar produtos")
        print("3 - Alterar produtos")
        print("4 - Excluir produtos")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_produtos()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            alterar_produtos()
        elif opcao == "4":
            excluir_produtos()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar_produtos():
    try:
        with open("produtos.txt", "a") as arquivo:
            nome = input("Digite o nome do produto: ")
            preco = input("Digite o preço do produto: ")
            quantidade = input("Digite a quantidade em estoque: ")
            
            arquivo.write(f"{nome};{preco};{quantidade}\n")
            print("Produto cadastrado com sucesso!")
            
    except:
        print("Erro ao cadastrar produto.")

def listar_produtos():
    try:
        with open("produtos.txt", "r") as arquivo:
            print("\n--- LISTA DE PRODUTOS ---")
            for linha in arquivo:
                dados = linha.strip().split(";")
                print(f"Nome: {dados[0]}, Preço: R${dados[1]}, Estoque: {dados[2]}")
                
    except:
        print("Nenhum produto cadastrado ainda.")

def alterar_produtos():
    try:
        with open("produtos.txt", "r") as arquivo:
            produtos = arquivo.readlines()
            
        if not produtos:
            print("Nenhum produto cadastrado.")
            return
            
        print("\n--- ALTERAR PRODUTO ---")
        for i, produto in enumerate(produtos):
            dados = produto.strip().split(";")
            print(f"{i+1} - {dados[0]} (R${dados[1]}, Estoque: {dados[2]})")
            
        try:
            indice = int(input("Digite o número do produto que deseja alterar: ")) - 1
            
            if 0 <= indice < len(produtos):
                nome = input("Novo nome (deixe em branco para manter): ")
                preco = input("Novo preço (deixe em branco para manter): ")
                quantidade = input("Nova quantidade (deixe em branco para manter): ")
                
                dados_antigos = produtos[indice].strip().split(";")
                
                novo_nome = nome if nome else dados_antigos[0]
                novo_preco = preco if preco else dados_antigos[1]
                nova_quantidade = quantidade if quantidade else dados_antigos[2]
                
                produtos[indice] = f"{novo_nome};{novo_preco};{nova_quantidade}\n"
                
                with open("produtos.txt", "w") as arquivo:
                    arquivo.writelines(produtos)
                    
                print("Produto alterado com sucesso!")
            else:
                print("Número inválido.")
                
        except ValueError:
            print("Digite um número válido.")
            
    except:
        print("Erro ao alterar produto.")

def excluir_produtos():
    try:
        with open("produtos.txt", "r") as arquivo:
            produtos = arquivo.readlines()
            
        if not produtos:
            print("Nenhum produto cadastrado.")
            return
            
        print("\n--- EXCLUIR PRODUTO ---")
        for i, produto in enumerate(produtos):
            dados = produto.strip().split(";")
            print(f"{i+1} - {dados[0]} (R${dados[1]}, Estoque: {dados[2]})")
            
        try:
            indice = int(input("Digite o número do produto que deseja excluir: ")) - 1
            
            if 0 <= indice < len(produtos):
                produto_excluido = produtos.pop(indice)
                
                with open("produtos.txt", "w") as arquivo:
                    arquivo.writelines(produtos)
                    
                print(f"Produto '{produto_excluido.split(';')[0]}' excluído com sucesso!")
            else:
                print("Número inválido.")
                
        except ValueError:
            print("Digite um número válido.")
            
    except:
        print("Erro ao excluir produto.")

# Iniciar o programa
menu()