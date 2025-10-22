class Pessoa: 
    def __init__(self, nome: str,  cpf: str) -> None:
        self.nome = nome
        self. cpf = cpf
    def apresentar(self) -> str:
        return f"Olá, eu sou {self.nome}"
    
class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: str, cpf: str) -> None:
        super().__init__(nome)
        super().__init__(cpf)
        self.matricula = matricula
        
    def apresentar(self):
        base = super().apresentar()
        return f"{base} e sou aluno, matrícula {self.matricula} e esse é o meu CPF: {self.cpf} "
  
pessoa = Pessoa("João")
aluno = Aluno("Ana", "A123" "432546865")

print(pessoa.apresentar())
print(aluno.apresentar())

class Professor(Pessoa):
     def __init__(self, nome: str, disciplina: str) -> None:
         super().__init__(nome)
         self.diciplina = disciplina
     
     def apresentar(self) -> str:
         return f"Professor {self.nome} de {self.diciplina}"
     

class BolsaMixin:
    def calcular_bolsa(self) -> float:
        return 1200.0
    
class alunoBolsista(BolsaMixin, Aluno):
    def presentar(self) -> str:
        base = super().apresentar()
        return f"{base} e recebo bolsa de R$ {self.calcular_bolsa():.2f}"
    