from src.back.utils.quizz_function import check_if_exists, BASE_PATH

"""
creeer quizz
* demande le nom du ficher-quizz à creer
* check s'il n'existe pas encore
* creer le fichier
    * demande à l'user et recuperer les premier question infos du quizz ligne par ligne
    * demander à l'user s'il veut arreter
*fin du process
* affochage du nom du fichier crée 
"""
def creer_quizz()->bool:
    print("++creation du quizz")
    file_name = str(input("Entrer un nom de fichier (sans extention) : > "))

    if check_if_exists(file_name):
        print("le ficher ", file_name, " existe dejas. Entrer un autre nom de fichier-quizz")
        return False

    try:
        quizz = open(BASE_PATH+file_name+".csv", "w", encoding="utf-8")
    except:
        print("Erreur l'ors de la creation de fichier", )
        return False

    while True:
        data =[]
        while True:
            niveau = input("choisir le niveau de difficultée de cette question: (1: Facile  2: Moyene  3: Dificile) >")
            if niveau not in ["1", "2", "3"]:
                print("Le choix est érroné. Bien vouloir recommencer. ")
            else:
                break
        data.append(input("Entrer une question: > "))
        data.append(input("Entrer la bonne reponse: > "))
        data.append(input("Entrer un autre choix de reponse: > "))
        data.append(input("Entrer un autre choix de reponse: > "))
        data.append(input("Entrer un autre choix de reponse: > "))
        data.append(
            "Facile" if niveau == "1" else ("Moyene" if niveau == "2" else "Dificile" ) 
        )
        annecdote_voulu = True if input("Voulez-vous une annecdote pour la question \n (1: oui   0: non ) ? > ") == "1" else False
        data.append(input("Entrez une annecdote pour la question: >")) if annecdote_voulu else ""
        quizz.write(";".join(data) + "\n")
        if input("Voulez vous entrer une autre question \n (1: oui   0: non ) ? > ") == "0":
            break

    quizz.close()
    print("Le quizz a bien été enregistré sous le nom de fichier : ", file_name)
    return True