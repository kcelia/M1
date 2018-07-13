# -*- coding: utf-8 -*-
"""
    TME 7
"""


import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt
# truc pour un affichage plus convivial des matrices numpy
np.set_printoptions(precision=2, linewidth=320)
plt.close('all')

def database( filename ):
    """
        charge les donnees
    """
    with open(filename, 'rb') as f:
        data = pkl.load(f, encoding='latin1')
        X = np.array(data.get('letters')) # récupération des données sur les lettres
        Y = np.array(data.get('labels')) # récupération des étiquettes associées
    return X, Y
    
filename = 'TME6_lettres.pkl'
X, Y = database(filename)


nCl = 26

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
    
y = groupByLabel(Y)

# Hypothese Gauche-Droite
def initGD( X, N ):
    """
        prend un ensemble de sequences d'observations et
        qui retourne l'ensemble des sequences d'etats
    """
    seq = np.ndarray(len(X), dtype=np.object)
    for i in range( len(X) ):
        a = np.floor(np.linspace(0,N-.00000001,len(X[i])))
        seq[i] = a
    return seq

    
#Xd = discretise(X, 10)
#seq = initGD(Xd, 4)
#print(seq[0])



# Apprentissage
def learnHMM(allx, allq, N, K, initTo0=False):
    """
        apprend un modele a partir d'un ensemble de couples
        allx : sequence d'observations
        allq : sequence d'etats
    """
    if initTo0:
        A = np.zeros((N,N))
        B = np.zeros((N,K))
        Pi = np.zeros(N)
    else:
        eps = 1e-8
        A = np.ones((N,N))*eps
        B = np.ones((N,K))*eps
        Pi = np.ones(N)*eps

    for i in allq:
        a = int(i[0])
        Pi[a] += 1
        for j in range( len(i) - 1 ):
            t = int(i[j])
            t_1 = int(i[j+1])
            A[t][t_1] += 1
    
    for k in range( len(allq) ):
        for l in range( len(allq[k]) - 1 ):
            b = int(allq[k][l])
            c = int(allx[k][l])
            B[b][c] += 1
        d = int(allq[k][l+1])
        e = int(allx[k][l+1])
        B[d][e] += 1
    """
    for q, x in zip(allq, allx):
        for k, l in zip(q, x):
            b = int(k)
            c = int(l)
            B[b][c] += 1
    """
    # normalisation
    A = A/np.maximum(A.sum(1).reshape(N,1),1)
    B = B/np.maximum(B.sum(1).reshape(N,1),1)
    Pi = Pi/Pi.sum()

    return Pi, A, B

K = 10 # discrétisation (=10 observations possibles)
N = 5  # 5 états possibles (de 0 à 4 en python) 
# Xd = angles observés discrétisés
Xd = discretise(X, K)
q = initGD(Xd, N)
Pi, A, B = learnHMM(Xd[Y=='a'],q[Y=='a'],N,K)
#print(Pi)
#print(A)
#print(B)

# Viterbi (en log)
def viterbi( x, Pi, A, B ):
    # declaration
    P = len( Pi )
    Q = len( x )
    delta = np.zeros((P,Q))
    psi = np.zeros((P, Q))
    
    # initialisation
    #for i in range( N ):
        #delta[i][0] = np.log(Pi[i]) + np.log(B[i][0])
        #psi[i][0] = (-1)
    delta[:, 0] = np.log(Pi) + np.log(B[:, int(x[0])])
    psi[:, 0] =-1
    
    # recursion
    for j in range( 1, Q ):
        for i in range( P ):
            t = delta[:, int(j-1)] + np.log(A[:, i])
            delta[i][j] = max(t) + np.log(B[i, int(x[j])])
            psi[i][j] = np.argmax(t)
    
    # terminaison
    p_est = max(delta[:, -1])
    
    # chemin
    s_est = [0] * Q
    s_est[Q-1] = np.argmax(delta[:, int(j)])
    for j in range( Q-2, 1, -1 ):
        s_est[j] = psi[:, int(j+1)][int(s_est[j+1])]
    
    #print(delta)
    #print(psi)
    
    return s_est, p_est


#s_est, p_est =  viterbi(Xd[0], Pi, A, B)
#print(s_est)

#lettres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
L = np.arange(97, 97+26)
lettres = [chr(i) for i in L] # alphabet de 'a' a 'z'

def baum_welch( X, Y, N, K, lettres ):
    """
        X : base de donnees
        N : nombre d'etats possibles
        K : nombre d'observations possibles (discretisation)
    """
    
    # initialisation des etats caches arbitraire
    allx = discretise(X, K)
    allq = initGD(allx, N)
    models = []
    for i in range( len(lettres) ):
        k = lettres[i]
        Pi, A, B = learnHMM(allx[Y==k], allq[Y==k], N, K)
        models.append((Pi, A, B))

    c = 1
    a = 0
    p = 0
    L = []
    cpt = 0
    while ( c > 1e-4 ):
        print("cpt = " + str(cpt))        
        #for i in range( len (models) ):
        for i in range(2):
            Pi, A, B = models[i]         
            #for x in allx:
            for x in range(2):
                s_est, p_est = viterbi(allx[x], Pi, A, B)
                #for j in range( len(x) ):
                for j in range(2):
                    obs = allx[x][j]
                    #print("obs = " + str(obs))
                    etat = s_est[j]
                    #print("etat = " + str(etat))
                    print("B = " + str(B[etat][obs]))
                    a += np.log(B[etat][obs])
                    print("a = " + str(a))
        p += a
        print("p = " + str(p))
        L.append(p)        
        if cpt != 0:
            c = (L[cpt-1] - p)/L[cpt-1]
        p = 0
        cpt =+ 1
        
    x = range( cpt + 1 )
    plt.plot(x, L)
    plt.show()

baum_welch(X, Y, N, K, lettres)    