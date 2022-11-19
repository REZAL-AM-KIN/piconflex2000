print("Demarrage 'setting.py'")


# Définition des variables reliée à l'objet setting définissant les paramètres de la box. Ces paramètres sont sauvegardés et résistent au reboot
class setting:
    projet_path = "/".join(__file__.split("/")[:-2]) + "/"
    # Nom de la box (Données par la BDD au démarrage), il définie le rôle de la box selon la première lettre (ATTENTION: Première lettre toujours en majuscule)
    nomBox = 'BZ2'
    # Numéro de la box, permet d'identifié de façon unique les boxs (clé primaire) pour la BDD
    numeroBox = 0
    # Version du système, permet de savoir quand une MAJ est a faire
    version = ''
    # Paramètre indiquand au système si la box a ping le serveur (010)
    rezalOn = False
    # Paramètre indiquand si la box est en mode hors ligne ou pas (001)
    rezalMode = False
    # Paramètre indiquant si la box à ping un réseau internet(100)
    rezalNet = False
    # IP de la box
    IP = ''
    # Adresse MAC de la box
    MAC = ''
    # Dictionnaire des produits de la box
    produits = {}
    # Définition du dictionnaire de connection à la BDD
    # Nom d'utilisateur
    # Mot de passe du nom d'utilisateur
    # Nom de la BDD
    # IP du serveur BDD
    connection = {"user": 'user',
                  "password": 'password',
                  "database": 'Guinche',
                  "host": 'X.X.X.X'}
    serveurNet = "8.8.8.8"
# Adresse IP DNS google qui répond au ping
