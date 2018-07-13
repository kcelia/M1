create table J(licence number(10), 
  cnum number(10) not null, 
  salaire number(10)  not null, 
  sport varchar(20)
);

drop table C;

create table C (  
  cnum number(10)  not null, 
  nom varchar(20)  not null,
  division number(1)  not null, 
  ville varchar(20),
  constraint cleC primary key(cnum)
);

@liste



select /*+ use_nl(j,c) index(C I_C_cnum) */ J.licence, C.nom
FROM J, C
where C.cnum = J.cnum
and J.salaire > 10;


desc BigJoueur

select * from BigJoueur where salaire<1;

select /*+ ordered */ *
from BigJoueur b, C
where b.cnum = c.cnum;

select b1.cnum, b1.prenom, b2.prenom
from BigJoueur b1, BigJoueur b2 
where b1.cnum = b2.cnum;

