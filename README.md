# Projet-S4---Robot-Delta
Projet de session hiver 2020 Équipe 1 Université de Sherbrooke - Robot Delta

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
//Pas prendre cette commande//pyside2-uic Mainwindow.ui -o Mainwindow38.py
pyside-uic Mainwindow.ui -o Mainwindow34.py

### Creation de l'environnement virtual à programmer
Pour programmer le UI, il faut un environnement virtuel qui contient les librairies utilisées.
Pour ce faire, lorsque la solution est téléchargée, premièrement enlever du dossier l'environnement
virtuel appelé RaspberryPi et en créer un nouveau en allant dans "Explorateur de solutions". Choisir 
la version de python et ensuite prendre le fichier requirements.txt pour télécharger les bonnes 
librairies.

### Programmer les moteurs
Pour programmer les moteurs Dynamixel, il faut le IDE d'Arduino avec la librairie de OpenCR.
La programmation n'est pas très complexe, puisque la librairie contient des exemples de codes qui 
permettent de facilement intégrer la fonctionnalité désirée.

http://emanual.robotis.com/docs/en/parts/controller/opencr10/
http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/
