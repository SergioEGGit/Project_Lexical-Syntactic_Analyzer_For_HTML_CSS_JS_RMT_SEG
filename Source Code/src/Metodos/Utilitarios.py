# ---------------------------------------------------Imports------------------------------------------------------------
import subprocess
import webbrowser

from pathlib import Path
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename
from tkinter.messagebox import askyesnocancel, showinfo, askyesno

from src.Design import Objetos
from src.Variables import Variables
from src.Analizadores import AnalizadorLexicoHMTL as AnalizadorHTML, AnalizadorLexicoCSS as AnalizadorCSS, \
    AnalizadorLexicoJS as AnalizadorJS, AnalizadorLexicoRMT as AnalizadorRMT


# ----------------------------------------------------Métodos-----------------------------------------------------------

# Método Nuevo
def OpcionNuevo():

    # Verificar Si Hay Un Archivo Abierto

    if Variables.rutaarchivo != "":

        # Verificar Si Se Desea Guardar O No El Archivo
        bandera = askyesnocancel(title="Aviso", message="¿Desea Guardar El Documento Que Esta Modificando?")

        if bandera:
            OpcionGuardar()
            Objetos.richtextboxarchivo.delete(1.0, "end-1c")
            Variables.rutaarchivo = ""
            Variables.extensionarchivo = ""
            OpcionGuardarComo()
        elif bandera is None:
            print("")
        elif not bandera:
            Objetos.richtextboxarchivo.delete(1.0, "end-1c")
            Variables.rutaarchivo = ""
            Variables.extensionarchivo = ""
            OpcionGuardarComo()

    else:

        # Guardar Documento
        OpcionGuardarComo()


# Método Abrir Archivo
def OpcionAbrir():

    # Asingacion
    Variables.lineasarchivo[:] = []

    # Obtener El Nombre Del Archivo
    nombrearchivo = askopenfilename(initialdir="C:\\", title="Abrir Archivo", filetypes=(
        ("Archivos HTML", "*.html"), ("Archivos CSS", "*.css"), ("Archivos JS", "*.js"),
        ("Archivos rmt", "*.rmt")))

    Variables.nombrearchivo = Path(nombrearchivo).stem

    # Verificar Si No Se Presiono Cancelar
    if nombrearchivo != "":
        # Limpiar TextBox
        Objetos.richtextboxarchivo.delete(1.0, "end-1c")

        # Obtener Ruta Archivo
        arreglosplit = nombrearchivo.split(".")

        # Guardar Ruta Y Extension Del Archivo
        Variables.rutaarchivo = nombrearchivo.strip()
        Variables.extensionarchivo = arreglosplit[1].strip()

        # Abrir Archivo En Modo Lectura
        nuevoarchivo = open(nombrearchivo, "r")

        # Obtener Texto Por Lineas
        for Linea in nuevoarchivo.readlines():

            Variables.lineasarchivo.append(Linea)

        nuevoarchivo.close()

        # Abrir Archivo En Modo Lectura
        nuevoarchivo = open(nombrearchivo, "r")

        # Obtener Texto Completo
        Variables.cadenaarchivo = nuevoarchivo.read()
        nuevoarchivo.close()

        # Colocar Texto En Rich Text
        Objetos.richtextboxarchivo.insert("end-1c", Variables.cadenaarchivo)
        Objetos.richtextboxconsola.delete(1.0, "end-1c")


# Método Guardar Archivo
def OpcionGuardar():
    # Verificar Que Existe Archivo Abierto
    if Variables.rutaarchivo != "":
        # Abrir Archivo En Modo Escritura
        archivomodificado = open(Variables.rutaarchivo, "w")

        # Obtener El Texto Del Rich Text
        cadenaarchivo = Objetos.richtextboxarchivo.get(1.0, "end-1c")

        # Escribir En Archivo
        archivomodificado.write(cadenaarchivo)
        archivomodificado.close()


# Método Guardar Como
def OpcionGuardarComo():
    # Obtener Directorio Guardar Archivo
    nombrearchivo = asksaveasfilename(initialdir="C:\\", title="Guardar Como...", filetypes=(
        ("Archivos HTML", "*.html"), ("Archivos CSS", "*.css"), ("Archivos JS", "*.js"),
        ("Archivos Rmt", "*.rmt")), defaultextension=".html")

    # Obtener Ruta
    arreglosplit = nombrearchivo.split(".")
    Variables.extensionarchivo = arreglosplit[len(arreglosplit) - 1]
    Variables.nombrearchivo = Path(nombrearchivo).stem
    Variables.rutaarchivo = nombrearchivo

    if nombrearchivo != "":

        # Abrir Archivo En Modo Lectura
        nuevoarchivo = open(nombrearchivo, "w")

        # Si Se Indico Un Archivo
        if nombrearchivo != "":
            # Escribir En Archivo
            nuevoarchivo.write(Objetos.richtextboxarchivo.get(1.0, "end-1c"))
            nuevoarchivo.close()

            # Mensaje
            showinfo("Información", "Archivo Guardado Con Exito!")


# Método Salir
def OpcionSalir():
    Objetos.ventanaprincipal.quit()


# Método Acerca De
def OpcionAcercaDe():

    showinfo("Acerca De...", "             Proyecto_1: SEG_P1 \n  Sergio Alexander Echigoyen Gomez\n         "
                             "           201801628")


# Modulo Decisión
def ModuloDecisionAnalizador():
    # Obtener Texto Archivo
    Variables.cadenaarchivo = Objetos.richtextboxarchivo.get(1.0, "end-1c")

    # Limpiar Consola
    Objetos.richtextboxconsola.delete(1.0, "end-1c")

    # Verificar Si Hay Una Archivo Abierto
    if Variables.extensionarchivo != "":

        # Verificar Extensión
        if Variables.extensionarchivo.strip() == "html":

            AnalizadorHTML.AnalizadorLexicoHTML()

        elif Variables.extensionarchivo.strip() == "css":

            AnalizadorCSS.AnalizadorLexicoCSS()

        elif Variables.extensionarchivo.strip() == "js":

            AnalizadorJS.AnalizadorLexicoJS()

        elif Variables.extensionarchivo.strip() == "rmt":

            AnalizadorRMT.AnalizadorLexicoRMT()
    else:

        showinfo("Información", "Aún No Se Ha Abierto Ningún Archivo Valido")


# Generar Archivo HTML Sin Errores
def ArchivoSinErroresHTML(nombrearchivo):
    # Variables
    rutaarchivo = ""
    rutastring = ""
    listacomentarios = []
    listasplit = []

    # Asignacion
    listacomentarios[:] = []
    listasplit[:] = []
    rutastring = "C:\\Output\\html"

    # Obtener Ruta Archivo
    for Tokens in Variables.listatokenshtml:

        # Obtener Comentarios
        if Tokens[1] == "Comentario":
            # Agregar Token A Lista
            listacomentarios.append(Tokens[2].strip())

    # Obtener Ruta Archivo
    for Comentario in listacomentarios:

        # Verificar Que Contenga Una Ruta
        if ":" in Comentario:

            # Split Comentario
            listasplit = Comentario.split(":", maxsplit=1)

            # Verificar Si La Ruta Es Valida
            if listasplit[0].strip() == "PATHW":
                # Obtener Ruta Para Windows
                rutaarchivo = listasplit[1].strip()

    # Verificar Ruta Archivo
    if rutaarchivo != "":

        # Convertir String A Ruta
        patharchivo = Path(rutaarchivo)

        # Verificar Si Existe El Directorio
        if not patharchivo.is_dir():
            # Crear Directorios
            patharchivo.mkdir(parents=True)

        # Crear Archivo
        reporteerrores = open(rutaarchivo + nombrearchivo.strip() + "_Corregido.html", "w")

        # Path Salida
        pathsalida = rutaarchivo + nombrearchivo + "_Corregido.html"

    else:

        # Convertir String A Ruta
        patharchivo = Path(rutastring)

        # Verificar Si Existe El Directorio
        if not patharchivo.is_dir():
            # Crear Directorios
            patharchivo.mkdir(parents=True)

        reporteerrores = open(rutastring + "\\" + nombrearchivo + "_Corregido.html", "w")

        # Path Salida
        pathsalida = rutastring + "\\" + nombrearchivo + "_Corregido.html"

        showinfo("Error!", "No Se Especifico La Ruta Para Guardar El Archivo \n"
                           "Se Guardara En La Siguiente Ruta: \n" +
                 rutastring)

    # Escribir En Archivo
    reporteerrores.write(Variables.archivohtml)

    # Cerrar Archivo
    reporteerrores.close()

    # Preguntar Si Se Desea Abrir El Reporte
    resultado = askyesno("Archivo Corregidos!", "¿Desea Abrir El Archivo Corregido?")

    # Abrir Archivo
    if resultado:
        # Abrir Archivos Corregidos
        # Abrir Archivo HTML
        webbrowser.open_new_tab(pathsalida)


# Generar Archivo CSS Sin Errores
def ArchivoSinErroresCSS(nombrearchivo):
    # Variables
    rutaarchivo = ""
    rutastring = ""
    listacomentarios = []
    listasplit = []

    # Asignacion
    listacomentarios[:] = []
    listasplit[:] = []
    rutastring = "C:\\Output\\css"

    # Obtener Ruta Archivo
    for Tokens in Variables.listatokenscss:

        # Obtener Comentarios
        if Tokens[1] == "Comentario":
            # Agregar Token A Lista
            listacomentarios.append(Tokens[2].strip())

    # Obtener Ruta Archivo
    for Comentario in listacomentarios:

        # Verificar Que Contenga Una Ruta
        if ":" in Comentario:

            # Split Comentario
            listasplit = Comentario.split(":", maxsplit=1)

            # Verificar Si La Ruta Es Valida
            if listasplit[0].strip() == "PATHW":
                # Obtener Ruta Para Windows
                rutaarchivo = listasplit[1].strip()

    # Verificar Ruta Archivo
    if rutaarchivo != "":

        # Convertir String A Ruta
        patharchivo = Path(rutaarchivo)

        # Verificar Si Existe El Directorio
        if not patharchivo.is_dir():
            # Crear Directorios
            patharchivo.mkdir(parents=True)

        # Crear Archivo
        reporteerrores = open(rutaarchivo + nombrearchivo.strip() + "_Corregido.css", "w")

        # Path Salida
        pathsalida = rutaarchivo + nombrearchivo + "_Corregido.css"

    else:

        # Convertir String A Ruta
        patharchivo = Path(rutastring)

        # Verificar Si Existe El Directorio
        if not patharchivo.is_dir():
            # Crear Directorios
            patharchivo.mkdir(parents=True)

        reporteerrores = open(rutastring + "\\" + nombrearchivo + "_Corregido.css", "w")

        # Path Salida
        pathsalida = rutastring + "\\" + nombrearchivo + "_Corregido.css"

        showinfo("Error!", "No Se Especifico La Ruta Para Guardar El Archivo \n"
                           "Se Guardara En La Siguiente Ruta: \n" +
                 rutastring)

    # Escribir En Archivo
    reporteerrores.write(Variables.archivocss)

    # Cerrar Archivo
    reporteerrores.close()

    # Preguntar Si Se Desea Abrir El Reporte
    resultado = askyesno("Archivo Corregidos!", "¿Desea Abrir El Archivo Corregido?")

    # Abrir Archivo
    if resultado:
        # Abrir Archivos Corregidos
        # Abrir Archivo CSS
        subprocess.run(["notepad", pathsalida])


# Generar Archivo JS Sin Errores
def ArchivoSinErroresJS(nombrearchivo):
    # Variables
    rutaarchivo = ""
    rutastring = ""
    listacomentarios = []
    listasplit = []

    # Asignacion
    listacomentarios[:] = []
    listasplit[:] = []
    rutastring = "C:\\Output\\js"

    # Obtener Ruta Archivo
    for Tokens in Variables.listatokensjs:

        # Obtener Comentarios
        if Tokens[1] == "Comentario_UniLinea":
            # Agregar Token A Lista
            listacomentarios.append(Tokens[2].strip())

    # Obtener Ruta Archivo
    for Comentario in listacomentarios:

        # Verificar Que Contenga Una Ruta
        if ":" in Comentario:

            # Split Comentario
            listasplit = Comentario.split(":", maxsplit=1)

            # Verificar Si La Ruta Es Valida
            if listasplit[0].strip() == "PATHW":
                # Obtener Ruta Para Windows
                rutaarchivo = listasplit[1].strip()

    # Verificar Ruta Archivo
    if rutaarchivo != "":

        # Convertir String A Ruta
        patharchivo = Path(rutaarchivo)

        # Verificar Si Existe El Directorio
        if not patharchivo.is_dir():
            # Crear Directorios
            patharchivo.mkdir(parents=True)

        # Crear Archivo
        reporteerrores = open(rutaarchivo + nombrearchivo.strip() + "_Corregido.js", "w")

        # Path Salida
        pathsalida = rutaarchivo + nombrearchivo + "_Corregido.js"

    else:

        # Convertir String A Ruta
        patharchivo = Path(rutastring)

        # Verificar Si Existe El Directorio
        if not patharchivo.is_dir():
            # Crear Directorios
            patharchivo.mkdir(parents=True)

        reporteerrores = open(rutastring + "\\" + nombrearchivo + "_Corregido.js", "w")

        # Path Salida
        pathsalida = rutastring + "\\" + nombrearchivo + "_Corregido.js"

        showinfo("Error!", "No Se Especifico La Ruta Para Guardar El Archivo \n"
                           "Se Guardara En La Siguiente Ruta: \n" +
                 rutastring)

    # Escribir En Archivo
    reporteerrores.write(Variables.archivojs)

    # Cerrar Archivo
    reporteerrores.close()

    # Preguntar Si Se Desea Abrir El Reporte
    resultado = askyesno("Archivo Corregidos!", "¿Desea Abrir El Archivo Corregido?")

    # Abrir Archivo
    if resultado:
        # Abrir Archivos Corregidos
        # Abrir Archivo JS
        subprocess.run(["notepad", pathsalida])


# Generar Archivo RMT Sin Errores
def ArchivoSinErroresRMT(nombrearchivo):
    # Variables
    rutastring = ""

    # Asignacion
    rutastring = "C:\\Output\\rmt"

    # Convertir String A Ruta
    patharchivo = Path(rutastring)

    # Verificar Si Existe El Directorio
    if not patharchivo.is_dir():
        # Crear Directorios
        patharchivo.mkdir(parents=True)

    reporteerrores = open(rutastring + "\\" + nombrearchivo + "_Corregido.rmt", "w")

    # Path Salida
    pathsalida = rutastring + "\\" + nombrearchivo + "_Corregido.rmt"

    showinfo("Error!", "No Se Especifico La Ruta Para Guardar El Archivo \n"
                       "Se Guardara En La Siguiente Ruta: \n" +
             rutastring)

    # Escribir En Archivo
    reporteerrores.write(Variables.archivormt)

    # Cerrar Archivo
    reporteerrores.close()

    # Preguntar Si Se Desea Abrir El Reporte
    resultado = askyesno("Archivo Corregidos!", "¿Desea Abrir El Archivo Corregido?")

    # Abrir Archivo
    if resultado:
        # Abrir Archivos Corregidos
        # Abrir Archivo JS
        subprocess.run(["notepad", pathsalida])


# Mostrar Tokens
def MostrarTokens(extensionarchivo):
    # Variables
    listatokens = ""

    # Cambiar De Color
    Objetos.richtextboxconsola.config(fg='#FF4500', font=("arial", 14), background='#FAF0E6')

    # Modulo De Decision
    if extensionarchivo == "html":

        # Mostrar Tokens
        for Token in Variables.listatokenshtml:
            listatokens += "Id: " + str(Token[0]) + "." + "  Tipo: " + Token[1] + "." + "  Lexema: " + Token[2] + "." \
                           + "  Columna: " + str(Token[3]) + "." + "  Fila: " + str(Token[4]) + "." + "\n\n"

    elif extensionarchivo == "css":

        # Mostrar Tokens
        for Token in Variables.listatokenscss:
            listatokens += "Id: " + str(Token[0]) + "." + "  Tipo: " + Token[1] + "." + "  Lexema: " + Token[2] + "." \
                           + "  Columna: " + str(Token[3]) + "." + "  Fila: " + str(Token[4]) + "." + "\n\n"

    elif extensionarchivo == "js":

        # Mostrar Tokens
        for Token in Variables.listatokensjs:
            listatokens += "Id: " + str(Token[0]) + "." + "  Tipo: " + Token[1] + "." + "  Lexema: " + Token[2] + "." \
                           + "  Columna: " + str(Token[3]) + "." + "  Fila: " + str(Token[4]) + "." + "\n\n"

    elif extensionarchivo == "rmt":

        # Mostrar Tokens
        for Token in Variables.listatokensrmt:
            listatokens += "Id: " + str(Token[0]) + "." + "  Tipo: " + Token[1] + "." + "  Lexema: " + Token[2] + "." \
                           + "  Columna: " + str(Token[3]) + "." + "  Fila: " + str(Token[4]) + "." + "\n\n"

    # Insertar Texto
    Objetos.richtextboxconsola.delete(1.0, "end-1c")
    Objetos.richtextboxconsola.insert("end-1c", listatokens)


# Mostrar Errores
def MostrarErrores(extensionarchivo):
    # Variables
    listaerrores = ""

    # Cambiar De Color
    Objetos.richtextboxconsola.config(fg='#DC143C', font=("arial", 14), background='#FAF0E6')

    # Modulo De Decision
    if extensionarchivo == "html":

        # Mostrar Errores
        for Error in Variables.listaerroreshtml:
            listaerrores += "Id: " + str(Error[0]) + "." + "  Tipo: " + Error[1] + "." + "  Lexema: " + Error[2] + "." \
                            + "  Columna: " + str(Error[3]) + "." + "  Fila: " + str(Error[4]) + "." + "\n\n"

    elif extensionarchivo == "css":

        # Mostrar Errores
        for Error in Variables.listaerrorescss:
            listaerrores += "Id: " + str(Error[0]) + "." + "  Tipo: " + Error[1] + "." + "  Lexema: " + Error[2] + "." \
                            + "  Columna: " + str(Error[3]) + "." + "  Fila: " + str(Error[4]) + "." + "\n\n"

    elif extensionarchivo == "js":

        # Mostrar Errores
        for Error in Variables.listaerroresjs:
            listaerrores += "Id: " + str(Error[0]) + "." + "  Tipo: " + Error[1] + "." + "  Lexema: " + Error[2] + "." \
                            + "  Columna: " + str(Error[3]) + "." + "  Fila: " + str(Error[4]) + "." + "\n\n"

    elif extensionarchivo == "rmt":

        # Mostrar Errores
        for Error in Variables.listaerroresrmt:
            listaerrores += "Id: " + str(Error[0]) + "." + "  Tipo: " + Error[1] + "." + "  Lexema: " + Error[2] + "." \
                            + "  Columna: " + str(Error[3]) + "." + "  Fila: " + str(Error[4]) + "." + "\n\n"

    # Insertar Texto
    Objetos.richtextboxconsola.delete(1.0, "end-1c")
    Objetos.richtextboxconsola.insert("end-1c", listaerrores)
