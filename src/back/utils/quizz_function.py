import os
from src.front.ui import *
import random

BASE_PATH = "src/back/files/"

def check_file_name():
    ...

# check si un fichier exsite dans un repertoire
def check_if_exists(file_name):
    return True if os.path.exists(BASE_PATH+file_name+".csv") else False

# la fonction crée et renvoie un jeu de donnée classé en fonction de la difficultée on auras 
# data["1"] ==> toutes les données relatives aux question faciles 
# data["1"][0] ==> données relatives à la 1ere lignes des questions faciles
# data["1"][0][0] ==> question de la 1er ligne des question faciles
def recuperer_donnes(file_name: str):
    data = {
    "1": [],
    "2": [],
    "3": []
    }
    try:
        quizz = open(BASE_PATH+file_name+".csv", encoding="utf-8")
    except:
        print("Erreur l'ors de l'ouverture de fichier")
    print("Chargement du fichier-quizz... ")
    for line in quizz.readlines():
        easy_questions = line.split(";")
        if easy_questions[5] == "Facile":
            data["1"].append(easy_questions)
        elif easy_questions[5] == "Moyen":
            data["2"].append(easy_questions)
        else:
            data["3"].append(easy_questions)

    return data
            

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
            "Facile" if niveau == "1" else ("Moyene" if niveau == "2" else "3" ) 
        )
        annecdote_voulu = True if input("Voulez-vous une annecdote pour la question \n (1: oui   0: non ) ? > ") == "1" else False
        data.append(input("Entrez une annecdote pour la question: >")) if annecdote_voulu else ""
        quizz.write(";".join(data) + "\n")
        if input("Voulez vous entrer une autre question \n (1: oui   0: non ) ? > ") == "0":
            break

    quizz.close()
    print("Le quizz a bien été enregistré sous le nom de fichier : ", file_name)
    return True


"""
jouer quizz
* demande le nom du fichier
* check si le fichier existe
*recupere le niveau de difficulté choisi
    * niveau facile: 3 questions faciles
    * niveau moyen: 2 questions faciles 2 questions moyennes
    * niveau difficle: 3 question moyennes 2 difficiles
"""


def jouer_quizz()-> bool:
    score = 0
    question_nber = 0
    print('++ Jouer un quizz')
    file_name = input("Entrer un nom de fichier: > ")
    while True:
        if not check_if_exists(file_name):
            file_name = input("Fichier non trouvé. bien vouloir recommencer: > ")
        else:
            break

    
    while True:
        niveau = input("choisir le niveau de difficultée de cette question: (1: Facile  2: Moyene  3: Dificile) 4: Très Difficile > ")
        if niveau not in ["1", "2", "3", "4"]:
            print("Le choix est érroné. Bien vouloir recommencer. ")
        else:
            break
    
    data = recuperer_donnes(file_name)
    match niveau:
        case "1":
            print("nombres de question faciles: ", len(data["1"]))
            random.shuffle(data["1"])
            # pour cahque question, on * recupere et desordonne les reponses * 
            for item in range(3):
                print("question: ", data["1"][item][0])
                answer = data["1"][item][1]
                responses_table = []
                # desordre et affichage des choix de reponses
                for j in range(1, 5):
                    responses_table.append(data["1"][item][j])
                random.shuffle(responses_table)
                for j in range(4):
                    print(j,": ", responses_table[j])
                
                # recuperation de la reponse de l'utilisateur
                user_response = input("Entrez un choix: > ")
                while True:
                    if user_response not in ["0", "1", "2", "3"]:
                        user_response = input("Choix érroné un choix (1, 2, 3, 4) :> ")
                    else:
                        user_response = int(user_response)
                        break
                
                if data["1"][item][user_response] == answer:
                    print("Trouvé ")
                    score += 1
                else:
                    print("Raté")
                # Affichage de l'annecdote
                if len(data["1"][item]) == 7:
                    print(data["1"][item][6])

                # affichage du score
                print("Votre Score : ", score)

        case "2":
            print("nombres de question moyennes: ", len(data["2"]))
        case "3":
            print("nombres de question difficiles: ", len(data["3"]))


def modifier_quizz():
    print('++ Modifier un quizz')
    file_name = input("Entrer un nom de fichier")


def supprimer_quizz(file_name):
    print('++ Supprimer un fichier:')
    response = int(input("Voulez-vous vraiment supprimer le quizz "+ str(file_name)+ "?"))
    if response == 1:
        os.remove(BASE_PATH+file_name)
        return True
    else:
        return False