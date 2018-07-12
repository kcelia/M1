
@liste

create type matiere as object(
nom varchar2(10),
prix number,
masse number
);
/
create type piece as object(
nom varchar2(10),
not instantiable member function masse return number,
not instantiable member function prix return number,
not instantiable member function nb_piece_base return number,
not instantiable member function composee_de return number
) not instantiable not final;
/
create  type pieceDeBase under piece (
mat ref matiere,
not instantiable member function volume return number,
overriding  member function masse return number,
overriding  member function prix return number,
overriding  member function nb_piece_base return number,
overriding  member function composee_de return number
)not instantiable not final;
/
create type sphere under pieceDeBase(
rayon number,
overriding member function volume return number
);
/
create type parall under pieceDeBase(
longueur number,
largeur number,
hauteur number,
overriding member function volume return number
);
/
create type cylindre under piecedebase(
hauteur number,
rayon number,
overriding member function volume return number
);
/
create type quantiteDePiece as object (
quantite number,
p ref piece
);
/
create type ensQuantiteDePiece as table of quantiteDePiece ;
/
create  type composite under piece (
cout_assemblage number,
ensp ensQuantiteDePiece,
overriding  member function masse return number,
overriding  member function prix return number,
overriding  member function nb_piece_base return number,
overriding  member function composee_de return number
);
/
---Table
Create table lesmatieres of matiere;
create table lespiecesdebase of piecedebase;
create table lescomposites of composite
nested table ensp store as t1;
--instance
insert into lesmatieres values(matiere('bois',10,2));
insert into lesmatieres values(matiere('fer',5,3));
insert into lesmatieres values(matiere('ferrite',6,10));
--
select value(m)
from lesmatieres m;
---
insert into lespiecesdebase values(parall('plateau',
					       (select ref(m)
       	    		    		        from lesmatieres m
					        where m.nom ='bois'),
						1,100,80)
);
insert into lespiecesdebase values(sphere('boule',( select ref(m)
       	    		    			    from lesmatieres m
						    where m.nom='fer'),
						    30)
);
insert into lespiecesdebase values(sphere('pied',(select ref(m)
       	    		    		          from lesmatieres m
						  where m.nom = 'bois'),
						  30)					
);
insert into lespiecesdebase values(cylindre('canne',(select ref(m)
       	    		    		             from lesmatieres m
						     where m.nom = 'bois'),
						     2, 30 )
);
insert into lespiecesdebase values(cylindre('clou',(select ref(m)
       	    		    		             from lesmatieres m
						     where m.nom = 'fer'),
						    1, 20 )
);						     
insert into lespiecesdebase values(cylindre('aimant',(select ref(m)
       	    		    		             from lesmatieres m
						     where m.nom = 'ferrite'),
						    2,5 )
);						 
insert into lescomposites values(composite('table',100,ensQuantiteDePiece( quantiteDePiece(4, (select ref(p) from lespiecesdebase p where p.nom = 'pied')),
       	    		  						   quantiteDePiece(12, (select ref(p) from lespiecesdebase p where p.nom = 'clou')),
									   quantiteDePiece (1, (select ref(p) from lespiecesdebase p where p.nom = 'plateau'))
									   )
	                                  )
);
insert into lescomposites values(composite('billard',10,ensQuantiteDePiece(quantiteDePiece(1, (select ref(ens) from lescomposites ens  where ens.nom = 'table')),
								   	   quantiteDePiece(3, (select ref(p) from lespiecesdebase p where p.nom = 'boule')),
       	    							           quantitedepiece(2, (select ref(p) from lespiecesdebase p where p.nom = 'canne'))
								    )
				   )
);
@liste

-- Methode:
--M1					
create or replace type body cylindre as
overriding member function volume return number is
res number; 
begin
res := 3.14 * self.rayon * self.rayon * self.hauteur ;
return res;
end;
end;


--teste
select p.volume()
from  lespiecesdebas p
where p.nom = 'canne';



create or replace type body sphere  as
overriding member function volume return number is
res number; 
begin
res := (3.14 * self.rayon * self.rayon *self.rayon)/3  ;
return res;
end;
end;
@liste

create or replace type body parall   as
overriding member function volume return number is
res number; 
begin
res := self.hauteur * self.largeur *self.longueur  ;
return res;
end;
end;

create or replace body  pieceDeBase as
overriding member function masse return number is
res number;
m matiere;
begin
	select deref(self.mat) into m
	from dual ;
	res :=	self.volume()* m.masse;
end;
overriding  member function nb_piece_base return number is
begin
 return 1;
end;
--
end;

