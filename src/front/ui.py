# fonction qui affiche le menue et recupère un choix de reponse
def print_menu_option():
    print(
        """
            ====== Quizz Game =======
            1- creer un quizz
            2- Suprimmer un quizz
            3- jouer un quizz
            4- quitter
        """
    )
    response = input("Entrez votre choix: > ")
    if response not in ['1', '2', '3', '4']:
        print("Mauvais choix. réssayer")
        return print_menu_option()
    else:
        return response