# On importe la librairie et on utilise que la fonction pyplot
import matplotlib.pyplot as pyplot
# On importe Numpy pour effectuer des calculs mathématiques ensuite dans le traitement
import numpy as np

# Déclaration des labels et des données dans des tableaux (listes)
labels = ['Paris', 'Seine et Marne', 'Yvelines', 'Essone', 'Haut-de-Seine', 'Seine-Saint-Denis','Val-de-Marne','Val-D\'Oise']
values = [1107, 70, 78, 111, 367, 369, 354, 69]

# Fonction proposée par l'équipe de Matplotlib
# Permettant d'afficher la valeur réelle au label % du chart
def real_label(pct, allvals):
    absolute = int(round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d})".format(pct, absolute)

# On configure le chart
'''
fig1, ax1 = pyplot.subplots()
ax1.pie(values, explode = (0, 0.2, 0, 0, 0, 0, 0, 0), labels=labels, autopct=lambda pct: real_label(pct, values))
ax1.axis('equal')  # Pour avoir un chart 100% circulaire
'''


pyplot.figure(figsize = (10, 10))
pyplot.pie(values, explode = (0, 0, 0, 0, 0.2, 0, 0, 0),
           labels = labels,
           colors = ['lightseagreen', 'mediumaquamarine','teal','greenyellow', 'springgreen', 'limegreen', 'green', 'seagreen'],
           autopct = lambda x: str(round(x, 2)) + '%',
           pctdistance = 0.7, labeldistance = 1.4,
           shadow = True)
#pyplot.legend()

# On affiche notre chart avec toutes ses configurations
pyplot.show()