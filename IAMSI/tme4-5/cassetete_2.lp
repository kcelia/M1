%%%% CASSE TETE LOGIQUE %%%%

%%%%%% Univers %%%%%%
%% Définition de l'univers
pos(1..5).
couleur(bleu; rouge; blanc; vert; jaune).
boisson(the; cafe; lait; biere; eau).
nationalite(britannique; suedois; danois; norvegien; allemand).
animal(chien; poisson; chat; cheval; oiseau).
cigarette(princess; blend; dunhill; pallmall; bluemaster).


%%%%%% Unicité %%%%%%
%% Génération des maisons (avec contraintes d'intégrité)
1{maison(X, C) : pos(X)}1 :- couleur(C).
% Deux maisons ne peuvent avoir la même couleur
:- maison(X1, C), maison(X2, C), pos(X1;X2), couleur(C), X1!=X2.
% Deux maisons de différentes couleurs ne peuvent être à la même position
:- maison(X, C1), maison(X, C2), pos(X), couleur(C1;C2), C1 != C2.

%% Génération des relations d'habitat (avec contraintes d'intégrité)
1{habite(N, X) : pos(X)}1 :- nationalite(N).
% Deux personnes ne peuvent habiter dans la même maison
:- habite(N1, X), habite(N2, X), pos(X), nationalite(N1;N2), N1!=N2.

% NB : habite(N, X) : la personne de nationalité N habite la maison à la position X


%% Génération des relations de boisson (avec contraintes d'intégrité)
1{boit(N, B) : boisson(B)}1 :- nationalite(N).
% Deux personnes ne peuvent boire la même boisson
:- boit(N1, B), boit(N2, B), boisson(B), nationalite(N1;N2), N1!=N2.

%% Génération des relations d'élevage d'animaux (avec contraintes d'intégrité)
1{garde(N, A) : animal(A)}1 :- nationalite(N).
% Deux personnes ne peuvent garder le même animal
:- garde(N1, A), garde(N2, A), animal(A), nationalite(N1;N2), N1!=N2.

%% Génération des relations de fumette (avec contraintes d'intégrité)
1{fume(N, C) : cigarette(C)}1 :- nationalite(N).
% Deux personnes ne peuvent fumer la même cigarette
:- fume(N1, C), fume(N2, C), cigarette(C), nationalite(N1;N2), N1!=N2.


%%%%%% Contraintes %%%%%%
%%%%%% 1 %%%%%
% Si j'ai une maison rouge à la position X alors le britannique habite la maison en position X
habite(britannique, X) :- maison(X, rouge), pos(X).

%%%%%% 2 %%%%%
% Le suédois garde un chien
garde(suedois, chien).

%%%%%% 3 %%%%%
% Le danois boit du thé
boit(danois, the).

%%%%%% 4 %%%%%
% Si j'ai une maison blanche et alors la maison voisine est verte
maison(X1, vert) :- maison(X2, blanc), pos(X1;X2), X1+1==X2.

%%%%%% 5 %%%%%
% Si une personne habite dans une maison verte alors elle boit du café
boit(N, cafe) :- habite(N, X), maison(X, vert), pos(X), nationalite(N).

%%%%%% 6 %%%%%
% Si une personne fume du pallmall alors elle garde des oiseaux
garde(N, oiseau) :- fume(N, pallmall), nationalite(N).

%%%%%% 7 %%%%%
% Si une personne habite la maison jaune alors elle fume du dunhill
fume(N, dunhill) :- habite(N, X), maison(X, jaune), pos(X), nationalite(N).

%%%%%% 8 %%%%%
% si une personne habite une maison située au centre (position 3) alors elle boit du lait
boit(N, lait) :- habite(N, 3), nationalite(N). 

%%%%%% 9 %%%%%
% Le norvegien habite la première maison
habite(norvegien, 1).

%%%%%% 10 %%%%%
% Si une personne de nationalité N garde fume du blend et qu'une personne de nationalité N1 garde un chat, alors elles sont voisines
|X-X1|==1 :- garde(N1, chat), habite(N, X), fume(N, blend), habite(N1, X1), pos(X;X1), nationalite(N;N1).

%%%%%% 11 %%%%%
% Si une personne de nationalité N garde fume du dunhill et qu'une personne de nationalité N1 garde des chevaux, alors elles sont voisines
|X-X1|==1 :- garde(N1, cheval), habite(N, X), fume(N, dunhill), habite(N1, X1), pos(X;X1), nationalite(N;N1).

%%%%%% 12 %%%%%
% Si une personne fume du bluemaster alors elle boit de la bière
boit(N, biere) :- fume(N, bluemaster), nationalite(N).

%%%%%% 13 %%%%%
% L'allemand fume des princess
fume(allemand, princess).

%%%%%% 14 %%%%%
% Si j'ai une maison habitée par le norvegien et une maison bleue, alors ces deux maisons sont voisines
|X-X1|==1 :- maison(X1, bleu), habite(norvegien, X), pos(X), pos(X1).

%%%%%% 15 %%%%%
% Si une personne de nationalité N garde fume du blend et qu'une personne de nationalité N1 boit de l'eau, alors elles sont voisines
|X1-X|==1 :- boit(N1, eau), habite(N, X), fume(N, blend), habite(N1, X1), pos(X;X1), nationalite(N;N1).

#show garde/2.