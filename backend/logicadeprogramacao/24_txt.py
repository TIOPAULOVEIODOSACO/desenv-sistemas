# 02 sou o dono de uma concessionaria e vi o sistema do dono da padaria. gostaria de um sistema igual para meus carros.


def menu():
    while True:
        print("\n======== MENU DE OPÇÕES ========")
        print("1 - Cadastrar veículo")
        print("2 - Listar veículos")
        print("3 - Alterar veículo")
        print("4 - Excluir veículo")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_veiculos()
        elif opcao == "2":
            listar_veiculos()
        elif opcao == "3":
            alterar_veiculos()
        elif opcao == "4":
            excluir_veiculos()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar_veiculos():
    try:
        with open("veiculos.txt", "a") as arquivo:
            modelo = input("Digite o modelo do veículo: ")
            marca = input("Digite a marca do veículo: ")
            ano = input("Digite o ano do veículo: ")
            cor = input("Digite a cor do veículo: ")
            preco = input("Digite o preço do veículo: R$ ")
            estoque = input("Digite a quantidade em estoque: ")
            
            arquivo.write(f"{modelo};{marca};{ano};{cor};{preco};{estoque}\n")
            print("Veículo cadastrado com sucesso!")
            
    except:
        print("Erro ao cadastrar veículo.")

def listar_veiculos():
    try:
        with open("veiculos.txt", "r") as arquivo:
            print("\n--- LISTA DE VEÍCULOS ---")
            for i, linha in enumerate(arquivo, 1):
                dados = linha.strip().split(";")
                print(f"{i} - Modelo: {dados[0]}, Marca: {dados[1]}, Ano: {dados[2]}")
                print(f"   Cor: {dados[3]}, Preço: R${dados[4]}, Estoque: {dados[5]}")
                print("   " + "-" * 40)
                
    except:
        print("Nenhum veículo cadastrado ainda.")

def alterar_veiculos():
    try:
        with open("veiculos.txt", "r") as arquivo:
            veiculos = arquivo.readlines()
            
        if not veiculos:
            print("Nenhum veículo cadastrado.")
            return
            
        print("\n--- ALTERAR VEÍCULO ---")
        for i, veiculo in enumerate(veiculos, 1):
            dados = veiculo.strip().split(";")
            print(f"{i} - {dados[0]} {dados[1]} ({dados[2]}) - R${dados[4]}")
            
        try:
            indice = int(input("Digite o número do veículo que deseja alterar: ")) - 1
            
            if 0 <= indice < len(veiculos):
                dados_antigos = veiculos[indice].strip().split(";")
                
                print("\nDeixe em branco para manter o valor atual")
                modelo = input(f"Novo modelo ({dados_antigos[0]}): ")
                marca = input(f"Nova marca ({dados_antigos[1]}): ")
                ano = input(f"Novo ano ({dados_antigos[2]}): ")
                cor = input(f"Nova cor ({dados_antigos[3]}): ")
                preco = input(f"Novo preço (R${dados_antigos[4]}): ")
                estoque = input(f"Nova quantidade ({dados_antigos[5]}): ")
                
                novo_modelo = modelo if modelo else dados_antigos[0]
                nova_marca = marca if marca else dados_antigos[1]
                novo_ano = ano if ano else dados_antigos[2]
                nova_cor = cor if cor else dados_antigos[3]
                novo_preco = preco if preco else dados_antigos[4]
                nova_quantidade = estoque if estoque else dados_antigos[5]
                
                veiculos[indice] = f"{novo_modelo};{nova_marca};{novo_ano};{nova_cor};{novo_preco};{nova_quantidade}\n"
                
                with open("veiculos.txt", "w") as arquivo:
                    arquivo.writelines(veiculos)
                    
                print("Veículo alterado com sucesso!")
            else:
                print("Número inválido.")
                
        except ValueError:
            print("Digite um número válido.")
            
    except:
        print("Erro ao alterar veículo.")

def excluir_veiculos():
    try:
        with open("veiculos.txt", "r") as arquivo:
            veiculos = arquivo.readlines()
            
        if not veiculos:
            print("Nenhum veículo cadastrado.")
            return
            
        print("\n--- EXCLUIR VEÍCULO ---")
        for i, veiculo in enumerate(veiculos, 1):
            dados = veiculo.strip().split(";")
            print(f"{i} - {dados[0]} {dados[1]} ({dados[2]}) - R${dados[4]}")
            
        try:
            indice = int(input("Digite o número do veículo que deseja excluir: ")) - 1
            
            if 0 <= indice < len(veiculos):
                veiculo_excluido = veiculos.pop(indice)
                
                with open("veiculos.txt", "w") as arquivo:
                    arquivo.writelines(veiculos)
                    
                dados_excluido = veiculo_excluido.split(";")
                print(f"Veículo '{dados_excluido[0]} {dados_excluido[1]}' excluído com sucesso!")
            else:
                print("Número inválido.")
                
        except ValueError:
            print("Digite um número válido.")
            
    except:
        print("Erro ao excluir veículo.")

# Iniciar o programa
menu()