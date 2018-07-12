(define (domain blockWorld) 
	(:requirements :strips :typing) 
	(:types object)
	(:types block - object support - object) 
	(:predicates
		(on ?x - block ?y - object)
		(clear ?x - object)
	)
	(:constants table - support)
	(:action moveTo
		;;; action qui déplace un block sur un autre
		:parameters (?x - block ?y - object ?z - block)
		:precondition (and (clear ?x) (clear ?z) (on ?x ?y))
		:effect (and (on ?x ?z)
			(clear ?y)
			(not (on ?x ?y))
			(not (clear ?z)))
	)
	(:action moveToTable
		;;; action qui déplace un block sur la table
		:parameters (?x - block ?y - block)
		:precondition (and (on ?x ?y) (clear ?x))
		:effect (and (on ?x table)
			(clear ?y)
			(not (on ?x ?y)))
	)
)
