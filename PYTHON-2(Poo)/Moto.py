class Moto:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        
    def acelerar(self, valor):
        self.velocidade += valor
        print (f"Esse é o modelo da moto: {self.modelo}. Acelerou {self.velocidade} km/h ")
        
        
    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"Esse é o modelo da moto: {self.modelo}. Desacelerou {self.velocidade} km/h")
        
    
    def detalhes(self):
        return (f"Modelo: {self.modelo}. Marca: {self.marca}. Ano: {self.ano}. Cor: {self.cor}. Velocidade: {self.velocidade}Km/h") 
        

        
moto1 = Moto("Toyota", "Corolla", 2020, "Preto")
moto2 = Moto("Ducati", "Panigale", 2021, "Vermelho e preto")




print("-----------------------------------------------------------------------------")

moto1.acelerar(50)
moto2.acelerar(40)

print("-----------------------------------------------------------------------------")

moto1.frear(20)
moto2.frear(15)

print("-----------------------------------------------------------------------------")

print(moto1.detalhes())
print(moto2.detalhes())

print("-----------------------------------------------------------------------------")
