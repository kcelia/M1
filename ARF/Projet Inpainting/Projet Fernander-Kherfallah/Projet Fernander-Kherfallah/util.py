import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm, trange
from random import shuffle

from util import *

from matplotlib.colors import rgb_to_hsv, hsv_to_rgb

from sklearn.linear_model import Lasso

H = 20
DEAD = -100
IMG_FILE = "img.png"


def build_dic(im,step=H): #X
    """
    """    
    """ construction du dictionnaire : tous les patchs sans pixels morts en parcourant step by step l'image """
    res=[]
    step = step
    for i in range(0,im.shape[0],step):
        for j in range(0,im.shape[1],step):
            if inside(i,j,im) and np.sum(get_patch(i,j,im)[:,:,0]<=DEAD)==0:
                res.append(patch2X(get_patch(i,j,im)))
    return np.array(res).T

def patch2X(patch): #X
    """ transformation d'un patch en vecteur """
    return patch.reshape(-1)

def X2patch(X,h=H):
    """ transformation d'un vecteur en patch image"""
    return X.reshape(2*h+1,2*h+1,3)


def inside(i,j,im,h=H): #X
    """ test si un patch est valide dans l'image """
    return i-h >=0 and j-h >=0 and i+h+1<=im.shape[0] and j+h+1<=im.shape[1]

def get_patch(i,j,im,h=H): #X
    """ retourne un patch centre en i,j """
    print(i,j)
    return im[(i-h):(i+h+1),(j-h):(j+h+1)]

def remove_patch(i,j,im,h=H): #X
    """ Supprime le patch de l'image """
    imn= im.copy()
    imn[(i-h):(i+h+1),(j-h):(j+h+1)]=DEAD
    return imn,get_patch(i,j,im)

def noise_patch(patch,prc=0.2): #X
    """ Supprime des pixels aleatoirement """
    npatch = patch.copy().reshape(-1,3)
    height,width = patch.shape[:2]
    nb =int(prc*height*width)
    npatch[np.random.randint(0,height*width,nb),:]=DEAD
    return npatch.reshape(height,width,3)

def show(im,fig= None): #X
    """ affiche une image ou un patch """
    im = im.copy()
    if len(im.shape)==1 or im.shape[1]==1:
        im = X2patch(im)
    im[im<=DEAD]=-0.5
    if fig is None:
        plt.figure()
        fig = plt.imshow(hsv_to_rgb(im+0.5))
    fig.set_data(hsv_to_rgb(im+0.5))
    plt.draw()
    plt.pause(0.001)
    return fig

def read_img(img): #X
    """ lit un fichier image """
    im = plt.imread(img)
    im = im[:, :, :3]
    if im.max()>200:
        im = im/255.
    return rgb_to_hsv(im)-0.5

def get_patches(img, size, step): #X
    d = []
    n = []
    for i in range(0, len(img) - size, step):
        for j in range(0, len(img) - size, step):
            if DEAD in img[i:i+size, j:j+size, :].flatten():
                n.append(img[i:i+size, j:j+size, :])
            else:
                d.append(img[i:i+size, j:j+size, :])
    return d, n

