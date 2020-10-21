from particula import Particula

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