class Medico:
    def FalarComPaciente(self):
        print("O medico esta falando com um paciente")
        
class Enfermeira:
    def FalarComPaciente(self):
        print("A enfermeira(o) esta falando com um paciente")
        
class Residente:
    def FalarComPaciente(self):
        print("O Residente esta falando com um residente")
    
    
def FalarComPaciente(obj):
    obj.FalarComPaciente()
    
m = Medico()
e = Enfermeira()
r = Residente()

FalarComPaciente(m)
FalarComPaciente(e)
FalarComPaciente(r)


print("----------------------- OUTRO -----------------------------")

objetos = [Medico(), Enfermeira(), Residente()]

for i in objetos:
    i.FalarComPaciente()
        