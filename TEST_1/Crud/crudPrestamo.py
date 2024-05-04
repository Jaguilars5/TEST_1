from Client.customer import Cliente
from Components.components import Menu, Valida
from datetime import date, timedelta
from Json.jsonClass import JsonFile
from Prestamo.DetalleCoutasPrestamo import DetalleCoutasPrestamo
from Prestamo.TasaInteres import TasaInteres
from Prestamo.TipoPrestamo import TipoPrestamo
from Prestamo.prestamo import Prestamo
from Utilities.utilities import borrarPantalla, green_color, reset_color, blue_color, purple_color, red_color
import json
import os
import time

# Obtiene la ruta del archivo actual
ruta_script = os.path.abspath(__file__)  # Ruta absoluta del script
ruta_padre = os.path.dirname(os.path.dirname(ruta_script))


class CrudPrestamo:

    def create(self):
        validador = Valida()
        borrarPantalla()
        ruta_archivo_clientes = ruta_padre + "/Data/clients.json"
        ruta_archivo_tipo_prestamo = ruta_padre + "/Data/tipoPrestamo.json"
        ruta_archivo_tasas_interes = ruta_padre + "/Data/tasas_interes.json"
        ruta_archivo_prestamo = ruta_padre + "/Data/prestamo.json"

        json_clientes = JsonFile(ruta_archivo_clientes)
        json_tipo_prestamo = JsonFile(ruta_archivo_tipo_prestamo)
        json_tasas_interes = JsonFile(ruta_archivo_tasas_interes)
        json_prestamo = JsonFile(ruta_archivo_prestamo)

        cedula_cliente = validador.cedula("Ingresa la cédula del cliente: ", "Cedula inválida")
        cliente = json_clientes.find("cedula", cedula_cliente)

        if not cliente:
            print("No existe ningún cliente con ese número de cédula")
            time.sleep(2)
            return

        tipos_prestamo = json_tipo_prestamo.read()
        if tipos_prestamo:
            opciones_tipos_prestamo = [f"\t{tipo['id']}) {tipo['descripcion']}" for tipo in tipos_prestamo]

            menu_tipos_prestamo = Menu("\tSeleccione el tipo de préstamo:", opciones_tipos_prestamo)

            id_tipo_prestamo_seleccionado = int(menu_tipos_prestamo.menu())

            tipo_prestamo_seleccionado = json_tipo_prestamo.find("id", id_tipo_prestamo_seleccionado)

            if tipo_prestamo_seleccionado:
                tipo_prestamo = TipoPrestamo(tipo_prestamo_seleccionado[0]["id"], tipo_prestamo_seleccionado[0]["descripcion"])
                cliente_actual = Cliente(cliente[0]["cedula"], cliente[0]["nombre"], cliente[0]["apellido"])
                fecha_prestamo = date.today()
                fecha_prestamo_str = fecha_prestamo.strftime("%d/%m/%Y")
                valor_prestamo = validador.solo_decimales("Ingrese el valor del préstamo", "El valor ingresado es inválido")

                tasa_interes_seleccionada = json_tasas_interes.find("id", id_tipo_prestamo_seleccionado)

                tasa_interes = TasaInteres(tasa_interes_seleccionada[0]["id"], tasa_interes_seleccionada[0]["valor"])

                valor_total = valor_prestamo * (1 + tasa_interes.getJson()['valor'] / 100)
                valor_total = round(valor_total, 3)

                num_pagos = validador.solo_numeros("Ingrese el número de pagos", "El valor ingresado es inválido")

                valor_cuota = valor_total / num_pagos

                detalles_cuotas = []

                for i in range(1, num_pagos + 1):
                    # Calcular cuántos meses han pasado desde que se inició el préstamo
                    months_passed = i % 12
                    # Calcular cuántos años han pasado en total
                    years_passed = i // 12
                    # Calcular el nuevo año
                    new_year = fecha_prestamo.year + years_passed
                    # Calcular el nuevo mes
                    new_month = fecha_prestamo.month + months_passed
                    # Ajustar el mes y el año si el mes excede 12
                    if new_month > 12:
                        new_year += 1
                        new_month -= 12
                    # Crear la fecha de pago de la cuota
                    fecha_pago_cuota = date(new_year, new_month, fecha_prestamo.day)
                    fecha_pago_cuota_str = fecha_pago_cuota.strftime("%d/%m/%Y")
                    detalle_cuota = DetalleCoutasPrestamo(id=i, fecha_pago=fecha_pago_cuota_str, valor_cuota=valor_cuota)
                    detalles_cuotas.append(detalle_cuota.getJson())


                json_prestamo_data=json_prestamo.read()
                
                if json_prestamo_data:
                    ult_id = json_prestamo_data[-1]["id"] + 1
                else:
                    ult_id = 1
                    
                prestamo = Prestamo(id=ult_id, cliente=cliente_actual.getJson(), tipo_prestamo=tipo_prestamo.getJson(), fecha_prestamo=fecha_prestamo_str, valor_prestamo=valor_prestamo, interes=tasa_interes.getJson(), valor_total=valor_total, num_pagos=num_pagos)
                detalles_prestamo = prestamo.addDetalleCoutasPrestamo(detalleCoutas=detalles_cuotas)

                prestamo_json = prestamo.getJson()
                json_prestamo_data.append(prestamo_json)
                json_prestamo.save(json_prestamo_data)
            else:
                print("El tipo ingresado es inválido")
                time.sleep(2)
                return
        else:
            print("No se pudo encontrar el archivo")
            time.sleep(2)


    def consult(self):
        borrarPantalla()
        validar = Valida()
        ruta_archivo_prestamo = ruta_padre + "/Data/prestamo.json"
        json_prestamo = JsonFile(ruta_archivo_prestamo)

        prestamos_data = json_prestamo.read()

        # Menú de selección
        print("1. Consultar préstamo por ID")
        print("2. Mostrar todos los préstamos")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = validar.solo_numeros("Ingrese el ID del préstamo: ", "El ID ingresado es inválido")

            prestamo_id = json_prestamo.find("id", id)

            if prestamo_id is not None:
                prestamo_encontrado = False
                for prestamo in prestamos_data:
                    if prestamo["id"] == prestamo_id[0]["id"]:
                        prestamo_encontrado = True
                        print("Detalles del Préstamo:")
                        print("--------------------------------------")
                        print("ID de Préstamo:", prestamo["id"])
                        print("Cliente:", prestamo["cliente"]["nombre"], prestamo["cliente"]["apellido"])
                        print("Fecha del Préstamo:", prestamo["fecha_prestamo"])
                        print("Valor del Préstamo:", prestamo["valor_prestamo"])
                        print("Tipo de Préstamo:", prestamo["tipo_prestamo"]["descripcion"])
                        print("Número de Pagos:", prestamo["num_pagos"])
                        print("--------------------------------------")
                        break
                if not prestamo_encontrado:
                    print("No se encontró ningún préstamo con el ID proporcionado.")
            else:
                print("No se encontró ningún préstamo con el ID proporcionado.")
        elif opcion == "2":
            if prestamos_data:
                print("Listado de Préstamos:")
                for prestamo in prestamos_data:
                    print("--------------------------------------")
                    print("ID de Préstamo:", prestamo["id"])
                    print("Cliente:", prestamo["cliente"]["nombre"], prestamo["cliente"]["apellido"])
                    print("Fecha del Préstamo:", prestamo["fecha_prestamo"])
                    print("Valor del Préstamo:", prestamo["valor_prestamo"])
                    print("Tipo de Préstamo:", prestamo["tipo_prestamo"]["descripcion"])
                    print("Número de Pagos:", prestamo["num_pagos"])
                    print("--------------------------------------")
            else:
                print("No hay préstamos registrados.")
        else:
            print("Opción no válida.")

        input("\nPresiona Enter para volver al menú principal.")





# Código para probar la clase CrudPrestamo
if __name__ == "__main__":
    crud_prestamo = CrudPrestamo()
    crud_prestamo.create()
