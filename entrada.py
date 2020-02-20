
def cargar_datos(fichero):
    datos = {}
    with open(fichero) as f:
        for i in range(10):
            print(f.readline())

if __name__ == '__main__':
    cargar_datos("README.md")
