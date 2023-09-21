
import zooAnimales

class Animal():
    totalAnimal = 0


    def __init__(self,nombre,edad,habitat,genero,zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal.totalAnimal += 1
        self._zona = zona
        zona.agregarAnimales(self)

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad
    
    def getHabitat(self):
        return self._habitat
    
    def getGenero(self):
        return self._genero
    
    def getZona(self):
        return self._zona
    


    @classmethod
    def totalPorTipo(cls):
        m = zooAnimales.mamifero.Mamifero.cantidadMamiferos()
        a = zooAnimales.ave.Ave.cantidadAves()
        r = zooAnimales.reptil.Reptil.cantidadReptiles()
        p = zooAnimales.pez.Pez.cantidadPeces()
        an = zooAnimales.anfibio.Anfibio.cantidadAnfibios()

        return (f'Mamiferos : {m}\nAves : {a}\nReptiles : {r}\nPeces : {p}\nAnfibios : {an}')


    def toString(self):
        if self.getZona() == None:
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}"
        
        return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}, la zona en la que me ubico es {self.getZona()}, en el zoo {self.zona.getZoo()}"


