class Nota:
    
    def __init__(self, nota=None):

        if nota is None:
            
            nota = int(input("Digite sua nota: "))
        
        self.__nota = nota
        
    @property
    def suaNota(self):
        return self.__nota
    
    @suaNota.setter
    def suaNota(self, newValor):
        if newValor >= 0 and newValor <= 10:
            self.__nota = newValor
        else:
            print("Err0: Valor inválido!")
            
    def atualizarNotaPonto(self, newValor):
        if newValor >= 0 and newValor <= 3 and self.__nota <= 10:
            self.__nota += newValor
            
            if self.__nota > 10:
                self.__nota = 10
            
        elif newValor > 3:
            print("Err0!")
            
nota = Nota()
print("sua nota é: ", nota.suaNota)

nota.suaNota = 9
print("Sua nota após tentativa de mudar: ", nota.suaNota)

nota.atualizarNotaPonto(3)
print("Sua nota atualizada é: ", nota.suaNota)