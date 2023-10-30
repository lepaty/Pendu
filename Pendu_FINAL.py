import random
import os

BOLD = "\033[1m"
UNDERLINE = "\033[4m"
YELLOW = "\033[1;33m"
RED = "\033[91m"
BLUE = "\033[94m"
LIGHT_GREEN = "\033[1;32m"
RESET = "\033[0m"


def choisir_mot_mystere(niveau):
    facile = ["table", "chien", "pomme", "avion", "plage", "livre", "asile", "crise", "doigt", "voile"]
    moyen = ["musique", "travaux", "sourire", "chanson", "lutteur", "danseur", "acarien", "cellule", "inodore",
             "sanguin"]
    difficile = ["imprimerie", "formidable", "tradition", "attention", "parapluie", "dynamique", "agonisant",
                 "bourricot", "coiffeuse", "infection"]

    if niveau == 1:
        return random.choice(facile)
    elif niveau == 2:
        return random.choice(moyen)
    elif niveau == 3:
        return random.choice(difficile)
    else:
        print(f"{RED}ERREUR{RESET}: Veuillez introduire un choix valide. ({BOLD}1, 2 ou 3{RESET}")


def jeu_mystere(niveau, victoire_facile, victoire_moyen, victoire_difficile):
    mot_mystere = choisir_mot_mystere(niveau)
    lettres_trouvees = []
    lettres_inexistantes = []
    tentatives = 10
    mot_partiel = ["*"] * len(mot_mystere)
    os.system('cls')  # clear console

    jeu = True

    while jeu:
        print(f"{BLUE}--------------------------------{RESET}")
        print(f"Le {BOLD}mot mystère{RESET} contient{BLUE} {len(mot_mystere)} {RESET}lettres.")
        print(f"Mot partiel :{BLUE} {"".join(mot_partiel)}{RESET}")
        print(f"Lettres ne figurant pas dans le {BOLD}mot mystère{RESET} :{RED} {lettres_inexistantes}{RESET}")
        print(f"Tentatives restantes : {BLUE}{tentatives}{RESET}")
        print(f"{BLUE}--------------------------------{RESET}")
        proposition = input("Entrez une lettre : ").lower()
        os.system('cls')  # clear console
        if len(proposition) == 1 and proposition.isalpha():
            if proposition in lettres_trouvees or proposition in lettres_inexistantes:
                print("Vous avez déjà deviné cette lettre.")
            elif proposition in mot_mystere:
                lettres_trouvees.append(proposition)
                for indice, lettre in enumerate(mot_mystere):
                    if lettre in lettres_trouvees:
                        mot_partiel[indice] = lettre
                if ''.join(mot_partiel) == mot_mystere:
                    print(f"{LIGHT_GREEN}Félicitations{RESET}, "
                          f"vous avez trouvé le {BOLD}mot mystère{RESET} en {BLUE}{tentatives}{RESET} tentatives.")
                    if niveau == 1:
                        victoire_facile += 1
                        print(f"Parties gagnées en difficulté facile : {victoire_facile}")
                    elif niveau == 2:
                        victoire_moyen += 1
                        print(f"Parties gagnées en difficulté moyen : {victoire_moyen}")
                    elif niveau == 3:
                        victoire_difficile += 1
                        print(f"Parties gagnées en difficulté difficile : {victoire_difficile}")
                    jeu = False
            elif proposition not in lettres_trouvees and proposition not in mot_mystere:
                lettres_inexistantes.append(proposition)
                print(f"La lettre ne figure pas dans le {BOLD}mot mystère{RESET}.")
                tentatives -= 1
        else:
            print(f"{RED}ERREUR{RESET}: Caractère invalide !")

        if tentatives == 0:
            print(f"Vous avez {RED}perdu{RESET} !")
            jeu = False

        match tentatives:
            case 9:
                print(f"  {YELLOW}______{RESET}")
            case 8:
                print(f"{YELLOW}|   \n|   \n|   \n|   \n| ______{RESET}")
            case 7:
                print(f"{YELLOW}----\n|   \n|   \n|   \n|   \n| ______{RESET}")
            case 6:
                print(f"{YELLOW}----\n|    |\n|   \n|   \n|   \n| ______{RESET}")
            case 5:
                print(f"{YELLOW}----\n|    |\n|    O\n|   \n|   \n| ______{RESET}")
            case 4:
                print(f"{YELLOW}----\n|    |\n|    O\n|    |\n|   \n| ______{RESET}")
            case 3:
                print(f"{YELLOW}----\n|    |\n|    O\n|   -|\n|   \n| ______{RESET}")
            case 2:
                print(f"{YELLOW}----\n|    |\n|    O\n|   -|-\n|   \n| ______{RESET}")
            case 1:
                print(f"{YELLOW}----\n|    |\n|    O\n|   -|-\n|   / \n| ______{RESET}")
            case 0:
                print(f"{YELLOW}----\n|    |\n|    O\n|   -|-\n|   / \\\n| ______{RESET}")

    return victoire_facile, victoire_moyen, victoire_difficile


recommencer = True
victoire_facile = 0
victoire_moyen = 0
victoire_difficile = 0
while recommencer:
    niveau = 0
    while niveau not in [1, 2, 3]:
        print("")
        print(f"{RED} ▄█          ▄████████         ▄███████▄    ▄████████ ███▄▄▄▄   ████████▄  ███    █▄  ")
        print(f"███         ███    ███        ███    ███   ███    ███ ███▀▀▀██▄ ███   ▀███ ███    ███ {RESET}")
        print(f"{BLUE}███         ███    █▀         ███    ███   ███    █▀  ███   ███ ███    ███ ███    ███ ")
        print(f"███        ▄███▄▄▄            ███    ███  ▄███▄▄▄     ███   ███ ███    ███ ███    ███ {RESET}")
        print(f"{LIGHT_GREEN}███       ▀▀███▀▀▀          ▀█████████▀  ▀▀███▀▀▀     ███   ███ ███    ███ ███    ███ ")
        print(f"███         ███    █▄         ███          ███    █▄  ███   ███ ███    ███ ███    ███ {RESET}")
        print(f"{YELLOW}███▌    ▄   ███    ███        ███          ███    ███ ███   ███ ███   ▄███ ███    ███ ")
        print(f"█████▄▄██   ██████████       ▄████▀        ██████████  ▀█   █▀  ████████▀  ████████▀  {RESET}")
        print("")
        try:
            niveau = int(input(f"Bienvenue dans le jeu du {BOLD}mot mystère.{RESET} "
                               f"\n"
                               f"\nVeuillez choisir un niveau de difficulté : "
                               f"\n {BLUE}------------------------------{RESET}"
                               f"\n{BLUE}|{RESET} 1. {LIGHT_GREEN}Facile{RESET} (5 lettres)        {BLUE}|{RESET}"
                               f"\n {BLUE}------------------------------{RESET}"
                               f"\n{BLUE}|{RESET} 2. {YELLOW}Moyen{RESET} (7 lettres)         {BLUE}|{RESET}"
                               f"\n {BLUE}------------------------------{RESET}"
                               f"\n{BLUE}|{RESET} 3. {RED}Difficile{RESET} (9 lettres)     {BLUE}|{RESET}"
                               f"\n {BLUE}------------------------------{RESET}"
                               f"\nVotre sélection : "))
            if niveau not in [1, 2, 3]:
                os.system('cls')  # clear console
                print(f"{RED}ERREUR{RESET}: Veuillez entrer un choix valide ({BOLD}1, 2 ou 3{RESET}).")
        except ValueError:
            os.system('cls')  # clear console
            print(f"{RED}ERREUR{RESET}: Veuillez entrer un choix valide ({BOLD}1, 2 ou 3{RESET}).")

    victoire_facile, victoire_moyen, victoire_difficile = jeu_mystere(niveau, victoire_facile, victoire_moyen,
                                                                      victoire_difficile)

    recommencer_partie = 0

    while recommencer_partie not in [1, 2]:
        try:
            recommencer_partie = int(input(f"Voulez-vous recommencer une partie ?"
                                           f" {LIGHT_GREEN}1. Oui{RESET} / {RED}2. Non{RESET} : "))
            if recommencer_partie == 1:
                recommencer_partie = 1
                os.system('cls')  # clear console
            elif recommencer_partie == 2:
                print("Merci d'avoir joué.")
                recommencer_partie = 2
            else:
                os.system('cls')  # clear console
                print(f"{RED}ERREUR{RESET}: Veuillez entrer un choix valide ({BOLD}1 ou 2{RESET}).")
        except ValueError:
            os.system('cls')  # clear console
            print(f"{RED}ERREUR{RESET}: Veuillez entrer un choix valide ({BOLD}1 ou 2{RESET}).")

    if recommencer_partie == 2:
        recommencer = False

print(f"Nombre de parties gagnées en difficulté facile : {victoire_facile}")
print(f"Nombre de parties gagnées en difficulté moyen : {victoire_moyen}")
print(f"Nombre de parties gagnées en difficulté difficile : {victoire_difficile}")
