from lib2to3.pgen2 import token
from Token import Token

class Analizador:
    lexema = ''
    tokens= []
    estado = 1
    fila = 1
    columna = 1
    generar = False
    

    def __init__(self, entrada):
        self.estado = 1
        self.lexema = ''
        self.tokens = []
        self.fila = 1
        self.columna = 1
        self.generar = True
        tipos = Token("lexema", -1, -1, -1)

        entrada = entrada + '#'
        actual = ''
        longitud = len(entrada)

        for i in range(longitud):
            actual = entrada[i]
            
            if self.estado == 1:
                if actual.isalpha():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual == '"':
                    self.estado = 3
                    self.columna += 1
                    self.lexema += actual
                elif actual == "'":
                    self.estado = 4
                    self.columna += 1 
                    self.lexema +=actual
                elif actual == '~':
                    self.columna +=1
                    self.lexema += actual
                    self.AgregarToken(tipos.SIMBOLO)
                elif actual == '>':
                    self.columna +=1
                    self.lexema += actual
                    self.AgregarToken(tipos.MAYOR)
                elif actual == '<':
                    self.columna += 1
                    self.lexema += actual
                    self.AgregarToken(tipos.MENOR)
                elif actual == '[':
                    self.columna += 1
                    self.lexema += actual
                    self.AgregarToken(tipos.CORCH_ABRE)
                elif actual == ']':
                    self.columna += 1
                    self.lexema += actual
                    self.AgregarToken(tipos.CORCH_CIERRA)
                elif actual == ':':
                    self.columna += 1
                    self.lexema += actual
                    self.AgregarToken(tipos.DOS_PUNTOS)
                elif actual == ',':
                    self.columna +=1
                    self.lexema += actual
                    self.AgregarToken(tipos.COMA)
                elif actual == ' ':
                    self.columna +=1
                    self.estado = 1
                elif actual == '\n':
                    self.fila += 1
                    self.estado = 1
                    self.columna = 1
                elif actual =='\r':
                    self.estado = 1
                elif actual == '\t':
                    self.columna += 5
                    self.estado = 1
                elif actual == '#' and i ==longitud - 1:
                    print('Analisis terminado')
                else:
                    self.lexema += actual
                    self.AgregarToken(tipos.DESCONOCIDO)
                    self.columna += 1
                    self.generar = False
                
            
            elif self.estado == 2:
                if actual.isalpha():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    continue
                else:
                    if self.Reservada():
                        self.AgregarToken(self.tipo)
                        i -= 1
                        continue
                    else:
                        self.AgregarToken(tipos.PALABRAS)
                        i -= 1
                        continue   

            elif self.estado == 3:
                if actual != '"':
                    self.estado = 3
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual == '"':
                    self.estado = 4
                    self.columna += 1
                    self.lexema += actual
                    self.AgregarToken(tipos.CADENA)

            elif self.estado == 4:
                if actual != "'":
                    self.estado = 4    
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual == "'":
                    self.estado = 4
                    self.lexema += actual
                    self.AgregarToken(tipos.CADENA_SIMPLE) 

    
    def AgregarToken(self,tipo):
        self.tokens.append(Token(self.lexema, tipo, self.fila, self.columna))
        self.lexema = ""
        self.estado = 1


    def Reservada(self):
        palabra = self.lexema.upper();
        #lista_palabras = ['TIPO', 'VALOR','FONDO','NOMBRE','VALORES', 'EVENTO', 'FORMULARIO']
        if palabra == 'TIPO':
            self.tipo = Token.TIPO  
            return True
        if palabra == 'VALOR':
            self.tipo = Token.VALOR 
            return True
        if palabra == 'FONDO':
            self.tipo = Token.FONDO
            return True
        if palabra == 'NOMBRE':
            self.tipo = Token.NOMBRE
            return True
        if palabra == 'VALORES':
            self.tipo = Token.VALORES
            return True
        if palabra == 'EVENTO':
            self.tipo = Token.EVENTO
            return True
        if palabra == 'FORMULARIO':
            self.tipo = Token.FORMULARIO
            return True
        return False

    def Imprimir(self):
        print("---Tokens---")
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if x.tipo != tipos.DESCONOCIDO:
                print(x.getLexema()," --> ",x.getTipo(),' --> ',x.getFila(), ' --> ',x.getColumna())
    

    def ImprimirErrores(self):
        print("---TokensErrores---")
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if x.tipo == tipos.DESCONOCIDO:
                print(x.getLexema()," --> ",x.getFila(), ' --> ',x.getColumna(),'--> Error Lexico')

    def reporteTokens(self):

        print("Se ha generado el reporte")
        f = open('ReporteTokens.html','w')
        f.write("<!doctype html>")
        f.write("<html lang=\"en\">")
        f.write("<head>")
        f.write("<!-- Required meta tags -->")
        f.write(" <meta charset=\"utf-8\">")
        f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
        f.write("<!-- Bootstrap CSS -->")
        f.write("<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We\" crossorigin=\"anonymous\">")
        f.write("<title>Reporte Tokens</title>")
        f.write("<style>table, th, td {border: 1px solid black; text-align: center}""</style>")
        f.write("</head>")
        f.write("<body>")
        f.write("<H1 style=\"color:white; background-color:teal\">\n<center> REPORTE TOKENS</center>\n</H1>\n")
        f.write("<h3>Roberto Gómez - 202000544</h3>")
        f.write("<center><table><tr><th>Posicion</th><th>Token</th><th>Precio</th><th>Fila</th><th>Columna</th></tr>")
        j=1
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if x.tipo != tipos.DESCONOCIDO:
                f.write("<tr class=\"table-primary\">")
                f.write("<center><td><h4>"+ str(j) +"</h4></td>"+"<td><h4>" +x.getLexema() +"</h4></td>"+"<td><h4>"+ str(x.getTipo())+"</h4></td>"+"<td><h4>"+ str(x.getFila())+"</h4></td>"+ "<td><h4>"+str(x.getColumna())+"</h4></td></center>")
                f.write("</tr>")
            j+=1
        f.write("</table></center>")
        f.write("<!-- Optional JavaScript; choose one of the two! -->")
        f.write("<tr class=\"table-primary\">")
        f.write(" <!-- Option 1: Bootstrap Bundle with Popper -->")
        f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj\" crossorigin=\"anonymous\"></script>")
        f.write("<!-- Option 2: Separate Popper and Bootstrap JS -->")
        f.write(" <!--")
        f.write("<script src=\"https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js\" integrity=\"sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp\" crossorigin=\"anonymous\"></script>")
        f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js\" integrity=\"sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/\" crossorigin=\"anonymous\"></script>")
        f.write("-->")
        f.write("</body>")
        f.write("</html>")
        f.close()

    def reporteErorres(self):
        
        print("Se ha generado el reporte")
        f = open('ReporteErrores.html','w')
        f.write("<!doctype html>")
        f.write("<html lang=\"en\">")
        f.write("<head>")
        f.write("<!-- Required meta tags -->")
        f.write(" <meta charset=\"utf-8\">")
        f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
        f.write("<!-- Bootstrap CSS -->")
        f.write("<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We\" crossorigin=\"anonymous\">")
        f.write("<title>Reporte Errores</title>")
        f.write("<style>table, th, td {border: 1px solid black; text-align: center}""</style>")
        f.write("</head>")
        f.write("<body>")
        f.write("<H1 style=\"color:white; background-color:teal\">\n<center> REPORTE ERRORES</center>\n</H1>\n")
        f.write("<h3>Roberto Gómez - 202000544</h3>")
        f.write("<center><table><tr><th>Posicion</th><th>Token</th><th>Precio</th><th>Fila</th><th>Columna</th></tr>")
        j=1
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if x.tipo == tipos.DESCONOCIDO:
                f.write("<tr class=\"table-primary\">")
                f.write("<center><td><h4>"+ str(j) +"</h4></td>"+"<td><h4>" +x.getLexema() +"</h4></td>"+"<td><h4>"+ str(x.getTipo())+"</h4></td>"+"<td><h4>"+ str(x.getFila())+"</h4></td>"+ "<td><h4>"+str(x.getColumna())+"</h4></td></center>")
                f.write("</tr>")
            j+=1
        f.write("</table></center>")
        f.write("<!-- Optional JavaScript; choose one of the two! -->")
        f.write("<tr class=\"table-primary\">")
        f.write(" <!-- Option 1: Bootstrap Bundle with Popper -->")
        f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj\" crossorigin=\"anonymous\"></script>")
        f.write("<!-- Option 2: Separate Popper and Bootstrap JS -->")
        f.write(" <!--")
        f.write("<script src=\"https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js\" integrity=\"sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp\" crossorigin=\"anonymous\"></script>")
        f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js\" integrity=\"sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/\" crossorigin=\"anonymous\"></script>")
        f.write("-->")
        f.write("</body>")
        f.write("</html>")
        f.close()