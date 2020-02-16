# Projet-S4---Robot-Delta
Projet de session hiver 2020 Équipe 1 Université de Sherbrooke - Robot Delta


# Designer .UI
Pour accéder au designer de .ui de Qt, accéder au virtualEnvironnement appeler RaspberryPi.
Dans le fichier, tu vas ensuite dans "Lib", "site-packages", "PySide2"
et tu cliques sur le .exe appelé "designer.exe"

# Converting .ui to .py 
Aller dans le menu de VS "outils" ou "tools", ensuite aller dans "ligne de commande",
"invite de commande développeur" et entrer les deux commandes suivantes :
cd Controls
pyside2-uic Mainwindow.ui -o Mainwindow.py