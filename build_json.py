# importation des librairies
from contextlib import contextmanager
import sys

# Ouverture du fichier original flights_first.json en mode read
# Ouverture du fichier contenant le bon format en mode write
f1 = open("data/flights_first.json", "r")
f2 = open("data/flights.json", "w")

# Création d'un générateur capable récupérer les lignes une par une
rec_lines = (line for line in f1)

# Initialisation de la variable base contenant le stdout de base
base = sys.stdout

# Changement de l'environnement de saisie à celui du fichier flights.json
sys.stdout = f2

# Création d'une boucle for qui nous permet de spliter les lignes au niveau du caractère "
# la modification des caractères ' en ", la rejointure des parties de la ligne après transformation
# cela est fait pour chaque ligne. Ajout de retour à la ligne après des lignes dans le fichier.
for i, rec in enumerate(rec_lines):
    splited = rec.split('"')
    for p, j in enumerate(splited):
        if (j.__contains__(":")):
            splited[p] = j.replace("'", '"')
    rec = '"'.join(splited)
    if i+1 < 32000:
        print(rec, end='')
    else:
        print(rec)
        
# Remise de l'environnement de saisie à la normale
sys.stdout = base

# Fermeture des deux fichiers
f1.close()
f2.close()