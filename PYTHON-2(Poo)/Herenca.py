class Pessoa: 
    def __init__(self, nome: str,  cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf
    def apresentar(self) -> str:
        return f"Olá, eu sou {self.nome} e esse é o meu CPF: {self.cpf}"
    
class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: str, cpf: str) -> None:
        super().__init__(nome, cpf)
        self.matricula = matricula
        
    def apresentar(self):
        base = super().apresentar()
        return f"{base} e sou aluno, matrículado(a) {self.matricula}."
  
class Professor(Aluno):
     def __init__(self, nome: str = None, matricula: str = None, disciplina: str = None, cpf: str = None):
        
        if nome is None:
            nome = input("Digite o seu nome: ")
        if matricula is None:
            matricula = input("Digite a sua matrícula: ")
        if disciplina is None:
            disciplina = input("Digite sua disciplina: ")
        if cpf is None:
            cpf = input("Qual o seu CPF: ")
            
        super().__init__(nome, matricula, cpf)
        self.diciplina = disciplina
     
     def apresentar(self) -> str:
         return f"\nProfessor {self.nome} de {self.diciplina}, matrícula {self.matricula} e CPF {self.cpf} \n -----------------------------------------------------------------------------"
     
class Aluno(Aluno):
    def __init__(self, nome: str = None, matricula: str = None, cpf: str = None):
        
         if nome is None:
             nome = input("digite seu nome: ")
         if matricula is None:
             matricula = input("qual e sua matricula: ")
         if cpf is None:
             cpf = input("coloque seu cpf: ")
         
         super().__init__(nome, matricula, cpf)
        
    def apresentar(self) -> str:
         return f"\n o aluno {self.nome},sua matricula {self.matricula} e CPF {self.cpf} \n -----------------------------------------------------------------------------"        
        



# class BolsaMixin:
#     def calcular_bolsa(self) -> float:
#         return 1200.0
    
# class alunoBolsista(BolsaMixin, Aluno):
#     def presentar(self) -> str:
#         base = super().apresentar()
#         return f"{base} e recebo bolsa de R$ {self.calcular_bolsa():.2f}"
   
   
# pessoa = Pessoa("João", "62768495379")
# aluno = Aluno("Ana", "123456789", "43254686545")

# print(pessoa.apresentar())
# print(aluno.apresentar())


professor = Professor()
print(professor.apresentar())

Aluno = Aluno()
print(Aluno.apresentar())