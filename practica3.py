class NoSonDelMismoTipo(Exception):
    """Capturamos con esta clase la excepción que pueda salir en la clase funciones

    Args:
        Exception (Excepción): Excepción
    """
    pass

class funciones():
    """Clase funciones con la que podremos realizar diversas funciones 

    Atributos:
    ==========
    x:
        Primer valor a operar
    y:
        Segundo valor a operar
    
    Métodos:
    ========
    **suma_ent**:
        Método para *sumar* dos valores enteros
    **resta_ent**:
        Método para *restar* dos valores enteros
    **concatenacion_cadenas**:
        Método para *concatenar* dos cadenas

    Ejemplos:
    =========

    >>>> ``suma_ent(2,3)``
    >>>> ``resta_ent(8,5)``
    >>>> ``concatenacion_cadenas("hola", "a todos")``
    """
    def __init__(self,x,y):
        """Función de inicializa

        Args:
            x (int o str ): Entero o string dependiendo de la función
            y (int o str): Entero o string dependiendo de la función
        """
        self.x=x
        self.y=y
    def suma_ent(self):
        """Generamos la suma de los dos argmentos pasados a la clase si son los dos de tipo entero

        Raises:
            NoSonDelMismoTipo: Lanza una excepción cuando los datos no son de tipo entero

        Returns:
            int: Devuelve un tipo entero que es la suma de los dos argumentos 
        """
        if isinstance(self.x,int) and isinstance(self.y,int):
            return self.x+self.y
        else:
            raise NoSonDelMismoTipo("No son los dos enteros")

    def resta_ent(self):
        """Generamos la resta de los dos argumentos pasados a la clase si son los dos de tipo entero

        Raises:
            NoSonDelMismoTipo: Lanza una excepción cuando los datos no son de tipo entero

        Returns:
            int: Devuelve un tipo entero que es la resta de los dos argumentos
        """
        if isinstance(self.x,int) and isinstance(self.y,int):
         return self.x-self.y
        else:
            raise NoSonDelMismoTipo("No son los dos enteros")

    def concatenacion_cadenas(self):
        """GEneramos una cadena final producto de la concatenación de las cadenas pasadas a la clase

        Raises:
            NoSonDelMismoTipo: Lanza una excepción cuando los dos argumentos de la clase no son cadenas de texto

        Returns:
            str: Devuelve un tipo cadena de texto que es la concatenación de los dos argumentos
        """
        if isinstance(self.x, str) and isinstance(self.y,str):
            return self.x+''+self.y
        else:
            raise NoSonDelMismoTipo("No son los dos cadenas de texto")
