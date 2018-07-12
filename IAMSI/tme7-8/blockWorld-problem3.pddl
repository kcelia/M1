(define (problem blockProblem)
	(:domain blockWorld)
	(:objects A B C D E F G H I J K L M N - block)
	(:init 
		;;; Première pile
		(clear B) (ontable C) (on B D) (on D H) (on H J) (on J I) (on I C) 
		;;; Deuxième pile		
		(clear F) (ontable A) (on F E) (on E A) 
		;;; Troisième pile
		(clear M) (ontable L) (on M K) (on K N) (on N L)
		;;; Mains vides		
		(handempty))
	(:goal (and (on A B) (on B C) (on C D) (on D E) (on E F) 
		(ontable F) (clear A) 
		(on H K) (on K L) (on L M) (on M N) (on N I) (on I J) 
		(ontable J) (clear H)		
		(handempty)))
)
