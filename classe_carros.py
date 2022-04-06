### Arquivo para a criação da Classe Carros ###

class Carros():
    # Atributos de classe são escritos fora do método construtor
    cor= 'Branco'
    
    
    def __init__(self,marca,modelo):
        self.marca= marca
        self.modelo= modelo
        
    def descricaocarro(self):
        print('Esse carro é {self.marca} e o modelo é {self.modelo}')