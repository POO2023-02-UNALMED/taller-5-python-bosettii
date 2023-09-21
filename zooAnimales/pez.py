from zooAnimales.animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    @classmethod
    def cantidadPeces(cls):
        return cls.listado.__len__
    
    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        color = "rojo"
        cantidad = 6
        h = "oceano"
        cls.listado.append(Pez(nombre,edad,h,genero,color,cantidad))
        cls.salmones +=1

    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        color = "gris"
        cantidad = 6
        h = "oceano"
        cls.listado.append(Pez(nombre,edad,h,genero,color,cantidad))
        cls.bacalaos +=1


