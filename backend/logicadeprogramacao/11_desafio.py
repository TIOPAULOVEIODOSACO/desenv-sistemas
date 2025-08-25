#criar função de opções e pedir a opção desejada ao usuario
#criar função de depósito
#criar função de saque
#criar função de ver saldos 
#ao digitar "sair" encerrar o programa

def menu():
    print("======== MENU DE OPÇÕES ========\n")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Ver saldo")
    print( "Sair\n")
    while opcao != "sair":
        
        
        opcao = input("Escolha uma opção: ")
        
        if opcao = "1":
            valor_deposito = float(input("Digite o valor do depósito:"))
            saldo = saldo_total + valor_deposito

        elif opcao = "2":
            valor_saque = float(input("Digite o valor do saque: R$"))
            sacar(saldo)

        elif opcao = "3":
            ver_saldo(saldo)

        elif opcao = "sair":
            print("Saindo...")

            break
        else:
            print("Opção inválida. Tente novamente.")

def depositar(saldo):
    deposito = input("valor do depósito:")
    saldo =+ deposito
   

def sacar(saldo, valor_saque):
    if valor_saque > saldo:
        print("Saldo insuficiente para realizar o saque.")
    else:
        saldo -= valor_saque
        print("Saque realizado com sucesso de R$:", saldo)

    saldo = saldo_total - valor_saque

def ver_saldo(saldo):
    print("Seu saldo atual é:", saldo)

    
    

