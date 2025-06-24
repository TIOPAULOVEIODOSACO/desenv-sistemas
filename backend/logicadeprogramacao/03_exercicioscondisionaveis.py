nota1 = int(input("Digite a sua Nota: "))
nota2 = int(input("Digite a sua Nota: "))
nota3 = int(input("Digite a sua Nota: "))
nota4 = int(input("Digite a sua Nota: "))

nota_final = (nota1 + nota2 + nota3 + nota4)/ 4
print("Sua nota foi: ", nota_final)

if  nota_final >= 80:
    print("Parabéns!")

elif (nota_final > 80 ) :
    print("pode melhorar!")

elif (nota_final <= 60):
    print("até ano que vem!")