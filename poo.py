#Ejemplo de ejercicios que estan en las diapositivas que envio la instructora Sandra
#Ejemplo
class Estudiante:
 codigo=0
 nombre=""
 apellido=""
 def imprimir_Datos(self,codigo,nombre,apellido):
     print(self.codigo, self.nombre, self.apellido)
#crear objeto adso
adso=Estudiante()

#Accediendo a través del objeto adso a los atributos de la clase estudiante y dando valores
adso.codigo = 1
adso.nombre = 'Sandra'
adso.apellido='Cruz'
adso.imprimir_Datos()

#Clase Constructor
class Estudiante1:
    def __init__(self, codigo, nombre,apellido):
     self.codigo = codigo
     self.nombre = nombre
     self.apellido=apellido

    def imprimir_Informacion(self):
        print (self.codigo, self.nombre, self.apellido)
        
adso1 =Estudiante1(2,'Maria','Galindo')
adso1.imprimir_Informacion()
