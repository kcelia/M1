
import java.sql.*;
import java.io.*;


/**
 *  NOM, Prenom 1 : KHERFALLAH Celia
 *  NOM, Prenom 2 : FERNANDEZ Stieban
 *  Binome        :
 *  Groupe        :
 *
 * La classe GeneriqueXHTMLf
 **/
public class GeneriqueXHTML {
    
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

        /* initialisation */
        GeneriqueXHTML c = new GeneriqueXHTML();
        
	/* requete */
	c.traiteRequete(requete);
    }
    
    /**
     * Constructeur : initialisation
     **/
    private GeneriqueXHTML(){
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
            
    	    out.println("<html>\n<title>Résultat</title></head>\n<body>");
    	    out.println("<h1>La requete est : </h1>" + requete);
    	    out.println("<h3>Le resultat est : </h3>");
    	    out.println("<table border='2'>");
    	    out.print("<tr>");
    	    for(int i=1; i <= rsmd.getColumnCount(); i++){
    	    	out.print("<th>" + rsmd.getColumnName(i) + "</th>");
    	    }
    	    out.println("</tr>");
 
            while (resultat.next()) {
            	out.print("<tr>");
            	for(int i=1; i <= rsmd.getColumnCount(); i++){
            		out.print("<td>" + resultat.getString(i) + "</td>");
            	}
            	out.println("</tr>");
            }
            
            out.println("</table>\n</body>\n</html>");
            
    	    resultat.close();
    	    lecture.close();
    	    connexion.close();
	    


        }

        /* getion des exceptions */
        catch(Exception e){ Outil.gestionDesErreurs(connexion, e);}
    }
}
