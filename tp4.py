"""
observer visuellement l impact de certaines operations
souvent destructives d informations, sur des images
"""
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.misc import ascent
import cv2

def quantifie(img, nb_bits):
    """
    retourne une copie de l'image mais quantifiee sur nb_bits
    si on quantifie sur 4 bits on aura 2^4=16 valeurs possibles
    """
    min_value = 0
    max_value = 2**nb_bits - 1
    quantized_img = np.copy(img)
    quantized_img = np.round(quantized_img * (max_value / 255))#quantification
    quantized_img = np.clip(quantized_img, min_value, max_value)#pour s assurer que la valeur reste dans l intervalle
    quantized_img = quantized_img.astype(np.uint8)#convertit les valeurs quantifiées en entiers non signés
    return quantized_img
def sous_echantillonnage(img, facteur):
    """
    effectue un sous-echantillonage en reduisant les dimensions de l image
    selon le facteur en parametre
    """
    hauteur, largeur = img.shape[:2]
    nouvelle_largeur = largeur // facteur
    nouvelle_hauteur = hauteur // facteur
    img_sous_echantillonee = cv2.resize(img, (nouvelle_largeur, nouvelle_hauteur), interpolation=cv2.INTER_NEAREST)
    #ici interpolation=cv2.INTER_NEAREST on dit que les pixels supprimé on veut qu'ils soient remplacé par des pixels voisins
    #c est une methode assez simple mais une perte d informations peut survenir
    return img_sous_echantillonee
def sur_echantillonnage(img, facteur):
    """
    effectue un sur-echantillonage en augmantant les dimensions de l image
    selon le facteur en parametre
    """
    hauteur, largeur = img.shape[:2]
    nouvelle_largeur = largeur * facteur
    nouvelle_hauteur = hauteur * facteur
    img_sous_echantillonee = cv2.resize(img, (nouvelle_largeur, nouvelle_hauteur), interpolation=cv2.INTER_NEAREST)
    return img_sous_echantillonee
if __name__ == "__main__":
    """
    image_path = "img.jpg"
    image = Image.open(image_path)
    """
    image = ascent()
    """
    min_value = image.min()
    max_value = image.max()
    print("Taille de l'image :", image.shape)
    print("Valeur minimale de l'image :", min_value)
    print("Valeur maximale de l'image :", max_value)
    """
    nb_bits, facteur = 15, 10
    image_quantifiee = quantifie(image, nb_bits)
    image_sur_echantillonee = sur_echantillonnage(image, facteur)
    image_sous_echantillonee = sous_echantillonnage(image, facteur)
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Image originale')
    plt.subplot(2, 2, 2)
    plt.imshow(image_quantifiee, cmap='gray')
    plt.title('Image quantifiée')
    plt.subplot(2, 2, 3)
    plt.imshow(image_sur_echantillonee, cmap='gray')
    plt.title('image sur echantillonée')
    plt.subplot(2, 2, 4)
    plt.imshow(image_sous_echantillonee, cmap='gray')
    plt.title('image sous echantillonée')
    plt.show()


