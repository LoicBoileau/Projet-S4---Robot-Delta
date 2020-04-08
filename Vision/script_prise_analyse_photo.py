import cv2
import numpy as np
import csv
from numpy import zeros


def lecture_image(Nom_Image_Enregistree):
    image = cv2.imread(Nom_Image_Enregistree)
    return image


def convertir_image_tons_gris(image):
    image_grise = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return image_grise


def prise_photo(frame, Compteur_Image):
    Nom_Image_Enregistree = 'Image{}.png'.format(Compteur_Image)
    cv2.imwrite(Nom_Image_Enregistree, frame)
    print("{} a ete ecrit!".format(Nom_Image_Enregistree))
    return Nom_Image_Enregistree


def ecriture_csv(coordonnee_bleu, coordonnee_noir, Compteur_Image):
    nom_du_fichier = 'Position{}.csv'.format(Compteur_Image)

    with open(nom_du_fichier, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        somme_coordonnee = len(coordonnee_bleu) + len(coordonnee_noir)
        f.write('{0}-{1}-{2}\n'.format(len(coordonnee_bleu),len(coordonnee_noir),somme_coordonnee))

        for z in coordonnee_bleu:
            writer.writerow(z)
        f.write('\n')

        for z in coordonnee_noir:
            writer.writerow(z)


def nombre_contours(image_grise, limite_inferieure, limite_superieure):
    masque = cv2.inRange(image_grise, limite_inferieure, limite_superieure)
    #cv2.imshow('masque', masque)

    ret, thresh = cv2.threshold(masque, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours


def calcul_coordonnee(image, contours, Couleur_Choisie):
    coordonnee = zeros([len(contours), 3])
    i = 0

    for c in contours:
        j = 0
        M = cv2.moments(c)

        if M["m00"] != 0:
            cX = round(M["m10"] / M["m00"], 3)
            cY = round(M["m01"] / M["m00"], 3)
        else:
            cX, cY = 0, 0

        cZ = 0
        cv2.circle(image, (int(cX), int(cY)), 5, (255, 255, 255), -1)
        cv2.putText(image, "centroid {}".format(Couleur_Choisie), (int(cX) - 50, int(cY) - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        coordonnee[i][j] = cX
        j = j + 1
        coordonnee[i][j] = cY
        j = j + 1
        coordonnee[i][j] = cZ
        i = i + 1
        cv2.imshow('image2', image)

    return coordonnee

camera = cv2.VideoCapture(0)  # La webcam fait une capture vidéo
Prendre_Photo = False
Compteur_Image = 0


limite_inferieure_bleu = np.array([50, 120, 50])#90,60,0
limite_superieure_bleu = np.array([121, 255, 200])#121,255,200
limite_inferieure_noir = np.array([0, 0, 0])#0,0,0
limite_superieure_noir = np.array([200, 200, 80])#180,180,65



while (1):
    if camera.isOpened() == True:
        _, frame = camera.read()
        cv2.imshow('frame', frame)

        '''
        Nom_Image_Enregistree = prise_photo(frame, Compteur_Image)
        image = lecture_image(Nom_Image_Enregistree)
        image_grise = convertir_image_tons_gris(image)
        masque_bleu = cv2.inRange(image_grise, limite_inferieure_bleu, limite_superieure_bleu)
        cv2.imshow('masque_bleu', masque_bleu)
        masque_noir = cv2.inRange(image_grise, limite_inferieure_noir, limite_superieure_noir)
        cv2.imshow('masque_noir', masque_noir)
        '''

        if Prendre_Photo == True:
            Compteur_Image += 1
            Prendre_Photo = False
            Nom_Image_Enregistree = prise_photo(frame, Compteur_Image)

            image = lecture_image(Nom_Image_Enregistree)
            image_grise = convertir_image_tons_gris(image)


            contours_bleu = nombre_contours(image_grise, limite_inferieure_bleu, limite_superieure_bleu)
            contours_noir = nombre_contours(image_grise, limite_inferieure_noir, limite_superieure_noir)

            coordonnee_bleu = calcul_coordonnee(image, contours_bleu, 'bleu')
            coordonnee_noir = calcul_coordonnee(image, contours_noir, 'noir')
            print('Nombre de bloc(s) bleu(s): ',len(coordonnee_bleu))
            print('Nombre de bloc(s) noir(s): ',len(coordonnee_noir))
            print('Somme de bloc(s): ', len(coordonnee_bleu) + len(coordonnee_noir))
            ecriture_csv(coordonnee_bleu, coordonnee_noir, Compteur_Image)

    else:
        print("La camera ne c'est pas ouverte correctement")
        break

    k = cv2.waitKey(1)

    if k % 256 == 27:
        print("Escape a ete appuye")
        break
    elif k % 256 == 32:
        Prendre_Photo = True



camera.release()
cv2.destroyAllWindows()
