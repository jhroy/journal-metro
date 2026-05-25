# journal-metro

## Moissonnage du Journal Métro et de Métro Québec

---

Pour [*Le Trente*](https://www.fpjq.org/fr/les-editions), bimestriel de la [Fédération professionnelle des journalistes du Québec (FPJQ)](https://www.fpjq.org/fr/), j'ai moissonné la totalité du contenu du [*Journal Métro*](https://journalmetro.com/) et de son édition de Québec, [*Métro Québec*](https://metroquebec.com/), depuis leur renaissance le 1<sup>er</sup> octobre 2025.

L'objectif de ce moissonnage était d'analyser la part de l'IA générative dans la production des deux médias en ligne. [Au moment de relancer leurs activités](https://journalmetro.com/actualites/3202240/le-journal-metro-relance-officiellement-ses-activites/), les artisans du journal avaient annoncé qu'ils seraient, à leur connaissance, **«&nbsp;la première salle de presse d’une grande ville canadienne à utiliser l’intelligence artificielle pour générer directement une partie du contenu&nbsp;»**.

Après sept mois d'activités, le moment était venu d'examiner cette utilisation.

### Moissonner WordPress

Les deux journaux utilisent WordPress comme système de gestion du contenu. WordPress dispose d'une API cachée qui permet d'accéder à des données structurées en JSON sur un article donné. Il suffit de connaître les numéros d'identification unique de chaque article.

Pour s'assurer de moissonner l'ensemble de ce qui a été publié, il suffit de tester **tous les numéros possibles** à partir d'un numéro de départ correspondant à un article ayant été publié à la date à laquelle on souhaite commencer. Dans ce cas-ci, la date de départ est le 1<sup>er</sup> octobre. J'ai donc pris les articles qui annonçaient la relance des activités du *Journal Métro* et de *Métro Québec* comme point de départ dans les deux cas.

Dans l'URL de l'article pour l'édition montréalaise, on voit que le numéro d'identification unique est **3202240**&nbsp;:
* https://journalmetro.com/actualites/3202240/le-journal-metro-relance-officiellement-ses-activites/

Dans l'URL de l'article pour l'édition de Québec, on voit que le numéro d'identification unique est **395109**&nbsp;:
* https://metroquebec.com/actualites/395109/metro-quebec-relance-officiellement-ses-activites/

