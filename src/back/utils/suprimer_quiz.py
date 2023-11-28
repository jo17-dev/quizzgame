from src.back.utils.quizz_function import check_if_exists, BASE_PATH
import os

def supprimer_quizz():
    print('++ Supprimer un fichier:')
    while 1:
        file_name = input("Entrer le nom du fichier à suprimmer (sans extention) : > ")
        if check_if_exists(file_name):
            break
        else:
            print("le nom de fichier est invalude. ")

    response = input("Voulez-vous vraiment supprimer le quizz "+ str(file_name)+ ".csv ? (1: Oui  0: Non): > ")
    if response == "1":
        os.remove(BASE_PATH+file_name+ ".csv")
        print("Fichié supprimé ")
        return True
    else:
        return False