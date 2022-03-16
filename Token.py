class Token():
    lexema_valido = ''
    tipo = 0
    fila = 0
    columna = 0

    TIPO = 1
    VALOR = 2
    FONDO = 3
    NOMBRE = 4
    VALORES = 5
    EVENTO = 6
    PALABRAS = 7
    DESCONOCIDO = 8
    SIMBOLO = 9
    MAYOR = 10
    MENOR = 11
    CORCH_ABRE = 12
    CORCH_CIERRA = 13
    COMA = 14
    DOS_PUNTOS = 15
    CADENA = 16
    CADENA_SIMPLE = 17
    FORMULARIO = 18
    def __init__(self,lexma,tipo,fila,columna):
        self.lexema_valido = lexma
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def getLexema(self):
        return self.lexema_valido

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna

    def getTipo(self):
        if self.tipo == self.TIPO:
            return 'TIPO'
        elif self.tipo == self.VALOR:
            return 'VALOR'
        elif self.tipo == self.FONDO:
            return 'FONDO'
        elif self.tipo == self.NOMBRE:
            return 'NOMBRE'
        elif self.tipo == self.VALORES:
            return 'VALORES'
        elif self.tipo == self.EVENTO:
            return 'EVENTO'
        elif self.tipo == self.PALABRAS:
            return 'PALABRAS'
        elif self.tipo == self.DESCONOCIDO:
            return 'DESCONOCIDO'
        elif self.tipo == self.SIMBOLO:
            return 'SIMBOLO'
        elif self.tipo == self.MAYOR:
            return 'MAYOR'
        elif self.tipo == self.MENOR:
            return 'MENOR'
        elif self.tipo == self.CORCH_ABRE:
            return 'CORCH_ABRE'
        elif self.tipo == self.CORCH_CIERRA:
            return 'CORCH_CIERRA'
        elif self.tipo == self.COMA:
            return 'COMA'
        elif self.tipo == self.DOS_PUNTOS:
            return 'DOS_PUNTOS'
        elif self.tipo == self.CADENA:
            return 'CADENA'
        elif self.tipo == self.CADENA_SIMPLE:
            return 'CADENA_SIMPLE'
        elif self.tipo == self.FORMULARIO:
            return 'FORMULARIO'
        