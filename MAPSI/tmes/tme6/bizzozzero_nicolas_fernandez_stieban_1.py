# -*- coding: utf-8 -*-
""" MAPSI, TME6
Auteurs :
- Stieban Fernandez
- Bizzozzero Nicolas

# Test (affectation dans les classes sur critère MV)
1. Le signal a une probabilité plus élevée d'être un z qu'un a tandis que le
   signal est de classe a, donc le signal est mal classé.
2. Les inf proviennent des np.log(0).

# Biais d'évaluation, notion de sur-apprentissage
* On remarque que plus le nombe d'états lors de la discrétisation est grand,
  moins les performances sont bonnes pour l'ensemble de test.
"""

import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt


FILEPATH = "data/TME6_lettres.pkl"

RATIO_APPRENTISSAGE = 0.8


def charger_donnees(file_path, encoding='latin1'):
    with open(file_path, 'rb') as f:
        data = pkl.load(f, encoding=encoding)
    return np.array(data.get('letters')), np.array(data.get('labels'))


def tracer_lettre(lettre, save=False, filename="exlettre.png"):
    a = -lettre * np.pi / 180  # conversion en rad
    coord = np.array([[0, 0]])  # point initial
    for i in range(len(a)):
        x = np.array([[1, 0]])
        rot = np.array([[np.cos(a[i]), -np.sin(a[i])],
                        [np.sin(a[i]), np.cos(a[i])]])
        xr = x.dot(rot)  # application de la rotation
        coord = np.vstack((coord, xr + coord[-1, :]))

    plt.figure()
    plt.plot(coord[:, 0], coord[:, 1])
    plt.show()
    if save:
        plt.savefig(filename)
    

def discretise(X, nombre_etats):
    """ Transforme une série d'angles en série de `etats` differents
    intervalles.
    """
    taille_intervalle = 360. / nombre_etats
    return np.array([np.floor(x / taille_intervalle) for x in X])


def group_by_label(y):
    index = []
    for i in np.unique(y):  # pour toutes les classes
        ind, = np.where(y == i)
        index.append(ind)
    return index
    

def learn_markov_model(Xc, d):
    # Initialisation
    A = np.ones((d, d))
    Pi = np.ones(d)

    # Parcours et increment
    for x in Xc:
        Pi[int(x[0])] += 1
        for i in range(len(x) - 1):
            A[int(x[i])][int(x[i + 1])] += 1

    # Normalisation
    A /= np.maximum(A.sum(1).reshape(d, 1), 1)
    Pi /= Pi.sum()

    return Pi, A


def proba_sequence(s, Pi, A):
    """ Retourne la log-probabilité d'une séquence `s` dans le modèle {Pi, A}.
    """
    return np.log(Pi[int(s[0])]) +\
        np.log(np.array([A[int(s[t-1])][int(s[t])] for t in range(1, s.size)])).sum()


def separe_train_test(y, pc):
    """ Separation app/test.
    pc: ratio de points en apprentissage
    """
    indTrain = []
    indTest = []
    for i in np.unique(y): # pour toutes les classes
        ind, = np.where(y == i)
        n = len(ind)
        indTrain.append(ind[np.random.permutation(n)][:np.floor(pc * n).astype(int)])
        indTest.append(np.setdiff1d(ind, indTrain[-1]))
    return indTrain, indTest


def construire_modele(X, Y, d):
    """ Construit un modèle d'apprentissage.
    X: Données représentant les lettres
    Y: Classe associées aux données
    d: paramètre de discretisation
    """
    Xd = discretise(X, d)      # Discretisation
    index = group_by_label(Y)  # Groupement des signaux par classe

    ## Parcours de toutes les classes et optimisation des modèles
    model = [learn_markov_model(Xd[index[cl]], d) for cl in
                 range(len(np.unique(Y)))]
    return Xd, model

            
def classifier_accuracy(Xd, Y, models, display=True):
    proba = np.array([[proba_sequence(Xd[i], models[cl][0], models[cl][1])\
        for i in range(len(Xd))] for cl in range(len(np.unique(Y)))])
    
    # Evaluation des performances
    # Calcul d'une version numérique des Y
    Ynum = np.zeros(Y.shape)
    for num, char in enumerate(np.unique(Y)):
        Ynum[Y == char] = num

    # Calcul de la classe la plus probable
    pred = proba.argmax(0) # max colonne par colonne

    # Calcul d'un pourcentage de bonne classification
    accuracy = np.where(pred != Ynum, 0., 1.).mean()
    if display:
        print("Performances avec {} états : {}".format(len(models[0][0]),
                                                       accuracy))    
    return accuracy


def matrice_confusion(Xd, models, Y):
    conf = np.zeros((26, 26))
    proba = np.array([[proba_sequence(Xd[i], models[cl][0], models[cl][1])\
                for i in range(len(Xd))] for cl in range(len(np.unique(Y)))])
    Ynum = np.zeros(Y.shape)

    for num, char in enumerate(np.unique(Y)):
        Ynum[Y == char] = num
    pred = proba.argmax(0)
    for i in range(len(Xd)):
        conf[pred[i]][int(Ynum[i])] += 1
    
    # Construction des graphes
    plt.figure()
    plt.imshow(conf, interpolation='nearest')
    plt.colorbar()
    plt.xticks(np.arange(26), np.unique(Y))
    plt.yticks(np.arange(26), np.unique(Y))
    plt.xlabel(u'Vérité terrain')
    plt.ylabel(u'Prédiction')
    plt.savefig("mat_conf_lettres.png")


def generate(Pi, A, length):
    seq = np.zeros(length)
    seq[0] = np.argmax(np.cumsum(Pi) > np.random.rand())
    A_sc = np.cumsum(A, axis=1)
    for i in range(1, length):
        seq[i] = np.argmax(A_sc[int(seq[i-1])] > np.random.rand())
    return seq
    
    

if __name__ == '__main__':
    X, Y = charger_donnees(FILEPATH)
    
    # Discrétisation
    d = 3
    Xd = discretise(X, d)
    np.testing.assert_array_equal(Xd[0],\
           np.array([ 0.,  2.,  2.,  2.,  2.,  2.,  2.,  2.,  1.,
           1.,  1.,  1.,  1., 1.,  2.,  2.,  2.,  2.,  0.,  0.,
           0.,  0.,  0.]))        
    # --------------------------------
           
    # Regrouper les indices des signaux par classe
    # (pour faciliter l'apprentissage)
    index_a = group_by_label(Y)[0]
    np.testing.assert_array_equal(index_a, 
        np.array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10]))
    # --------------------------------
        
    # Apprendre les modèles CM
    lmm_a3 = learn_markov_model(Xd[index_a], d)
    # print(lmm_a3)
    # --------------------------------
    
    # Stocker les modèles dans une liste
    Xd3, models3 = construire_modele(X, Y, d)
    # Test
    test = np.zeros(len(models3))
    for i, (Pi, A) in enumerate(models3):
        test[i] = proba_sequence(Xd[0], Pi, A)
    # print(test)
    
    # Application de la méthode précédente pour tous les signaux 
    # et tous les modèles de lettres
    """
    classifier_accuracy(Xd3, Y, models3)
    Xd20, models20 = construire_modele(X, Y, 20)    
    classifier_accuracy(Xd20, Y, models20)
    """
    # --------------------------------
    
    # Biais d'évaluation, notion de sur-apprentissage
    # exemple d'utilisation
    RATIO_APPRENTISSAGE = 0.8
    itrain, itest = separe_train_test(Y, RATIO_APPRENTISSAGE)
    # Construction du modèle sur la base d'apprentissage
    ia = []
    for i in itrain:
        ia += i.tolist()    
    it = []
    for i in itest:
        it += i.tolist()
    
    # On remarque que plus le nombe d'états lors de la discrétisation
    # est grand, moins les performances sont bonnes pour le testSet
    # --------------------------------
    
    # Après modification de la fonction learn_markov_model
    # On va tester cette fois-ci avec une initialisation à 1
    states = range(2,30)
    train_acc, test_acc = [], []
    
    for di in states:
        Xd_train, models = construire_modele(X[ia], Y[ia], di)
        Xd_test = discretise(X[it], di)
        train_acc.append(classifier_accuracy(Xd_train, Y[ia], models, False))
        test_acc.append(classifier_accuracy(Xd_test, Y[it], models, False))
    plt.plot(states, train_acc)
    plt.plot(states, test_acc)
    
    # Les performances du testSet sont nettement meilleures que précédemment
    # --------------------------------
    
    # Partie optionnelle
    # Evaluation qualitative
    
    Xd_train3, models_train3 = construire_modele(X[ia], Y[ia], d)
    Xd_test3 = discretise(X[it], d)
    Xd_train20, models_train20 = construire_modele(X[ia], Y[ia], 20)
    Xd_test20 = discretise(X[it], 20)
    
    
    matrice_confusion(Xd_test3, models_train3, Y[it])
    matrice_confusion(Xd_test20, models_train20, Y[it])
    
    # --------------------------------
    
    # Modèle génératif
    d = 20
    letter = 0 # indice de la lettre à générer
    
    Xd, models = construire_modele(X, Y, d)
    
    newl = generate(models[letter][0],models[letter][1], 25) # generation d'une séquence d'états
    intervalle = 360./d # pour passer des états => valeur d'angles
    newl_continu = np.array([i*intervalle for i in newl]) # conv int => double
    tracer_lettre(newl_continu)
