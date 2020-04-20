# ReadMe pour la vision.
## Étapes pour faire fonctionner la vision
* Installer pip avec la commande: sudo apt-get install python3-pip (si ce n'est pas fait);
* Installer la librairie OpenCV avec la commande: pip install opencv-python==3.4.1.15;
* Installer la librairie numpy avec la commande: pip install numpy;
* Installer la librairie csv avec la commande: pip install csv; 
* Se connecter au Raspberry Pi avec un écran et un clavier;
* Brancher la Webcam au RaspberryPi via la prise USB;
* Exécuter le code dans Python IDLE ou autre et prendre la planche de travail en photo lorsque souhaité;
* Pour la documentation du code allez voir les commentaires dans ce dernier.

## Informations utiles
* À cause de la distanciation sociale, il a été impossible d'intégrer la vision au robot c'est pourquoi la touche espace est présente pour prendre les photos. 

* Pour les tests, l'IDE PyCharm sur un ordinateur personnel a été utilisé, dans le but d'avoir plus de rapidité de traitement d'image ainsi qu'une meilleure qualité de caméra. Cependant, le code fonctionne très bien sur le Raspberry Pi. Il suffit d'utiliser Python IDLE et d'exécuter le code. 
  
## Sources utilisées
* Pour le calcul du centre de masse: https://www.learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/
* Pour l'algorithme de détection de contours: https://www.youtube.com/watch?v=6AY5p1uC5gM
