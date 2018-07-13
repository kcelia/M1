import java.io.PrintStream;
import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.ResultSet;


public class Schema {
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
    public static void main(String param[]) {
        Schema c = new Schema();
    	if (param.length == 0) {
    	    throw new RuntimeException("Pas de  requete, arret immediat");
    	}
        
    	String relation = param[0];
        
        c.donneInfos(relation);
    }
    
    
    /**
     * Constructeur : initialisation
     **/
    public Schema(){
        try {

            /* Chargement du pilote JDBC */
	    Class.forName("oracle.jdbc.driver.OracleDriver");
        }
        catch(Exception e) {
            Outil.erreurInit(e);
        }
    }
    
    public void donneInfos(String relation) {
        try {
	    String url = "jdbc:oracle:thin:@" + server + ":" + port + ":" + database;
	    out.println("Connexion avec l'URL: " + url);
	    out.println("utilisateur: " + user + ", mot de passe: " + password);
        connexion = DriverManager.getConnection(url, user, password);
        DatabaseMetaData dm = connexion.getMetaData();
        
        out.println("Le schéma de " + relation + "est :");
        out.println("NOM\t\tTYPE");
        out.println("----------------------------");
        ResultSet rs = dm.getColumns(null, null, relation, null);
		while (rs.next()) {
            String tuple = rs.getString("COLUMN_NAME") + "\t" + rs.getString("TYPE_NAME");
            out.println(tuple);
        }
   
        

	    rs.close();
	    connexion.close();
        }

        /* getion des exceptions */
        catch(Exception e){ Outil.gestionDesErreurs(connexion, e);}
    }
}
