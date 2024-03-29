# ---------------------------------------------------Imports------------------------------------------------------------
from src.Design import Objetos
from src.Variables import Variables


# ----------------------------------------------------Métodos-----------------------------------------------------------

# HMTL
# Colorear Texto HTML
def ColorearTextoHTML():
    # Recorrer Lista
    filaauxiliar = 0
    filaauxiliarcadena = 0
    filaauxiliarcomentario = 0
    columnaauxiliar = 0
    columnaauxiliarcadena = 0
    columnaauxiliarcomentario = 0
    fin = 0
    fincadena = 0
    fincomentario = 0

    for Token in Variables.listatokenshtml:

        rango = 0

        if Token[2].strip() == "\"":
            filaauxiliar = Token[4]
            columnaauxiliar = Token[3]

        if Token[1].strip() == "Texto":

            if filaauxiliar == Token[4]:

                rango = 0

            else:

                rango = Token[4] - filaauxiliar
                fin = Token[3]

        if Token[2].strip() == ">":
            filaauxiliarcadena = Token[4]
            columnaauxiliarcadena = Token[3]

        if Token[1].strip() == "Cadena":

            if filaauxiliarcadena == Token[4]:

                rango = 0

            else:

                rango = Token[4] - filaauxiliarcadena
                fincadena = Token[3]

        if Token[2].strip() == "!":

            filaauxiliarcomentario = Token[4]
            columnaauxiliarcomentario = Token[3]

        if Token[1].strip() == "Comentario":

            if filaauxiliarcomentario == Token[4]:

                rango = 0

            else:

                rango = Token[4] - filaauxiliarcomentario
                fincomentario = Token[3]

        if Token[1].strip() == "Cadena":

            ColorearHTML(Token[2], Token[1], Token[4], Token[3], rango + 1, columnaauxiliarcadena, fincadena)

        elif Token[1].strip() == "Texto":

            ColorearHTML(Token[2], Token[1], Token[4], Token[3], rango + 1, columnaauxiliar, fin)

        elif Token[1].strip() == "Comentario":

            ColorearHTML(Token[2], Token[1], Token[4], Token[3], rango + 1, columnaauxiliarcomentario, fincomentario)

        else:

            ColorearHTML(Token[2], Token[1], Token[4], Token[3], rango + 1, 0, 0)


# Verificar Colores HTML
def ColorearHTML(token, tipotoken, fila, columna, rango, columnaauxiliar, otrofin):

    color = SelectorColorHTML(tipotoken)
    largo = len(token)

    if tipotoken == "Cadena":

        if rango > 1:

            for i in range(rango):

                if i > 0:
                    columnaauxiliar = 0

                inicio = str(fila - rango + i + 1) + "." + str(columnaauxiliar)

                if i == rango - 1:

                    fin = str(fila - rango + i + 1) + "." + str(otrofin)

                else:

                    fin = str(fila - rango + i + 1) + ".100"

                Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
                Objetos.richtextboxarchivo.tag_config(color, foreground=color)

        else:

            fin = str(fila) + "." + str(columna)
            inicio = str(fila) + "." + str(columna - largo)
            Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
            Objetos.richtextboxarchivo.tag_config(color, foreground=color)

    elif tipotoken == "Texto":

        if rango > 1:

            for i in range(rango):

                if i > 0:
                    columnaauxiliar = 0

                inicio = str(fila - rango + i + 1) + "." + str(columnaauxiliar)

                if i == rango - 1:

                    fin = str(fila - rango + i + 1) + "." + str(otrofin)

                else:

                    fin = str(fila - rango + i + 1) + ".100"

                Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
                Objetos.richtextboxarchivo.tag_config(color, foreground=color)

        else:

            fin = str(fila) + "." + str(columna)
            inicio = str(fila) + "." + str(columna - largo)
            Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
            Objetos.richtextboxarchivo.tag_config(color, foreground=color)

    elif tipotoken == "Comentario":

        if rango > 1:

            for i in range(rango):

                if i > 0:
                    columnaauxiliar = 0

                if i == 0:

                    inicio = str(fila - rango + i + 1) + "." + str(columnaauxiliar + 2)
                else:

                    inicio = str(fila - rango + i + 1) + "." + str(columnaauxiliar)

                if i == rango - 1:

                    fin = str(fila - rango + i + 1) + "." + str(otrofin - 2)

                else:

                    fin = str(fila - rango + i + 1) + ".100"

                Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
                Objetos.richtextboxarchivo.tag_config(color, foreground=color)

        else:

            fin = str(fila) + "." + str(columna - 2)
            inicio = str(fila) + "." + str(columna - largo - 2)
            Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
            Objetos.richtextboxarchivo.tag_config(color, foreground=color)

    else:

        fin = str(fila) + "." + str(columna)
        inicio = str(fila) + "." + str(columna - largo)
        Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
        Objetos.richtextboxarchivo.tag_config(color, foreground=color)


# Selector Colores HTML
def SelectorColorHTML(tipotoken):

    # Selector De Colores HTML
    Html = {

        "Palabra_Reservada": "red",
        "Identificador": "green",
        "Texto": "yellow",
        "Comentario": "gray",
        "Cadena": "black",
        "Simbolo": "black"

    }

    return Html.get(tipotoken, "black")


# CSS
# Colorear Texto CSS
def ColorearTextoCSS():

    # Recorrer Lista
    filaauxiliar = 0
    filaauxiliarcomentario = 0
    columnaauxiliar = 0
    columnaauxiliarcomentario = 0
    fin = 0
    fincomentario = 0

    for Token in Variables.listatokenscss:

        rango = 0

        if Token[2].strip() == "\"":

            filaauxiliar = Token[4]
            columnaauxiliar = Token[3]

        if Token[1].strip() == "Texto":

            if filaauxiliar == Token[4]:

                rango = 0

            else:

                rango = Token[4] - filaauxiliar
                fin = Token[3]

        if Token[2].strip() == "*":

            filaauxiliarcomentario = Token[4]
            columnaauxiliarcomentario = Token[3]

        if Token[1].strip() == "Comentario":

            if filaauxiliarcomentario == Token[4]:

                rango = 0

            else:

                rango = Token[4] - filaauxiliarcomentario
                fincomentario = Token[3]

        if Token[1].strip() == "Texto":

            ColorearCSS(Token[2], Token[1], Token[4], Token[3], rango + 1, columnaauxiliar, fin)

        elif Token[1].strip() == "Comentario":

            ColorearCSS(Token[2], Token[1], Token[4], Token[3], rango + 1, columnaauxiliarcomentario, fincomentario)

        else:

            ColorearCSS(Token[2], Token[1], Token[4], Token[3], rango + 1, 0, 0)


# Verificar Colores CSS
def ColorearCSS(token, tipotoken, fila, columna, rango, columnaauxiliar, otrofin):

    color = SelectorColoresCSS(tipotoken)
    largo = len(token)

    if tipotoken == "Texto":

        if rango > 1:

            for i in range(rango):

                if i > 0:
                    columnaauxiliar = 0

                inicio = str(fila - rango + i + 1) + "." + str(columnaauxiliar)

                if i == rango - 1:

                    fin = str(fila - rango + i + 1) + "." + str(otrofin)

                else:

                    fin = str(fila - rango + i + 1) + ".100"

                Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
                Objetos.richtextboxarchivo.tag_config(color, foreground=color)

        else:

            fin = str(fila) + "." + str(columna)
            inicio = str(fila) + "." + str(columna - largo)
            Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
            Objetos.richtextboxarchivo.tag_config(color, foreground=color)

    elif tipotoken == "Comentario":

        if rango > 1:

            for i in range(rango):

                if i > 0:
                    columnaauxiliar = 0

                if i == 0:

                    inicio = str(fila - rango + i + 1) + "." + str(columnaauxiliar)
                else:

                    inicio = str(fila - rango + i + 1) + "." + str(columnaauxiliar)

                if i == rango - 1:

                    fin = str(fila - rango + i + 1) + "." + str(otrofin)

                else:

                    fin = str(fila - rango + i + 1) + ".100"

                Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
                Objetos.richtextboxarchivo.tag_config(color, foreground=color)

        else:

            fin = str(fila) + "." + str(columna)
            inicio = str(fila) + "." + str(columna - largo)
            Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
            Objetos.richtextboxarchivo.tag_config(color, foreground=color)

    else:

        fin = str(fila) + "." + str(columna)
        inicio = str(fila) + "." + str(columna - largo)
        Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
        Objetos.richtextboxarchivo.tag_config(color, foreground=color)


# Selector Colores CSS
def SelectorColoresCSS(tipotoken):

    # Selector CSS
    Css = {

        "Palabra_Reservada": "red",
        "Identificador": "green",
        "Texto": "yellow",
        "Numero": "blue",
        "Comentario": "gray",
        "Operador": "orange",
        "Simbolo": "black"

    }
    return Css.get(tipotoken, "black")


# JS
# Colorear Texto JS
def ColorearTextoJS():

    # Recorrer Lista
    filaauxiliar = 0
    filaauxiliars = 0
    filaauxiliarcomentario = 0
    columnaauxiliar = 0
    columnaauxiliars = 0
    columnaauxiliarcomentario = 0
    fin = 0
    fins = 0
    fincomentario = 0

    for Token in Variables.listatokensjs:

        rango = 0

        if Token[2].strip() == "\"":

            filaauxiliar = Token[4]
            columnaauxiliar = Token[3]

        if Token[1].strip() == "Texto_D":

            if filaauxiliar == Token[4]:

                rango = 0

            else:

                rango = Token[4] - filaauxiliar
                fin = Token[3]

        if Token[2].strip() == "'":

            filaauxiliars = Token[4]
            columnaauxiliars = Token[3]

        if Token[1].strip() == "Texto_S":

            if filaauxiliars == Token[4]:

                rango = 0

            else:

                rango = Token[4] - filaauxiliars
                fins = Token[3]

        if Token[2].strip() == "*":

            filaauxiliarcomentario = Token[4]
            columnaauxiliarcomentario = Token[3]

        if Token[1].strip() == "Comentario_MultiLinea":

            if filaauxiliarcomentario == Token[4]:

                rango = 0

            else:

                rango = Token[4] - filaauxiliarcomentario
                fincomentario = Token[3]

        if Token[1].strip() == "Texto_D":

            ColorearJS(Token[2], Token[1], Token[4], Token[3], rango + 1, columnaauxiliar, fin)

        elif Token[1].strip() == "Texto_S":

            ColorearJS(Token[2], Token[1], Token[4], Token[3], rango + 1, columnaauxiliars, fins)

        elif Token[1].strip() == "Comentario_MultiLinea":

            ColorearJS(Token[2], Token[1], Token[4], Token[3], rango + 1, columnaauxiliarcomentario, fincomentario)

        else:

            ColorearJS(Token[2], Token[1], Token[4], Token[3], rango + 1, 0, 0)


# Verificar Colores JS
def ColorearJS(token, tipotoken, fila, columna, rango, columnaauxiliar, otrofin):

    color = SelectorColoresJS(tipotoken)
    largo = len(token)

    if tipotoken == "Texto_S":

        if rango > 1:

            for i in range(rango):

                if i > 0:
                    columnaauxiliar = 0

                inicio = str(fila - rango + i + 1) + "." + str(columnaauxiliar)

                if i == rango - 1:

                    fin = str(fila - rango + i + 1) + "." + str(otrofin)

                else:

                    fin = str(fila - rango + i + 1) + ".100"

                Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
                Objetos.richtextboxarchivo.tag_config(color, foreground=color)

        else:

            fin = str(fila) + "." + str(columna)
            inicio = str(fila) + "." + str(columna - largo)
            Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
            Objetos.richtextboxarchivo.tag_config(color, foreground=color)

    elif tipotoken == "Texto_D":

        if rango > 1:

            for i in range(rango):

                if i > 0:
                    columnaauxiliar = 0

                inicio = str(fila - rango + i + 1) + "." + str(columnaauxiliar)

                if i == rango - 1:

                    fin = str(fila - rango + i + 1) + "." + str(otrofin)

                else:

                    fin = str(fila - rango + i + 1) + ".100"

                Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
                Objetos.richtextboxarchivo.tag_config(color, foreground=color)

        else:

            fin = str(fila) + "." + str(columna)
            inicio = str(fila) + "." + str(columna - largo)
            Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
            Objetos.richtextboxarchivo.tag_config(color, foreground=color)

    elif tipotoken == "Comentario_MultiLinea":

        if rango > 1:

            for i in range(rango):

                if i > 0:
                    columnaauxiliar = 0

                if i == 0:

                    inicio = str(fila - rango + i + 1) + "." + str(columnaauxiliar)
                else:

                    inicio = str(fila - rango + i + 1) + "." + str(columnaauxiliar)

                if i == rango - 1:

                    fin = str(fila - rango + i + 1) + "." + str(otrofin)

                else:

                    fin = str(fila - rango + i + 1) + ".100"

                Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
                Objetos.richtextboxarchivo.tag_config(color, foreground=color)

        else:

            fin = str(fila) + "." + str(columna)
            inicio = str(fila) + "." + str(columna - largo)
            Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
            Objetos.richtextboxarchivo.tag_config(color, foreground=color)

    else:

        fin = str(fila) + "." + str(columna)
        inicio = str(fila) + "." + str(columna - largo)
        Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
        Objetos.richtextboxarchivo.tag_config(color, foreground=color)


# Selector Colores JS
def SelectorColoresJS(tipotoken):

    # Selector JS
    Js = {

        "Palabra_Reservada": "red",
        "Identificador": "green",
        "Texto_S": "yellow",
        "Texto_D": "yellow",
        "Numero": "blue",
        "Boolean": "blue",
        "Comentario_UniLinea": "gray",
        "Comentario_MultiLinea": "gray",
        "Operador": "orange",
        "Simbolo": "black"

    }
    return Js.get(tipotoken, "black")


# RMT
# Colorear Texto RMT
def ColorearTextoRMT():

    for Token in Variables.listatokensrmt:

        rango = 0

        ColorearRMT(Token[2], Token[1], Token[4], Token[3], rango + 1, 0, 0)


# Verificar Colores RMT
def ColorearRMT(token, tipotoken, fila, columna, rango, columnaauxiliar, otrofin):

    color = SelectorColoresRMT(tipotoken)
    largo = len(token)

    fin = str(fila) + "." + str(columna)
    inicio = str(fila) + "." + str(columna - largo)
    Objetos.richtextboxarchivo.tag_add(color, inicio, fin)
    Objetos.richtextboxarchivo.tag_config(color, foreground=color)


# Selector Colores RMT
def SelectorColoresRMT(tipotoken):

    # Selector JS
    Rmt = {

        "Identificador": "green",
        "Numero": "blue",
        "Operador": "orange",
        "Simbolo": "black"

    }
    return Rmt.get(tipotoken, "black")



