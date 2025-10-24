class User:
    def __init__(self, nome = None, email = None, cpf = None, senha = None):
        
        print("-------------------------------------------------------")
        
        if nome is None:
            nome = input("Digite seu nome de usuário: ")
        if email is None:
            email = input("Digete seu e-mail: ")
        if cpf is None:
            cpf = input("Digete seu CPF: ")
        if senha is None:
            senha = input("Digete sua senha: ")
            
        self.nome = nome
        self.email = email
        self.cpf = cpf 
        self.senha = senha
        
    def cadrastro(self):
        
        print("----------------------------------------------------")
        print("---------------- CADASTRO REALIZADO ----------------")
        print("----------------------------------------------------")
        
        print(f"Nome: {self.nome}\nE-mail: {self.email}\nCPF: {self.cpf}\nSenha: {self.senha}")
        print("----------------------------------------------------")
        
class Admin(User):
    def __init__(self, nome = None, email = None, cpf = None, senha = None, nomeEmpresa = None):
        
        print("-------------------------------------------------------")
        
        if nomeEmpresa is None:
            nomeEmpresa = input("Qual o nome da empresa: ")
        if nome is None:
            nome = input("Digite seu nome de usuário: ")
        if email is None:
            email = input("Digete seu e-mail: ")
        if cpf is None:
            cpf = input("Digete seu CPF: ")
        if senha is None:
            senha = input("Digete sua senha: ")
            
        super().__init__(nome, email, cpf, senha)
        self.nomeEmpresa = nomeEmpresa
            
    def login(self):
        
        if self.nome == "Eric" and self.email == "adm.1234@gmail.com" and self.cpf == "12332112345" and self.senha == "1234567":
            
            print("---------------- LOGIN ADMIN REALIZADO ----------------")
            print("-------------------------------------------------------")
            
            print (f"Bem-vindo querido(a) admin")
            print(f"Nome: {self.nome}\nE-mail: {self.email}\nCPF: {self.cpf}\nSenha: {self.senha}")
            print("-------------------------------------------------------")
        else:
            print("---------------- LOGIN ADMIN NEGADO ----------------")
            print("----------------------------------------------------")
            print("Ocorreu um erro! Algum dado está incorreto!")
            print("----------------------------------------------------")
            

def inicializar():
    escolha = int(input("Você quer se cadastrar ou logar como ADM? \nDigite 1 para cadastro e 2 para login ADM: "))
    
    if escolha == 1:
        user = User()
        user.cadrastro()
    if escolha == 2:
        admin = Admin()
        admin.login()
    if escolha != 1 and escolha != 2:
        print("----------------------------------------------------")
        print("Erro!")
        print("----------------------------------------------------")
        
inicializar()