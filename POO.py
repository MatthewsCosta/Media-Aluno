class Aluno:
    def __init__(self, nome, n1, n2):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.media = (n1 + n2) / 2


aluno1 = Aluno("matheus", 10, 15)
print(aluno1.nome)
print(aluno1.media)
