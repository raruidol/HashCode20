from entrada import cargar_datos
from datetime import datetime

def score_library(library):
    n_puntos = 0
    n_libros = len(library['libros'])
    ratio = float(library['libros_dia'])
    signup = float(library['signup'])
    for libro in library['libros']:
        n_puntos += float(libro[0])

    return float(float((n_puntos*(float(n_libros/ratio))))/signup)


def score_library2(library, scanned, rem):
    n_puntos = 0
    set_libros = set(library['libros']) - set(scanned)
    n_libros = len(set_libros)
    ratio = float(library['libros_dia'])
    signup = float(library['signup'])
    ships = float(library['libros_dia'])
    for libro in set_libros:
        n_puntos += float(libro[0])

    return n_puntos*(rem-signup)*ships


def librerias_ordenadas(libs, scanned, remain):
    lib_score = []
    for libreria in libs:
        lib_score.append((score_library2(data['librerias'][libreria], scanned, remain), libreria))

    return sorted(lib_score)


if __name__ == '__main__':
    ficheros = ['a_example', 'b_read_on', 'c_incunabula', 'd_tough_choices', 'e_so_many_books', 'f_libraries_of_the_world']
    for fichero in ficheros:
        print(fichero, datetime.now())
        f = open('output/out_'+fichero+'.txt', 'w')

        data = cargar_datos("data/"+fichero+".txt")
        #print(data)
        book_scores = data['scores']
        lib_score = []
        #for id_libreria in range(len(data['librerias'])):
        #    lib_score.append((score_library2(data['librerias'][id_libreria], book_scores), id_libreria))

        scanned_books = {}
        added_libs = {}
        num_libs = 0
        rem_days = data['numero_dias']
        list1 = []
        list2 = []
        set_libs = set(list(data['librerias']))
        for library in librerias_ordenadas(set_libs, scanned_books, rem_days):
            lib_score = []
            signup_time = data['librerias'][library[1]]['signup']
            n_ships = data['librerias'][library[1]]['libros_dia']
            sendable_books = (rem_days-signup_time)*n_ships
            sent_books = {}
            for book in sorted(data['librerias'][library[1]]['libros'], reverse=True):
                if book not in scanned_books and len(sent_books) < sendable_books:
                    sent_books[book] = 1
                    scanned_books[book] = 1
            if len(sent_books) == 0:
                continue
            rem_days -= signup_time
            num_libs += 1
            if rem_days < 1:
                break
            added_libs[library] = 1
            list1.append("{0} {1}\n".format(library[1],len(sent_books)))
            list2.append(' '.join([str(x[1]) for x in sent_books.keys()]))
            set_libs.remove(library[1])
            #for id_libreria in range(len(data['librerias'])):
            #    lib_score.append((score_library2(data['librerias'][id_libreria], book_scores), id_libreria))
            #f.write("{0} {1}\n".format(library[1],len(sent_books)))
            #f.write(' '.join([str(x[1]) for x in sent_books.keys()]))
            #f.write('\n')

        f.write(str(num_libs) + '\n')
        for i in range(len(list1)):
            f.write(list1[i])
            f.write(list2[i])
            f.write('\n')

        f.close()
