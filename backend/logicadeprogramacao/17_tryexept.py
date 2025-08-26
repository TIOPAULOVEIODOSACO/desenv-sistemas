#Usando (laços, função e try/except) crie um sistema para receber as 3 notas de um aluno
 #e calcule a media anual. Se digitar algo sem ser o numero tratar o erro.


def media():
    try:

        nota1 = float(input("Nota da 1 Prova: ")) 
        nota2 = float(input("Nota da 2 Prova: ")) 
        nota3 = float(input("Nota da 3 Prova: ")) 


        media = nota1 + nota2 + nota3 /3
        print("soma:", media)
     
     
     

        
    except TypeError as error:
        print(f"Erro: {error} - Não é possível somar tipos incompatíveis.")

    except ValueError:
        print("Erro: você digitou algo que não é um número.")

    except NameError as error:
        print(f"Erro: {error} - Variável não definida.")


media()