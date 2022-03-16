import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
from help import Leer_Archivo
from Lexico import Analizador
def boton_cargaArchivo_command():
    arch = Leer_Archivo()
    textt.insert(tk.INSERT, arch)

def buscar_Repor():
    opcion = lista.get()
    if opcion == "Reporte Token":
        texto = textt.get(1.0,'end')
        lexico = Analizador(texto)
        lexico.reporteTokens()
    elif opcion == "Reporte Errores":
        texto = textt.get(1.0,'end')
        lexico = Analizador(texto)
        lexico.reporteErorres()
    elif opcion == "Manual de Usuarios":
        print("Manual de Usuarios")
    elif opcion == "Manual Técnico":
        print("Manual Técnico")
    else:
        None

def guardar_Archivo():
    Tk().withdraw()
    filedir = filedialog.askopenfilename(filetypes=[("Archivo data","*.form")])
    texto = textt.get(1.0,'end')
    with open(filedir,"r+",encoding = "utf-8") as f:
        f.truncate(0)
        f.write(texto)

def analizar_Report():
    texto = textt.get(1.0,'end')
    lexico = Analizador(texto)
    lexico.Imprimir()
    lexico.ImprimirErrores()



root =Tk()
root.title('Menu')
fuente = tkFont.Font(family='Arial', size = 12)

fram = ttk.Frame(root)
framee = ttk.Frame(fram, width=800, height=600)


textt = tk.Text(root)
textt["font"] = fuente
textt.place(x=75,y=75,width= 550, height=450)

cArchivo=tk.Button(root)
cArchivo["font"] = fuente
cArchivo["justify"] = "center"
cArchivo["text"] = "Cargar archivo"
cArchivo.place(x=75,y=10,width=121,height=50)
cArchivo["command"] = boton_cargaArchivo_command 



guardar=tk.Button(root)
guardar["font"] = fuente
guardar["justify"] = "center"
guardar["text"] = "Guardar archivo"
guardar.place(x=250,y=10,width=121,height=50)
guardar["command"] = guardar_Archivo 

label1=tk.Label(root)
label1["font"] = fuente
label1["justify"] = "center"
label1["text"] = "Reportes"
label1.place(x=625,y=320,width=180,height=30)

generar=tk.Button(root)
generar["font"] = fuente
generar["justify"] = "center"
generar["text"] = "Buscar Reporte"
generar.place(x=650,y=430,width=120,height=50)
generar["command"] = buscar_Repor 


lista=ttk.Combobox(root)
lista["state"]="readonly"
lista["font"] = fuente
lista["justify"] = "center"
lista["values"] = ["Reporte Token", "Reporte Errores", "Manual de Usuarios", "Manual Técnico"]
lista.place(x=650,y=350,width=130,height=30)

analiza=tk.Button(root)
analiza["font"] = fuente
analiza["justify"] = "center"
analiza["text"] = "Analizar"
analiza.place(x=650,y=210,width=121,height=50)
analiza["command"] =analizar_Report


fram.pack()
framee.pack()



root.mainloop()
