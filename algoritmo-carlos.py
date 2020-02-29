from entrada import cargar_datos
from timeit import default_timer as timer
from collections import defaultdict
from datetime import timedelta, datetime
# from functools import partial
from multiprocessing import Pool


def ejecucion(fichero):

    def score_library3(library_id):
        library_dict = data['librerias'][library_id]
        libros_libreria = library_dict['libros']
        signup = float(library_dict['signup'])
        ships = float(library_dict['libros_dia'])
        envios_posibles = (rem_days - signup) * ships
        n_puntos = 0
        cuenta_envios = 0

        libros_ordenados[library_id] = sorted(
            [(puntuacion_libros[book[1]], book[1]) for book in libros_libreria if book[1] not in scanned_books],
            reverse=True)

        # for libro in libros_libreria:
        for libro in libros_ordenados[library_id]:
            if cuenta_envios == envios_posibles:
                break

            else:
                cuenta_envios += 1
                n_puntos += libro[0]
        return n_puntos, library_id

    def score_books():
        scores_libros = defaultdict(int)
        for id_libro in range(len(data['scores'])):
            scores_libros[id_libro] = data['scores'][id_libro] / copias_libros[id_libro]\
                if copias_libros[id_libro] > 0 else 0
        return scores_libros

    def mejor_libreria():
        # func = partial(score_library3, scanned, remain)
        lib_score = map(score_library3, set_libs)
        return max(lib_score)

    def apariciones_libros():
        cuentas_libros = defaultdict(int)
        for libreria in set_libs:
            for libro in data["librerias"][libreria]["libros"]:
                cuentas_libros[libro[1]] += 1
        return cuentas_libros

    start_file = timer()
    f = open('output/out_' + fichero + '.txt', 'w')

    data = cargar_datos("data/" + fichero + ".txt")

    scanned_books = set()
    num_libs = 0
    rem_days = data['numero_dias']
    list1 = []
    list2 = []
    set_libs = set(list(data['librerias']))
    copias_libros = apariciones_libros()
    puntuacion_libros = score_books()
    libros_ordenados = {}

    while len(set_libs) > 0:

        library = mejor_libreria()

        signup_time = data['librerias'][library[1]]['signup']
        n_ships = data['librerias'][library[1]]['libros_dia']
        sendable_books = (rem_days - signup_time) * n_ships
        sent_books = []

        # for book in data['librerias'][library[1]]['libros']:
        for book in libros_ordenados[library[1]]:

            if len(sent_books) < sendable_books:
                sent_books.append(book)
                scanned_books.add(book)
            else:
                puntuacion_libros[book[1]] = book[0] / copias_libros[book[1]] if copias_libros[book[1]] > 0 else 0
                copias_libros[book[1]] -= 1

        if len(sent_books) == 0:
            set_libs.remove(library[1])
            continue

        rem_days -= signup_time
        num_libs += 1

        if rem_days < 1:
            end_file = timer()
            print(fichero, end_file - start_file)
            break

        list1.append("{0} {1}\n".format(library[1], len(sent_books)))
        list2.append(' '.join([str(x[1]) for x in sent_books]))
        set_libs.remove(library[1])

    end_file = timer()
    t_inicio = timedelta(seconds=start_file - start)
    t_ejecucion = timedelta(seconds=end_file - start_file)
    print(fichero, t_inicio, t_ejecucion)

    f.write(str(num_libs) + '\n')
    for i in range(len(list1)):
        f.write(list1[i])
        f.write(list2[i])
        f.write('\n')

    f.close()


if __name__ == '__main__':
    print(datetime.now())
    start = timer()
    ficheros = ['a_example', 'b_read_on', 'c_incunabula', 'd_tough_choices', 'e_so_many_books',
                'f_libraries_of_the_world']

    for fichero in ficheros:
        ejecucion(fichero)

    end = timer()
    print(end - start)
