(define (domain singeBananes)
	(:requirements :strips :typing)
	(:types entity place level)
	(:types actor - entity obj - entity)
	(:predicates 
		(situe ?x - entity ?y - place) 
		(niveau ?x - entity ?y - level) 
		(possede ?x - actor ?y - obj) 
		(mainsVides))
	(:constants 
		singe - actor 
		bananes - obj
		caisse - obj
		haut - level
		bas - level
		a - place
		b - place
		c - place
	)
	(:action seDeplace
		;;; Le singe se déplace de l'emplacement x à l'emplacement b
		:parameters (?x - place ?y - place)
		:precondition (and (situe singe ?x) (niveau singe bas))
		:effect (and (situe singe ?y)
			(not (situe singe ?x)))
	)
	(:action prend
		;;; Le singe prend l'object X (un seul objet)
		:parameters (?x - obj ?n - level ?p - place)
		:precondition (and (mainsVides) 
				(niveau singe ?n) (situe singe ?p) 
				(niveau ?x ?n) (situe ?x ?p))
		:effect (and (possede singe ?x)
			(not (mainsVides))
			(not (situe ?x ?p))
			(not (niveau ?x ?n)))
	)
	(:action depose
		;;; Le singe dépose l'objet X
		:parameters (?x - obj ?p - place ?n - level)
		:precondition (and (possede singe ?x) (situe singe ?p) (niveau singe ?n))
		:effect (and (mainsVides)
			(situe ?x ?p)
			(niveau ?x ?n)
			(not (possede singe ?x)))
	)
	(:action monteCaisse
		;;; Le singe monte sur la caisse
		:parameters (?p - place)
		:precondition (and (situe singe ?p) (niveau singe bas) 
				(situe caisse ?p) (niveau caisse bas)
				(mainsVides))
		:effect (and (niveau singe haut)
			(not (niveau singe bas)))
	)
)
	
