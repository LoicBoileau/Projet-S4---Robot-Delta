# Projet-S4---Robot-Delta
Projet de session hiver 2020 Équipe 1 Université de Sherbrooke - Robot Delta


## Designer .UI
Pour accéder au designer de .ui de Qt, accéder au virtualEnvironnement appelé RaspberryPi.
Dans le fichier, aller ensuite dans "Lib", "site-packages", "PySide2"
et cliquer sur le .exe appelé "designer.exe".

## Converting .ui to .py 
Aller dans le menu de VS "outils" ou "tools", ensuite aller dans "ligne de commande",
"invite de commande développeur" et entrer les deux commandes suivantes :
cd Controls
//Pas prendre cette commande//pyside2-uic Mainwindow.ui -o Mainwindow38.py
pyside-uic Mainwindow.ui -o Mainwindow34.py

## Creating the virtual environnement to program
Pour programmer le UI, il faut un environnement virtuel qui contient les librairies utilisées.
Pour ce faire, lorsque la solution est téléchargée, premièrement enlever du dossier l'environnement
virtuel appelé RaspberryPi et en créer un nouveau en allant dans "Explorateur de solutions". Choisir 
la version de python et ensuite prendre le fichier requirements.txt pour télécharger les bonnes 
librairies.
