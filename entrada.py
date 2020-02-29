
def cargar_datos(fichero):
    datos = {}
    with open(fichero) as f:
        l = f.readline().split(" ")
        numero_libros = int(l[0])
        numero_librerias = int(l[1])
        datos["numero_dias"] = int(l[2])
        datos["librerias"] = {}
        datos["scores"] = [int(x) for x in f.readline().split(" ")]

        for libreria in range(int(numero_librerias)):
            linea1 = [int(x) for x in f.readline().split(" ")]
            datos["librerias"][libreria] = {}
            datos["librerias"][libreria]["numero_libros"] = linea1[0]
            datos["librerias"][libreria]["signup"] = linea1[1]
            datos["librerias"][libreria]["libros_dia"] = linea1[2]

            datos["librerias"][libreria]["libros"] = sorted([(datos['scores'][int(x)],int(x)) for x in f.readline().split(" ")], reverse=True)





    return datos


if __name__ == '__main__':
    cargar_datos("data/a_example.txt")
