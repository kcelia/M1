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

/* Exo2 */
subsS1(C,C).
subsS1(C, D) :- subs(C, D), C\==D.
subsS1(C, D):- subs(C, E), subsS1(E, D), E\==D.

/*2.4*/

subsS(C, D) :- subsS(C, D, [C]).
subsS(C, C, _).
subsS(C, D, _) :- subs(C, D), C\==D.
subsS(C, D, L) :- subs(C, E), not(member(E, L)), subsS(E, D, [E|L]), E\==D.

/*2.8*/

equiv(A,B):- subsS(A,B), subsS(B,A).

/*Les modifications:*/

equiv(chien, canide).
equiv(carnivore, all(mange, animal)).
equiv(herbivore, all(mange, plante)).


