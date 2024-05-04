class Prestamo:
    def __init__(
        self,
        id,
        cliente,
        tipo_prestamo,
        fecha_prestamo,
        valor_prestamo,
        interes,
        valor_total,
        num_pagos,
    ):
        self.id = id
        self.cliente = cliente
        self.tipo_prestamo = tipo_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.valor_prestamo = valor_prestamo
        self.interes = interes
        self.valor_total = valor_total  # valor_prestamo*interes
        self.num_pagos = num_pagos
        self.detalleCuotasPrestamos = []

    def addDetalleCoutasPrestamo(self,detalleCoutas):
        self.detalleCuotasPrestamos=detalleCoutas

    def getJson(self):
        return {
            "id": self.id,
            "cliente": self.cliente,
            "tipo_prestamo": self.tipo_prestamo,
            "fecha_prestamo": self.fecha_prestamo,
            "valor_prestamo": self.valor_prestamo,
            "interes": self.interes,
            "valor_total": self.valor_total,
            "num_pagos": self.num_pagos,
            "detalleCuotasPrestamos": self.detalleCuotasPrestamos,
        }
