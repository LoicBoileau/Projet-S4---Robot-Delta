# Simulations Physiques

![DeltaRobot](https://1ugn2l2m3z2y31d4y73c1m5w-wpengine.netdna-ssl.com/wp-content/uploads/2016/01/Delta-Robot-Diagram.jpg)

## Simulation MotionGenesis

Logiciel de simulation physique, semblable à MatLab, permettant de faire des opérations vectorielles.
>Disponible [ici](http://www.motiongenesis.com/). 

 Est utilisé pour faire la cinématique directe et, éventuellement, la cinématique inverse.

### Cinématique directe
Description statique du robot. 
- Prend en **entrée** les angles &theta;<sub>1</sub>, &theta;<sub>2</sub> et &theta;<sub>3</sub> des moteurs.
- Donne en **sortie** la position P(x,y,z) de la "pince" du robot.

Est décrit par le fichier **MotionGenesis.txt**.

### Cinématique inverse
Description statique du robot. 
- Donne en **sortie** la position P(x,y,z) de la "pince" du robot.
- Prend en **entrée** les angles &theta;<sub>1</sub>, &theta;<sub>2</sub> et &theta;<sub>3</sub> des moteurs.
