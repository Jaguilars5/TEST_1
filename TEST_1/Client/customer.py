class Cliente:
    def __init__(self,id, nombre,apellido):
        self.cedula = id
        self.nombre = nombre
        self.apellido=apellido
        
    def getJson(self):
        return{
            "cedula":self.cedula,
            "nombre":self.nombre,
            "apellido":self.apellido
        }