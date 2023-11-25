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

# Joue un tour avec une question: item--> numéro de question   data->jeu de données
def generer_questions(data, item, niveau):
    score_temporel = 0
    print("question: ", data[niveau][item][0])
    answer = data[niveau][item][1]
    responses_table = []
    # desordre et affichage des choix de reponses dans la table des reponses
    for j in range(1, 5):
        responses_table.append(data[niveau][item][j])
    random.shuffle(responses_table)
    for j in range(4):
        print(j,": ", responses_table[j])
    
    # recuperation de la reponse de l'utilisateur et comparaison
    user_response = input("Entrez un choix: > ")
    while True:
        if user_response not in ["0", "1", "2", "3"]:
            user_response = input("Choix érroné. Entrez un choix (0, 1, 2, 3) :> ")
        else:
            user_response = int(user_response)
            break
    print("responses choisie: ", responses_table[user_response])
    if responses_table[user_response] == answer:
        print("Bon Choix ")
        score_temporel += 1
    else:
        print("Mauvais choix")
    # Affichage de l'annecdote
    if len(data[niveau][item]) == 7:
        print(data[niveau][item][6])
    return score_temporel


def quizz_nombre(nbre_facile, nbre_moyen, nbre_difficile, data):
    score = 0
    print("nombres de question faciles: ", len(data["1"]))
    for item in range(nbre_facile):
        score += generer_questions(data, item, "1")

    for item in range(nbre_moyen):
        score += generer_questions(data, item, "2")

    for item in range(nbre_difficile):
        score += generer_questions(data, item, "3")
    # affichage du score
    print("Votre Score : ", score)

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
    random.shuffle(data["1"])
    random.shuffle(data["2"])
    random.shuffle(data["3"])
    match niveau:
        case "1":
            quizz_nombre(3, 0, 0, data)

        case "2":
            quizz_nombre(2, 2, 0, data)

        case "3":
            quizz_nombre(2, 2, 2, data)


def modifier_quizz():
    print('++ Modifier un quizz')
    file_name = input("Entrer un nom de fichier")


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