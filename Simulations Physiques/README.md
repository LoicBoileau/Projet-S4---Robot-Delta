# Simulation Physiques

![DeltaRobot](https://1ugn2l2m3z2y31d4y73c1m5w-wpengine.netdna-ssl.com/wp-content/uploads/2016/01/Delta-Robot-Diagram.jpg)

## Simulation MotionGenesis

Logiciel de simulation physique permettant semblable à MatLab, permettant de faire des opérations vectoriels.
>Disponible [ici](http://www.motiongenesis.com/). 

 Est utilisé pour faire la cinématique directe, et éventuellement la cinématique inverse.

### Cinématique directe
Description statiques du robot. 
- Prend en **entrée** les angles ![equation](http://www.sciweavers.org/tex2img.php?eq=%20%5Ctheta_1%2C%20%5Ctheta_2&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0) et ![equation](http://www.sciweavers.org/tex2img.php?eq=%20%5Ctheta_3&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0) des moteurs.
- Donne en **sortie** la position ![equation](http://www.sciweavers.org/tex2img.php?eq=P%28x%2Cy%2Cz%29&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0) de la "pince" du robot.

Est décrit par le fichier **MotionGenesis.txt**.

### Cinématique inverse
Description statiques du robot. 
- Donne en **sortie** la position ![equation](http://www.sciweavers.org/tex2img.php?eq=P%28x%2Cy%2Cz%29&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0) de la "pince" du robot.
- Prend en **entrée** les angles ![equation](http://www.sciweavers.org/tex2img.php?eq=%20%5Ctheta_1%2C%20%5Ctheta_2&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0) et ![equation](http://www.sciweavers.org/tex2img.php?eq=%20%5Ctheta_3&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0) des moteurs.
