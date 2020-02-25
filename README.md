# Projet-S4---Robot-Delta
Projet de session hiver 2020 Équipe 1 Université de Sherbrooke - Robot Delta

## License MIT
Pour une description complète de la License, voir le fichier License.

## Partie mécanique
Pour voir la liste des matériaux, les étapes d'assemblage du robot ainsi qu'une description des fichiers et des pièces allez voir dans la fichier Robot_Delta_CAD.

## Mathématiques du modèle
Une simulation physique a été conçu pour décrire la cinématique directe et inverse du robot.
-Disponible [ici](https://github.com/LoicBoileau/Projet-S4---Robot-Delta/tree/master/Simulations%20Physiques).

## Programmer les moteurs
Pour programmer les moteurs Dynamixel, il faut aller consulter le fichier "README" dans le répertoire "Controle_moteurs" 

## Requis pour l'Interface graphique
### Coposantes
  - RaspberryPi avec python 3.4 installé (ou une version moins récente)
  - Python 3.4 installé pour programmer sur un ordinateur 
  - Librairie pyside et pyserial installé dans python 3.4 ou dans un environnement virtuel
  - IDE de programmation pour python (i.e. Visual Studio ou Visual Studio Code)
  
### Main pour Interface graphique
GUI.py est le main pour l'interface graphique et dépend du fichier de setup du UI appelé Mainwindow34.py

### Designer .UI
Pour accéder au designer de .ui de Qt, accéder au virtualEnvironnement ou le dossier contenant les librairies de python 3.4.
Dans le fichier, aller ensuite dans "Lib", "site-packages", "PySide"
et cliquer sur le .exe appelé "designer.exe".

### Convertir .ui à .py 
Aller dans le menu de VS "outils" ou "tools", ensuite aller dans "ligne de commande",
"invite de commande développeur" et entrer les deux commandes suivantes :
cd Controls
pyside-uic Mainwindow.ui -o Mainwindow34.py

### Creation de l'environnement virtual à programmer
Pour programmer le UI, il faut un environnement virtuel qui contient les librairies utilisées.
Pour ce faire, lorsque la solution est téléchargée, premièrement enlever du dossier l'environnement
virtuel appelé RaspberryPi et en créer un nouveau en allant dans "Explorateur de solutions". Choisir 
la version de python et ensuite prendre le fichier requirements.txt pour télécharger les bonnes 
librairies.


