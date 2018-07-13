import java.sql.*;
import java.io.*;


/**
 * La classe Outil
 **/
public class Outil {
    
    public static PrintStream out = System.out;    // affichage des résulats à l'ecran
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    
    /* méthodes pour la gestion des erreurs */


    
    /**
     * methode erreurInit: gère les erreurs d'initialisation
     **/
    static void erreurInit(Exception e){
        /* info pour débogage */
        //e.printStackTrace();

        if (e instanceof ClassNotFoundException){
            out.println("pilote introuvable " + e);
            out.println("Exécuter la commande : source config");
        }
	throw new RuntimeException("Arret immediat car erreur d'initialisation");
    }


    /**
     * methode gestionDesErreurs
     **/    
    static void gestionDesErreurs(Connection connexion, Exception e) {
        out.println("Probleme d'acces a la base: " + e);
        
        /* pour facilier le débogage,
           afficher la ligne ou l'erreur s'est produite*/
        e.printStackTrace();
        
        /* En cas de pb d'acces, on ferme la connexion */
        try {
            if (connexion != null)
                connexion.close();
        }
        catch(Exception se) {
            out.println("Tout autre probleme: " + se);
        }
        throw new RuntimeException("Arret immediat");
    }


    static String lireValeur(String message) throws Exception{
	out.println("");
	out.println(message);
	return in.readLine();
    }
    
}
