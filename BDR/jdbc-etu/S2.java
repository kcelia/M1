import java.sql.*;
import java.io.*;


/**
 *  NOM, Prenom 1 :
 *  NOM, Prenom 2 :
 *
 * La classe Joueur
 **/
public class S2 {
    
    /* Commentaire: */
    
    String server = "oracle.ufr-info-p6.jussieu.fr";
    String port = "1521";
    String database = "ora10";
    String user = "anonyme";
    String password = "anonyme";
    String requete = "select count(*) as nb from Sponsor";

    Connection connexion = null;
    public static PrintStream out = System.out;    // affichage des résulats à l'ecran
    
    /**
     * methode main: point d'entrée
     **/
    public static void main(String a[]) {

        /* Commentaire: */
        S2 c = new S2();
        
	c.traiteRequete();
    }
    
    /**
     * Constructeur : initialisation
     **/
    protected S2(){
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
     *  Commentaire :
     *
     */
    public void traiteRequete() {
        try {

            /* Commentaire: */
	    String url = "jdbc:oracle:thin:@" + server + ":" + port + ":" + database;
            connexion = DriverManager.getConnection(url, user, password);
            
            /* Commentaire: */
            Statement lecture =  connexion.createStatement();
            
            /* Commentaire: */
            ResultSet resultat = lecture.executeQuery(requete);
            
            /* Commentaire: */
            while (resultat.next()) {
                String tuple = resultat.getString(1) ;
                out.println(tuple);
            }

            /* Commentaire: */
	    resultat.close();
	    lecture.close();
	    connexion.close();
        }

        /* Commentaire: */
        catch(Exception e){ Outil.gestionDesErreurs(connexion, e);}
    }
}
