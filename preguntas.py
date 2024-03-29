"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.
"""

data = open("data.csv", "r").readlines()
data = [x.replace("\n","") for x in data]
data = [x.split("\t") for x in data]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    return sum(list(map(lambda x: int(x[1]), data)))




def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.
    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    """
    cuenta = {"A":0,"B":0,"C":0,"D":0,"E":0}
    for i in data :
        cuenta[i[0]]+=1
    lista = [(X,cuenta[X])for X in cuenta]
    return lista



#sorted([(x[0],x[1])for x in data], key= lambda x: x[0])
def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
    cuenta = {"A":0,"B":0,"C":0,"D":0,"E":0}
    for i in data :
        cuenta[i[0]]+=int(i[1])
    lista = [(X,cuenta[X])for X in cuenta]
    return lista

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.
    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    dicc = ({f"0{x}" : 0 for x in range(1,10)})
    dicc.update({f"{x}" : 0 for x in range(10,13)})
    for i in data:
        numero = (i[2][5:7])
        dicc[numero]+= 1
    dicc = [(X,dicc[X])for X in dicc]
    return dicc 


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    """
    lista = [("A", 0, 100),("B", 0, 100),("C", 0, 100),("D", 0, 100),("E", 0, 100)]
    for i in data :
        index = ord(i[0]) - 65
        if int(i[1]) > lista[index][1]:
            lista[index] = (lista[index][0],int(i[1]),lista[index][2])
        if int(i[1]) < int(lista[index][2]):
            lista[index] = (lista[index][0],lista[index][1],int(i[1]))
    return lista




def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    """
    dicc = {"aaa":[0,100],"bbb":[0,100],"ccc":[0,100],"ddd":[0,100],"eee":[0,100],"fff":[0,100],"ggg":[0,100],"hhh":[0,100],"iii":[0,100],"jjj":[0,100]}
    for i in data:
        lista = i[4].split(",")
        for j in lista:
            index = j[:3]
            if int(j[4:]) > dicc[index][0] :
                dicc[index][0] = int(j[4:])
            if int(j[4:]) < dicc[index][1]:
                dicc[index][1] = int(j[4:])
    dicc = [(X,dicc[X][1],dicc[X][0])for X in dicc]
    return(dicc)
            


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    """
    lista=[(i,[]) for i in range(10)]
    for i in data:
        index = int(i[1])
        lista[index][1].append(i[0])
    return lista
    

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.
    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]
    """
    lista=[(i,[]) for i in range(10)]
    for i in data:
        index = int(i[1])
        if i[0] not in lista[index][1]:
            lista[index][1].append(i[0])
    for i in lista:
        i[1].sort()
    return lista

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
    """
    dicc = {"aaa":0,"bbb":0,"ccc":0,"ddd":0,"eee":0,"fff":0,"ggg":0,"hhh":0,"iii":0,"jjj":0}
    for i in data:
        lista = i[4].split(",")
        for j in lista:
            index = j[:3]
            dicc[index] += 1
    return dicc

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    return [(i[0],len(i[3].split(",")),len(i[4].split(","))) for i in data]


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.
    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    dicc = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,}
    for i in data:
        lista = i[3].split(",")
        for j in lista:
            dicc[j] += int(i[1])
    return dicc

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }
    """
    dicc = {'A':0,'B':0,'C':0,'D':0,'E':0}
    for i in data:
        lista = i[4].split(",")
        for j in lista:
            dicc[i[0]] += int(j[4:])
    return dicc
