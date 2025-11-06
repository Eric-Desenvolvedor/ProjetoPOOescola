class Pagamento:       
    def __init__(self, nome: str = None, cpf_numero: str = None, valor: str = None):
        self.nome = nome
        self.cpf_numero = cpf_numero
        self.valor = valor
        
    def metodo(self):
        print("Selecione um método de pagamento: ")
        
class Pix(Pagamento):  
    def metodo(self):
        print("Pix - 1")
        
    def pagar(self, nome: str = None, cpf_numero: str = None, valor: str = None):
        
        if nome is None:
            nome = input("Qual o nome da conta: ")
        if cpf_numero is None:
            cpf_numero = input("Digite o número ou CPF da conta: ")
        if valor is None:
            valor = input("Digite o valor da compra: ")
            
        super().__init__(nome, cpf_numero, valor)
        
    def enviar(self):
        return "Pagado com SUCESSO!"
        
class CartaoDebito(Pagamento):
    def metodo(self):
        print("Debito - 2")
    
    def pagar(self, nome: str = None, numeroConta: str = None, valor: str = None):
        
        if nome is None:
            nome = input("Digite o nome da conta: ")
        if numeroConta is None:
            numeroConta = input("Digite o número da conta: ")
        if valor is None:
            valor = input("Digite o valor da compra: ")
            
        super().__init__(nome, valor)
        self.numeroConta = numeroConta
        
    def enviar(self):
        return "Pagado com SUCESSO!"
        
class CartaoCredito(Pagamento):
    def metodo(self):
        print("Crédito - 3")
        
    def pagar(self, nome: str = None, numeroConta: str = None, valor: str = None, parcelas: int = None):
        
        if nome is None:
            nome = input("Digite o nome da conta: ")
        if numeroConta is None:
            numeroConta = input("Digite o número da conta: ")
        if valor is None:
            valor = input("Digite o valor da compra: ")
        if parcelas is None:
            parcelas = input("Digite a quantidade de parcelas: ")
            
        super().__init__(nome, valor)
        self.numeroConta = numeroConta
        self.parcelas = parcelas
        
    def enviar(self):
        return "Pagado com SUCESSO! Aguardando próximos pagamentos."
        
class Boleto(Pagamento):
    def metodo(self):
        print("Boleto - 4")
        
    def pagar(self, nome: str = None, numeroConta: str = None, valor: str = None, parcelas: int = None):
        
        if nome is None:
            nome = input("Digite o nome da conta: ")
        if valor is None:
            valor = input("Digite o valor da compra: ")
            
        super().__init__(nome, valor)
        self.numeroConta = numeroConta
        
    def enviar(self):
        return "Pagado com SUCESSO!"
        
metodos = [Pagamento(), Pix(), CartaoDebito(), CartaoCredito(), Boleto()]

for i in metodos:
    i.metodo()
    
numeroEscolha = int(input("Escolha um desses métodos: "))

if numeroEscolha == 1:
    print("---------------------------------------------------------")
    p = Pix()
    p.pagar()
    print("---------------------------------------------------------")
    print(p.enviar())
    print("---------------------------------------------------------")
    
elif numeroEscolha == 2:
    print("---------------------------------------------------------")
    cd = CartaoDebito()
    cd.pagar()
    print("---------------------------------------------------------")
    print(cd.enviar())
    print("---------------------------------------------------------")
    
elif numeroEscolha == 3:
    print("---------------------------------------------------------")
    cc = CartaoCredito()
    cc.pagar()
    print("---------------------------------------------------------")
    print(cc.enviar())
    print("---------------------------------------------------------")
    
elif numeroEscolha == 4:
    print("---------------------------------------------------------")
    b = Boleto()
    b.pagar()
    print("---------------------------------------------------------")
    print(b.enviar())
    print("---------------------------------------------------------")
    
else:
    print("Err0!")