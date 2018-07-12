;;; IAMSI 2018 : séance TME 3 EXO3
;;; mycin.clp

; Binome: Stieban Fernandez / Celia Kherfallah 


; On considere dans ce qui suit que  
; tache rouge == rougeur
; pustule == erruption cutanée
; amydales == gongllion 
; question 3 : il active la regle qui a le plus de premisse, en cas d'egalité il prend le fait plus recent 
; question 4 : clips utilise un chainage avant.
; La maladie diagnostiquée est la rougeole 


; main dans CLIPS

(defrule my_init
	 (initial-fact)
	 

=>
	(watch facts)
	(watch rules)

	(assert (rougeur patient))
	(assert (peu_bouton patient))
	(assert (froid patient))
	(assert (forte_fievre patient))
	(assert (douleur_yeux patient))
	(assert (amydales_rouges patient))
	(assert (peau_seche patient))
	(assert (peau_pele patient))

)

; Eruption cutanee si le patient a peu ou bcp de bouton 

(defrule R1Eruptioncutanee1
	 (peu_bouton ?patient)
=>
	(assert (eruption_cutanee ?patient ))
)
;

(defrule R2Eruptioncutanee2
	 (bcp_bouton ?patient)
=>
	(assert (eruption_cutanee ?patient ))
)
;

; Le patient a un exanthéme s il a des eruptions cutanées ou des rougeurs 

(defrule R3exantheme
	 (eruption_cutanee ?patient)
=>
	(assert (exantheme ?patient ))
)
;

(defrule R4exantheme
	 (rougeur ?patient)
=>
	(assert (exantheme ?patient ))
)
;

; état febrile s il a des fortes fievre ou sil ressent une sensation de froid 

(defrule R5febrile
	(forte_fievre ?patient)
=>
	(assert( febrile ?patient))
)

(defrule R6febrile
	(froid ?patient)
=>
	(assert( febrile ?patient))
)

; etat suspect = avoir des amydales rouges + taches rouges et la peau qui pele 


(defrule R6etat_suspect
	(amydales_rouges ?patient)
	(rougeur ?patient)
	(peau_pele ?patient)
=>
	(assert( etat_suspect ?patient))
)



(defrule R7notrougeole
	
	(peu_fievre ?patient)
	(peu_boutons ?patient)
=>
	(assert(notRougeole ?patient))
)

; rougeole 

(defrule R8rougeole
	
	(febrile ?patient)
	(douleur_yeux ?patient)
	( exantheme ?patient)
	( not ( notRougeole ?patient) )
=>
	(assert( rougeole ?patient))
)

(defrule R9rougeole
	
	(etat_suspect ?patient)
	(forte_fievre ?patient)
	( not ( notRougeole ?patient) )
=>
	(assert( rougeole ?patient))
)



;on releve une douleur si le patient a des douleurs au dos ou douleurs aux yeux_douloureux

(defrule R10Douleur1

	(douleur_yeux ?patient)
	
=> 
	(assert (douleur ?patient))
)
(defrule R11Douleur2
	(douleur_dos ?patient)
	
	
=> 
	(assert (douleur ?patient))
)


(defrule R12grippe 
		(douleur_dos ?patient)
		(febrile ?patient)
		
=>
		(assert(grippe ?patient))
)

(defrule R13varicelle 
		(forte_demangeaisons ?patient)
		(eruption_cutanee ?patient)	
=>
		(assert(varicelle ?patient)))

(defrule R14rubeole
		(peau_seche ?patient)
		(amydales_rouges ?patient)
		(not(eruption_cutanee ?patient))
		(not(froid ?patient))
=>
		(assert (rubeole ?patient))
)

; si pas de rougeloe on peut diagnostiqué la rubéole et la varicelle

(defrule R15rubeole_varicelle
	( notRougeole ?patient )
=>
	(assert(rubeole_varicelle ?patient))
	(assert(rubeole_varicelle ?patient))
)


; ----- fin fichier mycin.clp
