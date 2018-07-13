import numpy as np

import matplotlib.pyplot as plt

from random import shuffle

from matplotlib.colors import rgb_to_hsv, hsv_to_rgb

H = 20
DEAD = -100

def load_usps(fn):
    with open(fn,"r") as f:
        f.readline()
        data = [[float(x) for x in l.split()] for l in f if len(l.split())>2]
    tmp = np.array(data)
    n = tmp.shape[0]
    tmp[:, 1:] = (tmp[:, 1:] - tmp[:, 1:].min(axis=1).reshape(n, 1)) / tmp[:, 1:].max(axis=1).reshape(n, 1)
    return tmp[:, 1:], tmp[:, 0].astype(int)

def show_usps(data):
    plt.imshow(data.reshape((16,16)),interpolation="nearest",cmap="gray")

def filter_classes(X, Y, y1, y2, balance=True):
    #y1 et y2 peuvent etre des listes
    y1 = list(np.array([y1]).flatten())
    y2 = list(np.array([y2]).flatten())
    yg = y1 + y2
    X, Y = list(zip(*filter(lambda c: c[1] in yg, zip(X, Y))))
    Y = list(map(lambda y: int(y in y1), Y)) #binarise the classes
    if balance:
        data = list(zip(X, Y))
        positives = list(filter(lambda c: c[1], data))
        negatives = list(filter(lambda c: not c[1], data))
        shuffle(positives)
        shuffle(negatives)
        positives = positives[:min(len(positives), len(negatives))]
        negatives = negatives[:len(positives)]
        data = positives + negatives
        shuffle(data)
        X, Y = list(zip(*data))
    return np.array(X), np.array(Y)


def read_img(img):
    """Chargement de l'image en hsv.
    
    :param img: chemin de l'image a charger
    
    :type img: str
    
    :return: l'image en hsv sous forme de matrice 3D
    :rtype: np.array (3D)
    """
    im = plt.imread(img)[:, :, :3]
    im = im / 255. if im.max() >= 200 else im
    return rgb_to_hsv(im) - .5


def get_patches(img, size, step):
    """Construit les listes des patchs de l'image, 
    patchs contenant ou non des pixels morts.
    
    :param img: image dont on veut extraire les patchs
    :param size: taille du patch
    :param step: pas utilisé pour extraire les patchs
    
    :return: les listes des patchs morts et non morts
    :rtype: tuple(list(np.array), list(np.array))
    """
    d, n = [], []
    for i in range(0, len(img) - size, step):
        for j in range(0, len(img) - size, step):
            if DEAD in img[i:i + size, j:j + size, :].flatten():
                n.append(img[i:i + size, j:j + size, :])
            else:
                d.append(img[i:i + size, j:j + size, :])
    return d, n

def get_patch(i,j,im,h=H): #TODO: comment
    """Retourne un patch centre en i, j de taille h."""
    return im[(i - h):(i + h + 1), (j - h):(j + h + 1)]

def noise_patch(patch, prc=.2):
    """Met a mort certain pixels de maniere aleatoire
    en fonction du pourcentage de perte choisi.
    
    :param patch: patch dont on souhaite supprimer des pixels
    :param prc: pourcentage de perte des pixels
    
    :return: le meme patch avec des pertes
    :rtype: np.array (2D)
    """
    npatch = patch.copy().reshape(-1, 3)
    height, width = patch.shape[:2]
    nb = int(prc * height * width)
    npatch[np.random.randint(0, height * width, nb), :] = DEAD
    return npatch.reshape(height, width, 3)


def X2patch(L, h=H):
    """Transrome un patch applati en patch de la bonne dimension.
    
    :param L: liste de valeurs a reconvertir en patch
    :param h: hauteur du patch
    
    :type L: np.array
    :type h: int
    
    :return: le patch en 3D
    :rtype: np.array (3D)
    """
    return L.reshape(2 * h + 1, 2 * h + 1, 3)

def show(im):
    """Affiche une image depuis l'espace hsv (corrompue ou non).
    
    :param im: image a afficher
    """
    im = im.copy()
    if len(im.shape)==1 or im.shape[1]==1:
        im = X2patch(im)
    im[im <= DEAD] = -.5
    plt.figure()
    fig = plt.imshow(hsv_to_rgb(im + .5))
    fig.set_data(hsv_to_rgb(im + .5))
    plt.draw()
    return fig



def remove_patch(i, j, im, h=H): #TODO: comment
    """Supprime un patch de taille h de l'image centré en i, j.
    
    :param i:..."""
    imn = im.copy()
    imn[(i - h):(i + h + 1), (j - h):(j + h + 1)] = DEAD
    return imn, get_patch(i,j,im)


def affichageHeuristique(mapy):
    plt.imshow(mapy, cmap = "gray")
    for i in range(len(mapy)):
        for j in range(len(mapy)):
            plt.text(j,i,mapy[i][j])






NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
turn_right = {NORTH: E, E: S, S: W, W: NORTH} # old -> new direction

def spiral2(width, height):
    x, y = width // 2, height // 2 # start near the center
    dx, dy = NORTH # initial direction
    matrix = [[None] * width for _ in range(height)]
    count = width *  height
    while True:
        count -= 1
        matrix[y][x] = count # visit
        # try to turn right
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go
            
def sp(m, n, start = 0):
    if n == 0:
        yield ()
    else:
        yield tuple(range(start, m + start))
        for row in zip(*list(sp(n - 1, m, m + start))[::-1]):
            yield row
            
def spiral(w, h):
    return np.array(list(sp(w, h)))
            
            
def hautDroite(img,x,y):
    return img[x-1, y-1, 0] != DEAD

def hautGauche(img,x,y):
    return img[x-1, y+1, 0] != DEAD

def basDroite(img,x,y):
    return img[x+1, y+1, 0] != DEAD

def basGauche(img,x,y):
    return img[x+1, y-1, 0] != DEAD


