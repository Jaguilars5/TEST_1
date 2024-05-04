class TipoPrestamo: # hipotecario, comercial, emprendimiento
    def __init__(self,id,descripcion):
        self.id=id
        self.descripcion = descripcion
    
    def getJson(self):
        return{
            "id":self.id,
            "descripcion":self.descripcion
        }