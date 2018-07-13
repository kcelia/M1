import java.sql.*;
import java.io.*;


/**
 *  NOM, Prenom 1 :
 *  NOM, Prenom 2 :
 *  Binome        :
 *  Groupe        :
 *
 * La classe Sponsor
 **/
public class Sponsor {
    
    /* parametres de connexion */

    String url1 = "jdbc:oracle:thin:@db-oracle.ufr-info-p6.jussieu.fr:1521:oracle"; // base tennis

    // remplacer 1234567 par votre numéro
    String user = "E1234567";

    // remplacer 1234567 par votre numéro
    String password = "E1234567";
    
    Connection connexionTennis = null;

    String url2 = "jdbc:oracle:thin:@oracle.ufr-info-p6.jussieu.fr:1521:ora10"; // base des sponsors
    String user2 ="anonyme";             // acces anonyme
    String password2 ="anonyme";
    Connection connexionSponsor = null;

    static PrintStream out = System.out;    // affichage des resulats a l'ecran
    
    /**
     * methode main: point d'entrée
     **/
    public static void main(String a[]) {
        
        /* initialisation */
        Sponsor c = new Sponsor();
        out.println("here");
        /* test des méthodes que vous avez écrites */
        c.traiteRequete();
    }
    
    /**
     * Constructeur : initialisation
     **/
    private Sponsor(){
        try {
            /* Chargement du pilote JDBC */
	    Class.forName("oracle.jdbc.driver.OracleDriver");
        }
        catch(Exception e) {
            Outil.erreurInit(e);
        }
    }
    
    
    /**
     *  La methode traiteRequete
     *  affiche le resultat d'une requete
     */
    public void traiteRequete() {
        try {
        /* Connexion a la base */
        
        	try {
        	connexionSponsor = DriverManager.getConnection(url2, user, password);
        	out.println("Successfully connected to the SponsorDB");
        	}catch (Exception e ){
        		out.println("Could not find the db1");
        		
        	}
        	try {
        	connexionTennis = DriverManager.getConnection(url1, user, password);
        	out.println("Successfully connected to the TennisDB");
        	}catch (Exception e ){
        		out.println("Could not find the db2");
        		
        	}
        	// sponsor doit etre scrollable

        	Statement statement = connexionSponsor.createStatement
        			(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY);

	    
	    /* à compléter Donner le nom et la nationalité des joueurs avec le nom et la nationalité 
	     * de leurs sponsors, dans l’ordre des noms de joueur*/	
        	
        /* Methode3 tri fussion */
        	
        String requete = "SELECT s.nom, s.nationalite "
        				+ "FROM  Sponsor s ORDER BY s.nom" ;
        
        //PreparedStatement lecture =  connexionSponsor.prepareStatement(requete);
        ResultSet results = statement.executeQuery(requete);
        
        //out.println("Cursor position " + results.getRow() + ", is before first ? " + results.isBeforeFirst());
        /**if (results.next()){
        	out.print(results.getString(1));
        }**/
        /* results.getRow(), results.isFirst(), results.isLast(), results.isLast(),.isAfterLast()*/
        
       /**///Affichage du resultat de la premiere requete 
        /**  while (results.next()) {
        	String tuple = results.getString(1) + "\t" + results.getString(2);
            out.println(tuple);
        }/**/
       
        String requete2 = "SELECT distinct j.nom, j.nationalite , g.Sponsor FROM  Joueur j, Gain g WHERE j.NuJoueur = g.NuJoueur ORDER BY g.Sponsor" ;
        PreparedStatement lecture2 =  connexionTennis.prepareStatement(requete2);
       
        
        ResultSet results2 = lecture2.executeQuery();
        
        /**/// Affichage du resultat de la deuxieme requete */
        /**while (results2.next()) {
      	String tuple = results2.getString(1) + "\t" + results2.getString(2) + "\t" + results2.getString(3);
          out.println(tuple);
      	}/**/
       results.next(); //sinon probleme
        // attention getString commence a 1 et non 0
        results.first();
    
        results.next();
       
        
     while (results2.next()) {
        	String sponsorj = results2.getString(3);
        	//out.println("en premier " + sponsorj);
        	while(results.next()){
        		//out.println("d2 " +results.getString(1));
        		//out.println(sponsorj.equals(results.getString(1) ));
        		if ( sponsorj.equals(results.getString(1) )){
        			out.println ( "Joueur " + results2.getString(1) + " sa nationalité " +  results2.getString(2) +", Sponsor "+
        		        results.getString(1) + " nationalitéS " + results.getString(2) ) ;
        			//results.first();
        			break;
        		}       		
        	}
    		results.first();        	
        }
     
   //methode 1 boucle imbriquée
        
  /*      
    results.first();
    results.next();
     results2 = lecture2.executeQuery();
  out.println("Boucle imbriquée");
  while (results2.next()) {
     	String sponsorj = results2.getString(3);
     	//out.println("en premier " + sponsorj);
     	while(results.next()){
     		//out.println("d2 " +results.getString(1));
     		//out.println(sponsorj.equals(results.getString(1) ));
     		if ( sponsorj.equals(results.getString(1) )){
     			out.println ( "Joueur " + results2.getString(1) + " sa nationalité " +  results2.getString(2) +", Sponsor "+
     		        results.getString(1) + " nationalitéS " + results.getString(2) ) ;
     			//results.first();
     		}
     	}
 		results.first();
     }*/
  
//     out.println("HERe");
        
        
        
        
        
        
        
  //methode 2 prepareStatement, le tri ne sert a rien
     

        
/*

    String requete1 = "SELECT s.nom, s.nationalite " + "FROM  Sponsor s WHERE s.nom = ? " ;
    PreparedStatement lecture1 =  connexionSponsor.prepareStatement(requete1);
    
    
    requete2 = "SELECT distinct j.nom, j.nationalite , g.Sponsor FROM  Joueur j, Gain g WHERE j.NuJoueur = g.NuJoueur ORDER BY g.Sponsor" ;
    lecture2 =  connexionTennis.prepareStatement(requete2); // state
    
    
    results2 = lecture2.executeQuery();
    

    String tmp= " ";
    String nas = " ";
    
    		        			
    while( results2.next()){
    	
    	String sponsorj = results2.getString(3);
    	
    	if (!tmp.equals(sponsorj)){
    		lecture1.setString(1, sponsorj);;
    		
    		ResultSet resultat = lecture1.executeQuery();
    		
        	 while( resultat.next()){
        		 if ( sponsorj.equals(resultat.getString(1) )){
        			 tmp = sponsorj;
        			 nas = resultat.getString(2);
        			 break;
        		 }
        	 }
    		
    	}
    		out.println ( "Joueur " + results2.getString(1) + " sa nationalité " +  results2.getString(2) +", Sponsor "+
     		        tmp + " nationalitéS " + nas ) ;
    	
    }
 
		*/

        /* Fermeture des connexion */
        connexionTennis.close();
        connexionSponsor.close();
        lecture2.close();
        
	}
	/* getion des exceptions */
	catch(Exception e){ gestionDesErreurs(e);}
    }
    
    //---------------------------------------------------------------------
    
    /* méthodes pour la gestion des erreurs */
    
    protected void gestionDesErreurs(Exception e) {
	out.println("Probleme d'acces a la base: " + e);
	
	/* pour facilier le débogage,
	   afficher la ligne ou l'erreur s'est produite*/
	e.printStackTrace();
	
	/* En cas de pb d'acces, on ferme la connexion */
	try {
	    if (connexionTennis != null)
		connexionTennis.close();
	    if (connexionSponsor != null)
		connexionSponsor.close();
	}
	catch(Exception se) {
	    out.println("Tout autre probleme: " + se);
	}
        throw new RuntimeException("Arret immediat");
    }
    
}
