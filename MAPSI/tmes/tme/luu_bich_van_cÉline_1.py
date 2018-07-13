# -*- coding: utf-8 -*-
"""
    TME 9
"""

import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import pickle as pkl

# Estimation de pi par Monte Carlo

def tirage( m ):
    """
        float -> float x float
        m : nombre reel
        Retourne un point tire aleatoirement selon la loi uniforme 
        dans le carre [-m, m] x [-m, m]
    """
    x = npr.uniform(-m, m)
    y = npr.uniform(-m, m)
    return (x, y)
    
def monteCarlo( N ):
    """
        int -> float x float np.array x float np.array
        N : nombre de tirages
        Retourne un triplet compose d'une estimation de pi par Monte Carlo
        ainsi que du tableau des N abscisses et du tableau des N ordonnees qui
        ont permis d'obtenir cette estimation
    """
    x = []
    y = []
    cpt = 0 # compteur du nombre de points dans le quart de disque de rayon 1
    for i in range ( N ):
        a, b = tirage( 1 )
        x.append(a)
        y.append(b)
        if (a*a + b*b) <= 1:
            cpt += 1
    x = np.array(x, float) 
    y = np.array(y, float)
    return (4.*cpt)/N, x, y

def dessin():
    plt.figure()

    # trace le carré
    plt.plot([-1, -1, 1, 1], [-1, 1, 1, -1], '-')

    # trace le cercle
    x = np.linspace(-1, 1, 100)
    y = np.sqrt(1- x*x)
    plt.plot(x, y, 'b')
    plt.plot(x, -y, 'b')

    # estimation par Monte Carlo
    pi, x, y = monteCarlo(int(1e4))

    # trace les points dans le cercle et hors du cercle
    dist = x*x + y*y
    plt.plot(x[dist <=1], y[dist <=1], "go")
    plt.plot(x[dist>1], y[dist>1], "ro")
    plt.show()

#dessin()


# Decodage par la methode de Metropolis-Hastings

def loadData( filename_pkl, filename_txt ):
    """
        charge les donnees
    """
    with open(filename_pkl, 'rb') as f:
        (count, mu, A) = pkl.load(f) #, encoding='latin1')
    secret = (open(filename_txt, "r")).read()[0:-1] # -1 pour supprimer le saut de ligne
    return count, mu, A, secret

count, mu, A, secret = loadData("countWar.pkl", "secret2.txt")

def swapF( tau_t ):
    """
        (char, char)dict -> (char, char)dict
        tau = fonction de decodage
        Retourne une nouvelle fonction de decodage tau
        - tau(c) = tau_t(c) pour tout c different de c1 et c different de c2
        - tau(c1) = tau_t(c2)
        - tau(c2) = tau_t(c1)
    """
    np.random.seed()
    tau = dict(tau_t)
    keys = tau_t.keys()
    # on choisit les 2 lettres a echanger
    n1 = npr.randint(0, len(keys))
    n2 = npr.randint(0, len(keys))
    # si c1 == c2 - pas obligatoire
    while( n2 == n1 ):
        n2 = npr.randint(0, len(keys))
    c1 = keys[n1]
    c2 = keys[n2]
    #print("c1 = " + c1)
    #print("c2 = " + c2)
    tmp = tau[c1]
    tau[c1] = tau_t[c2]
    tau[c2] = tmp
    return tau
    
#tau = {'a' : 'b', 'b' : 'c', 'c' : 'a', 'd' : 'd' }
#t = swapF(tau)
#print(t)

def decrypt( mess, tau ):
    """
        string x (char, char)dict -> string
        mess : chaine a decoder
        tau : fonction de decodage
        Retourne la chaine de caracteres obtenue par decodage de mess par tau
    """
    msg = ""
    for s in mess:
        msg += tau[s]
    return msg

#mess1 = decrypt ( "aabcd", tau )
#mess2 = decrypt ( "dcba", tau )
#print(mess1)
#print(mess2)

chars2index = dict(zip(np.array(list(count.keys())), np.arange(len(count.keys()))))

def logLikelihood( mess, mu, A, chars ):
    """
        string x float np.array x float np.2d-array x char list -> float
        mess : message
        mu : vecteur de probabilites initiales
        A : matrice de transition
        chars : pour obtenir l'indice correspondant a une lettre
        Retourne la log-probabilite du message mess
    """
    chars = list(chars)
    index = chars.index(mess[0])
    proba = np.log(mu[index])
    
    for i in range(len(mess) - 1):
        t = chars.index(mess[i])
        t_1 = chars.index(mess[i+1])
        proba += np.log(A[t][t_1])
    return proba

#p1 = logLikelihood( "abcd", mu, A, chars2index )
#p2 = logLikelihood( "dcba", mu, A, chars2index )


def MetropolisHastings( mess, mu, A, tau, N, chars ):
    """
        mess : message code
        mu, A : modele de bigrammes
        tau : fonction de decodage initiale
        N : nombre maximum d'iteration de l'algorithme
        Retourne le message decode le plus vraisemblable    
    """
    
    msg_tau = decrypt(mess, tau)
    log_tau = logLikelihood(msg_tau, mu, A, chars)
    maxMsg = msg_tau
    maxLog = log_tau
    for i in range( N ):
        new_tau = swapF(tau)
        msg_new_tau = decrypt(mess, new_tau)
        log_new_tau = logLikelihood(msg_new_tau, mu, A, chars)
        alpha = min(1, np.exp(log_new_tau-log_tau))
        u = np.random.uniform(0, 1)
        if u <= alpha:
            tau = new_tau
            msg_tau = msg_new_tau
            log_tau = log_new_tau
            if log_new_tau > maxLog:
                maxMsg = msg_new_tau
                maxLog = log_new_tau
                print("log-vraisemblance : " + str(maxLog))
                print(maxMsg)
                   
    return maxMsg

def identityTau (count):
    tau = {}
    for k in list(count.keys ()):
        tau[k] = k
    return tau

#mh = MetropolisHastings( secret, mu, A, identityTau (count), 100, chars2index)
#print(mh)

# ATTENTION: mu = proba des caractere init, pas la proba stationnaire
# => trouver les caractères fréquents = sort (count) !!
# distribution stationnaire des caracteres
freqKeys = np.array(list(count.keys()))
freqVal  = np.array(list(count.values()))
# indice des caracteres: +freq => - freq dans la references
rankFreq = (-freqVal).argsort()

# analyse mess. secret: indice les + freq => - freq
cles = np.array(list(set(secret))) # tous les caracteres de secret
rankSecret = np.argsort(-np.array([secret.count(c) for c in cles]))
# ATTENTION: 37 cles dans secret, 77 en général... On ne code que les caractères les plus frequents de mu, tant pis pour les autres
# alignement des + freq dans mu VS + freq dans secret
tau_init = dict([(cles[rankSecret[i]], freqKeys[rankFreq[i]]) for i in range(len(rankSecret))])

mh = MetropolisHastings(secret, mu, A, tau_init, 50000, chars2index)
print(mh)