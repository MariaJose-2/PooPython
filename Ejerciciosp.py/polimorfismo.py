#definicion de la clase base Animal
class Animal:
    #metodo sonido sin implementacion(abstracto)
    def sonido(self):
        pass

#definicion de la clase derivada Perro que hereda de Animal
class Perro(Animal):
    #implementacion del metodo sonido (para no utilizar el metodo init) especifica para Perro
    def sonido(self):
        return "Guau"

#definicion de la clase derivada Gato que hereda de Animal
class Gato(Animal):
    #implementacion del metodo sonido especifica para Gato
    def sonido(self):
        return "Miau"

#funcion que utiliza polimorfismo
def hacerSonar(animal):
    #llamada al metodo sonido del objeto animal (polimorfismo)
    return animal.sonido()

#creacion de instancias de las clases derivadas Perro y Gato
perro = Perro()
gato = Gato()
#llamadas a la funcion hacerSonar con diferentes instancias
#imprime: Guau, ya que se llama al metodo sonido de la clase Perro
print(hacerSonar(perro))

#imprime: Miau, ya que se llama al metodo sonido de la clase Gato
print(hacerSonar(gato))