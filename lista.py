from particula import Particula
import json

class Lista:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0,particula)

    def __str__(self):
        string = ''
        for particula in self.__particulas:
            string += str(particula) + '\n'
        return string

    def guardar(self, ubicacion):
        try:
            with open(ubicacion,'w') as archivo:
                lista = [particula.to_dic() for particula in self.__particulas]
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas=[Particula(**particula) for particula in lista]
            return 1
        except:
            return 0