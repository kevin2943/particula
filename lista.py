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

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration

    def sort(self, key, reverse=False):
        self.__particulas.sort(key=key, reverse=reverse)

    def getGraph(self):
        g = dict()
        for i in self.__particulas:
            u = ((i.origen_x, i.origen_y), i.distancia)
            v = ((i.destino_x, i.destino_y), i.distancia)
            if u[0] in g:
                g[u[0]].append(v)
            else:
                g[u[0]] = [v]

            if v[0] in g:
                g[v[0]].append(u)
            else:
                g[v[0]] = [u]
        return g