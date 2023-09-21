from zooAnimales.animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0
    
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)
   
    def getColorEscamas(self):
        return self._colorEscamas
    
    def getLargoCola(self):
        return self._largoCola

    @classmethod
    def cantidadReptiles(cls):
        return cls.listado.__len__
    
    @classmethod
    def crearIguana(cls,nombre,edad,genero):
        color = "verde"
        l = 3
        h = "humedal"
        cls.listado.append(Reptil(nombre,edad,h,genero,color,l))
        cls.iguanas +=1

    @classmethod
    def crearSerpiente(cls,nombre,edad,genero):
        color = "blanco"
        l = 1
        h = "jungla"
        cls.listado.append(Reptil(nombre,edad,h,genero,color,l))
        cls.serpientes +=1