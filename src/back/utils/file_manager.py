# this file will contains the functions who has a link with file managing



class file_manager:
    def __init__(self):
        pass

    def lire_fichier(self, chemin: str):
        try:
            f = open(chemin, "r", encoding="utf-8")
            print("lecture du fichier en cour")
            for word in f.readlines(1):
                print(word)
                print("========================================")
            print(len(f.readlines()))
            f.close()
        except:
            print("Erreur liée à l'ouverture du fichier. existe t-il ?")

    def rechercher_fichier(self, chemin: str):
        ...