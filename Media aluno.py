aluno1 = str(input("digite seu nome: "))
an1 = float(input("Digite a primeira nota > "))
an2 = float(input("Digite a segunda nota > "))

aluno2 = str(input("digite seu nome: "))
an3 = float(input("Digite a primeira nota > "))
an4 = float(input("Digite a segunda nota > "))

media1 = (an1 + an2) / 2
media2 = (an3 + an4) / 2
print(f"A média de {aluno1} foi {media1}, e a média de {aluno2} foi {media2}.")

print("o historico de notas dos alunos ficou:")
print(f"{aluno1}  e  {aluno2}")
print(f"{an1}  e  {an3} na primeira avaliação")
print(f"{an2}   e  {an4} na segunda avaliação")
print(f"{media1}  e  {media2} na média")
if media1 > media2:
    print(f"{aluno1} tirou a maior nota")
else:
    print(f"{aluno2} tirou a maior nota")
