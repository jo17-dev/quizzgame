from src.front.ui import *
from src.back.utils.quizz_function import *
from src.back.utils.modifier_quiz import modifier_quizz
from src.back.utils.creer_quiz import creer_quizz
from src.back.utils.suprimer_quiz import supprimer_quizz
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
            print("======= Modifier un quizz ==============")
            modifier_quizz()
            main()
        case 5:
            print("======= Quitter ==============")
    
os.system("cls")
main()