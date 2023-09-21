from zooAnimales.animal import Animal

class Zona():

    animales = []

    def __init__(self,nombre,zoo = None):
        self._nombre=nombre
        if zoo == None:
            zoo = []
        self._zoo=zoo
        
    def getNombre(self):
        return self._nombre
    
    def getZoo(self):
        return self._zoo
    
    def agregarAnimales(self,animal,lista = None):
        if lista == None:
            lista = []
        lista.append(animal)

    @ classmethod
    def cantidadAnimales(cls):
        return cls.animales.__len__
