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
public class MaxPrime2 {

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
        MaxPrime2 c = new MaxPrime2();
        c.traiteRequete();
    }
 
   
    /**
     * Constructeur : initialisation
     **/
    private MaxPrime2(){
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
            
        String requete = "select nom, max(prime) from Gain g, Joueur j"
		+ " where g.nujoueur = j.nujoueur and annee = ? group by nom";
        PreparedStatement lecture =  connexion.prepareStatement(requete);
        
	    while(true){
	    	try{
	    		String val = Outil.lireValeur("Saisir une annee");
	    		lecture.setInt(1, Integer.parseInt(val));
			    /* Commentaire:  */
			    out.println("statement...");
			    out.println("execute la requete : " + requete);
		        ResultSet resultat = lecture.executeQuery();
		            
			    out.println("resultat...");
		        while (resultat.next()) {
		        	String tuple = resultat.getString(1) + "\t" + resultat.getString(2);
		            out.println(tuple);
	            }
		        resultat.close();
	    	}catch (NumberFormatException e){
	    		out.println(e);
	    		out.println("Fin des requetes");
	    		break;
	    	}
	    }
	    
	    
	    lecture.close();
	    connexion.close();
        }

        /* getion des exceptions */
        catch(Exception e){ Outil.gestionDesErreurs(connexion, e);}
    }
}
