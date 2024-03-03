# -*- coding: utf-8 -*-
import requests
from gtts import gTTS
from playsound import playsound
import os
import requests

# Fonction pour demander les informations à l'utilisateur
def demander_infos():
    domaine = input("Veuillez entrer le domaine (exemple : reddit.com) : ")
    prenom = input("Veuillez entrer le prénom : ")
    nom = input("Veuillez entrer le nom : ")
    return domaine, prenom, nom

# Fonction pour trouver l'email via l'API Hunter
def trouver_email_hunter(domaine, prenom, nom, api_key):
    url = "https://api.hunter.io/v2/email-finder?domain={domaine}&first_name={prenom}&last_name={nom}&api_key={api_key}".format(domaine=domaine, prenom=prenom, nom=nom, api_key=api_key)
    response = requests.get(url)  # Add this line to make the request
    data = response.json()

    if response.status_code == 200 and 'data' in data and 'email' in data['data']:
        email = data['data']['email']
        score = data['data']['score']
        texte = "L'adresse e-mail trouvée est : {} avec un score de confiance de {}%.".format(email, score)
        print(texte)
        annoncer_resultat(texte)
    else:
        texte = "Aucune adresse e-mail trouvée ou une erreur est survenue."
        print(texte)
        annoncer_resultat(texte)

# Fonction pour annoncer le résultat via synthèse vocale
def annoncer_resultat(texte):
    tts = gTTS(text=texte, lang='fr')
    fichier_temp = "resultat.mp3"
    tts.save(fichier_temp)
    playsound(fichier_temp)
    os.remove(fichier_temp)

# Remplacez 'VOTRE_CLE_API' par votre clé API Hunter réelle
API_KEY = ''

# Exécution du script
if __name__ == "__main__":
    domaine, prenom, nom = demander_infos()
    trouver_email_hunter(domaine, prenom, nom, API_KEY)