# Projet-S4---Robot-Delta
Projet de session hiver 2020 Équipe 1 Université de Sherbrooke - Robot Delta


## Designer .UI
Pour accéder au designer de .ui de Qt, accéder au virtualEnvironnement créer pour être capable de runner pyside.
Dans le fichier, aller ensuite dans "Lib", "site-packages", "PySide"
et cliquer sur le .exe appelé "designer.exe".

## Convertir .ui à .py 
Aller dans le menu de VS "outils" ou "tools", ensuite aller dans "ligne de commande",
"invite de commande développeur" et entrer les deux commandes suivantes :
cd Controls
pyside-uic Mainwindow.ui -o Mainwindow34.py

## Creation de l'environnement virtual à programmer
Pour programmer le UI, il faut un environnement virtuel qui contient les librairies utilisées.
Pour ce faire, lorsque la solution est téléchargée, en créer un nouveau en allant dans "Explorateur de solutions". Choisir 
la version de python et ensuite prendre le fichier requirements.txt pour télécharger les bonnes 
librairies.

## Programmer les moteurs
Pour programmer les moteurs Dynamixel, il faut le IDE d'Arduino avec la librairie de OpenCR.
La programmation n'est pas très complexe, puisque la librairie contient des exemples de codes qui 
permettent de facilement intégrer la fonctionnalité désirée.

http://emanual.robotis.com/docs/en/parts/controller/opencr10/
http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/
