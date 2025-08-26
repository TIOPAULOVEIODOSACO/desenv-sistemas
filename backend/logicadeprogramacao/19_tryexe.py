#crie uma lista com cadastro de usuario 
#cadastrar
#alterar
#excluir 
#listar
#usar (função, lista, try exept, laços)

usuarios = []

def cadastrar_usuario():
    try:
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        usuarios.append({"nome": nome, "idade": idade})
        print("Usuário cadastrado com sucesso!\n")
    except ValueError:
        print("Idade inválida. Tente novamente.\n")


def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
    else:
        print("Lista de usuários:")
        for indice, usuario in enumerate(usuarios):
            print(f"{indice} - Nome: {usuario['nome']}, Idade: {usuario['idade']}")
        print()


def alterar_usuario():
    try:
        listar_usuarios()
        indice = int(input("Digite o número do usuário que deseja alterar: "))
        if 0 <= indice < len(usuarios):
            novo_nome = input("Digite o novo nome: ")
            nova_idade = int(input("Digite a nova idade: "))
            usuarios[indice]["nome"] = novo_nome
            usuarios[indice]["idade"] = nova_idade
            print("Usuário alterado com sucesso!\n")
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Entrada inválida. Tente novamente.\n")


def excluir_usuario():
    try:
        listar_usuarios()
        indice = int(input("Digite o número do usuário que deseja excluir: "))
        if 0 <= indice < len(usuarios):
            usuarios.pop(indice)
            print("Usuário excluído com sucesso!\n")
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Entrada inválida. Tente novamente.\n")




menu()
