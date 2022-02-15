#def main():
#    try:
#        configuration = open("config.txt")
#    except FileNotFoundError:
#        print("No se encontró el archivo")
#    except IsADirectoryError:
#        print("Se encontró config.txt pero es un directorio, no es posible leerlo")
#
#if __name__ == '__main__':
#    main()

#def main():
#    try:
#        configuration = open("config.txt")
#    except FileNotFoundError as err:
#        print("No se encontró el archivo:", err)
#    except IsADirectoryError as err:
#        print("Se encontró config.txt pero es un directorio, no es posible leerlo", err)

#if __name__ == '__main__':
#    main()

import os


def main():
    try:
        configuration = open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("No se encontró el archivo:", err.strerror)
        elif err.errno == 21:
            print("Se encontró config.txt pero es un directorio, no es posible leerlo: ", err.strerror)

if __name__ == '__main__':
    main()