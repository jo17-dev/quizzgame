from src.front.ui import *
from src.back.utils.file_manager import *
from src.back.utils.quizz_function import *
import os

def main():
    response = int(print_menu_option())

    match response:
        case 1:
            print("======= creer un quizz =======")
            creer_quizz()
            input("Appuyez sur 'entrer' pour continuer")
            os.system("cls")
            main()
        case 2:
            print("======= Suprimer un quizz ======")
            supprimer_quizz()
            main()
        case 3:
            print("======= Jouer un quizz =======")
            jouer_quizz()

            main()
        case 4:
            print("======= Quitter ==============")

    # file_manager().lire_fichier("./src/back/files/quiz_test.csv")
    
os.system("cls")
main()