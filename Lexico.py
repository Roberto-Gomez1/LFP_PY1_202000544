from Token import Token
from formm import lista

class Analizador:
    lexema = ''
    tokens= []
    estado = 1
    fila = 1
    columna = 1
    generar = False
    lista=[]
    var_aux=''
    def __init__(self, entrada):
        self.var_aux = entrada
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
                        self.AgregarToken(tipos.DESCONOCIDO)
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

    
    def guardarDatos(self):
        tipos = Token("lexema", -1, -1, -1)
        for x in range(len(self.tokens)):
            aux = self.tokens[x].getLexema()
            aux1 = aux.replace('"','').lower()
            if aux1 == 'etiqueta':
                aux_tipo = "etiqueta"
                aux_valor = self.tokens[x+3].getLexema().replace('"',"")
                self.lista.append(lista(aux_tipo,aux_valor,"","","",""))
            elif aux1 == "texto":
                aux_tipo = 'texto'
                aux_valor = self.tokens[x+3].getLexema().replace('"',"")
                aux_fondo = self.tokens[x+6].getLexema().replace('"',"")
                #print(aux_fondo)
                self.lista.append(lista(aux_tipo,aux_valor,aux_fondo,"","",""))
            elif aux1 == "grupo-radio":
                aux_valores=[]
                aux_tipo = 'grupo-radio'
                aux_nombre = self.tokens[x+3].getLexema().replace('"',"")
                contador = x+7
                if self.tokens[contador].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador].getLexema().replace("'",""))
                if self.tokens[contador+2].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+2].getLexema().replace("'",""))
                if self.tokens[contador+4].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+4].getLexema().replace("'",""))
                if self.tokens[contador+6].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+6].getLexema().replace("'",""))
                if self.tokens[contador+8].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+8].getLexema().replace("'",""))
                if self.tokens[contador+10].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+10].getLexema().replace("'",""))
                if self.tokens[contador+12].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+12].getLexema().replace("'",""))
                if self.tokens[contador+14].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+14].getLexema().replace("'",""))
                if self.tokens[contador+16].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+16].getLexema().replace("'",""))
                if self.tokens[contador+18].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+18].getLexema().replace("'",""))
                #if self.tokens[contador+20].tipo == tipos.CADENA_SIMPLE:
                    #aux_valores.append(self.tokens[contador+20].getLexema().replace("'",""))
                #print(aux_valores)
                self.lista.append(lista(aux_tipo,"","",aux_nombre,aux_valores,""))
            elif aux1 == "grupo-option":
                aux_valores=[]
                aux_tipo = 'grupo-option'
                aux_nombre = self.tokens[x+3].getLexema().replace('"',"")
                contador = x+7
                if self.tokens[contador].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador].getLexema().replace("'",""))
                if self.tokens[contador+2].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+2].getLexema().replace("'",""))
                if self.tokens[contador+4].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+4].getLexema().replace("'",""))
                if self.tokens[contador+6].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+6].getLexema().replace("'",""))
                if self.tokens[contador+8].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+8].getLexema().replace("'",""))
                if self.tokens[contador+10].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+10].getLexema().replace("'",""))
                if self.tokens[contador+12].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+12].getLexema().replace("'",""))
                if self.tokens[contador+14].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+14].getLexema().replace("'",""))
                if self.tokens[contador+16].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+16].getLexema().replace("'",""))
                if self.tokens[contador+18].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+18].getLexema().replace("'",""))
                #if self.tokens[contador+20].tipo == tipos.CADENA_SIMPLE:
                    #aux_valores.append(self.tokens[contador+20].getLexema().replace("'",""))
                #print(aux_valores)
                self.lista.append(lista(aux_tipo,"","",aux_nombre,aux_valores,""))
            elif aux1 == "boton":
                aux_tipo ='boton'
                aux_valor = self.tokens[x+3].getLexema().replace('"',"")
                aux_evento = self.tokens[x+6].getLexema().replace('"',"")
                print(aux_evento)
                self.lista.append(lista(aux_tipo,aux_valor,"","","",aux_evento))




                


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
    
    def generacion(self):
        print("formulario creado")
        f = open('Formulario.html','w')
        f.write("<!doctype html>")
        f.write("<html lang=\"en\">")
        f.write("<head>")
        f.write("<!-- Required meta tags -->")
        f.write(" <meta charset=\"utf-8\">")
        f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
        f.write("<!-- Bootstrap CSS -->")
        f.write("<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We\" crossorigin=\"anonymous\">")
        f.write("<title>Formulario</title>")
        f.write("</head>")
        f.write("<script>")
        f.write("function Mostrar(){")
        f.write("alert('Info')")

        f.write("}")
        f.write("</script>")
        f.write("<body>")
        f.write("<H1 style=\"color:white; background-color:teal\">\n<center> Formulario </center>\n</H1>\n")
        f.write("<ul><center>")
        for x in range(len(self.lista)):
            if self.lista[x].tipo == "etiqueta":
                f.write("<li><label>"+self.lista[x].valor+"</label></li><br>")
            if self.lista[x].tipo == "texto":
                f.write("<li>")
                if self.lista[x].valor != "":
                    f.write("<label>"+self.lista[x].valor+" </label>")
                else:
                    None
                f.write("<input type='text' name='Name' placeholder = "+self.lista[x].fondo+"/><br>")
                f.write("</li>")
            if self.lista[x].tipo == "grupo-radio":
                f.write("<li>")
                if self.lista[x].nombre != "":
                    f.write("<br><label>"+self.lista[x].nombre +" </label>")
                else:
                    None
                o = self.lista[x].valores
                for j in o:
                    f.write("<input type='radio'>"+j)
                f.write("</li>")
            if self.lista[x].tipo == "grupo-option":
                f.write("<li>")
                if self.lista[x].nombre != "":
                    f.write("<br><label>"+self.lista[x].nombre +": </label>")
                else:
                    None
                o = self.lista[x].valores
                f.write("<select >")
                for j in o:
                    f.write("<option>"+j+"</option>")
                f.write("</select>")
                f.write("</li>")
            if self.lista[x].tipo == "boton":
                f.write("<li>")
                if self.lista[x].evento == "entrada":
                    f.write("<br><button id='open'>"+self.lista[x].valor+"</button>")
                    f.write("<div id='modal_container' class='modal-container'>")
                    f.write("<div class='modal'>")
                    f.write("<h1>Ventana Modal</h1>")
                    f.write("<p>")
                    f.write(self.var_aux)
                    f.write("</p>")
                    f.write("<button id='close'>Cerrar</button>")
                    f.write("</div>")
                    f.write("</div>")
                elif self.lista[x].evento == "info":
                    f.write("<button onclick='Mostrar();'>"+ self.lista[x].valor +"</button>")
                f.write("</li>")
                f.write("</li>")
        f.write("</ul></center>")
        f.write("<!-- Optional JavaScript; choose one of the two! -->")
        f.write("<tr class=\"table-primary\">")
        f.write(" <!-- Option 1: Bootstrap Bundle with Popper -->")
        f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj\" crossorigin=\"anonymous\"></script>")
        f.write("<!-- Option 2: Separate Popper and Bootstrap JS -->")
        f.write(" <!--")
        f.write("<script src=\"https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js\" integrity=\"sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp\" crossorigin=\"anonymous\"></script>")
        f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js\" integrity=\"sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/\" crossorigin=\"anonymous\"></script>")
        f.write("-->")
        f.write("<script src='script.js'></script>")
        f.write("</body>")
        f.write("</html>")
        self.lista.clear()
        f.close()
    