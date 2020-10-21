from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self,id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue):
        self.id = id
        self.origen_x = origen_x
        self.origen_y = origen_y
        self.destino_x = destino_x
        self.destino_y = destino_y
        self.velocidad = velocidad
        self.red = red
        self.green = green
        self.blue = blue
        self.distancia = distancia_euclidiana(origen_x,origen_y,destino_x,destino_y)

    def __str__(self):
        string = f'Id: {self.id}\n'
        string+= f'Origen x: {self.origen_x }\n'
        string+= f'Origen Y: {self.origen_y }\n'
        string+= f'Destino X: {self.destino_x }\n'
        string+= f'Destino Y: {self.destino_y }\n'
        string+= f'Velocidad: {self.velocidad }\n'
        string+= f'Rojo: {self.red }\n'
        string+= f'Verde: {self.green}\n'
        string+= f'Azul: {self.blue}\n'
        string+= f'Distancia: {self.distancia}\n'
        return string