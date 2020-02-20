from entrada import cargar_datos


def score_library(library, b_scores):
    n_puntos = 0
    n_libros = len(library['libros'])
    ratio = float(library['libros_dia'])
    signup = float(library['signup'])
    for libro in library['libros']:
        n_puntos += float(b_scores[libro[1]])

    return float(float((n_puntos*(float(n_libros/ratio))))/signup)
    



if __name__ == '__main__':
    fichero = 'a_example'
    #
    #
    #
    #
    #
    f = open('out_'+fichero+'.txt', 'w')

    data = cargar_datos("data/"+fichero+".txt")
    print(data)
    book_scores = data['scores']
    lib_score = []
    for id_libreria in range(len(data['librerias'])):
        lib_score.append((score_library(data['librerias'][id_libreria], book_scores), id_libreria))

    scanned_books = {}
    rem_days = data['numero_dias']
    num_libs = len(lib_score)
    f.write(str(num_libs)+'\n')

    for library in sorted(lib_score, reverse=True):

        signup_time = data['librerias'][library[1]]['signup']
        n_ships = data['librerias'][library[1]]['libros_dia']
        sendable_books = (rem_days-signup_time)*n_ships
        sent_books = {}
        for book in sorted(data['librerias'][library[1]]['libros'], reverse=True):
            if book not in scanned_books and len(sent_books) < sendable_books:
                sent_books[book] = 1
                scanned_books[book] = 1

        rem_days -= signup_time
        f.write("{0} {1}\n".format(library[1],len(sent_books)))
        for x in sent_books.keys():
            f.write(str(x[1])+' ')
        f.write('\n')






