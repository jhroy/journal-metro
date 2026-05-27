# ©2026 Jean-Hugues Roy, UQAM.
# coding : utf-8

### ÉTAPE 1 - ON IMPORTE LES MODULES REQUIS

import csv, requests, json
from bs4 import BeautifulSoup as soupe

### ÉTAPE 2 - ON MONTRE PATTE BLANCHE ET ON FAIT DE LA RECHERCHE
### (SURTOUT DE LA RECHERCHE EN JOURNALISME)
### À VISIÈRE LEVÉE ET ON S'IDENTIFIE DANS CHACUNE DES REQUÊTES QU'ON VA ENVOYER À MÉTRO

entete = {
	"From":"Jean-Hugues Roy, UQAM; roy.jean-hugues@uqam.ca; 514/778-6102"
}

### ÉTAPE 3 - JE CRÉE UNE VARIABLE CONTENANT LE NOM DE CHAQUE JOURNAL ET LES NUMÉROS DE DÉPART ET DE FIN DE CHACUN

journaux = [
	{
		"journal":"journalmetro",
		"début":3202100,
		"fin":3213601
	},
	{
		"journal":"metroquebec",
		"début":395000,
		"fin":402351
	},
	]

### NOM DU FICHIER DANS LEQUEL LES RÉSULTATS SERONT SAUVEGARDÉS
fichierOut = "articlesMetro.csv"

### ÉTAPE 4 - BOUCLE POUR GÉNÉRER TOUS LES URLS QU'ON SOUHAITE VÉRIFIER

for journal in journaux:
	for p in range(journal["début"],journal["fin"]):
		# print(p, journal["journal"])
		url = f'https://{journal["journal"]}.com/wp-json/wp/v2/posts/{p}'
		# print(url)

		contenu = requests.get(url, headers=entete)
		print(contenu,url)

		if contenu.status_code == 200: ### ON NE PROCÈDE QUE SI ON OBTIENT UN 200
			d = contenu.json()

			### ON VA CHERCHER TOUTES LES INFOS PERTINENTES

			url = d["link"]
			cree = d["date"]
			modif = d["modified"]
			titre = soupe(d["title"]["rendered"],"html.parser").text.strip()
			texte = soupe(d["content"]["rendered"],"html.parser").text.replace("\xa0"," ").replace("\n"," ") ### ON RETRANCHE LES ESPACES INSÉCABLES ET LES RETOURS DE CHARIOT DANS LE TEXTE
			while "  " in texte:
				texte = texte.replace("  ", " ").strip() ### ON RETRANCHE LES DOUBLE ESPACES DANS LE TEXTE
			auteur = d["author_name"]
			section1 = d["yoast_primary_term"]["term_name"]
			section2 = d["yoast_primary_term"]["term_link"]

			try:
				urlImage = d["featured_image_a_la_une_full"]
				# print(urlImage)
				nomImage = urlImage.split("/")[-1].strip()
				# print(nomImage)
			except:
				urlImage = "?"
				nomImage = "?"

			### SI IMAGE IL Y A, ON LA SAUVEGARDE DANS UN RÉPERTOIRE APPELÉ «FOTOS»

			try:
				data = requests.get(urlImage, headers=entete).content
				f2 = open(f"fotos/{nomImage}",'wb')
				f2.write(data)
				f2.close()
			except:
				pass

			infos = [journal,p,cree,modif,url,titre,auteur,section1,section2,texte,nomImage,urlImage]
			print(infos)

			### ENREGISTREMENT DES DÉTAILS DANS LE FICHIER CSV

			jounal = open(fichierOut, "a")
			metro = csv.writer(jounal)
			metro.writerow(infos)
			jounal.close()
			print(".....")