class Zona():

    animales = []

    def __init__(self,nombre,zoo = None):
        self._nombre=nombre
        self._zoo=zoo
        
    def getNombre(self):
        return self._nombre
    
    def getZoo(self):
        return self._zoo
    
    def agregarAnimales(self,animal,lista = None):
        if lista == None:
            lista = []
        lista.append(animal)

    def cantidadAnimales(self):
        return (len(self._animales))
