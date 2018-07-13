/*T-box*/

subs(chat, felin).
subs(lion, felin).

subs(chien,canide).
subs(canide,chien).

subs(souris, mammifere).
subs(felin, mammifere).
subs(canide, mammifere).

subs(mammifere, animal).
subs(canari, animal).

subs(animal, etreVivant).

subs(and(animal, plante), nothing).

subs(and(animal, some(aMaitre)), pet).

subs(pet, some(aMaitre)).

subs(some(aMaitre), all(aMaitre, humain)).

subs(chihuahua, and(chien, pet)).

subs(carnivore,all(mange,animal)).
subs(herbivore,all(mange,plante)).
subs(lion, carnivore).
subs(carnivore, predateur).
subs(animal, some(mange)).
subs(animal,some(mange)).
subs(and(all(mange,nothing), some(mange)), nothing).

/* Abox*/

inst(felix, chat).
inst(pierre, humain).
inst(princesse, chihuahua).
inst(marie, humaine).
inst(jerry, souris).
inst(titi, canari).

instR(felix, mange, jerry).
instR(felix, mange, titi).

instR(princesse, aMaitre, marie).
instR(felix, aMaitre, pierre).


equiv(A,B):- subsS(A,B), subsS(B,A).


equiv(chien, canide).
equiv(carnivore, all(mange, animal)).
equiv(herbivore, all(mange, plante)).

subsS(C, D) :- subsS(C, D, [C]).
subsS(all(R,C),D,_):- subs(D,all(R,E)), subsS(all(R,C), all(R,E),_).
subsS(all(R,C), all(R,D),_) :- subsS(C, D).
subsS(C, C, _).
subsS(C, D, _) :- subs(C, D), C\==D.
subsS(C, D, L) :- subs(C, E), not(member(E, L)), subsS(E, D, [E|L]), E\==D.


subsS(C, and(D1, D2), L) :- D1\=D2, subsS(C, D1, L), subsS(C, D2, L).
subsS(C, D, L) :- subs(and(D1, D2), D), E=and(D1, D2), not(member(E,L)), subsS(C, E, [E|L]), E\==C.
subsS(and(C, C), D, L) :- nonvar(C), subsS(C, D, [C|L]).
subsS(and(C1, C2), D, L) :- C1\=C2, subsS(C1, D, [C1|L]).
subsS(and(C1, C2), D, L) :- C1\=C2, subsS(C2, D, [C2|L]).
subsS(and(C1, C2), D, L) :- subs(C1, E1), E=and(E1, C2), not(member(E, L)), subsS(E, D, [E|L]), E\==D.
subsS(and(C1, C2), D, L) :- Cinv=and(C2, C1), not(member(Cinv, L)), subsS(Cinv, D, [Cinv|L]).
subsS(and(C1, C2), all(R, D),_) :- subsS(C1,all(R,E)), subsS(C2, all(R,L)), subsS(and(E,L),D).
subsS(A, B, _) :- inst(A,C), subsS(C,B). 

subsS(A, all(B, C), _) :- instR(A, B, C).
subsS(A, all(B, C), _) :- C=and(D, F), instR(A, B, D), instR(A, B, F).
subsS(A, all(B, C), _) :- instR(A, B, and(C, D)), C\==D.
