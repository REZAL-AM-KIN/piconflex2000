projet_path="/".join(__file__.split("/")[:-2])+"/"

print("Démarrage 'boot.py'")
exec(open(
    script_path+'PICONFLEX2000-CLIENT/launch.py').read())  # Permet de se servir directement de toutes les fonctionnalités de la box quand il est lancé (Très utile pour DEV)
try:
    exec(open(script_path+'PICONFLEX2000-CLIENT/init.py').read())  # Effectue les premières communications avec le serveur
except:
    exec(open(script_path+'PICONFLEX2000-CLIENT/error.py').read())  # Script de gestion et affichage des erreurs
while True:  # Boucle infinie du script
    try:
        exec(open(
            script_path+'PICONFLEX2000-CLIENT/loop.py').read())  # Execution du script se répétant jusqu'à l'arrêt du système
    except:
        exec(open(script_path+'PICONFLEX2000-CLIENT/error.py').read())  # Script de gestion et affichage des erreurs
