# Escribir una función que lea dos ficheros csv con una lista larga
# de datos de personas (50 personas y 1000 personas) y llame a
# dos funciones que pongan su nombre en formato capitalizado y
# calculen la letra de DNI correspondiente. Realiza la comprobación
# de rendimiento con la librería cProfile y muestra los datos.
# Describe que indica cada dato que nos proporciona cProfile.
import csv
import cProfile


nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M", "6": "Y", "7": "F",
            "8": "P", "9": "D", "10": "X", "11": "B", "12": "N", "13": "J", "14": "Z", "15": "S",
            "16": "Q", "17": "V", "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}


def check_username(nombre):
    nombre_nuevo = nombre.title()
    return nombre_nuevo


def check_nif(nif_usuario):
    resto = int(nif_usuario[0:8]) % 23
    return nif_usuario[0:8] + nif_dict[str(resto)]


def leer_ficheros(fichero_uno, fichero_dos):
    lista = []
    with open(fichero_uno, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", dialect=csv.excel)
        for persona in reader:
            lista.append(persona)
    with open(fichero_dos, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", dialect=csv.excel)
        for persona in reader:
            lista.append(persona)
    for usuario in lista:
        usuario[0] = check_username(usuario[0])
        usuario[1] = check_nif(usuario[1])
    with open(fichero_uno, encoding='utf-8') as final:
        cvsfinal = open("salida.csv", "w", newline="")
        final = csv.writer(cvsfinal, quotechar=' ', quoting=csv.QUOTE_ALL)
        for linea in lista:
            final.writerow(linea)


cProfile.run("leer_ficheros('50.csv', '1000.csv')")
