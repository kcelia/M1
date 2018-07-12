(define (domain blockWorld) 
	(:requirements :strips :typing) 
	(:types block) 
	(:predicates
		(on ?x - block ?y - block)
		(ontable ?x - block)
		(clear ?x - block)
		(handempty)
		(holding ?x - block)
	)
	(:action pickup
		;;; action qui ramasse un block pose sur la table
		:parameters (?x - block)
		:precondition (and (clear ?x) (ontable ?x) (handempty))
		:effect (and (not (ontable ?x))
			(not (clear ?x))
			(not (handempty))
			(holding ?x))
	)
	(:action putdown
		;;; action qui pose un block sur la table
		:parameters (?x - block)
		:precondition (holding ?x)
		:effect (and (ontable ?x)
			(handempty)
			(clear ?x)
			(not (holding ?x)))
	)
	(:action stack
		;;; action qui empile un block sur un autre bloc
		:parameters (?x - block ?y - block)
		:precondition (and (clear ?y) (holding ?x))
		:effect (and (on ?x ?y)
			(clear ?x)
			(handempty)
			(not (clear ?y))
			(not (holding ?x)))
	)
	(:action unstack
		;;; action qui dépile un block sur un autre block
		:parameters (?x - block ?y - block)
		:precondition (and (on ?x ?y) (clear ?x) (handempty))
		:effect (and (clear ?y)
			(holding ?x)
			(not (on ?x ?y))
			(not (clear ?x))
			(not (handempty)))
	)
)
