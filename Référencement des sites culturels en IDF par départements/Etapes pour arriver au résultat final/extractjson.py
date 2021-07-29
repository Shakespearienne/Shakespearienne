import requests
import json

# On ouvre le fichier JSON
f = open('cidfjson.json',)

# On récupère le JSON en dictionnaire
data = json.load(f)

# EDIT Alexandre : permet de vérifier le nombre de musée dispo, ici 2525
print(len(data))

# On initialise les listes qui contiendront nos données X et Y
x_value = []
y_value = []


# On fait une boucle FOR pour récupérer une à une les différentes données de notre JSON
# La limite de notre FOR correspond à la longueur de l'objet JSON qu'on reçoit
# EDIT Alexandre : On fait la boucle avec la limite du nombre de musées (soit 2525)
# la variable i ira de 0 à 2524 (2525 pas inclus)
# EDIT Alexandre : Je vérifie si je peux bien récupérer la première donnée
#print(data[0]['NOM_LIEU'])
# Et aussi la deuxième
#print(data[1]['NOM_LIEU'])

for i in range(len(data)):
    # Je récupère le nom du musée
    x_departement = data[i]['DEP']
   
    x_value.append(x_departement)
    
#print(x_value)

print(x_value.count(75))
print(x_value.count(77))
print(x_value.count(78))
print(x_value.count(91))
print(x_value.count(92))
print(x_value.count(93))
print(x_value.count(94))
print(x_value.count(95))


   