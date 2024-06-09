aluno1 = input("digite seu nome: ")
an1 = int(input("Digite a primeira nota > "))
an2 = int(input("Digite a segunda nota > "))

aluno2 = input("digite seu nome: ")
an3 = int(input("Digite a primeira nota > "))
an4 = int(input("Digite a segunda nota > "))

media1 = (an1+an2)/2
media2 = (an3+an4)/2
print(f"A média de {aluno1} foi {media1}, e a média de {aluno2} foi {media2}.")

if media1 > media2:
    print (f"{aluno1} tirou a maior nota")
else:
    print (f"{aluno2} tirou a maior nota")