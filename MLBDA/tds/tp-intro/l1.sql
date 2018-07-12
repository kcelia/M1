-- MABD TP1 Prise en main de PL/SQL


-- -------------------- binome -------------------------
-- NOM
-- Prenom

-- NOM
-- Prenom
-- -----------------------------------------------------


-- procédure L1


create or replace procedure l1 is
  cursor c is select distinct object_name, object_type, status
  from user_objects
  order by object_name;

  n user_objects.object_name%type;
  t user_objects.object_type%type;
  s user_objects.status%type;

begin
   DBMS_OUTPUT.ENABLE (100000);

   dbms_output.put_line('liste des objets de l''utilisateur'); 
   dbms_output.put_line(rpad('nom', 20, ' ') || rpad('type', 20, ' ') || 'statut'); 
   dbms_output.put_line(rpad('-', 46, '-')); 
   open c;
  loop 
    fetch c into n, t, s;
    exit when c%notfound;
    dbms_output.put_line(rpad(n, 20, '.') || rpad(t, 20, '.') || s); 
  end loop;
  close c;
end;

/
show err
 


-- exécuter la procédure l1:

begin
  l1;
end;
/

