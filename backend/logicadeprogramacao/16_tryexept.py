    #try/exept pode ser usado para a correção de codigos, ou seja quando tem um erro, chamados de exceções, podem interromper a execução do seu programa e mostrar mensagens estranhas para o usuário. 
    #TIPOS DE EXEÇÃO

    #TypeError: Ocorre quando uma operação ou função é aplicada a um objeto de tipo inadequado, como tentar somar um número e uma string. 

    #ZeroDivisionError: Lançada quando você tenta dividir um número por zero. 

    #TypeError: Ocorre quando uma operação ou função é aplicada a um objeto de tipo inadequado, como tentar somar um número e uma string. 

    #try:
    # Código que pode gerar um erro
    #except <TipoDeErro> as erro:
    # Código para tratar o erro
    #else:
    # Código executado se não ocorrer erro
    #finally:
    # Código que sempre será executado

    #Exemplo de TypeError: Tentando somar um número e uma string:   
    a = 10
    b = "texto"


    try:
        print(a + b)
        
    except TypeError as error:
        print(f"Erro: {error} - Não é possível somar tipos incompatíveis.")

#Exemplo de ZeroDivisionError Tentando dividir por zero
a = 10
b = 0

try:
    print(a / b)
except ZeroDivisionError as error:
    print(f"Erro: {error} - Não é possível dividir por zero.")



#Exemplo de IndexError Tentando acessar um índice fora do alcance de uma lista
lista = [1, 2, 3, 4, 5]
indice = 10

try:
    print(lista[indice])
except IndexError as error:
    print(f"Erro: {error} - Índice fora do alcance.")


# Testando a função
print(dividir(10, 2))  # Saída: 5.0
print(dividir(10, 0))  # Saída: Erro: division by zero - Não é possível dividir por zero.


    #tambem da para usar o finally e o else no try/exept

    

    a = 10
    b = 0

    try:
        print(a / b) # código que pode gerar um erro
    except ZeroDivisionError as error:
        print(f"Erro: {error}")# código a ser executado caso ocorra um erro
    else:#se não tiver erros
        print("Sem erros!")
    finally:
        print("Aqui sempre vai executar!")


