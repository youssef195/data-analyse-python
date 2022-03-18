# data-analyse-python
on m'a confier un projet qui comprend de la data analyse avec un grand pré-traitement en python

initialement, on m'a confier juste la réalisation d'un graphique de monter en charge sur power BI.
Vue le data set initial, il me manquer beaucoup de donnée.

voici un exemple du data set que je devais recevoir:

![image](https://user-images.githubusercontent.com/99668071/159010816-d2c3e584-f62c-4a5b-bfef-172c58f2fd69.png)

cela represente que 1 élement pour chaque colone, hors j'ai ce type de donnée pour plus de 20 000 train, soit pour un volume total de plus de 10 milliard de ligne.
cette quantité de donée est trop impprtant à la fois pour un ordinateur et un serveur.
par conséquent par soucis de place j'ai recu ce même dataset avec les ligne 0 suprimé.

![image](https://user-images.githubusercontent.com/99668071/159011399-16e9a742-6e8e-41ba-9a00-2dfcd85525ed.png)

d'un point de vue taille de la donnée, cela est plus gérable et chargable dans un outils comme excel ou power BI.

le challenge est de crée ces valeur intermidaire sans les stoccker dans un data set.

Cela est facilement fesable en python avec un un filldown() et un cumsum() et j'ai même reussi à le faire (cf =capture.py), le probléme consistat à la capcité de calcul de l'ordinateur et la taille des fichiers. ils etait trop volumineux même pour des html.

j'ai même explorer des solutions power BI mais cela reste toujours un echec.

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
ce code permet de crée les valeurs manquante sans les stocker car elle sont mis en graph directement. cela fut une solution en python mais pas importable en power bi directement. en effet, on peut coder du python dans power bi mais il y'a pas lien direct hors code interne.

finalement, cela donne ce resultat.

![image](https://user-images.githubusercontent.com/99668071/159014221-25b4791e-06c7-48f6-93a7-09a91d678dd6.png)

![image](https://user-images.githubusercontent.com/99668071/159014359-541df663-dabb-4523-9b42-0caa1e5494e3.png)


le probléme aux 1re abord à l'air simple mais plus je l'ai explorer plus je me suis confronter à des probléme que j'ai resolue au fur et à mesure.


