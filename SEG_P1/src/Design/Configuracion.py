# ---------------------------------------------------Imports------------------------------------------------------------
from src.Design import Objetos
from src.Metodos import Utilitarios
from tkinter import WORD


# --------------------------------------------Conifguración Objetos-----------------------------------------------------

# Ventana Principal
def VentanaPrincipal():

    Objetos.ventanaprincipal.title("SEG: Proyecto_I")
    Objetos.ventanaprincipal.iconbitmap("assets/favicon.ico")
    Objetos.ventanaprincipal.state("zoomed")
    Objetos.ventanaprincipal.config(background='#ADD8E6')


# Barra De Menus
def MenuArchivo():

    # Menú Archivo
    Objetos.barrademenu.add_cascade(label="Archivo", menu=Objetos.menuarchivo)
    Objetos.menuarchivo.config(background='#FFEFD5', fg='#000080', tearoff=0)
    Objetos.menuarchivo.add_command(label="Nuevo Análisis", command=lambda: Utilitarios.OpcionNuevo())
    Objetos.menuarchivo.add_command(label="Abrir Archivo", command=lambda: Utilitarios.OpcionAbrir())
    Objetos.menuarchivo.add_separator()
    Objetos.menuarchivo.add_command(label="Guardar", command=lambda: Utilitarios.OpcionGuardar())
    Objetos.menuarchivo.add_command(label="Guardar como...", command=lambda: Utilitarios.OpcionGuardarComo())
    Objetos.menuarchivo.add_separator()
    Objetos.menuarchivo.add_command(label="Salir", command=lambda: Utilitarios.OpcionSalir())
    Objetos.ventanaprincipal.config(menu=Objetos.barrademenu)

    # Menú Herramientas
    Objetos.barrademenu.add_cascade(label="Herramientas", menu=Objetos.menuherramientas)
    Objetos.menuherramientas.config(background='#FFEFD5', fg='#000080', tearoff=0)
    Objetos.menuherramientas.add_command(label="Análisis", command=lambda: Utilitarios.ModuloDecisionAnalizador())
    Objetos.menuarchivo.add_separator()
    Objetos.ventanaprincipal.config(menu=Objetos.barrademenu)


# Rich Text Box
def RichText():

    width = 60
    height = 34
    Objetos.richtextbox.config(width=width, height=height, wrap=WORD)
    Objetos.richtextbox.grid(column=0, columnspan=3)
    Objetos.richtextbox.config(fg='#000080', font='helvetica', background='#FFEFD5')
    Objetos.richtextbox.place(relx=0.01, rely=0.08)


# Titulo Principal
def Titulo():

    Objetos.titulo.config(background='#ADD8E6', fg='#000080', text='SEG: ML WEB', font=('helvetica', 18))
    Objetos.titulo.place(relx=0.14, rely=0.02)
