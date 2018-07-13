# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from arftools import *

from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.svm import SVC, LinearSVC



clf = svm.SVC(kernel='linear')
#clf = svm.SVC(probability = True,C=0.5)

def load_usps(filename):
    with open(filename,"r") as f:
        f.readline()
        data =[ [float(x) for x in l.split()] for l in f if len(l.split())>2]
    tmp = np.array(data)
    return tmp[:,1:],tmp[:,0].astype(int)

USPS = load_usps("USPS_train.txt")
USPS_T = load_usps("USPS_test.txt")

"""
Pour extraire de la base USPS_train les éléments correspondant à des 0 et leur donner l'étiquette -1
et les éléments correspondant à des 1 et leur donner l'étiquette 1
""" 
def det_train():
    exemple = []
    label   = []
    labels = USPS[1]
    for i in range(0,len(USPS[0])):
        if labels[i] == 0:
            exemple.append(USPS[0][i])
            label.append(-1)
        if labels[i] == 1:
            exemple.append(USPS[0][i])
            label.append(1)
    return exemple, label
    
"""
Pour extraire de la base USPS_test les éléments correspondant à des 0 et leur donner l'étiquette -1
et les éléments correspondant à des 1 et leur donner l'étiquette 1
""" 

def det_test():
    exemple = []
    label   = []
    labels = USPS_T[1]
    for i in range(0,len(USPS_T[0])):
        if labels[i] == 0:
            exemple.append(USPS_T[0][i])
            label.append(-1)
        if labels[i] == 1:
            exemple.append(USPS_T[0][i])
            label.append(1)
    return exemple, label
          
ex,lab = det_train()
ex_test,label_test = det_test()

#one-against-one
# faire lextraction et étiquettage!

clf = svm.SVC(kernel='linear')
clf.fit(ex, lab)
clf.predict(USPS_T[0]) 
print clf.score(ex_test,label_test)

"""
pour analyser suivant les différentes valeurs de C
comment se comporte la séparation linéaire
"""
X, Y = gen_arti(2,2,0.5,500,0,0.02) #sans bruit
#plot_data(X,Y)
# figure number

fignum = 1

# fit the model
#for kernel in ('linear', 'poly', 'rbf'):

for penalty in (5, 2.5, 0.01):

    clf = svm.SVC(kernel = 'linear', C=penalty)
    clf.fit(X, Y)

    # get the separating hyperplane
    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-5, 5)
    yy = a * xx - (clf.intercept_[0]) / w[1]

    # plot the parallels to the separating hyperplane that pass through the
    # support vectors
    margin = 1 / np.sqrt(np.sum(clf.coef_ ** 2))
    yy_down = yy + a * margin
    yy_up = yy - a * margin

    # plot the line, the points, and the nearest vectors to the plane
    plt.figure(fignum, figsize=(4, 3))
    plt.clf()
    plt.plot(xx, yy, 'k-')
    plt.plot(xx, yy_down, 'k--')
    plt.plot(xx, yy_up, 'k--')

    plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80,
                facecolors='none', zorder=10)
    plt.scatter(X[:, 0], X[:, 1], c=Y, zorder=10, cmap=plt.cm.Paired)

    plt.axis('tight')
    x_min = -4.8
    x_max = 4.2
    y_min = -6
    y_max = 6

    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    Z = clf.predict(np.c_[XX.ravel(), YY.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(XX.shape)
    plt.figure(fignum, figsize=(4, 3))
    plt.pcolormesh(XX, YY, Z, cmap=plt.cm.Paired)

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.xticks(())
    plt.yticks(())
    fignum = fignum + 1

plt.show()

"""
Pour analyser suivant les différents noyaux comment se comporte 
la frontière sur les mêmes nuages de points
"""
for kernel in ('linear', 'poly', 'rbf', 'sigmoid'):
    clf = svm.SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)

    # plot the line, the points, and the nearest vectors to the plane
    plt.figure(fignum, figsize=(4, 3))
    plt.clf()

    plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80,
                facecolors='none', zorder=10)
    plt.scatter(X[:, 0], X[:, 1], c=Y, zorder=10, cmap=plt.cm.Paired)

    plt.axis('tight')
    x_min = -3
    x_max = 3
    y_min = -3
    y_max = 3

    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(XX.shape)
    plt.figure(fignum, figsize=(4, 3))
    plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
    plt.contour(XX, YY, Z, colors=['k', 'k', 'k'], linestyles=['--', '-', '--'],
                levels=[-.5, 0, .5])

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.xticks(())
    plt.yticks(())
    fignum = fignum + 1
plt.show()

"""
afin de déterminer les meilleurs paramètres on utilise GridSearchCV qui permet 
en lui passant tous les jeux de paramètres que l'on veut analyser de renvoyer
directement les tests.
"""
def best_parameters():  
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=0)
    tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]},
                    {'kernel':['poly'], 'degree':[3,5,7,9], 'C': [1, 10, 100, 1000]}]
    #GridSearch permet de faire varier les paramètres de façon plus simple
    clf = GridSearchCV(SVC(), tuned_parameters, cv=5)
    clf.fit(X_train, Y_train)
    
    gamma_rbf_c_1, erreur_rbf_c_1, gamma_rbf_c_10, erreur_rbf_c_10, gamma_rbf_c_100, erreur_rbf_c_100, gamma_rbf_c_1000, erreur_rbf_c_1000 = [],[],[],[],[],[],[],[]
    c_linear, erreur_linear = [],[]
    degree_poly_c_1,erreur_poly_c_1,degree_poly_c_10,erreur_poly_c_10,degree_poly_c_100,erreur_poly_c_100,degree_poly_c_1000,erreur_poly_c_1000 = [],[],[],[],[],[],[],[]
    
    for params, mean_score, scores in clf.grid_scores_:
        if params['kernel'] == 'rbf':
            if params['C'] == 1:
                gamma_rbf_c_1.append(params['gamma'])
                erreur_rbf_c_1.append(1-mean_score) #pour trouver l'erreur on fait 1 moins le score qui est une proba
            if params['C'] == 10:
                gamma_rbf_c_10.append(params['gamma'])
                erreur_rbf_c_10.append(1-mean_score)
            if params['C'] == 100:
                gamma_rbf_c_100.append(params['gamma'])
                erreur_rbf_c_100.append(1-mean_score)
            if params['C'] == 1000:
                gamma_rbf_c_1000.append(params['gamma'])
                erreur_rbf_c_1000.append(1-mean_score)
        if params['kernel'] == 'linear':
            c_linear.append(params['C'])
            erreur_linear.append(1-mean_score)
        if params['kernel'] == 'poly':
            if params['C'] == 1:
                degree_poly_c_1.append(params['degree'])
                erreur_poly_c_1.append(1-mean_score)
            if params['C'] == 10:
                degree_poly_c_10.append(params['degree'])
                erreur_poly_c_10.append(1-mean_score)
            if params['C'] == 100:
                degree_poly_c_100.append(params['degree'])
                erreur_poly_c_100.append(1-mean_score)
            if params['C'] == 1000:
                degree_poly_c_1000.append(params['degree'])
                erreur_poly_c_1000.append(1-mean_score)
      
    
    plt.plot(gamma_rbf_c_1,erreur_rbf_c_1)
    plt.title("SVM with gaussian kernel and C = 1")
    plt.xlabel("gamma")
    plt.ylabel("erreur")
    plt.show()
    
    plt.plot(gamma_rbf_c_10,erreur_rbf_c_10)
    plt.title("SVM with gaussian kernel and C = 10")
    plt.xlabel("gamma")
    plt.ylabel("erreur")
    plt.show()
    
    plt.plot(gamma_rbf_c_100,erreur_rbf_c_100)
    plt.title("SVM with gaussian kernel and C = 100")
    plt.xlabel("gamma")
    plt.ylabel("erreur")
    plt.show()
    
    plt.plot(gamma_rbf_c_1000,erreur_rbf_c_1000)
    plt.title("SVM with gaussian kernel and C = 1000")
    plt.xlabel("gamma")
    plt.ylabel("erreur")
    plt.show()
    
    plt.plot(c_linear,erreur_linear)
    plt.title("SVM with linaer kernel")
    plt.xlabel("C")
    plt.ylabel("erreur")
    plt.show()
    
    plt.plot(degree_poly_c_1,erreur_poly_c_1)
    plt.title("SVM with polynomial kernel and C = 1")
    plt.xlabel("degree")
    plt.ylabel("erreur")
    plt.show()
    
    plt.plot(degree_poly_c_10,erreur_poly_c_10)
    plt.title("SVM with polynomial kernel and C = 10")
    plt.xlabel("degree")
    plt.ylabel("erreur")
    plt.show()
    
    plt.plot(degree_poly_c_100,erreur_poly_c_100)
    plt.title("SVM with polynomial kernel and C = 100")
    plt.xlabel("degree")
    plt.ylabel("erreur")
    plt.show()
    
    plt.plot(degree_poly_c_1000,erreur_poly_c_1000)
    plt.title("SVM with polynomial kernel and C = 1000")
    plt.xlabel("degree")
    plt.ylabel("erreur")
    plt.show()

#best_parameters()  

#one vs one : score très proche 

ex,lab = det_train()
ex_test,label_test = det_test()

err_app = []
err_test = []

for penalty in np.arange(1,15,0.5):
    #création du modèle
    clf = svm.SVC(kernel='linear',C=penalty)
    #entrainement
    clf.fit(ex,lab)
    # évaluation du score
    err_app.append(clf.score(ex,lab))
    err_test.append(clf.score(ex_test,label_test))
    
plt.plot(np.arange(1,15,0.5),err_app,'b')
plt.plot(np.arange(1,15,0.5),err_test,'g')


ex,lab = det_train()
ex_test,label_test = det_test()

err_app = []
err_test = []

for penalty in np.arange(1,15,0.5):
    #création du modèle
    clf = OneVsRestClassifier(LinearSVC(random_state=0))
    #entrainement
    clf.fit(ex,lab)
    # évaluation du score
    err_app.append(clf.score(ex,lab))
    err_test.append(clf.score(ex_test,label_test))
    
plt.plot(np.arange(1,15,0.5),err_app,'b')
plt.plot(np.arange(1,15,0.5),err_test,'g')

X_train, Y_train = det_train()
X_test, Y_test = det_test()

def oneVsOne():
    ovo = svm.SVC(kernel='linear')
    ovo.fit(X_train,Y_train)
    print 'one vs one : '
    print ovo.predict(X_test)
    print ("The score of One-VS-One classsification is %0.3f" % ovo.score(X_test,Y_test))
#oneVsOne()
#--> 0.995

"""
Pour extraire de la base USPS_train les éléments correspondant à des 0 et leur donner l'étiquette -1
et les éléments correspondant à des 1 et leur donner l'étiquette 1
""" 
def det_train2(ind):
    exemple = []
    label   = []
    labels = USPS[1]
    for i in range(0,len(USPS[0])):
        if labels[i] == ind:
            exemple.append(USPS[0][i])
            label.append(1)
        if labels[i] != ind:
            exemple.append(USPS[0][i])
            label.append(-1)
    return exemple, label
    
"""
Pour extraire de la base USPS_test les éléments correspondant à des 0 et leur donner l'étiquette -1
et les éléments correspondant à des 1 et leur donner l'étiquette 1
""" 

def det_test2(ind):
    exemple = []
    label   = []
    labels = USPS_T[1]
    for i in range(0,len(USPS_T[0])):
        if labels[i] == ind:
            exemple.append(USPS_T[0][i])
            label.append(1)
        if labels[i] != ind:
            exemple.append(USPS_T[0][i])
            label.append(-1)
    return exemple, label
          
X_train,Y_train = det_train2(0)
X_test,Y_test = det_test2(0)
     
def oneVsAll():
    ova = LinearSVC(random_state=0)
    ova.fit(X_train,Y_train)
    print '\none vs all : '
    print ova.predict(X_test)
    print ("The score of One-VS-All classsification is %0.3f" % ova.score(X_train,Y_train))
    print ("The score of One-VS-All classsification is %0.3f" % ova.score(X_test,Y_test))   
oneVsAll()

#0
#The score of One-VS-All classsification is 1.000
#The score of One-VS-All classsification is 0.97

#1
#The score of One-VS-All classsification is 1.000
#The score of One-VS-All classsification is 0.99

# 2 
#The score of One-VS-All classsification is 0.993
#The score of One-VS-All classsification is 0.96

#3
#The score of One-VS-All classsification is 0.993
#The score of One-VS-All classsification is 0.96

#4
#The score of One-VS-All classsification is 0.993
#The score of One-VS-All classsification is 0.96

#5
#The score of One-VS-All classsification is 0.994
#The score of One-VS-All classsification is 0.96

#6
#The score of One-VS-All classsification is 1.000
#The score of One-VS-All classsification is 0.98

#7
#The score of One-VS-All classsification is 1.000
#The score of One-VS-All classsification is 0.98

# 8 
#--> 0.987 (train)
#--> 0.95 (test)

#9
#The score of One-VS-All classsification is 0.992
#The score of One-VS-All classsification is 0.97

#X, Y = gen_arti( 2, 2, 0.5, 500, 2, 0.02) #sans bruit
#plot_data(X,Y)
# figure number

