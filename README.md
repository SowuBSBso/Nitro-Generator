<img width="1716" height="841" alt="Capture d'écran 2025-08-12 091425" src="https://github.com/user-attachments/assets/95bab00d-09d1-4f84-8ab2-49098dac5017" />

Nitro Generator

Un outil Python pour générer des liens de type Discord Nitro et les envoyer automatiquement via un webhook Discord.

Fonctionnalités :

- Génère des liens aléatoires au format https://discord.com/gifts/XXXXXXXXXXXXXXX
- Envoie automatiquement ces liens à un webhook Discord fourni
- Affiche les messages envoyés et les erreurs dans la console

Installation :

1. Clone ce dépôt ou télécharge les fichiers.

2. Installe les dépendances nécessaires avec la commande :
   pip install -r requirements.txt

Utilisation :

Lance le script avec :
   python link_generator.py

À l’ouverture, tu seras invité à entrer l’URL du webhook Discord.  
Le script enverra environ 2 liens par seconde jusqu’à ce que tu l’arrêtes (Ctrl+C).

Précautions :

⚠️ Ce script génère des liens nitro et envoie des messages automatiquement.  
Utilise-le uniquement à des fins légales et responsables.  
L’auteur ne saurait être tenu responsable de toute utilisation abusive ou illégale du script.

Personnalisation :

Tu peux modifier le script pour ajuster la fréquence d’envoi, le format des liens, ou l’apparence.

Auteur :

Created by Uruma
