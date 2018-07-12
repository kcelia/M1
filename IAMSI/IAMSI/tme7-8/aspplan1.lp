% Nom du domaine blockWorld
% Déclaration des prédicats (blockWorld)
pred(on(X, Y)) :- block(X), block(Y).
pred(ontable(X)) :- block(X).
pred(clear(X)) :- block(X).
pred(handempty).
pred(holding(X)) :- block(X).
% Déclaration des actions (blockWorld)
action(pickup(X)) :- block(X).
% préconditions
pre(pickup(X), clear(X)) :- action(pickup(X)).
pre(pickup(X), ontable(X)) :- action(pickup(X)).
pre(pickup(X), handempty) :- action(pickup(X)).
% effects
del(pickup(X), ontable(X)) :- action(pickup(X)).
del(pickup(X), clear(X)) :- action(pickup(X)).
del(pickup(X), handempty) :- action(pickup(X)).
add(pickup(X), holding(X)) :- action(pickup(X)).
action(putdown(X)) :- block(X).
% préconditions
pre(putdown(X), holding(X)) :- action(putdown(X)).
% effects
del(putdown(X), holding(X)) :- action(putdown(X)).
add(putdown(X), ontable(X)) :- action(putdown(X)).
add(putdown(X), handempty) :- action(putdown(X)).
add(putdown(X), clear(X)) :- action(putdown(X)).
action(stack(X, Y)) :- block(X), block(Y).
% préconditions
pre(stack(X, Y), clear(Y)) :- action(stack(X, Y)).
pre(stack(X, Y), holding(X)) :- action(stack(X, Y)).
% effects
del(stack(X, Y), clear(Y)) :- action(stack(X, Y)).
del(stack(X, Y), holding(X)) :- action(stack(X, Y)).
add(stack(X, Y), on(X, Y)) :- action(stack(X, Y)).
add(stack(X, Y), clear(X)) :- action(stack(X, Y)).
add(stack(X, Y), handempty) :- action(stack(X, Y)).
action(unstack(X, Y)) :- block(X), block(Y).
% préconditions
pre(unstack(X, Y), on(X, Y)) :- action(unstack(X, Y)).
pre(unstack(X, Y), clear(X)) :- action(unstack(X, Y)).
pre(unstack(X, Y), handempty) :- action(unstack(X, Y)).
% effects
del(unstack(X, Y), on(X, Y)) :- action(unstack(X, Y)).
del(unstack(X, Y), clear(X)) :- action(unstack(X, Y)).
del(unstack(X, Y), handempty) :- action(unstack(X, Y)).
add(unstack(X, Y), clear(Y)) :- action(unstack(X, Y)).
add(unstack(X, Y), holding(X)) :- action(unstack(X, Y)).
% Déclaration des objets (problem) ou constantes (domain)
block(a;b;c;d).
% Etat initial
init(clear(b)).
init(ontable(a)).
init(on(b, a)).
init(clear(c)).
init(ontable(d)).
init(on(c, d)).
init(handempty).
% Etat final (but)
but(on(a, b)).
but(on(b, c)).
but(on(c, d)).
but(ontable(d)).
but(clear(a)).
but(handempty).

#const n=4.
time(0..n).

holds(P, 0) :- init(P).
1{perform(A, T) : action(A)} :- time(T), T!=n.
:- perform(A, T), not holds(P, T), pre(A, P), time(T), pred(P), action(A).
holds(P, T+1) :- perform(A, T), add(A, P), time(T), pred(P), action(A).
holds(P, T+1) :- holds(P, T), not del(A, P), perform(A, T), time(T), pred(P), action(A).
:- perform(A1, T), perform(A2, T), time(T), action(A1), action(A2), A1!=A2.
:- not holds(P, n), but(P), pred(P).

#show perform/2.
