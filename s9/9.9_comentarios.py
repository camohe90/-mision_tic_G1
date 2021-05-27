#Comentario de una lindea antes de codigo principal
def funcion(primer_parametro, segundo_parametro):
    """Que se utiliza para describir que hace la funcion

    primer_parametro -- Descripcion de ese paramatreo
    segundo_parametro -- Descrpcion de ese parametro"""


def quadratica(a, b ,c , x):
    """Resolver ecuacionas cuadraticas mediante la formula 
    x**2 + bx +c = 0
    Siempre voy a tener dos soluciones x_1 y x2"""

    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)
    return x_1, x_2
