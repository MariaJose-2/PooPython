#Ejercicios Propuestos

#Definicion de la clase avion
class Avion:
    #metodo __init__, constructor de la clase avion
    def __init__(self, fabricante, modelo, capacidadPasajeros):
        #inicializacion de atributos con los valores proporcionados
        self.fabricante = fabricante
        self.modelo = modelo
        self.capacidadPasajeros = capacidadPasajeros

#metodo para mostrar la informacion del avion
    def mostrarInformacion(self):
        #imprime la informacion utilizando atributos de la instancia
        print(f"Avion: {self.fabricante}, {self.modelo}, Capacidad de pasajeros: {self.capacidadPasajeros}")

#creacion de una instancia de la clase Avion(objeto avion1)
avion1 = Avion("Boeing", "747", "416")

#acceso al atributo 'fabricante' del objeto avion1 e impresión
print(avion1.fabricante)  #imprime:Boeing

#llamada al metodo 'mostrarInformacion' del objeto avion1
avion1.mostrarInformacion()  #imprime: Avion: Boeing, 747, capacidad de pasajeros: 416