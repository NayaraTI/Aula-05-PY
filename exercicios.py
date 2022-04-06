#################################################################
##################### Exercicio 1 #################################

class Bairro():
    pass

bairro1= Bairro()

print(bairro1)

print(type(bairro1))



###################### Exercicio 2 ########################

class Bairro1():
    def __init__(self):
        self.nomebairro= 'Kobrasol'
        self.rua= 'Koesa'
        
    def imprime(self):
        print('Esse bairro é %s e a rua é%s'%(self.nomebairro,self.rua))
        
bairro2= Bairro1()

print(bairro2.nomebairro)
print(bairro2.rua)



######################## Exercicio 3 ##########################

class Bairro2():
    def __init__(self,nomebairro,rua):
        self.nomebairro= nomebairro
        self.rua= rua
        
    def imprime(self):
        print('Esse bairro é %s, e essa rua é %s'%(self.nomebairro,self.rua))
        
bairro3= Bairro2('Campinas','Josué di Bernardi')

bairro4= Bairro2('Capoeiras','Irmã Bonavita')

print(bairro3.nomebairro)
print(bairro4.rua)
print(bairro3.rua)
print(bairro4.nomebairro)

bairro3.imprime()
bairro4.imprime()


    
        
