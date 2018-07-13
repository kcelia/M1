import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle


plt.ion()
parismap = mpimg.imread('data/paris-48.806-2.23--48.916-2.48.jpg')

## coordonnees GPS de la carte
xmin,xmax = 2.23,2.48   ## coord_x min et max
ymin,ymax = 48.806,48.916 ## coord_y min et max

def show_map():
    plt.imshow(parismap,extent=[xmin,xmax,ymin,ymax],aspect=1.5)
    ## extent pour controler l'echelle du plan

poidata = pickle.load(open("data/poi-paris.pkl","rb"))
## liste des types de point of interest (poi)
#print("Liste des types de POI" , ", ".join(poidata.keys()))

## Choix d'un poi
typepoi = "restaurant"
poiindice = 5

## Creation de la matrice des coordonnees des POI
geo_mat = np.zeros((len(poidata[typepoi]),2))
for i,(k,v) in enumerate(poidata[typepoi].items()):
    geo_mat[i,:]=v[0]
#print("geo_mat",geo_mat)
## Affichage brut des poi
show_map()
## alpha permet de regler la transparence, s la taille
plt.scatter(geo_mat[:,1],geo_mat[:,0],alpha=0.8,s=3)


###################################################

# discretisation pour l'affichage des modeles d'estimation de densite
steps = 10
xx,yy = np.meshgrid(np.linspace(xmin,xmax,steps),np.linspace(ymin,ymax,steps))
grid = np.c_[xx.ravel(),yy.ravel()]
#print("grid",grid)

##################################################

class methode_histogramme:
    """classe qui implemente une estimation d'histogramme"""
    
    def __init__(self, m, steps):
        self.x = m[:,1]
        self.y = m[:,0]
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.lstepsx = (self.xmax-self.xmin)/steps*1.0
        self.lstepsy = (self.ymax-self.ymin)/steps*1.0
        self.hist = np.zeros((steps,steps))
        
    def fit(self):
        
        for i in range(len(self.x)):
            tmp=xmin
            cpt=0
            while (tmp<self.x[i]):
                tmp+=self.lstepsx
                cpt+=1
            ix=cpt-2
            cpt=0
            tmp=ymin

            while (tmp<self.y[i]):
                tmp+=self.lstepsy
                cpt+=1
            iy=cpt-2
            #ix=self.x[i]%self.lstepsx
            #print("ix",ix)
            #iy=self.y[i]%self.lstepsy
            #print("iy",iy)
            self.hist[ix][iy]+=1
            #self.hist[ceil(self.x[self.poiindice][i]%self.lstepsx)][ceil(self.y[self.poiindice][i]%self.lstepsy)]
        self.hist=self.hist/len(self.x)*1.1        
       
        
    def predict(self, test):
        res=[]
        for t in test:
            tmp=xmin
            cpt=0
            while (tmp<t[0]):
                tmp+=self.lstepsx
                cpt+=1
            ix=cpt-2
            cpt=0
            tmp=ymin

            while (tmp<t[1]):
                tmp+=self.lstepsy
                cpt+=1
            iy=cpt-2
            res.append(self.hist[ix][iy])
        return np.array(res)

##################################################

mon_histo = methode_histogramme(geo_mat, steps)
mon_histo.fit()
res = mon_histo.predict(grid).reshape(steps, steps)
#print("res",res)
plt.figure()
show_map()
plt.imshow(res,extent=[xmin,xmax,ymin,ymax],interpolation='none', alpha=0.3,origin = "lower")
plt.colorbar()
plt.scatter(geo_mat[:,1],geo_mat[:,0],alpha=0.3)

##################################################

class noyau_parzen:
    
    def __init__(self, h, mat, d):
        self.h = h
        self.mat = mat
        self.d = d
        self.res = []
        
    def fit(self):
         self.fenetres = dict()
                    
    def predict(self, test):
        V = self.h**self.d
        for i in range(len(test)):
            ix = test[i][0]
            iy = test[i][1]
            self.fenetres[(ix, iy)] = 0
            for j in range(len(self.mat)):
                jx = self.mat[j][1]
                jy = self.mat[j][0]
                if (((jx >= ix - self.h) and (jx <= ix + self.h)) and ((jy >= iy - self.h) and (jy <= iy + self.h))):
                    self.fenetres[(ix, iy)] += 1
            self.fenetres[(ix, iy)] = self.fenetres[(ix, iy)]/(len(self.mat)*V)
            self.res.append(self.fenetres[(ix, iy)])
        return np.array(self.res)

##################################################
# A remplacer par res = monModele.predict(grid).reshape(steps,steps)
#res = np.random.random((steps,steps))
mon_parzen = noyau_parzen(0.01, geo_mat, 2)
mon_parzen.fit()
res = mon_parzen.predict(grid).reshape(steps, steps)
#print("res",res)
plt.figure()
show_map()
plt.imshow(res,extent=[xmin,xmax,ymin,ymax],interpolation='none', alpha=0.3,origin = "lower")
plt.colorbar()
plt.scatter(geo_mat[:,1],geo_mat[:,0],alpha=0.3)
