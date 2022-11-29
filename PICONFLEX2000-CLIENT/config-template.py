print("Démarrage 'config.py'")


class config:  # Définition des variables reliée à l'objet config définissant les paramètres du gala (guinche)
    # Les hash sont salés avec codeHash (précédemment avec codeGuinche).
    # codeGuinche (permet de différentier une carte provenant d'un guinche antérieur, à changer absolument à chaque guinche)
    # Code Admin permettant d'accéder au menu admin
    # Code modérateur permettant d'accéder au menu modérateur
    # Code helper permettant d'accéder au menu helper
    # Code VP permettant d'accéder au menu VP
    # Code user permettant d'accéder au menu user
    # Code permettant de débloquer la box en mode caisse
    # Code permettant de débloquer la box en mode Kve
    # Code permettant de débloquer la box en mode Oenols
    # Code permettant de débloquer la box en mode Gazole
    # Code permettant de débloquer la box en mode Bar
    # Code permettant de débloquer la box en mode Nourriture
    # Code permettant le passage en mode hors ligne de la box
    codeHash        = "AZERTYUIOP"
    codeGuinche     = "QSDFGHJKLM"
    codeAppro       = "WXCVBN"
    codeAdmin       = 2
    codeModerateur  = 3
    codeHelper      = 4
    codeVP          = 5
    codeUser        = 6
    codeCaisse      = 7
    codeKve         = 8
    codeOenols      = 9
    codeGazole      = 10
    codeBar         = 11
    codeNourriture  = 12
    codeSecss       = 13
    codeOffline     = 14

    # Configuration des blocks où sont sauvegardées les données sur les cartes
    # blockArgent : case RFID où sera mis le montant en clair
    # blockHashArgent : case RIFD où est mis le hash de l'argent (Permet d'éviter la triche montant)
    # blockHashUID : case RFID où sera mis le hash de l'UID de la carte (Permet de vérifier que le contenu d'une carte n'a pas été copié sur une autre)
    # blockHashCodeGuinche : case RFID où sera mis le hash du code guinche (vérifie si la carte est périmée)
    blockArgent             = 6
    blockHashArgent         = 4
    blockHashUID            = 8
    blockHashCodeGuinche    = 10

    # Montant en centimes minimal à pouvoir mettre pendant une transaction
    minMontant = 100
    # Montant max à pouvoir être mis sur une carte
    maxTransaction = 9900
    # Montant en centime maximal à pouvoir être contenu sur une carte
    maxMontant = 15000

    # Liste des menus et leurs sous menus associés
    menuAdmin = ["menuAdmin", "resetBDD", "resetLogQuery", "resetLogSQL", "resetLogError"]
    menuModerateur = ["menuModerateur", "githubPull", "MAJGitClone","setCarteAppro"]
    menuVP = ["menuVP", "setNumeroBox", "setRezalMode", "setIPServeur", "setNomBox", "setLoginBDD", "setMDPBDD"]
    menuHelper = ["menuHelper", "fusionCartes", "setCaisse", "setKve", "supprimerTransaction", "resetCarte",
                  "resetCarteRFID", "resetCarteBDD", "getCarteUID"]
    menuUser = ["menuUser", "viewMAC", "viewIP", "viewIPServeur", "viewPing", "viewProduits"]
    menuPrincipal = ["menuPrincipal", "menuUser", "menuHelper", "menuVP", "menuModerateur", "menuAdmin"]

    # pour avoir des affichages dans la console pour savoir à où le code en est
    debugging = False
