from src.back.utils.quizz_function import check_if_exists, BASE_PATH
from src.front.ui import menu_modifier_quizz

def modifier_quizz()->bool:

    print('++ Modifier un quizz')
    file_name = input("Entrer un nom de fichier: > ")
    if not check_if_exists(file_name):
        return False
    
    fichier = open(BASE_PATH+file_name+".csv", "r+", encoding='utf-8')
    i=0
    item_id = []
    fichier_lines = fichier.readlines()
    for line in fichier_lines:
        item_id.append(i)
        i += 1
        line_table = line.split(";")
        print(item_id[len(item_id) - 1] , ": ", line_table[0])

    response = int(input("\n ==== Entrer le chiffre corespondant a la question: > "))
    
    while 1:
        if response not in item_id:
            response = int(input("\n ==== Mauvais choix. réessayez : > "))
        else:
            break
    print(fichier_lines[response])

    fichier.close()

    action_response = menu_modifier_quizz()

    match action_response:
        case "1":
            print("Modification de la question: ")
            new_data = input("Récrire la question: > ")
            line = fichier_lines[response]
            line = line.split(";")
            line[0] = new_data
            fichier_lines[response] = ";".join(line)
            fichier = open(BASE_PATH+file_name+".csv", "w", encoding='utf-8')

            for item in fichier_lines:
                fichier.write(item)

            print("== opération terminée")
            fichier.close()
        case "2":
            print("++ Modification des choix")
            line = fichier_lines[response]
            line = line.split(";")
            for i in range(1, 5):
                print("choix numéro ", i, " : ", line[i])
                new_data = input("Modifier cette reponse ? (1: oui ): > ")
                if new_data == "1":
                    new_data = input("reécrire le choix 1: > ")
                    line[i] = new_data
                    fichier_lines[response] = ";".join(line)
                    fichier = open(BASE_PATH+file_name+".csv", "w", encoding='utf-8')
                    for item in fichier_lines:
                        fichier.write(item)
                    print("== opération terminée")
                    fichier.close()
        case "3":
            line = fichier_lines[response]
            line = line.split(";")
            if len(line) == 7:
                print("Annecdote: ", line[6])
                new_data = input("Entrer la nouvelle annecdote")
                line[6] = new_data
                fichier_lines[response] = ";".join(line)
                fichier = open(BASE_PATH+file_name+".csv", "w", encoding='utf-8')
                for item in fichier_lines:
                    fichier.write(item)
                print("== opération terminée")
                fichier.close()
            else:
                print("il n'y a pas d'annecdote pour cette question")
                line = ";".join()
            print("Opération terminée")
        case "4":
            line = fichier_lines[response]
            line = line.split(";")
            new_data = input("Suprimmer la quesiton ?:(1: Oui) > ")
            if new_data == "1":
                # del line[response]
                del fichier_lines[response]
                # fichier_lines[response] = ";".join(line)
                fichier = open(BASE_PATH+file_name+".csv", "w", encoding='utf-8')
                for item in fichier_lines:
                    fichier.write(item)
                print("== opération terminée")
                fichier.close()
            