from Client.customer import Cliente
from Components.components import Menu, Valida
from Json.jsonClass import JsonFile
from Utilities.utilities import (borrarPantalla,green_color,reset_color,blue_color,purple_color,red_color)

import datetime
import json
import os
import time


ruta_script = os.path.abspath(__file__)  # Ruta absoluta del script

ruta_padre = os.path.dirname(os.path.dirname(ruta_script))


class CrudClients():

    def create(self):
        borrarPantalla()
        validar = Valida()
        
        json_file = JsonFile(ruta_padre + "/Data/clients.json")

        dni = validar.cedula("Ingresa la cédula del cliente: ","Cedula invalida")

        client = json_file.find("cedula", dni)

        if client:
            print("Ya existe un cliente con el numero de cedula ingresado")
            return

        first_name = validar.solo_letras(mensaje="Ingrese el nombre", mensajeError="Solo se admiten letras")

        last_name = validar.solo_letras(mensaje="Ingrese el Apellido", mensajeError="Solo se admiten letras")

        cli = Cliente(id=dni,nombre=first_name,apellido=last_name)
        print(red_color + "¿Está seguro de guardar al cliente? (s/n): ", end="")
        procesar = input().lower()

        if procesar == "s":

            print("😊 Cliente Grabado satisfactoriamente 😊" + reset_color)
            cliente = json_file.read()
            data = cli.getJson()
            cliente.append(data)
            json_file.save(cliente)
            
        else:

            print("🤣 Creación de cliente cancelada 🤣" + reset_color)
        time.sleep(2)
        

    def delete(self):
        borrarPantalla()
        validar = Valida()
        dni = validar.cedula("Ingresa el numero de cedula para buscar el cliente: ","Numero de cedula invalido")
        ruta_archivo_clientes = ruta_padre + "/Data/clients.json"
        ruta_archivo_prestamo = ruta_padre + "/Data/prestamo.json"

        json_clientes = JsonFile(ruta_archivo_clientes)
        json_prestamo = JsonFile(ruta_archivo_prestamo)
        client_data = json_clientes.read()
        prestamo_data = json_prestamo.read()
        found_dni = json_clientes.find('cedula',dni)

        if found_dni:
            cliente_encontrado = found_dni[0]
            cliente_id = cliente_encontrado['cedula']

            prestamos_cliente = [prestamo for prestamo in prestamo_data if prestamo['cliente']['cedula'] == cliente_id]

            if prestamos_cliente:
                print(f"El cliente {cliente_encontrado['nombre']} {cliente_encontrado['apellido']} tiene un prestamo registrado, no se puede eliminar")
            else:
                # Eliminar el cliente de la lista de clientes
                client_data.remove(cliente_encontrado)
                # Guardar los cambios en el archivo de clientes
                json_clientes.save(client_data)
                print(f"El cliente {cliente_encontrado['nombre']} {cliente_encontrado['apellido']} fue eliminado con exito")
        else:
            print(f"El cliente {dni} no se encuentra registrado")

        time.sleep(2)
