#tarea_Figuras

# cree un programa, siguiendo el paradigma de programacion orientada a objetos
# que permita calcular el volume de una de las figuras geometrico: esfera,cilindro,cono

class Figura(object):
    pi = 0
    radio = 0
    altura = 0

    def __init__(self, altura, radio):
        self.altura = altura
        self.radio = radio

class Esfera(Figura):
    pi = 3.1416
    radio_esfera = float(input("INTRODUZCA RADIO DE ESFERA: "))
    area_esfera = 4 * pi * radio_esfera ** 2
    volumen_esfera = (pi * radio_esfera ** 3) / 3
    print("AREA DE LA ESFERA ES: ", area_esfera)
    print("VOLUMEN DE LA ESFERA ES: ", volumen_esfera)

print(" ")
class Cilindro(Figura):
    pi = 3.1416
    radio_cilindro = float(input("INTRODUZCA RADIO DE CILINDRO: "))
    altura = float(input("INTRODUZCA ALTURA DEL CILINDRO"))
    area_cilindro = (2 * pi * radio_cilindro) * (radio_cilindro + altura)
    print("VOLUMEN DE EL CILINDRO ES: ", area_cilindro )

print(" ")
class Cono(Figura):
    pi = 3.1416
    radio_cono = float(input("INTRODUZCA RADIO DEL CONO: "))
    area = float(input("INTRODUZCA ALTURA DEL CONO"))
    area_cono = (((radio_cono ** 2) * pi) * area) / 3
    print("EL VOLUMEN DE EL CILINDRO ES: ", area_cono )
