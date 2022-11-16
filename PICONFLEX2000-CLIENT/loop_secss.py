print("Demarrage 'loop_secss.py'")
while True: #Seconde boucle infinie permettant d'utiliser la commande "break" pour arreter la transaction
    RFID_waitRetireCarte() #Attente d'absence de cartes
    MENU_menuPrincipal() #Attente d'une carte et possibilité de naviguer dans les menus

    UID,argent,hashCodeType,hashUID,hashArgent=RFID_readCarte() #Multi lecture des données de la carte
    DATA_setVariable("rezalOn", bool(REZAL_pingServeur())) #Ping du serveur pour s'assurer que la connection est toujours présente

    if setting.rezalOn:
        if hashCodeType == CRYPT_hashage(config.codeGuinche) or len(SQL_SELECT(QUERRY_getArgent(STRING_uidStrToInt(UID))))>0:
            hint("CARTE D'ARGENT",4) #Affichage synchronisation
            sleep(2)
            break

        # syncronisation des données sur la carte
        if hashCodeType!=CRYPT_hashage(config.codeAprro):
            hint("SYNCH RFID H TYPE",4) #Affichage synchronisation
            RFID_setHashCodeType(config.codeAprro,UID)
        if hashUID!=CRYPT_hashage(UID):
            hint("SYNCH RFID H UID",4) #Affichage synchronisation
            RFID_setHashUID(UID) #Ecriture du hash de l'UID sur la carte

        # ecriture de l'UID dans la BDD
        hint("BDD SYNC",3) #Affichage synchronisation
        hint("ATTENTE COMMANDES",4) #Affichage synchronisation

        #attente du retrait de la carte
        while RFID_carteCheck():
            sleep(0.5)
            hint("",4) #Affichage synchronisation
            sleep(0.5)
            hint("ATTENTE COMMANDES",4) #Affichage synchronisation