from abc import ABC, abstractmethod

class IAnimal(ABC):
    
    @abstractmethod
    def falar(self):
        """defina na classe filha"""
     
    @abstractmethod   
    def andar(self):       
        """"defina na classe filha"""
    
    
class Cachorro(IAnimal):
    def falar(self):
        print("auau") 
        
    def andar(self):
        print("ando com 4 patas")  
        
    
    

class Pessoa:
    
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade
        self.__humano = True
        
    def fala_pessoa(self):
        print("falando")
        
    
pingo = Cachorro()
pingo.falar()



