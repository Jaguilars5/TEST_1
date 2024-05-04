from Components.components import Menu
from Utilities.utilities import borrarPantalla
from Crud.crudClients import CrudClients
from Crud.crudPrestamo import CrudPrestamo
import time


def MenuMain():

    menuOption = ""

    while menuOption != "4":

        borrarPantalla()

        menu_main = Menu(
            "Menu Facturación",
            [
                "1) Ingreso de prestamos",
                "2) Consulta de los prestamos",
                "3) Eliminar Clientes",
                "4) Ingreso de clientes",
                "5) Salir",
            ],
        )

        menuOption = menu_main.menu()

        if menuOption == "1":
            prestamo = CrudPrestamo()
            prestamo.create()

        elif menuOption == "2":
            prestamo = CrudPrestamo()
            prestamo.consult()
            
        elif menuOption == "3":
            client = CrudClients()
            client.delete()
            
        elif menuOption == "4":
            client = CrudClients()
            client.create()

        print("Regresando al menu Principal...")

    borrarPantalla()

    input("Presione una tecla para salir...")

    borrarPantalla()


MenuMain()
