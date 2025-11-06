class Pato: 
    def quack(self):
        print("O pato faz Quack!")
        
class Pessoa:
    def quack(self):
        print("A pessoa imita um pato: Quack!")
        
    def comer(self):
        print("A pessoa está comendo.")

def fazer_quack(obj):
    obj.quack()

p = Pato()
h = Pessoa()

fazer_quack(p)
fazer_quack(h)

class Gravacao:
    def quack(self):
        print("Som gravado! Quack quack!")

class Robo:
    def quack(self):
        print("Robô: Q-U-A-C-K em som metálico!")

print("-------------------------- OUTRA FORMA ------------------------------")


objetos = [Pato(), Pessoa(), Gravacao(), Robo()]

for obj in objetos:
    obj.quack()