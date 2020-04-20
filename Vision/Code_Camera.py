import cv2
import numpy as np
import csv
from numpy import zeros

#La caméra prend une une photo et l'enregistre grâce à un compteur qui incrémente alors les images ne se font pas écraser
def prise_photo(cadre, Compteur_Image):
    Nom_Image_Enregistree = 'Image{}.png'.format(Compteur_Image)
    cv2.imwrite(Nom_Image_Enregistree, cadre)
    print("{} La photo a été prise!".format(Nom_Image_Enregistree))#Indique que la photo a été prise
    return Nom_Image_Enregistree


#Lecture de l'image (doit être en format png et dans le même fichier que le code)
def lecture_image(Nom_Image_Enregistree):
    image = cv2.imread(Nom_Image_Enregistree)
    return image

#Converti l'image de couleur en HSV
def convertir_image_HSV(image):
    image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return image_HSV

#Crée un masque qui isole juste une couleur selon les limites données
def nombre_contours(image_grise, limite_inferieure, limite_superieure):
    masque = cv2.inRange(image_grise, limite_inferieure, limite_superieure)

    retour, seuil = cv2.threshold(masque, 127, 255, 0)
    #Trouve les contours des carrés dans le masque
    image2,contours, hierarchy = cv2.findContours(seuil, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

#Calcul les points milieux des contours d'une couleur choisie
def calcul_coordonnee(image, contours, Couleur_Choisie, Compteur_Image):
    coordonnee = zeros([len(contours), 3]) #Création d'un tableau vide
    i = 0

    #Pour chaque point qui forme le contour on entre dans la boucle
    for c in contours:
        j = 0
        #La fonction moments calcul les moments d'inertie selon les points qui forment les contours des carrés et
        #forme une matrice selon les axes analysés
        moment = cv2.moments(c)

        if moment["m00"] != 0: #Le if sert à éviter la division par 0
            cX = round(moment["m10"] / moment["m00"], 3)
            cY = round(moment["m01"] / moment["m00"], 3)
        else:
            cX, cY = 0, 0

        cZ = -0.2
        #On met un point blanc sur le carré pour mieux identifier le centre de masse ainsi que ça
        #couleur pour vérifier qu'il ne s'est pas trompé
        cv2.circle(image, (int(cX), int(cY)), 5, (255, 255, 255), -1)
        cv2.putText(image, "Centre de masse {}".format(Couleur_Choisie), (int(cX) - 88, int(cY) - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        #On associe les coordonnées X, Y et Z dans le tableau crée précédemment
        coordonnee[i][j] = cX
        j = j + 1
        coordonnee[i][j] = cY
        j = j + 1
        coordonnee[i][j] = cZ
        i = i + 1
        #On montre l'image avec les modifications dessus et on l'enregistre
        cv2.imshow('Photo avec les points milieu des carres', image)
        Nom_Image_Enregistree_2 = 'Image_Centre_Masse{}.png'.format(Compteur_Image)
        cv2.imwrite(Nom_Image_Enregistree_2, image)
    #On retourne un tableau de coordonnée
    return coordonnee


#Écriture des valeurs dans un fichier CSV
def ecriture_csv(coordonnee_bleu, coordonnee_noir, Compteur_Image):
    #Comme avec la prise de photo le même compteur est utilisé pour incrémenter le nom du fichier dans le but d'éviter
    #qu'il se fasse écraser
    nom_du_fichier = 'Position{}.csv'.format(Compteur_Image)

    #On crée un nouveau fichier et on écrit les coordonnees. La première ligne représente le nombre de carrés bleus,
    #ensuite le nombre de carrés noirs et finalmeent la somme des carré présents dans l'image

    #Par la suite, on écrit une ligne à la fois les coordonnées bleus séparés avec une tabulation entre ses coordonnées,
    #ensuite on saute la ligne pour écrire la prochaine coordonnée bleu. Pour séparé les coordonnées bleus et noirs
    #ensemble on saute une ligne supplémentaire pour laisser une ligne vide.
    with open(nom_du_fichier, 'w') as f:
        ecriture = csv.writer(f, delimiter='\t')
        somme_coordonnee = len(coordonnee_bleu) + len(coordonnee_noir)
        f.write('{0}-{1}-{2}\n'.format(len(coordonnee_bleu),len(coordonnee_noir),somme_coordonnee))

        for z in coordonnee_bleu:
            ecriture.writerow(z)
        f.write('\n')

        for z in coordonnee_noir:
            ecriture.writerow(z)
    return
########################################################################################################################

#La webcam fait une capture vidéo. Le nombre 0 représente la première caméra de l'ordinateur.
camera = cv2.VideoCapture(0)
#La variable qui décide de prendre une photo est initialisé à zéro
Prendre_Photo = False
#Le compteur qui dicte le nom du fichier le est initialisé à zéro
Compteur_Image = 0

#Les limites des couleurs que l'on souhaite désiré en code RGB

limite_inferieure_bleu = np.array([50, 120, 50])
limite_superieure_bleu = np.array([110, 255, 195])
limite_inferieure_noir = np.array([0, 0, 0])
limite_superieure_noir = np.array([180, 180, 60])


while (1):
    #Si la camera c'est ouverte correctement, on montre la vue de la camera et on a accès au fonction
    if camera.isOpened() == True:
        #On montre la vue de la caméra
        _, cadre = camera.read()
        cv2.imshow('Vue Camera', cadre)

        #On enlève les commentaires pour mieux déverminer les couleurs avec le code RGB, en effet on va voir les masques
        #donc on pourra voir si on doit augmenter ou descendre les limites
        '''
        Nom_Image_Enregistree = prise_photo(cadre, Compteur_Image)
        image = lecture_image(Nom_Image_Enregistree)
        image_HSV = convertir_image_HSV(image)
        cv2.imshow('image_HSV', image_HSV)
        masque_bleu = cv2.inRange(image_HSV, limite_inferieure_bleu, limite_superieure_bleu)
        cv2.imshow('masque_bleu', masque_bleu)
        masque_noir = cv2.inRange(image_HSV, limite_inferieure_noir, limite_superieure_noir)
        cv2.imshow('masque_noir', masque_noir)
        '''


        #Si la variable est a vrai on a accès au fonction et on les fait dans l'ordre sinon on boucle
        if Prendre_Photo == True:
            #Si une photo se fait prendre
            Compteur_Image += 1 #Pour permettre de prendre plusieurs photos et de ne pas écraser les fichiers
            Prendre_Photo = False #On remet la varialbe à faux pour ne pas prendre plusieurs photos

            Nom_Image_Enregistree = prise_photo(cadre, Compteur_Image)#Appel la fonction qui prend la photo

            image = lecture_image(Nom_Image_Enregistree)#Appel la fonction qui prend lit l'image
            image_HSV = convertir_image_HSV(image)#Appel la fonction qui convertie l'image en HSV

            #Trouve les contours bleus
            contours_bleu = nombre_contours(image_HSV, limite_inferieure_bleu, limite_superieure_bleu)
            #Trouve les contours noirs
            contours_noir = nombre_contours(image_HSV, limite_inferieure_noir, limite_superieure_noir)

            #Trouve les centres de masse bleus
            coordonnee_bleu = calcul_coordonnee(image, contours_bleu, 'bleu', Compteur_Image)
            #Trouve les centres de masse noirs
            coordonnee_noir = calcul_coordonnee(image, contours_noir, 'noir', Compteur_Image)

            #On affiche les résultats
            print('Nombre de bloc(s) bleu(s): ',len(coordonnee_bleu))
            print('Nombre de bloc(s) noir(s): ',len(coordonnee_noir))
            print('Somme de bloc(s): ', len(coordonnee_bleu) + len(coordonnee_noir))

            #On écrit dans un fichier CSV les coordonnées bleus et noirs trouvées
            ecriture_csv(coordonnee_bleu, coordonnee_noir, Compteur_Image)

    #Si la caméra a un problème de connexion ou ne s'ouvre pas
    else:
        print("La camera ne s'est pas ouverte correctement. Fermeture du programme")
        break

    #Une touche du clavier est appuyé et enregistré dans la variable Touche_Clavier
    Touche_Clavier = cv2.waitKey(1)

    #Touche clavier échap est appuyé et on sort du programme
    if Touche_Clavier % 256 == 27:
        print("Fermeture du programme avec l'appui de la touche echap")
        break

    #Touche clavier espace est appuyé et on met la variable qui prend une photo à vrai
    elif Touche_Clavier % 256 == 32:
        Prendre_Photo = True

#Ferme la caméra et les fenêtres utilisées
camera.release()
cv2.destroyAllWindows()
