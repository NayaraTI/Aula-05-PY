####### Por convenção sempre define uma classe com letra maiúscula #######
##########################################################################

class Livro():
    pass

## Instanciar um objeto

livro1= Livro()

print(livro1)

print(type(livro1))


### Criar uma classe com método mágico __init__ (método construtor)

class Livro1():
    def __init__(self):
        self.titulo= 'Curso de Python'
        self.autor =' Guido Van Rossum'
        
    def imprime(self):
        print('Esse livro é %s e o Autor %s'%(self.titulo,self.autor))   ## % pra vincular a variável na string
        

## Instanciar o objeto

livro2= Livro1()

## Listar os atributos do objeto
print(livro2.autor)
print(livro2.titulo)

## Listar o método

livro2.imprime()


### Classes com atributos em namespace variável ###

class Livro2():
    def __init__(self,titulo,autor):
        self.titulo =titulo
        self.autor =autor
        
    def imprime(self):
            print('Esse livro é %s e o Autor %s'%(self.titulo,self.autor))
            

## Instanciando(criando os objetos)

livro3= Livro2('Aprendendo a Cozinhar','O Chefe')

livro4= Livro2('Construindo Navios','O Marinheiro')

## Mostrar os atributos

print(livro4.autor)
print(livro3.titulo)


##  Chamar os métodos

livro3.imprime()
livro4.imprime()