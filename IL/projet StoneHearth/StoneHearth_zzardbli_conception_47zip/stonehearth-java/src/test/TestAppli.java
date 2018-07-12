package test;

import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.ArrayList;

import org.junit.Test;

import factory.ComposantFactory;
import Carte.Carte;
import Interface.ICarte;
import Interface.IInfoCompte;
import Interface.IInfoJoueur;
import Interface.IListeDeCartes;
import Interface.IPaiement;
import ListeDeCartes.GestListeDeCartes;

public class TestAppli {

	/*	@Test
		public void test() {
		
			/**IInfoCompte ic = ComposantFactory.createInfoCompte();
			ic.setIsConnected(true);
			
			IListeDeCartes coll = ComposantFactory.createCollection();
			
			ICarte dico =  ComposantFactory.createDico();
			
			for (String c : coll.listerCartesListe("toto", "coll")) {
				System.out.println(dico.infosCarte(c));
			}
		}
	*/
	@Test
	public void testDetruireCarte() {
		// Ligne de vie
		IPaiement ip = ComposantFactory.createCPaiementBouchon();
		ICarte iCarte = ComposantFactory.createCCarteBouchon(); // retourné le nombre de joyau
		IInfoJoueur iInfoJoueur = ComposantFactory.createCInfoJoueurBouchon(ip, iCarte);
		String idJoueur = "Bob";
			
		IListeDeCartes collection = iInfoJoueur.getCollection(idJoueur);
		Carte carteChat = iCarte.infosCarte("Chat");
		
		// Le joueur clique sur la carte chat
		int prix=iCarte.getPrixVente(carteChat.getNomCarte());
		int soldeInitJoyau = iInfoJoueur.getNb_joyaux(idJoueur);
		
		ArrayList<Integer> retour = iInfoJoueur.destructionCarte(idJoueur, carteChat.getNomCarte());
		assertEquals(retour.get(1), new Integer(1));
		assertEquals(retour.get(0), new Integer(soldeInitJoyau + prix));
		assertFalse(collection.listerCartesListe().contains(carteChat.getNomCarte()));
	}
	

	@Test
	public void testAcheterCarte() {
		ICarte iCarte = ComposantFactory.createCCarteBouchon(); // gestionnaire de cartes initialisé avec 6 cartes
		IInfoJoueur iInfoJoueur = ComposantFactory.createCInfoJoueurBouchon(null, iCarte);// le joueur qu'on veut tester 
		String idJoueur = "Bob";
		
		// le bouchon contient 6 cartes, on essaye d'acheter la 1ère de la liste
		// la fonction acheterCarte : 	appelle la fonction ip.payer(iInfoJoueur.getName(),iCarte.listerCartes().get(0)); 
		String nomCarte = iCarte.listerCartes().get(0);
		int soldeInitJoyau = iInfoJoueur.getNb_joyaux(idJoueur);
		int soldeRestantJoyau = iInfoJoueur.acheterCarte(idJoueur, nomCarte);
				
		int prix = iCarte.getPrixAchat(nomCarte);
		
		assertEquals(soldeInitJoyau - prix, soldeRestantJoyau);
		
		// pour verifier que le carte a bien été ajouté a la collection 
		// le vrai teste c'est assertEquals(iInfoJoueur.getCollection(iInfoJoueur.getName()).contains(iCarte.getNomCarte()), true);
		// comme on a mis des valeurs a la con dans le bouchon, la carte voleuse ... a été supprimé 
		assertEquals(iInfoJoueur.getCollection(idJoueur).listerCartesListe().contains(nomCarte), true);
	}
	

	@Test
	public void testAcheterEmplacementDeckPack() {
	    // Initialisation des lignes de vies
	    IInfoCompte infoCompte = ComposantFactory.createCInfoCompte();
	    IPaiement paiement = ComposantFactory.createCPaiement();
	    IInfoJoueur infoJoueur = ComposantFactory.createCInfoJoueur(paiement, null); //car pas de carte requise dans le diagramme de séquence
	    String idJoueur = "Bob";
	    
	    int n = infoJoueur.listerDeckJoueur(idJoueur).size();
	    infoCompte.acheterEmplacementDeckPack(idJoueur, false);
	    assertEquals(infoJoueur.listerDeckJoueur(idJoueur).size(), n+1);
	}
	
	
	@Test
	public void testAjouterCoordonneesBancaires() {
	
	}
	
/*	
	@Test
	public void testComposerDeck() {
	//ligne de vie
	IPaiement ip = ComposantFactory.createCPaiement();
	ICarte iCarte = ComposantFactory.createCCarte();
	IInfoJoueur iInfoJoueur = ComposantFactory.createCInfoJoueur(ip, iCarte);

	IListeDeCartes coll = ComposantFactory.createCListeDeCarte();
	
	for (String d : iInfoJoueur.listerDeckJoueur("Bob")) {
		System.out.println(d);
	}
	// le joueur choisit le deck D1
	for (String c : coll.listerCartesListe("Bob", "D1")) {
		System.out.println(c);
	}
	
	ArrayList<String> collection = iInfoJoueur.getCollection("Bob");
	for (String c : coll.listerCartesListe("Bob", "collection")) {
		System.out.println(c);
	}
		
	//le joueur clique sur la carte chat
	System.out.println(iCarte.infosCarte("chat"));
	
	Boolean vide= coll.verificationDeckEmplacementVide("Bob","D1");
	if (vide) {
		for(String c : coll.ajouterCarteListe("Bob", "chat", "D1")){
			System.out.println(c);
		}
	}
	else System.out.println("Vous n'avez plus de place dans votre deck.");
	
	}
	
*/
	public void testComposerDeck() {
		ICarte iCarte = ComposantFactory.createCCarteBouchon();
		IInfoJoueur iInfoJoueur = ComposantFactory.createCInfoJoueurBouchon(null, iCarte);
		String idJoueur = "Bob";
		IListeDeCartes coll = iInfoJoueur.getCollection(idJoueur);
		IListeDeCartes D1 = iInfoJoueur.listerDeckJoueur(idJoueur).get(0);
	
		// On vérifie que la collection contient la carte "chat" et le deck ne la contient pas
		assertFalse(D1.listerCartesListe().contains("chat"));
		assertTrue(coll.listerCartesListe().contains("chat"));
		
		// On ajoute la carte "chat" au deck
		D1.ajouterCarteListe(new ArrayList<String>(Arrays.asList("chat")));
	
		// On vérifie que la collection contient toujours la carte "chat" et que le deck la contient aussi
		assertTrue(D1.listerCartesListe().contains("chat"));
		assertTrue(coll.listerCartesListe().contains("chat"));
	}
	
	@Test
	public void testInscription() {
	
	}
	
	
	@Test
	public void testJouer() {
	
	}
	
	
	@Test
	public void testSeConnecter() {
		IInfoCompte iInfoCompte = ComposantFactory.createCInfoCompteBouchon(null, null);

		assertTrue(iInfoCompte.seConnecter("Bob", "MonSuperMotDePasse"));
		assertFalse(iInfoCompte.seConnecter("Bob", "MonFauxMotDePasse"));
	}
	
	
	@Test
	public void testSeDeconnecter() {
		IInfoCompte iInfoCompte = ComposantFactory.createCInfoCompteBouchon(null, null);
		
		// On connecte le joueur
		iInfoCompte.seConnecter("Bob", "MonSuperMotDePasse");
		
		assertTrue(iInfoCompte.seDeconnecter("Bob"));
	}
	
	
	@Test
	public void testOuvrirPack() {
	    // Initialisation des lignes de vies
	    IInfoJoueur infoJoueur = ComposantFactory.createCInfoJoueurBouchon(null, null);
	    
	    String idJoueur = "Bob";
	    IListeDeCartes collection = infoJoueur.getCollection(idJoueur);
		
	    ArrayList<String> cartes = infoJoueur.ouvrirPack(idJoueur);
	    for (String carte: cartes) {
	    	assertTrue(carte.equals(""));
	    }
	    
	    infoJoueur.donnerPack(idJoueur);
	    
	    cartes = infoJoueur.ouvrirPack(idJoueur);
	    for (String carte: cartes) {
	    	assertTrue(carte.equals(""));
	    	assertTrue(collection.listerCartesListe().contains(carte));
	    }
	    
	}
}