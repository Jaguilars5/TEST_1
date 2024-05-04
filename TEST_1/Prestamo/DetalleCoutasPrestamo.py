class DetalleCoutasPrestamo:
    def __init__(self, id, fecha_pago, valor_cuota):
        self.id = id
        self.fecha_pago = fecha_pago
        self.valor_cuota = valor_cuota

    def getJson(self):
        return {
            "id": self.id,
            "fecha_pago ": self.fecha_pago,
            "valor_cuota": self.valor_cuota,
        }
