import java.sql.*;
import java.io.*;


/**
 *  NOM, Prenom 1 : Kherfallah Celia
 *  NOM, Prenom 2 : Fernandez Stieban
 *
 * La classe Joueur
 **/
public class Joueur {
    
    /* Commentaire: Attributs permettant la connexion à la base */
    
    String server = "db-oracle.ufr-info-p6.jussieu.fr";
    String port = "1521";
    String database = "oracle";

    // remplacer 1234567 par votre numéro
    String user = "E3605205";

    // remplacer 1234567 par votre numéro
    String password = "E3605205";
    
    String requete = "select nom, prenom from Joueur";

    Connection connexion = null;
    public static PrintStream out = System.out;    // affichage des résulats à l'ecran
    
    /**
     * methode main: point d'entrée
     **/
    public static void main(String a[]) {

        /* Commentaire: Crée une instance de la classe Joueur et lance une requête en appelant traiteRequete */
        Joueur c = new Joueur();
        
	c.traiteRequete();
    }
    
    /**
     * Constructeur : initialisation
     **/
    protected Joueur(){
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

            /* Commentaire: Connexion à la base */
	    String url = "jdbc:oracle:thin:@" + server + ":" + port + ":" + database;
            connexion = DriverManager.getConnection(url, user, password);
            
            /* Commentaire: Crée une instance de Statement qui va permettre d'éxecuter la requête et obtenir les résultats */
            Statement lecture =  connexion.createStatement();
            
            /* Commentaire: ResultSet va contenir le résultat et permettre de naviguer parmi les lignes du résultat obtenu grâce à un curseur  */
            ResultSet resultat = lecture.executeQuery(requete);
            
            /* Commentaire: Navigation dans le résultat (ResulSet) avec un curseur, next donnant la ligne suivante 
             * On récupère les deux premiers attributs de la ligne et on les affiche en sortie */
            while (resultat.next()) {
                String tuple = resultat.getString(1) + "\t" + resultat.getString(2);
                out.println(tuple);
            }

            /* Commentaire: "Libère l'espace occupé par l'instance de ResultSet qui 
             * stockait le résultat, de même pour le Statement. Puis fermeture de la connexion */
	    resultat.close();
	    lecture.close();
	    connexion.close();
        }

        /* Commentaire: Lève une exception en case d'erreur de connexion */
        catch(Exception e){ Outil.gestionDesErreurs(connexion, e);}
    }
}
