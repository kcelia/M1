(define (problem blockProblem)
	(:domain blockWorld)
	(:objects A B C D E F - block)
	(:init 
		;;; Première pile
		(clear B) (ontable C) (on B D) (on D C) 
		;;; Deuxième pile		
		(clear F) (ontable A) (on F E) (on E A) 
		;;; Mains vides		
		(handempty))
	(:goal (and (on A B) (on B C) (on C D) (on D E) (on E F) 
		(ontable F) (clear A) (handempty)))
)
