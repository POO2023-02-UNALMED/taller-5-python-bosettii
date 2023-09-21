from zooAnimales.animal import Animal

class Anfibio(Animal):
    listado = []
    ranas = 0 
    salamandras = 0

    def __init__(self,nombre,edad,habitat,genero,colorPiel,venomoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel = colorPiel
        self._venomoso = venomoso
        Anfibio.listado.append(self)

    def getColorPiel(self):
        return self._colorPiel
    
    def isVenomoso(self):
        return self._venomoso
    

    @classmethod
    def cantidadAnfibios(cls):
        return cls.listado.__len__
    
    @ classmethod
    def crearRana(cls,nombre,edad,genero):
        c = "rojo"
        v = True
        h = "selva"
        cls.listado.append(Anfibio(nombre,edad,h,genero,c,v))
        cls.ranas +=1
        
    
    @ classmethod
    def crearRana(cls,nombre,edad,genero):
        c = "negro y amarillo"
        v = False
        h = "selva"
        cls.listado.append(Anfibio(nombre,edad,h,genero,c,v))
        cls.salamandras +=1
