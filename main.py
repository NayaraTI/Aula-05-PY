## Arquivo principal para importar módulos e classes ###

from classe_carros import Carros

## Instanciar objetos da classe importada Carros

carro1= Carros('Chevete','Chevrolet')
carro2= Carros('Ranger','Ford')

## Exibir os valores

print(carro1.modelo)
print(carro2.marca)

## Chamar os métodos

carro1.descricaocarro()

## Exibir um atributo de Classe
print(carro1.cor)

# Forma correta de exibir atributo de Classe
print(Carros.cor)

### Exibir as instancias dos objetos com o método mágico  __dict__  (dicionário)

print(carro1.__dict__)

print(carro2.__dict__)

print(Carros.__dict__)