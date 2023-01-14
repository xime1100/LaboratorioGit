listagatos = []

def printlista():
    for i in listagatos:    
        print(i)

class gato:
    def __init__(self):
        self.__nombre = ""
        self.__color = ""
        self.__edad = 0

    @property
    def nombre(self):
        return self.__nombre

    @property
    def color(self):
        return self.__color 

    @property
    def edad(self):
        return self.__edad

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre     

    @edad.setter
    def edad(self, nuevo_anio):
        self.__edad = nuevo_anio 

    @color.setter
    def color(self, nuevo_color):
        self.__color = nuevo_color 

    def __str__(self):
        output = f"{self.nombre}, {self.edad} annos, color: {self.color}"
        return output

    def aniadirlista(self):
        listagatos.append(self)
        





