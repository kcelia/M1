# -*- coding: utf-8 -*-
"""
    TME 6
"""

import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt

def database( filename ):
    """
        charge les donnees
    """
    with open(filename, 'rb') as f:
        data = pkl.load(f, encoding='latin1')
        X = np.array(data.get('letters')) # récupération des données sur les lettres
        Y = np.array(data.get('labels')) # récupération des étiquettes associées
    return X, Y

# affichage d'une lettre
def tracerLettre(let):
    a = -let*np.pi/180; # conversion en rad
    coord = np.array([[0, 0]]); # point initial
    for i in range(len(a)):
        x = np.array([[1, 0]]);
        rot = np.array([[np.cos(a[i]), -np.sin(a[i])],[ np.sin(a[i]),np.cos(a[i])]])
        xr = x.dot(rot) # application de la rotation
        coord = np.vstack((coord,xr+coord[-1,:]))
    plt.figure()
    plt.plot(coord[:,0],coord[:,1])
    plt.savefig("exlettre.png")
    return

def discretise( X, d ):
    """
        prend en entree la base des signaux et retourne une base des signaux discretises
    """
    intervalle = 360. / d
    X_new = np.ndarray(len(X), dtype=np.object)
    for k, i in enumerate(X):
        L = np.zeros( len(i) )
        for j in range( len(i) ):
            L[j] = np.floor( i[j] / intervalle )
        X_new[k] = L
    return X_new


def groupByLabel( y ):
    """
        Regroupe les indices des signaux par classe
        pour faciliter l'apprentissage
    """
    index = []
    for i in np.unique(y): # pour toutes les classes
        ind, = np.where(y==i)
        index.append(ind)
        
    return index


def learnMarkovModel( Xc, d ):
    """
        Xc : base de signaux discretises correspondant a la classe C
        d : nombre d'etats
        retourne un tuple contenant Pi et A
    """
    # initialisation
    A = np.zeros( (d, d) )
    Pi = np.zeros( d )
    
    for i in Xc:
        a = int(i[0])
        Pi[a] += 1
        for j in range( len(i) - 1 ):
            t = int(i[j])
            t_1 = int(i[j+1])
            A[t][t_1] += 1
            
    # normalisation
    A = A/np.maximum(A.sum(1).reshape(d,1),1)
    Pi = Pi/Pi.sum()
    
    return Pi, A

def learnMarkovModel_bis( Xc, d ):
    """
        Xc : base de signaux discretises correspondant a la classe C
        d : nombre d'etats
        retourne un tuple contenant Pi et A
    """
    # initialisation avec des matrices np.ones pour palier
    # au probleme de 0
    A = np.ones( (d, d) )
    Pi = np.ones( d )
    
    for i in Xc:
        a = int(i[0])
        Pi[a] += 1
        for j in range( len(i) - 1 ):
            t = int(i[j])
            t_1 = int(i[j+1])
            A[t][t_1] += 1
            
    # normalisation
    A = A/np.maximum(A.sum(1).reshape(d,1),1)
    Pi = Pi/Pi.sum()
    
    return Pi, A

def buildModel( X, Y, d ):
    """
        Construit un modele pour l'apprentissage des CM
        X : donnees sur les lettres
        Y : etiquettes associees
        d : nombre d'etats
    """
    Xd = discretise(X,d)  # application de la discrétisation
    index = groupByLabel(Y)  # groupement des signaux par classe
    models = []
    for cl in range(len(np.unique(Y))): # parcours de toutes les classes et optimisation des modèles
        models.append(learnMarkovModel(Xd[index[cl]], d))
    
    return Xd, models

def buildModel_bis( X, Y, d ):
    """
        Construit un modele pour l'apprentissage des CM
        X : donnees sur les lettres
        Y : etiquettes associees
        d : nombre d'etats
    """
    Xd = discretise(X,d)  # application de la discrétisation
    index = groupByLabel(Y)  # groupement des signaux par classe
    models = []
    for cl in range(len(np.unique(Y))): # parcours de toutes les classes et optimisation des modèles
        models.append(learnMarkovModel_bis(Xd[index[cl]], d))
    
    return Xd, models


def probaSequence( s, Pi, A ):
    """
        retourne la log-probabilite d'une sequence s dans le 
        modele M = {Pi, A}
    """  
    init = int(s[0])
    proba = np.log(Pi[init])
    for i in range( 1, s.size ):       
        t = int(s[i-1])       
        t_1 = int(s[i]) 
        proba += np.log(A[t][t_1])           
    
    return proba

def classification( Xd, Y, models ):
    
    proba = np.array([[probaSequence(Xd[i], models[cl][0], models[cl][1]) for i in range(len(Xd))]for cl in range(len(np.unique(Y)))])

    # Calcul d'une version numerique des Y
    Ynum = np.zeros(Y.shape)
    for num,char in enumerate(np.unique(Y)):
        Ynum[Y==char] = num
    
    # Calcul de la classe la plus probable
    pred = proba.argmax(0) # max colonne par colonne

    # Calcul d'un pourcentage de bonne classification
    perf = np.where(pred != Ynum, 0.,1.).mean()
    
    return perf

# separation app/test, pc=ratio de points en apprentissage
def separeTrainTest(y, pc):
    indTrain = []
    indTest = []
    for i in np.unique(y): # pour toutes les classes
        ind, = np.where(y==i)
        n = len(ind)
        indTrain.append(ind[np.random.permutation(n)][:int(np.floor(pc*n))])
        indTest.append(np.setdiff1d(ind, indTrain[-1]))
    return indTrain, indTest

# --------------------------------------------------------------------------- #
# TESTS 

# Chargement des donnees a partir d'un fichier
filename = 'lettres1.pkl'
X, Y = database(filename)

""" 1.1. Discretisation """
X_new = discretise(X, 3)
print("discretise(X, 3)[0] :")
print(X_new[0])
print()
# 1.2. Regroupage des indices des signaux par classe 
#print(groupByLabel(Y))

# 1.3. Apprendre les modeles CM
y = groupByLabel(Y)[0]
print("learnMarkovModel(Xd[y], 3) :")
print(learnMarkovModel( X_new[y], 3 ))
print()
# 1.4. Stocker les modeles dans une liste
d = 3
Xd, models = buildModel(X, Y, d)

# 2.1. Log-probabilite d'une sequence dans un modele
Pi, A = learnMarkovModel(Xd, d)
test = np.zeros( len(models) )
for i, (Pi, A) in enumerate( models ):
    test[i] = probaSequence(Xd[0], Pi, A)
print("log-probabilite du premier signal avec d = 3 etats :")
print(test)
print()
""" 
Reponses questions :
* log-proba('a') = -13.5 dans classe 'a'
* log-proba('z') = -12.5 dans classe 'a'
* log-proba('a') < log-proba('z') dans classe 'a'
--> donc signal mal classe
* -inf vient de log(0) -> en effet log(0) tend vers moins l'infini
"""
# 2.3. Evaluation des performances
Xd3, models3 = buildModel(X, Y, 3)
perf3 = classification(Xd3, Y, models3)
print("Performance avec 3 etats : " + str(perf3))
print()
Xd20, models20 = buildModel(X, Y, 20)
perf20 = classification(Xd20, Y, models20)
print("Performance avec 20 etats : " + str(perf20))
print()
# Biais d'evaluation, notion de sur-apprentissage
itrain,itest = separeTrainTest(Y,0.8)

# re-fusionner tous les indices d'apprentissage et de test
ia = []
for i in itrain:
    ia += i.tolist()    
it = []
for i in itest:
    it += i.tolist()

etats = range( 2,30 )   # nombre d'etats pour lesquels on va evaluer les modeles
train = []  # liste pour l'apprentissage sans biais
test = []   # liste pour l'apprentissage avec biais

# pour chaque methode d'apprentissage, on calcule ses performances 
# selon le nombre d'etats (discretisation)
for di in etats:
    Xd_train, models = buildModel(X[ia], Y[ia], di) # construire un modele pour l'evaluer sans biais
    Xd_test = discretise(X[it], di)
    train.append(classification(Xd_train, Y[ia], models))
    test.append(classification(Xd_test, Y[it], models))
# Afficher les courbes de performances
plt.plot(etats, train, 'b-', label='sans biais')
plt.plot(etats, test, 'r-', label='avec biais')
plt.legend(loc='lower left')
plt.title("Pourcentage de bonne classifcation en fonction du nombre d'etats - np.zeros")
plt.show()

# performances avec initialisation avec np.ones
train_bis = []
test_bis = []
for di_bis in etats:
    Xd_train_bis, models_bis = buildModel_bis(X[ia], Y[ia], di_bis) # construire un modele pour l'evaluer sans biais
    Xd_test_bis = discretise(X[it], di_bis)
    train_bis.append(classification(Xd_train_bis, Y[ia], models_bis))
    test_bis.append(classification(Xd_test_bis, Y[it], models_bis))
plt.plot(etats, train_bis, 'b-', label='sans biais')
plt.plot(etats, test_bis, 'r-', label='avec biais')
plt.legend(loc='lower left')
plt.title("Pourcentage de bonne classifcation en fonction du nombre d'etats - np.ones")
plt.show()