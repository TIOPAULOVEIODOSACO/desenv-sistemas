#trabalhando com arquvios

#with open ('comprastxt,'w')

#w abrir o arquivo no modo de escrita (apaga tudo que ta escrito)
#a abrir no modo edição (so vai adicionar)
#r abrir no modo leitura

with open ("tarefas.txt","w") as arquivo:
    arquivo.write("lavar a louça \n")
    arquivo.write("lavar quintal")


#ler o arquivo

with open ("compras.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#ler o arquivo por linha

with open ("compras.txt", "r")as arquivo:
    for produto in arquivo:
    print("produto"produto.strip())

#acrescentar dados ao final

with open ("compras.txt","a")as arquivo:
    arquivos.write("arroz")

#crie um arquivo de nome.txt
#arquivoe 5 alunos no arquivo
#confira abrindo o arquivo se eescreven
#leia o arquivo e faça o print de cada aluno no terminal




with open ("nome.txt","w") as arquivo:
    arquivo.write("vitor \n")
    arquivo.write("breno \n")
    arquivo.write("magni \n")
    arquivo.write("agner \n")
    arquivo.write("guilherme \n")
