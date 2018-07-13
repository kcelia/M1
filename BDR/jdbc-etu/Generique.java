import java.sql.*;
import java.io.*;


/**
 *  NOM, Prenom 1 : KHERFALLAH Celia
 *  NOM, Prenom 2 : FERNANDEZ Stieban
 *  Binome        :
 *  Groupe        :
 *
 * La classe Generique
 **/
public class Generique {
    
    /* les attributs */
    
    String server = "db-oracle.ufr-info-p6.jussieu.fr";
    String port = "1521";
    String database = "oracle";

    // remplacer 1234567 par votre numéro
    String user = "E3407186";

    // remplacer 1234567 par votre numéro
    String password = "E3407186";
    
    Connection connexion = null;
    static PrintStream out = System.out;    // affichage des résulats à l'ecran
    
    /**
     * methode main: point d'entrée
     **/
    public static void main(String param[]) {

	if (param.length == 0) {
	    throw new RuntimeException("Pas de  requete, arret immediat");
	}


	/* requete */
	String requete = param[0];
	out.println("La requete est " + requete);

        /* initialisation */
        Generique c = new Generique();
        
	/* requete */
	c.traiteRequete(requete);
    }
    
    /**
     * Constructeur : initialisation
     **/
    private Generique(){
        try {

            /* Chargement du pilote JDBC */
	    /* driver Oracle */
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
    public void traiteRequete(String requete) {
        try {
        	String url = "jdbc:oracle:thin:@" + server + ":" + port + ":" + database;
            connexion = DriverManager.getConnection(url, user, password);
        	
            Statement lecture =  connexion.createStatement();
            ResultSet resultat = lecture.executeQuery(requete);
            ResultSetMetaData rsmd = resultat.getMetaData();
            
    	    out.println("resultat...");
    	    for(int i=1; i <= rsmd.getColumnCount(); i++){
    	    	out.print(rsmd.getColumnName(i) + "\t");
    	    }
    	    out.println();
    	    for(int i=0; i < rsmd.getColumnCount(); i++){
    	    	out.print("----------");
    	    }
    	    out.println();
            while (resultat.next()) {
            	String tuple = "";
            	for(int i=1; i <= rsmd.getColumnCount(); i++){
            		tuple += resultat.getString(i) + "\t";
            	}
                out.println(tuple);
            }
    	    resultat.close();
    	    lecture.close();
    	    connexion.close();
	    


        }

        /* getion des exceptions */
        catch(Exception e){ Outil.gestionDesErreurs(connexion, e);}
    }
}
