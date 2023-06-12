import numpy as np

def quantifie(img, nb_bits):
    # Calcul de la plage de valeurs de l'image quantifiée
    min_value = 0
    max_value = 2**nb_bits - 1

    # Création d'une copie de l'image
    quantized_img = np.copy(img)

    # Quantification des niveaux de gris de l'image
    quantized_img = np.round(quantized_img * (max_value / 255))

    # Réajustement des valeurs quantifiées dans la plage spécifiée
    quantized_img = np.clip(quantized_img, min_value, max_value)

    # Conversion des valeurs quantifiées en entiers de 8 bits
    quantized_img = quantized_img.astype(np.uint8)

    return quantized_img

