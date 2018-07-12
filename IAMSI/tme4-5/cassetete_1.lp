%%%% CASSE TETE LOGIQUE %%%%

%% L'allemand garde les poissons

%% Nous avons interpreté les phrases de maniere differentes, nous obtenons le meme resultat, 
%% la difficulté qu'on a rencontré etait l'ordre des predicats et des operations.

pos(1..5).
couleur(bleu; rouge; blanc; vert; jaune).
boisson(the; cafe; lait; biere; eau).
nationalite(britannique; suedois; danois; norvegien; allemand).
animal(chien; poisson; chat; cheval; oiseau).
cigarette(princess; blend; dunhill; pallmall; bluemaster).

1{maison(X, C) : pos(X)}1 :- couleur(C).
:- maison(X1, C), maison(X2, C), pos(X1;X2), couleur(C), X1!=X2.
:- maison(X1, C1), maison(X2, C2), pos(X1;X2), couleur(C1;C2), X1==X2, C1 != C2.

1{habit(N, X) : pos(X)}1 :- nationalite(N).
:- habit(N1, X), habit(N2, X), pos(X), nationalite(N1;N2), N1!=N2.

1{boit(N, B) : boisson(B)}1 :- nationalite(N).
:- boit(N1, B), boit(N2, B), boisson(B), nationalite(N1;N2), N1!=N2.

1{garde(N, A) : animal(A)}1 :- nationalite(N).
:- garde(N1, A), garde(N2, A), animal(A), nationalite(N1;N2), N1!=N2.

1{fume(N, C) : cigarette(C)}1 :- nationalite(N).
:- fume(N1, C), fume(N2, C), cigarette(C), nationalite(N1;N2), N1!=N2.

%----------------------------------------------------------------------%

%1)
habit(britannique, X) :- maison(X, rouge), pos(X).
maison(X, rouge) :- habit(britannique, X), pos(X).

%2)
garde(suedois, chien).

%3)
boit(danois, the).

%4)
:- maison(X,vert), pos(X), X == 6 .
X1 +1 == X2 :- maison(X1, vert), maison(X2, blanc),  pos(X1;X2).

%5)
maison(X, vert) :- habit(N, X), boit(N, cafe), pos(X), nationalite(N).
boit(N,cafe) :-  habit(N, X), maison(X, vert), nationalite(N), pos(X).

%6)
garde(N,oiseau) :- fume(N,pallmall), nationalite(N).
fume(N,pallmall) :- garde(N,oiseau) , nationalite(N).

%7)
%maison(X,jaune) :- habit(N,X),	pos(X),	fume(N,dunhill), nationalite(N). %danoi qui a les poissons 
fume(N,dunhill):- habit(N,X),maison(X,jaune),pos(X), nationalite(N). 

%8)
boit(N, lait) :- habit(N, 3), nationalite(N).
habit(N, 3) :- boit(N, lait) , nationalite(N).

%9)
habit(norvegien, 1).


%10)

:- |X-X1|!=1, garde(N1, chat), habit(N, X), fume(N, blend), habit(N1, X1), pos(X;X1), nationalite(N;N1).
%|X1-X2|==1  :- fume(N1,blend), habit(N1,X1) , habit(N2,X2), garde(N2,chat) , nationalite(N2;N1) ,pos(X1), pos(X2).
%garde(N2,chat) :- fume(N1,blend), habit(N1,X1) , habit(N2,X2), |X1-X2|==1 , nationalite(N2;N1) ,pos(X1;X2).% meme resultat 

%11)
%:- |X-X1|!=1, garde(N1, cheval), habit(N, X), fume(N, dunhill), habit(N1, X1), pos(X;X1), nationalite(N;N1). % meme resultat
|X-X1|==1:-  garde(N1, cheval), habit(N, X), fume(N, dunhill), habit(N1, X1), pos(X;X1), nationalite(N;N1).


%12)
boit(N1,biere) :- fume(N1,bluemaster), nationalite(N1).

%13)
fume(allemand, princess).

%14)
%maison(X1, bleu) :- habit(norvegien, X), pos(X; X1), X+1== X1. % ma deduction %
%maison(X1, bleu) :- habit(norvegien, X), habit(N1, X1), pos(X;X1), |X1-X| == 1, nationalite(N1), N1 != norvegien.  
maison(X1, bleu) :- |X-X1|==1 , habit(norvegien, X), pos(X), pos(X1).

%15)
%boit(N1, eau):- fume(N, blend), habit(N, X), habit(N1, X1), pos(X;X1), nationalite(N1;N2),  |X1-X| == 1 . %meme resultat 
|X1-X| == 1 :- fume(N, blend), habit(N, X), habit(N1, X1), pos(X;X1), nationalite(N1;N2),   boit(N1, eau) .


#show garde/2.
%#show habit/2.
%#show fume/2.
%#show boit/2.
%#show maison/2 .