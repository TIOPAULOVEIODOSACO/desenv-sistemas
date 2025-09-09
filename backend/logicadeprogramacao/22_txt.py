# # eu, como dono de uma padaria quero um sistema de onde eu possa adastrar meus produtos,alem de poder listar , alterar em caso de error, 
# # e excluir quando acabar o estoque.Quero tambem que tenha um menu onde eu possa ver as opções possiveis


def menu():
    print("======== MENU DE OPÇÕES ========\n")
    print("1 - cadastro de produtos")
    print("2 -Sair")

    
    while opcao != "2":
        
        
        opcao = input("Escolha uma opção: ")
        
        if opcao = "1":
            cadastrar_produtos()

        if opcao = "2":
            excluir _produtos()

        elif opcao = "3":
            print("Saindo...")

            break
        else:
            print("Opção inválida. Tente novamente.")


def cadastrar_produtos():

    with open ("nome.txt","a") as produto:
        produto.write input("Digite o Nome do Produto \n")
        print("produto adicionado", produto)
    


        try:
            produto = input("Digite o nome do produto: ")
            
        except TypeError:
            print("Apenas letras. Tente novamente.\n")


def excluir_produtos():
    with open (excluir.txt)

    try:





    except

 
 








