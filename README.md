# data-analyse-python
on m'a confié un projet qui comprend de la data analyse avec un grand prétraitement en python

initialement, on m'a confié juste la réalisation d'un graphique de monter en charge sur power BI.
Vu le data cet initial, il me manquait beaucoup de donnée.

voici un exemple dû data set que je devais recevoir;

![image](https://user-images.githubusercontent.com/99668071/159010816-d2c3e584-f62c-4a5b-bfef-172c58f2fd69.png)

cela représente que 1 élément pour chaque colonne, or j'ai ce type de données pour plus de 20 0 00 trains, soit pour un volume total de plus de 10 milliards de lignes.
cette quantité de données est trop importante à la fois pour un ordinateur et un serveur.
par conséquent par soucis de place j'ai reçu ce même dataset avec les lignes 0 supprimées.

![image](https://user-images.githubusercontent.com/99668071/159011399-16e9a742-6e8e-41ba-9a00-2dfcd85525ed.png)

d'un point de vue taille de la donnée, cela est plus gérable et chargable dans un outil comme excel ou power BI.

le challenge est de créer ces valeurs intermédiaires sans les stocker dans un data set.

Cela est facilement faisable en python avec un filldown() et un cumsum() et j'ai même réussi à le faire (cf =capture py), le problème consista à la capacité de calcul de l'ordinateur et la taille des fichiers. Il était trop volumineux même pour des HTML.

j'ai même exploré des solutions power BI mais cela reste toujours un échec.

finalement la solution réside dans le python de power BI.

"""
import matplotlib.pyplot as plt 
import pandas as pd
ax=plt.gca()

dataset = dataset.groupby(["Heure"]).agg("sum").reset_index()
second_dataset = pd.DataFrame([[elem] for elem in range(24)], columns=["Heure"])
third_dataset=pd.DataFrame(["DATE"])

dataset = dataset.merge(second_dataset, on="Heure", how="outer").fillna(0)
dataset = dataset.sort_values(by="Heure", ascending=True)

dataset["nb_reservation"] = dataset["nb_reservation"].cumsum()

dataset.plot(kind='line',x="Heure",y="nb_reservation",color='red',ax=ax) 
plt.show()

"""""
ce code permet de créer les valeurs manquantes sans les stocker car elles sont mises en graph directement. cela fut une solution en python mais pas importable en power bi directement. en effet, on peut coder du python dans power bi mais il n’y a pas lieu direct hors code interne.

finalement, cela donne ce résultat.

![image](https://user-images.githubusercontent.com/99668071/159014221-25b4791e-06c7-48f6-93a7-09a91d678dd6.png)

![image](https://user-images.githubusercontent.com/99668071/159014359-541df663-dabb-4523-9b42-0caa1e5494e3.png)

finalement, pour industrialiser ma solution, grace à un code python  (que je peux pas partager due à la présence de paramètres du serveur Sncf) j'ai importé de l'excel original pour exécuter mon dataset à partir d'une requête SQL  pour les prochains dataset plus important vue que les performances sont meilleures.

le problème aux 1res abords a l'air simple mais plus je l'ai exploré plus je me suis confronté à des problèmes que j'ai résolus au fur et à mesure.


