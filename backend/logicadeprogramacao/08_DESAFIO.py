senhaincorreta  = input("Digite a Senha correta:")
senha = input ("Digite sua Senha: ")
nome = input ("Digite seu Nome: ")
salario = float(input("Digite seu salário: "))

while senha != senhaincorreta:
     
     print("senha incorreta")
     input("Digite a senha correta:")

print("Bem-vindo!", nome)
SalárioAnual = salario * 12
if (SalárioAnual>100000):
    print("rico")
else:
    print("Faz o L")
