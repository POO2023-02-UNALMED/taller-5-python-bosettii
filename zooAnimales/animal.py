
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil

class Animal():
    totalAnimal = 0


    def __init__(self,nombre,edad,habitat,genero,zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal.totalAnimal += 1
        self._zona = zona

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
    
    @ classmethod
    def totalPorTipo(self):
        return ("Mamiferos: " + Mamifero.cantidadMamiferos()+"\nAves: "+ Ave.cantidadAves() + "\nReptiles: " + Reptil.cantidadReptiles() + "\nPeces: " + Pez.cantidadPeces() + "\nAnfibios: " + Anfibio.cantidadAnfibios())

    def toString(self):
        if self.getZona() == None:
            return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + self.getEdad() + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero()
        
        return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + self.getEdad() + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero() + ", la zona en la que me ubico es" + self.getZona() + ", en el zoo" + self.zona.getZoo()


