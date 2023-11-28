# fonction qui affiche le menue et recupère un choix de reponse
def print_menu_option():
    print(
        """
            ====== Quizz Game =======
            1- creer un quizz
            2- Suprimmer un quizz
            3- jouer un quizz
            4- Modifier un quizz
            5- quitter
        """
    )
    response = input("Entrez votre choix: > ")
    if response not in ['1', '2', '3', '4', '5']:
        print("Mauvais choix. réssayer")
        return print_menu_option()
    else:
        return response
    


def menu_modifier_quizz():
    print("""
1- Modifier la question
2- Modifier les choix
3- Modifier l'annecdote
4- Suprimmer la question
""")
    action_response = input("faire un choix: > ")
    while 1:
        if action_response not in ["1", "2", "3", "4"]:
            action_response = input("Mauvais choix: reessayez: > ")
        else:
            break
    return action_response