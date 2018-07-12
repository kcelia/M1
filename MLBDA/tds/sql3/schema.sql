-- compléter l'entête 
-- ==================

-- NOM    : kherfallah
-- Prénom : celia


-- ================================================

set sqlbl on


-- nettoyer le compte
@vider

@liste

-- Définition des types de données

prompt

-- creation des types :

CREATE TYPE matiere AS OBJECT
( nom VARCHAR2(10),
kilo INT,
masse INT
);
@compile


CREATE  TYPE piece AS OBJECT 
(nom VARCHAR(20)
)
not final ;
@compile
@liste

CREATE  TYPE piece_base under piece 
(mat REF  MATIERE)
not final ;
@compile
@liste

CREATE TYPE piece_cylindre UNDER piece_base
(r INT, -- rayon 
 h INT -- hauteur 
);
@compile
@liste

CREATE TYPE piece_sphere  UNDER piece_base
( r INT
);
@compile
@liste

CREATE  TYPE ens_piece AS TABLE OF ref piece;
@compile
@liste

CREATE TYPE composite UNDER piece
(
lesEns_pieces  ens_piece
);
@compile
@liste




--creation des tables ";" SUFFIT pas besoin de @compile 

CREATE TABLE Table_piece_base of piece_base;
@liste

CREATE TABLE Table_composite of Composite
NESTED TABLE lesEns_pieces STORE AS nt_lesEn_pieces;
@liste

CREATE  TABLE table_matiere OF matiere;
@liste



-- inserer des elements dans la table matiere
INSERT INTO table_matiere VALUES (matiere('bois',10,2));


INSERT INTO table_matiere VALUES (matiere('fer',5,3));


INSERT INTO table_matiere VALUES (matiere('ferrite',21,8));


INSERT INTO table_matiere VALUES (matiere('ferrite',6,4));


-- AFFICHAGE DE LA TABLE_MATIERE

--  



SELECT  *
FROM table_matiere m;



INSERT INTO table_piece_base VALUES
(piece_base('boule1',( SELECT REF(M)
  		       FROM table_matiere m
		       WHERE M.kilo =6 AND M.masse=4)
	     )
);


INSERT INTO table_piece_base VALUES
(piece_base('boule5',( SELECT REF(M)
  		       FROM table_matiere m
		       WHERE M.kilo =10 AND M.masse=2)
	     )
);


INSERT INTO table_piece_base VALUES
(piece_base('boule3',( SELECT REF(M)
  		       FROM table_matiere m
		       WHERE M.kilo =21 AND M.masse=8)
	     )
);


SELECT value(t) ,DeReF(mat)
FROM table_piece_base t;



desc  table_composite

INSERT INTO table_composite VALUES
( Composite ('c1', ens_piece(( SELECT REF(p)
  	    	   	      FROM table_piece_base p
			      where p.nom = 'boule5'), ( SELECT REF(p)
  	    	   	      FROM table_piece_base p
			      where p.nom = 'boule3')
                            )
             )
);

SELECT *
FROM table_composite ;

@liste
