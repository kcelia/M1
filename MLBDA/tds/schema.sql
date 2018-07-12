-- compléter l'entête 
-- ==================

-- NOM    : MARCHAL	
-- Prénom : Louise

-- NOM    : BOURMAUD	
-- Prénom : Alexia

-- Groupe :
-- binome :

-- ================================================

set sqlbl on


-- nettoyer le compte
@vider
-- Définition des types de données
---@liste
---------------Matiere et PieceBase--------------
create type Piece as object(
       nom varchar2(20)
)not final;
/
create type PieceBase;
/
create type ref_piece_qt as object(
       p ref Piece,
       quantite Number(20)
);
/
create type Ens_Piece as table of ref_piece_qt;
/
create type Matiere as object(
       nom varchar2(20),
       prix Number(5),
       masseVol Number(5)
);
/
create type Composite;
/
create type PieceBase under Piece(
       matie Matiere,
       not instanciable Member function volume return Number,
       not instanciable Member function masse return Number,
       not instanciable Member function prix return Number
) not final not instanciable;
/
create type Cylindre under PieceBase(
       hauteur Number(5),
       rayon Number(5),
       Member function volume return Number,
       Member function masse return Number,
       Member function prix return Number       
);
/
create type Sphere under PieceBase(
       rayon Number(5),
       Member function volume return Number,
       Member function masse return Number,
       Member function prix return Number
);
/
create type Cubique under PieceBase(
       cote Number(5),
       Member function volume return Number,
       Member function masse return Number,
       overriding Member function prix return Number
);
/
create type Parallelepipede under PieceBase(
       hauteur Number(5),
       largeur Number(5),
       longueur Number(5),
       Member function volume return Number,
       Member function masse return Number,
       Member function prix return Number
);
/
----------Composite----------
create type Composite under Piece(
       prixFabr Number(5),
       composants Ens_Piece,
       composes Ens_Piece
);
/
-- liste de tous les types créés
@liste
---------STOCKAGE--------
create table LesMatieres of Matiere;
--create table LesPieces of Piece;
create table LesPiecesBase of PieceBase;
create table LesComposites of Composite nested table composants store as nt_c, nested table composes store as nt_co;
--------INSTANCE----------
insert into LesMatieres values ('bois',10,2);
insert into LesMatieres values ('fer',5,3);
insert into LesMatieres values ('ferrite',6,10);
insert into LesPiecesBase values(Cylindre('canne',(Select value(m)
       	    		  			   from LesMatieres m
						   where m.nom='bois'), 30,2));
insert into LesPiecesBase values(Cylindre('clou',(Select value(m)
       	    		  			  from LesMatieres m
						  where m.nom='fer'), 20,1));
insert into LesPiecesBase values(Cylindre('aimant',(Select value(m)
       	    		  			    from LesMatieres m
						    where m.nom='ferrite'), 5,2));
insert into LesPiecesBase values(Parallelepipede('plateau',(Select value(m)
       	    		  			            from LesMatieres m
						            where m.nom='bois'),1 ,100,80));
insert into LesPiecesBase values(Sphere('boule',(Select value(m)
       	    		  			 from LesMatieres m
						 where m.nom='fer'), 30));
insert into LesPiecesBase values(Sphere('pied',(Select value(m)
       	    		  			from LesMatieres m
						where m.nom='bois'), 30));
insert into LesComposites values(Composite('table',100,Ens_Piece(ref_piece_qt((Select ref(pbs)
								 	       from LesPiecesBase pbs
								               where pbs.nom='plateau'),1),
								 ref_piece_qt((Select ref(p)
								 	       from LesPiecesBase p
									       where p.nom='pied'),4),
							         ref_piece_qt((Select ref(p)
								 	       from LesPiecesBase p
									       where p.nom='clou'),12)								 
								 ),Ens_Piece()
					   )
			         );
insert into LesComposites values(Composite('billard',10,Ens_Piece(ref_piece_qt((Select ref(pbs)
								 	       from LesComposites pbs
								               where pbs.nom='table'),1),
								 ref_piece_qt((Select ref(p)
								 	       from LesPiecesBase p
									       where p.nom='boule'),3),
							         ref_piece_qt((Select ref(p)
								 	       from LesPiecesBase p
									       where p.nom='canne'),2)								 
								 ),Ens_Piece()
					   )
			         );					  
insert into table(Select c.composes
       	          from LesComposites c
		  where c.nom='table') values(ref_piece_qt((Select ref(c)
		  			                  from LesComposites c
					                  where c.nom='billard'),1));
--------Requete-----
--R1
Select m.nom, m.prix
from LesMatieres m;
--R2
Select m.nom
from LesMatieres m
where m.prix<=5;
--R3
select p.nom
from LesPiecesBase p
where p.matie.nom='bois';
--R4
select m.nom
from LesMatieres m
where m.nom like '%fer%';
--R5
Select value(q).p.nom
from LesComposites c, table(c.composants) q
where c.nom='billard';
--R6
Select m.nom, (Select Count(*)
       	       from LesPiecesBase p
	       where p.matie.nom=m.nom)
from LesMatieres m;
--R7
Select m.nom
from LesMatieres m
where (Select Count(*)
       	       from LesPiecesBase p
	       where p.matie.nom=m.nom)>=3;
-------Methode-------
--M1
Create type body cylindre as
member function volume return Number is
begin
	return 3.14 * rayon * hauteur;
end;
@compile
Create type body sphere as
member function volume return Number is
begin
	return 3.14*4/3 * rayon * rayon * rayon;
end;
Create type body parallelepipede as
member function volume return Number is
begin
	return hauteur * largeur * longeur;
end;
Create type body cubique as
member function volume return Number is
begin
	return cote * cote *cote;
end;
