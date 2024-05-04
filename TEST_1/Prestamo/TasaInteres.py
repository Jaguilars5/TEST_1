class TasaInteres:
    def __init__(self, id,valor):
        self.id = id
        self.valor = valor # porcentaje de tasa de interes
        
    def getJson(self):
        return{
            "id":self.id,
            "valor":self.valor
        }