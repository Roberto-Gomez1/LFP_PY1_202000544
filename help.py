from tkinter import Tk
from tkinter.filedialog import askopenfilename

def Leer_Archivo():
    raiz1 = Tk
    filename1 = askopenfilename(filetypes=[("Archivo form","*.form")])
    file1 = open(filename1,"r",encoding = "utf-8")
    texto1 = file1.read()
    return texto1

