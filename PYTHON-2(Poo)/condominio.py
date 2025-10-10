class Condominio:
    def __init__(self, apartamento=None, estacionamento=None, AreaLazer=None):
        self.apartamento = apartamento
        self.estacionamento = estacionamento
        self.AreaLazer = AreaLazer
        
    def pergunta(self):
        self.apartamento = input("Qual o número do apartamento: ")
        self.estacionamento = input("Tem direito a estacionamento: ")
        self.AreaLazer = input("Qual(is) a(s) área(s) de lazer disponível(is): ")
        
        return f"------------------------------------------\n O número do apartamento é: {self.apartamento}\n Direito a estacionamento: {self.estacionamento}\n Área(s) disponível(is): {self.AreaLazer}\n------------------------------------------"
    
cdA = Condominio()
print(cdA.pergunta())

class Residente:
    def __init__(self, nome=None, Numeroapatamento=None, pet=None):
        self.nome = nome
        self.numeroapatamento = Numeroapatamento
        self.pet = pet 
    
    def pergunta(self):
        self.nome  = input("qual o nome do residente: ")
        self.numeroapatamento = input("qual o numero do APÊ que voce mora: ")
        self.pet = input("voce possui algum pet em seu APÊ: ")
        
        return f"------------------------------------------\n O nome do residente é: {self.nome}\n mora no APÊ: {self.numeroapatamento}\n possui pet: {self.pet}\n------------------------------------------"
   
re = Residente()
print(re.pergunta())    

class ResidenteConvidado:
    
     def __init__(self, bloco=None, apartamento = None, NomedoResidente = None, SeuNome = None ):
         self.bloco = bloco
         self.apartamento = apartamento
         self.NomedoResidente = NomedoResidente
         self.SeuNome = SeuNome
         
     def inf(self):
         self.NomedoResidente = input("Qual é o nome do residente que lhe convidou? ")
         self.bloco = input("Qual é o bloco do residente? ")
         self.apartamento = input("Qual é o numero do apartamento? ")
         self.SeuNome = input("Qual é o seu nome? ")
             
         return f"------------------------------------------\n O nome da pessoa que lhe convidou é {self.NomedoResidente}. O bloco é {self.bloco}. O numero do apartamento é {self.apartamento} e o seu nome é {self.SeuNome}\n------------------------------------------"
        
Rcnv = ResidenteConvidado()
print(Rcnv.inf())