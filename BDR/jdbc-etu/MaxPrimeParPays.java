import java.sql.*;
import java.io.*;


/**
 *  NOM, Prenom 1 : Kherfallah Celia
 *  NOM, Prenom 2 : Fernandez Stieban
 *  Binome        :
 *  Groupe        :
 *
 * La classe MaxPrime
 **/
public class MaxPrimeParPays {

    String server = "db-oracle.ufr-info-p6.jussieu.fr";
    String port = "1521";
    String database = "oracle";

   // remplacer 1234567 par votre numéro
    String user = "E3407186";

    // remplacer 1234567 par votre numéro
    String password = "E3407186";

    Connection connexion = null;
    public static PrintStream out = System.out;    // affichage des résulats à l'ecran

    /**
     * methode main: point d'entrée
     **/
    public static void main(String a[]) {
        MaxPrimeParPays c = new MaxPrimeParPays();
        c.traiteRequete();
    }
 
   
    /**
     * Constructeur : initialisation
     **/
    private MaxPrimeParPays(){
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
     *  
     */
    public void traiteRequete() {
        try {
	    String url = "jdbc:oracle:thin:@" + server + ":" + port + ":" + database;
	    out.println("Connexion avec l'URL: " + url);
	    out.println("utilisateur: " + user + ", mot de passe: " + password);
            connexion = DriverManager.getConnection(url, user, password);

	    /* Commentaire:  */
	    String requete = "select nationalite, nom, max(prime) from Gain g, Joueur j"
		+ " where g.nujoueur = j.nujoueur group by (nationalite,nom) order by nationalite";
            
	    /* Commentaire:  */
	    out.println("statement...");
            Statement lecture =  connexion.createStatement();
            
	    out.println("execute la requete : " + requete);
            ResultSet resultat = lecture.executeQuery(requete);
            
	    out.println("resultat...");
	    String nationalite = "";
        while (resultat.next()) {
        	if (!nationalite.equals(resultat.getString(1))) {
        		nationalite = resultat.getString(1);
        		String aff1 = "Nationalite = " + resultat.getString(1) + "\n"
            		+ " JOUEUR | PRIME";
        		out.println(aff1);
        	}
            String aff2 = resultat.getString(2) + "\t" + resultat.getString(3);
            out.println(aff2);
        }
	    resultat.close();
	    lecture.close();
	    connexion.close();
        }

        /* getion des exceptions */
        catch(Exception e){ Outil.gestionDesErreurs(connexion, e);}
    }
}
