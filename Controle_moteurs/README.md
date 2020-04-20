### Programmer les moteurs
Pour programmer les moteurs Dynamixel, il faut le IDE d'Arduino avec la librairie de OpenCR.
Il faut également que les moteurs soient alimentés par une source d'alimentation externe, car l'alimentation fournie par le port USB de
l'ordinateur n'est pas suffisante au fonctionnement des moteurs.
La programmation n'est pas très complexe, puisque la librairie contient des exemples de codes qui 
permettent de facilement intégrer la fonctionnalité désirée. Les liens suivants dirigent vers les tutoriels appropriés.
Il est nécessaire de suivre les tutoriels afin d'identifier les moteurs. Afin de spécifier un déplacement des moteurs selon la 
position déterminée, il s'agit de copier dans le IDE d'Arduino le code Controle_Moteur qui permet d'utiliser les 3 moteurs contrairement 
à celui des librairies qui n'en contrôle qu'un seul.

http://emanual.robotis.com/docs/en/parts/controller/opencr10/
http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/

Les nombres spécifiés en paramètres dans la fonction "goalPosition" ne doivent pas dépasser 4096, qui est la résolution de chaque moteur.
Si une telle situation survient, il faut téléverser le programme à nouveau, car les moteurs vont tomber en "erreur". Pour un angle de
90 degrés, par exemple, il faut spécifier 1024 et ajuster par la suite, car la position 0 de chaque moteur n'est pas nécessairement la 
même. Il est également nécessaire de spécifier un délai minimal pour s'assurer que les moteurs atteignent leur position avant que le
prochain ne soit appelé.
