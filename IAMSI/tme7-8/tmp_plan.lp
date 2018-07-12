% Nom du domaine singeBananes
entity(X) :- actor(X).
entity(X) :- obj(X).
% Déclaration des prédicats (singeBananes)
pred(situe(X, Y)) :- entity(X), place(Y).
pred(niveau(X, Y)) :- entity(X), level(Y).
pred(possede(X, Y)) :- actor(X), obj(Y).
pred(mainsVides).
% Déclaration des actions (singeBananes)
action(seDeplace(X, Y)) :- place(X), place(Y).
% préconditions
pre(seDeplace(X, Y), situe(singe, X)) :- action(seDeplace(X, Y)).
pre(seDeplace(X, Y), niveau(singe, bas)) :- action(seDeplace(X, Y)).
% effects
del(seDeplace(X, Y), situe(singe, X)) :- action(seDeplace(X, Y)).
add(seDeplace(X, Y), situe(singe, Y)) :- action(seDeplace(X, Y)).
action(prend(X, N, P)) :- obj(X), level(N), place(P).
% préconditions
pre(prend(X, N, P), mainsVides) :- action(prend(X, N, P)).
pre(prend(X, N, P), niveau(singe, N)) :- action(prend(X, N, P)).
pre(prend(X, N, P), situe(singe, P)) :- action(prend(X, N, P)).
pre(prend(X, N, P), niveau(X, N)) :- action(prend(X, N, P)).
pre(prend(X, N, P), situe(X, P)) :- action(prend(X, N, P)).
% effects
del(prend(X, N, P), mainsVides) :- action(prend(X, N, P)).
del(prend(X, N, P), situe(X, P)) :- action(prend(X, N, P)).
del(prend(X, N, P), niveau(X, N)) :- action(prend(X, N, P)).
add(prend(X, N, P), possede(singe, X)) :- action(prend(X, N, P)).
action(depose(X, P, N)) :- obj(X), place(P), level(N).
% préconditions
pre(depose(X, P, N), possede(singe, X)) :- action(depose(X, P, N)).
pre(depose(X, P, N), situe(singe, P)) :- action(depose(X, P, N)).
pre(depose(X, P, N), niveau(singe, N)) :- action(depose(X, P, N)).
% effects
del(depose(X, P, N), possede(singe, X)) :- action(depose(X, P, N)).
add(depose(X, P, N), mainsVides) :- action(depose(X, P, N)).
add(depose(X, P, N), situe(X, P)) :- action(depose(X, P, N)).
add(depose(X, P, N), niveau(X, N)) :- action(depose(X, P, N)).
action(monteCaisse(P)) :- place(P).
% préconditions
pre(monteCaisse(P), situe(singe, P)) :- action(monteCaisse(P)).
pre(monteCaisse(P), niveau(singe, bas)) :- action(monteCaisse(P)).
pre(monteCaisse(P), situe(caisse, P)) :- action(monteCaisse(P)).
pre(monteCaisse(P), niveau(caisse, bas)) :- action(monteCaisse(P)).
pre(monteCaisse(P), mainsVides) :- action(monteCaisse(P)).
% effects
del(monteCaisse(P), niveau(singe, bas)) :- action(monteCaisse(P)).
add(monteCaisse(P), niveau(singe, haut)) :- action(monteCaisse(P)).
% Déclaration des objets (problem) ou constantes (domain)
level(haut;bas).
place(a;b;c).
obj(bananes;caisse).
actor(singe).
% Etat initial
init(situe(singe, a)).
init(situe(bananes, b)).
init(situe(caisse, c)).
init(niveau(singe, bas)).
init(niveau(bananes, haut)).
init(niveau(caisse, bas)).
init(mainsVides).
% Etat final (but)
but(possede(singe, bananes)).

%Planificateur STRIPS en ASP
#const n=6.
time(0..n).

holds(P, 0) :- init(P).
1{perform(A, T) : action(A)} :- time(T), T!=n.
:- perform(A, T), not holds(P, T), pre(A, P), time(T), pred(P), action(A).
holds(P, T+1) :- perform(A, T), add(A, P), time(T), pred(P), action(A).
holds(P, T+1) :- holds(P, T), not del(A, P), perform(A, T), time(T), pred(P), action(A).
:- perform(A1, T), perform(A2, T), time(T), action(A1), action(A2), A1!=A2.
:- not holds(P, n), but(P), pred(P).

#show perform/2.