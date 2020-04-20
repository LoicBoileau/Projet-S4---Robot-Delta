# ReadMe pour la vision.
## Étapes pour faire fonctionner la vision

* Installer l'image qui se trouve: https://github.com/LoicBoileau/Projet-S4---Robot-Delta
* Se connecter au Raspberry Pi;
* Brancher la Webcam au RaspberryPi via la prise USB;
* Exécuter le code et prendre la planche de travail en photo lorsque souhaité.


## Informations utiles
* À cause de la distanciation sociale il a été impossible d'intégrer la vision au robot c'est pourquoi la touche espace est présente pour prendre les photos. 

* Pour les tests, l'IDE PyCharm sur un ordinateur personnel a été utilisé, dans le but d'avoir plus de rapidité de traitement d'image ainsi qu'une meilleure qualité de caméra. Cependant, le code fonctionne très bien sur le Raspberry Pi. Il suffit d'utiliser Python IDLE et d'exécuter le code. 

## Option #2
* Si l'image mentionnée précédement n'est pas installée il faut installer l'image au lien suivant: https://github.com/UdeS-GRO/pi-gen et installer les paquets mentionnés dans le dossier stage5;

Si ce n'est pas fait il faut installer les paquets suivants pour l'interface robot avec Qt, si c'est fait on peut passer les 3 prochaines étapes:
* Installer pip avec la commande: sudo apt-get install python3-pip
* Installer PySide avec la commande: sudo apt-get install python3-pyside
* Installer PySerial avec la commande: python3 -m pip install pyserial

Suite des étapes:
* Ensuite il faut installer python3.4 avec la commande: sudo apt-get install python3.4;
* Installer la librairie OpenCV avec la commande: pip install opencv-python==3.4.1.15;
* Installer la librairie numpy avec la commande: pip install numpy;
* Installer la librairie csv avec la commande: pip install csv; 
  
## Sources utiles
* Pour le calcul du centre de masse: https://www.learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/
* Pour l'algorithme de détection de contours: https://www.youtube.com/watch?v=6AY5p1uC5gM
