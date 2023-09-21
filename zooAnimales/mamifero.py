from zooAnimales.animal import Animal


class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0


    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)

    def isPelaje(self):
        return self._pelaje
    
    def getPatas(self):
        return self._patas
    
    @ classmethod
    def cantidadMamiferos(cls):
        return cls.caballos + cls.leones
    
    @ classmethod
    def crearCaballo(cls,nombre,edad,genero):
        p = 4
        h = "pradera"
        pel = True
        cls.listado.append(Mamifero(nombre,edad,genero,p,h,pel))
        cls.caballos +=1

    @ classmethod
    def crearLeon(cls,nombre,edad,genero):
        p = 4
        h = "selva"
        pel = True
        cls.listado.append(Mamifero(nombre,edad,genero,p,h,pel))
        cls.caballos +=1