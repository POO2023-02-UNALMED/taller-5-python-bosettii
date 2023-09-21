class Zoologico() :

    def __init__(self,nombre,ubicacion):
        self._nombre = nombre
        self._ubicacion=ubicacion
        self._zona = []

    def getNombre(self):
        return self._nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def getZona(self):
        return self._zona
    
    def agregarZonas(self,zona):
        self._zona.append(zona)

    def cantidadTotalAnimales(self):
        total = 0
        for i in self._zona:
            total += i.cantidadAnimales()
        return total


    
