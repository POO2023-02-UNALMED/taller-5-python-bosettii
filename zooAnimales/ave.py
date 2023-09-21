from zooAnimales.animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)

    def getColorPlumas(self):
        return self._colorPlumas
    
    @classmethod
    def cantidadAves(cls):
        return cls.halcones + cls.aguilas
    
    @ classmethod
    def crearHalcon(cls,nombre,edad,genero):
        c = "cafe glorioso"
        h = "montanas"
        cls.listado.append(Ave(nombre,edad,h,genero,c))
        cls.halcones +=1

    @ classmethod
    def crearAguila(cls,nombre,edad,genero):
        c = "blanco y amarillo"
        h = "montanas"
        cls.listado.append(Ave(nombre,edad,h,genero,c))
        cls.aguilas +=1

    

