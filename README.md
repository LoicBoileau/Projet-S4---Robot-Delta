# Projet-S4---Robot-Delta
Projet de session hiver 2020 Équipe 1 Université de Sherbrooke - Robot Delta

## Licence MIT
Puisque notre projet est en open source, nous avons opté pour une licence MIT, car c'est une licence très permissive et très simple. Elle permet à tous les utilisateurs d'utiliser notre projet à leur guise, c'est-à-dire le modifier, le distribuer, l'utiliser à des fins commerciales ainsi que l'utiliser en privé. Toutefois, nous n'avons pas de garantie sur ce qui arrive avec ceux qui utilisent notre projet et ils ne peuvent pas nous poursuivre si jamais ils se blessent ou autre.

Pour une description complète de la License, voir le fichier License.

## Partie mécanique
Pour voir la liste des matériaux, les étapes d'assemblage du robot ainsi qu'une description des fichiers et des pièces, allez voir dans le fichier Robot_Delta_CAD.

## Mathématiques du modèle
Une simulation physique a été conçue pour décrire la cinématique directe et inverse du robot.
-Disponible [ici](https://github.com/LoicBoileau/Projet-S4---Robot-Delta/tree/master/Simulations%20Physiques).

## Programmer les moteurs
Pour programmer les moteurs Dynamixel, il faut aller consulter le fichier "README" dans le répertoire "Controle_moteurs" 

## Requis pour l'Interface graphique
### Composantes
  - RaspberryPi avec python 3.4 installé (ou une version moins récente)
  - Python 3.4 installé sur un ordinateur pour programmer sur un ordinateur 
  - Librairies PySide et PySerial installées dans python 3.4 ou dans un environnement virtuel
  - IDE de programmation pour python (i.e. Visual Studio ou Visual Studio Code)
  
### Main pour Interface graphique
GUI.py est le main pour l'interface graphique et dépend du fichier de setup du UI appelé Mainwindow34.py

### Designer .UI
Pour accéder au designer de .ui de Qt, accéder au virtualEnvironnement ou le dossier contenant les librairies de python 3.4.
Dans le fichier, aller ensuite dans "Lib", "site-packages", "PySide" et cliquer sur le .exe appelé "designer.exe".

### Convertir .ui à .py 
Aller dans le menu de VS "outils" ou "tools", ensuite aller dans "ligne de commande", "invite de commande développeur" et entrer les deux commandes suivantes :
* cd Controls
* pyside-uic Mainwindow.ui -o Mainwindow34.py

### Creation de l'environnement virtuel à programmer
Pour programmer le UI, il faut un environnement virtuel qui contient les librairies utilisées.
Pour en créer un nouveau,il faut aller dans "Explorateur de solutions". Choisir 
la version de python et ensuite prendre le fichier requirements.txt pour télécharger les bonnes 
librairies.


