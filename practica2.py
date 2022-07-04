class NoSonDelMismoTipo(Exception):
    pass

class funciones():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def suma_ent(self):
        if isinstance(self.x,int) and isinstance(self.y,int):
            return self.x+self.y
        else:
            raise NoSonDelMismoTipo("No son los dos enteros")

    def resta_ent(self):
        if isinstance(self.x,int) and isinstance(self.y,int):
         return self.x-self.y
        else:
            raise NoSonDelMismoTipo("No son los dos enteros")

    def concatenacion_cadenas(self):
        if isinstance(self.x, str) and isinstance(self.y,str):
            return self.x+''+self.y
        else:
            raise NoSonDelMismoTipo("No son los dos cadenas de texto")
