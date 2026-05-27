![](https://journalmetro.com/wp-content/uploads/2022/10/logo-metro.svg)

# Moissonnage du *Journal Métro* et de *Métro Québec*

---

Pour [*Le Trente*](https://www.fpjq.org/fr/les-editions), bimestriel de la [Fédération professionnelle des journalistes du Québec (FPJQ)](https://www.fpjq.org/fr/), j'ai moissonné la totalité du contenu du [*Journal Métro*](https://journalmetro.com/) et de son édition de Québec, [*Métro Québec*](https://metroquebec.com/), depuis leur renaissance le 1<sup>er</sup> octobre 2025.

L'objectif de ce moissonnage était d'analyser la part de l'IA générative dans la production des deux médias en ligne. [Au moment de relancer leurs activités](https://journalmetro.com/actualites/3202240/le-journal-metro-relance-officiellement-ses-activites/), les artisans du journal avaient annoncé qu'ils seraient, à leur connaissance, **«&nbsp;la première salle de presse d’une grande ville canadienne à utiliser l’intelligence artificielle pour générer directement une partie du contenu&nbsp;»**. 🤖

Après sept mois d'activités, le moment était venu d'examiner cette utilisation.

## Moissonner WordPress

Les deux journaux utilisent WordPress comme système de gestion du contenu. WordPress dispose d'une API cachée qui permet d'accéder à des données structurées en JSON sur un article donné. Il suffit de connaître les numéros d'identification unique de chaque article.

Pour s'assurer de moissonner l'ensemble de ce qui a été publié, il suffit de tester **tous les numéros possibles** à partir d'un numéro de départ correspondant à un article ayant été publié à la date à laquelle on souhaite commencer. Dans ce cas-ci, la date de départ est le 1<sup>er</sup> octobre. J'ai donc pris les articles qui annonçaient la relance des activités du *Journal Métro* et de *Métro Québec* comme point de départ dans les deux cas.

Dans l'URL de l'article pour l'édition montréalaise, on voit que le numéro d'identification unique est **3202240**&nbsp;:
* https://journalmetro.com/actualites/3202240/le-journal-metro-relance-officiellement-ses-activites/

Dans l'URL de l'article pour l'édition de Québec, on voit que le numéro d'identification unique est **395109**&nbsp;:
* https://metroquebec.com/actualites/395109/metro-quebec-relance-officiellement-ses-activites/

Cet API caché a la structure suivante&nbsp;:

```
https://<nom de domaine>/wp-json/wp/v2/posts/<numéro d'idenfication>
```

Ainsi, pour chacun des articles annonçant le retour en ligne des sites de *Métro*, on obtient&nbsp;:

* https://journalmetro.com/wp-json/wp/v2/posts/3202240
* https://metroquebec.com/wp-json/wp/v2/posts/395109

Les intervalles considérés pour m'assurer de ne rater aucun article sont&nbsp;:

* Dans le cas du *Journal Métro* (Montréal), de 3202100 à 3213601 (ou 11&nbsp;000 possibilités)
* Dans le cas de *Métro Québec*, de 395000 à 402351 (ou 7&nbsp;350 possibilités)

Le [script qui accompagne ce répertoire (**metro.py**)](https://github.com/jhroy/journal-metro/blob/main/metro.py) fait donc 18&nbsp;850 appels aux sites de Métro Média.

## Trois types de réponse possibles

En testant tous ces numéros, j'ai obtenu trois réponses différentes.

### `404`

Le numéro d'identification n'a jamais été utilisé. C'est le code HTTP de réponse le plus courant que j'aie obtenu, comme [ici](https://journalmetro.com/wp-json/wp/v2/posts/3202100).

### `401`

Le numéro d'identification a déjà été utilisé, mais l'article n'a jamais été publié ou a été retranché. En tous cas, on obtient le code `401`, ce qui signifie *Forbidden*, comme [ici](https://journalmetro.com/wp-json/wp/v2/posts/3202195).

### `200`

Ça marche! Un article en ligne correspond à ce numéro. Je peux en extraire le contenu aux fins de cette recherche, incluant l'image principale utilisée par l'article, car l'IA dans la génération des images est également un enjeu dans la relance de ce média.

![Capture d'écran d'un article de Métro Québec](patinoireSteFouilleOuilleOuille.png)
#### Cette image d'une patinoire qui n'existe pas est [toujours en ligne sur le site de *Métro Québec*](https://metroquebec.com/actualites/400677/la-ville-de-quebec-optimise-la-gestion-de-ses-patinoires-exterieures/) au moment de mettre ce répertoire en ligne (capture d'écran - 25 mai 2026).

---

Mon code génère un fichier CSV. [Il est accessible dans ce répertoire](https://github.com/jhroy/journal-metro/blob/main/articlesMetro_pourGithub.csv).

Mais je l'ai modifié ainsi :

* J'ai retranché le contenu des articles car, même s'il est en grande partie (plus de le moitié du contenu et des articles ont été rédigés par un [**«&nbsp;Agent IA&nbsp;»**](https://journalmetro.com/auteur/miametro/)), il est protégé par la *Loi sur le droit d'auteur* du Canada.

* J'ai ajouté une colonne (« mention ia dans texte ») pour signaler les textes qui se terminaient par une mention que le texte a été généré par l'IA. Cette mention est généralement celle-ci&nbsp;: *«&nbsp;Cet article a été produit par l’intelligence artificielle et édité par un journaliste. Veuillez consulter notre [Politique d’utilisation de l’intelligence artificielle à des fins journalistiques](https://journalmetro.com/politique-dutilisation-de-lintelligence-artificielle-du-journal-metro/) pour en savoir davantage sur nos pratiques concernant l’IA. Pour toute question, contactez Olivier Robichaud, rédacteur en chef, à l’adresse orobichaud@journalmetro.com.&nbsp;»*
