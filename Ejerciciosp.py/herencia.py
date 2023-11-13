# Definicion de la clase Computadora
class Computadora:
    #metodo especial __init__, constructor de la clase
    def __init__(self, marca, modelo):
        #inicializacion de atributos con los valores proporcionados
        self.marca = marca
        self.modelo = modelo

    #metodo para mostrar informacion de la computadora
    def mostrarInformacion(self):
        #imprime informacion utilizando atributos de la instancia
        print(f"Computadora: {self.marca} {self.modelo}")

#Definicion de la clase derivada Laptop que hereda de Computadora
class Laptop(Computadora):
    #metodo especial __init__, constructor de la clase Laptop
    def __init__(self, marca, modelo, pantallaSize):
        
        #llamada al constructor de la clase base Computadora
        super().__init__(marca, modelo)
        
        #inicializacion de un nuevo atributo especifico de Laptop que sera el tamaño de la pantalla
        self.pantallaSize = pantallaSize

    #metodo para mostrar informacion de la laptop (sobrescribe el metodo en la clase base)
    def mostrarInformacion(self):
        
        #llamada al metodo de la clase base Computadora
        super().mostrarInformacion()
        
        #imprime informacion adicional especifica de Laptop
        print(f"Tamaño de pantalla: {self.pantallaSize} pulgadas")

#creacion de una instancia de la clase derivada Laptop (objeto laptop1)
laptop1 = Laptop("Dell", "XPS 13", 13.3)

#llamada al metodo 'mostrarInformacion' del objeto laptop1
laptop1.mostrarInformacion()