"""
Prise en main de l'environnement Python/Numpy
"""
import numpy
from matplotlib import pyplot
np = numpy
plt = pyplot

def delta(nb_entree):
    """
    retourne 1 pour nb_entree = 0, 0 sinon
    """
    return nb_entree == 1
def unit(nb_entree):
    """
    retourne 0 pour n < 0 1 sinon
    """
    return nb_entree > 0
if __name__ == "__main__":
    x = range(-20, 21)
    fig, axs = plt.subplots(2, 2)
    # Plot pour δ(n)
    axs[0, 0].stem(x, [delta(n) for n in x])
    axs[0, 0].set_title("δ(n)")
    # Plot pour δ(-n)
    axs[0, 1].stem(x, [delta(-n) for n in x])
    axs[0, 1].set_title("δ(-n)")
    # Plot pour δ(n-5)
    axs[1, 0].stem(x, [delta(n-5) for n in x])
    axs[1, 0].set_title("δ(n-5)")
    # Plot pour δ(n+5)
    axs[1, 1].stem(x, [delta(n+5) for n in x])
    axs[1, 1].set_title("δ(n+5)")
    plt.tight_layout()
    # Affichage de la figure
    plt.show()

