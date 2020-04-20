# Projet-S4---Robot-Delta
Projet de session hiver 2020 Équipe 1 Université de Sherbrooke - Robot Delta

## Licence MIT
Puisque notre projet est en open source, nous avons opté pour une licence MIT, car c'est une licence très permissive et très simple. Elle permet à tous les utilisateurs d'utiliser notre projet à leur guise, c'est-à-dire le modifier, le distribuer, l'utiliser à des fins commerciales ainsi que l'utiliser en privé. Toutefois, nous n'avons pas de garantie sur ce qui arrive avec ceux qui utilisent notre projet et ils ne peuvent pas nous poursuivre si jamais ils se blessent ou autre.

Pour une description complète de la License, voir le fichier License.

## Partie mécanique
Pour voir la liste des matériaux, les étapes d'assemblage du robot ainsi qu'une description des fichiers et des pièces, allez voir dans le fichier Robot_Delta_CAD.

## Partie vision
Pour voir le code de la vision, allez voir dans le fichier vision.

## Mathématiques du modèle
Une simulation physique a été conçue pour décrire la cinématique directe et inverse du robot.
-Disponible [ici](https://github.com/LoicBoileau/Projet-S4---Robot-Delta/tree/master/Simulations%20Physiques).

## Programmer les moteurs
Pour programmer les moteurs Dynamixel, il faut aller consulter le fichier "README" dans le répertoire "Controle_moteurs" 

## Requis pour l'Interface graphique
### Composantes
  - RaspberryPi avec python 3.4 installé (ou une version moins récente)
  - Python 3.4 32 bits installé sur un ordinateur pour programmer sur un ordinateur 
  - Librairies PySide et PySerial installées dans python 3.4 ou dans un environnement virtuel
  - IDE de programmation pour python (i.e. Visual Studio ou Visual Studio Code)
  
### Fonctionnement
L'interface graphique est codée en python et se compile à l'aide du fichier principal (GUI.py) et le fichier de widgets (mainwindow34.py et mainwindow34.ui
Le fichier mainwindow34.py est composé à partir du .ui qui lui se modifie à l'aide du designer.exe de QT. Donc pour modifier le fichier mainwindow34.py, 
il est nécessaire de suivre les instructions suivantes.

### Main pour Interface graphique
GUI.py est le main pour l'interface graphique et dépend du fichier de setup du UI appelé Mainwindow34.py

### Designer .UI
Pour accéder au designer de .ui de Qt, accéder au virtualEnvironnement ou le dossier contenant les librairies de python 3.4.
Dans le fichier, aller ensuite dans "Lib", "site-packages", "PySide"  et trouver le .exe appelé "designer.exe".

### Convertir .ui à .py 
Il est nécessaire de convertir le .ui à .py. Pour ce faire, aller dans le menu de VS "outils" ou "tools", ensuite aller dans "ligne de commande", 
"invite de commande développeur" et entrer les deux commandes suivantes :
* cd Controls
* pyside-uic Mainwindow.ui -o Mainwindow34.py

### Création de l'environnement virtuel à programmer
Pour programmer le UI, il faut un environnement virtuel qui contient les librairies utilisées. (PySide et PySerial)
Pour que les librairies soient disponibles, il est nécessaire de télécharger python3.4 32bits. Ensuite, soit par Visual Studio 
ou par l'invite de commande, installer les librairies.


### Installation des paquets sur le Raspberry Pi
* Installer l'image qui se trouve au lien suivant: https://github.com/UdeS-GRO/pi-gen et installer les paquets mentionnés dans le dossier stage5;
* Ensuite il faut installer python3.4 avec la commande: sudo apt-get install python3.4;
* Installer pip avec la commande: sudo apt-get install python3-pip;
* Installer PySide avec la commande: sudo apt-get install python3-pyside;
* Installer PySerial avec la commande: python3 -m pip install pyserial.
