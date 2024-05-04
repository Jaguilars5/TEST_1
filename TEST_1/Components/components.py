from Utilities.utilities import borrarPantalla
import time
from Utilities.utilities import borrarPantalla, green_color, reset_color, blue_color, purple_color, red_color


class Menu:
    def __init__(self, titulo="", opciones=[]):
        self.titulo = titulo
        self.opciones = opciones


    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input(f"Elija opcion[1...{len(self.opciones)}]: ")
        return opc


class Valida:
    def solo_numeros(self, mensaje, mensajeError):
        while True:
            valor = input(f"          ------>   | {mensaje} ")
            try:
                valor_int = int(valor)
                if valor_int > 0:
                    return valor_int
                else:
                    print("          ------><  |", mensajeError)
            except ValueError:
                print("          ------><  |", mensajeError)

    def solo_letras(self, mensaje, mensajeError):
        while True:
            valor = input(f"          ------>   | {mensaje} ")
            if valor.isalpha():
                return valor
            else:
                print("          ------><  |", mensajeError)

    def solo_decimales(self, mensaje, mensajeError):
        while True:
            valor = input(f"          ------>   | {mensaje} ")
            try:
                valor_float = float(valor)
                if valor_float > 0:
                    return valor_float
                else:
                    print("          ------><  |", mensajeError)
            except ValueError:
                print("          ------><  |", mensajeError)

    def cedula(self, mensaje, mensajeError):
        while True:
            cedula = input(f"          ------>   | {mensaje}")
            
            if len(cedula) == 10 and cedula.isdigit():
                coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
                suma = 0
                
                for i in range(9):
                    digito = int(cedula[i]) * coeficientes[i]
                    if digito > 9:
                        digito -= 9
                    suma += digito
                
                total = suma % 10
                if total != 0:
                    total = 10 - total
                
                if total == int(cedula[9]):
                    return cedula
            
            print("          ------><  |", mensajeError)
