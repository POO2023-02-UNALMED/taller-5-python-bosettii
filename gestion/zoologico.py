class Zoologico() :

    def __init__(self,nombre,ubicacion,zona = None):
        self._nombre = nombre
        self._ubicacion=ubicacion
        
        if zona == None:
            zona = []
        
        self._zona = zona

    def getNombre(self):
        return self._nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def getZona(self):
        return self._zona
    
    def agregarZona(self,zona, lista = None):
        if lista == None:
            lista = []
        lista.append(zona)

    def cantidadTotalAnimales(self):
        total = 0
        for i in range(self.zona.__len__):
            total = total +self.getZona()[i].cantidadAnimales


    
