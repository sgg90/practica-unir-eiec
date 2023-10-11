"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_SPANISH = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    spanish_print = DEFAULT_SPANISH
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        spanish_print = sys.argv[3].lower() == "sp"
    else:
        if spanish_print:
            print("Se debe indicar el fichero como primer argumento")
            print("El segundo argumento indica si se quieren eliminar duplicados")
            print("El tercer argumento indica si se quiere que el texto sea en sp")
            sys.exit(1)
        else:
            print("You must specify the file as the first argument")
            print("The second argument indicates whether you want to remove duplicates")
            print("The third argument indicates whether you want the text to be in Spanish (sp)")
            sys.exit(1)

    if spanish_print:
        print(f"Se leerán las palabras del fichero {filename}")
    else:
        print(f"Words will be read from the file {filename}")

    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        if spanish_print:
            print(f"El fichero {filename} no existe")
        else:
            print(f"The file {filename} does not exist")

        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list))
