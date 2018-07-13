import numpy as np
from collections import Counter
import pickle
try:
    import pydot  #pour l'affichage graphique d'arbres
except ImportError:
    print("Pydot non disponible pour l'affichage graphique, allez sur http://www.webgraphviz.com/ pour generer un apercu de l'arbre")

###############################
# Fonctions auxiliaires
###############################

def p_log_p(freq):
    """ fonction pour calculer \sum p_i log(p_i) """
    return np.nan_to_num(np.sum(freq*np.log2(freq)))

def entropy(y):
    """ calcul de l'entropie d'un ensemble"""
    ylen = float(y.size)
    if ylen <= 1:
        return 0
    freq = np.array(list(Counter(y).values()))/ylen
    return -p_log_p(freq)

def entropy_cond(y_list):
    h, total = 0.,0.
    for y in y_list:
        h += len(y)*entropy(y)
        total += len(y)
    return h/total

###############################
# Classes
###############################


class Classifier(object):
    """ Classe generique d'un classifieur
        Dispose de 3 méthodes :
            fit pour apprendre
            predict pour predire
            score pour evaluer la precision
    """
    def fit(self,data,y):
        raise NotImplementedError("fit non  implemente")
    def predict(self,data):
        raise NotImplementedError("predict non implemente")
    def score(self,data,y):
        return (self.predict(data)==y).mean()


class Split(object):
    """ Permet de coder un split pour une variable continue
    """
    def __init__(self,idvar=None,threshold=None,gain=None):
        """
        :param idvar: numero de la variable de split
        :param threshold: seuil
        :param gain: gain d'information du split
        :return:
        """
        self.idvar=idvar
        self.threshold=threshold
        self.gain=gain

    def predict(self,data):
        """ Prediction pour une matrice d'exemples, -1 si <= threshold, +1 sinon
        :param x: matrice d'exemples
        :return: vecteur des labels
        """
        if len(data.shape)==1:
            data=data.reshape((1,data.shape[0]))
        return [-1 if data[i,self.idvar]<=self.threshold else 1 for i in range(data.shape[0])]

    @staticmethod
    def best_gain(x,y):
        """  calcul le meilleur seuil pour la colonne x (1-dimension) et les labels y
        :param x: vecteur 1d des donnees
        ;param y: vecteur des labels
        :return:
        """
        ylen = float(y.size)
        idx_sorted = np.argsort(x)
        h=entropy(y)
        xlast=x[idx_sorted[0]]
        split_val=x[idx_sorted[0]]
        hmin = h
        for i in range(y.size):
            if x[idx_sorted[i]]!=xlast:
                htmp = entropy_cond([y[idx_sorted[:i]], y[idx_sorted[i:]]])
                if htmp<hmin:
                    hmin=htmp
                    split_val=(xlast+x[idx_sorted[i]])/2.
            xlast=x[idx_sorted[i]]
        return (h-hmin/ylen),split_val

    @staticmethod
    def find_best_split(data,y):
        if len(data.shape)==1:
            data = data.reshape((1,data.shape[0]))
        hlist = [[Split.best_gain(data[:,i],y),i] for i in range(data.shape[1])]
        (h,threshold),idx= max(hlist)
        return Split(idx,threshold,h)

    def __str__(self):
        return "var %s, thresh %f (gain %f)" %(self.idvar,self.threshold, self.gain)

class Node(Classifier):
    """ Noeud d'un arbre
    """
    def __init__(self,split=None,parent=None,left=None,right=None,leaf=True,depth=-1,label=None,**kwargs):
        """
        :param split:  split du noeud
        :param parent: noeud parent, None si root
        :param left: fils gauche
        :param right: fils droit
        :param leaf: boolean vrai si feuille
        :param depth: profondeur
        :param label: label preponderant
        :return:
        """
        self.split, self.parent, self.left, self.right, self.leaf, self.label, self.depth = \
                                            split, parent, left, right, leaf, label, depth
        self.info = dict(kwargs)

    def predict(self,data):
        if len(data.shape)==1:
            data=data.reshape((1,data.shape[0]))
        if self.leaf:
            return [self.label]*data.shape[0]
        return [self.left.predict(data[i,:])[0] if res<0 else self.right.predict(data[i,:])[0]
                for i, res in enumerate(self.split.predict(data))]

    def fit(self, data, y):
        counts=Counter(y)
        self.split=Split.find_best_split(data, y)
        self.label = counts.most_common()[0][0]

    def __str__(self):
        if self.leaf:
            return "Leaf : %s" % (self.label,)
        return "Node : %s (%s)" % (self.split,self.info)

class DecisionTree(Classifier):
    """ Arbre de decision
    """

    def __init__(self,max_depth=None,min_samples_split=2):
        """
        :param max_depth: profondeur max
        :param min_samples_split:  nombre d'exemples minimal pour pouvoir spliter le noeud
        :return:
        """
        self.max_depth, self.min_samples_split = max_depth, min_samples_split
        self.root = None

    def fit(self,data,y):
        """ apprentissage de l'arbre de maniere iterative
        on apprend un noeud, puis on cree les deux enfants de ce noeud, que l'on ajoute a la pile des noeuds
        a traiter par la suite (nodes_to_treat), ainsi que les index des exemples associes (dic_idx)
        """
        self.root = Node(depth=0)
        nodes_to_treat = [self.root]
        dic_idx = dict({self.root : range(len(y))})
        while len(nodes_to_treat)>0:
            # recuperation du noeud courant
            curnode = nodes_to_treat.pop()
            #recuperation de la liste des indices des exemples associes, x[idx_train,:] contient l'ensemble des
            #exemples a traiter
            idx_train = dic_idx.pop(curnode)
            # infos complementaires sur le nombre d'exemples en apprentissage par label
            for lab,clab in Counter(y[idx_train]).items():
                curnode.info[lab]=clab
            curnode.fit(data[idx_train,:],y[idx_train])

            # recupere les predictions pour partager entre fils droit et gauche les exemples
            pred = curnode.split.predict(data[idx_train,:])
            l_idx = [ idx_train[i] for i in range(len(idx_train)) if pred[i]<0 ]
            r_idx = list(set(idx_train).difference(l_idx))

            #Condition d'arrets
            if entropy(y[idx_train])==0 or curnode.depth >= self.max_depth or \
                    len(l_idx) < self.min_samples_split or len(r_idx) < self.min_samples_split:
                curnode.leaf=True
                continue
            #Creation des deux enfants
            curnode.left = Node(parent=curnode,depth=curnode.depth+1)
            curnode.right = Node(parent=curnode,depth=curnode.depth+1)
            curnode.leaf = False
            #On enregistre les indices correspondant aux deux noeuds
            dic_idx[curnode.left]=l_idx
            dic_idx[curnode.right]=r_idx
            #On ajoute les deux enfants a la liste des noeuds a traiter
            nodes_to_treat = [curnode.left,curnode.right]+nodes_to_treat

    def predict(self,data):
        return self.root.predict(data)

    def __str__(self):
        return self.print_tree()

    def to_dot(self,dic_var=None):
        s="digraph Tree {"
        cpt=0
        nodes = [(self.root,cpt)]
        while len(nodes)>0:
            curnode,idx = nodes.pop()
            labinfo = ",".join(["%s: %s" % (lab,slab) for lab,slab in curnode.info.items()])
            if not curnode.leaf:
                s+="%d [label=\"%s <= %f\n IG=%f\n " %(idx,curnode.split.idvar \
                    if not dic_var else dic_var[curnode.split.idvar],curnode.split.threshold,curnode.split.gain)
                s+= " %s \n \",shape=\"box\" ];\n"  % (labinfo,)
                lidx = cpt +1
                ridx = cpt +2
                s+= "%d -> %d; %d -> %d;\n" % (idx,lidx,idx,ridx)
                cpt+=2
                nodes += [(curnode.left,lidx),(curnode.right,ridx)]
            else:
                s+= "%d [label=\"label=%s\n %s \"];\n" %(idx,curnode.label,labinfo)
        return s+"}"

    def to_pdf(self,filename,dic_var=None):
        pydot.graph_from_dot_data(self.to_dot(dic_var))[0].write_pdf(filename)

    def print_tree(self,fields=None):
        s=""
        nodes=[self.root]
        while len(nodes)>0:
            curnode=nodes.pop()
            if type(curnode)==str:
                s+=curnode
            else:
                if not curnode.leaf:
                    s+= "\t"*curnode.depth + "var %s :  > %f \n"  %(str(curnode.split.idvar) if not fields else fields[curnode.split.idvar],curnode.split.threshold)
                    nodes+=[curnode.left, "\t"*curnode.depth + "var %s :  <= %f \n"  %(str(curnode.split.idvar) if not fields else fields[curnode.split.idvar],curnode.split.threshold), curnode.right]
                else:
                    s+= "\t"*curnode.depth + "class : %s %s\n" %(curnode.label,str(curnode.info))
        return s
