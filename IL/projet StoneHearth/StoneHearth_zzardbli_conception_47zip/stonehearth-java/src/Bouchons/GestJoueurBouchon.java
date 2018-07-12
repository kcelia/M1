package Bouchons;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;

import Interface.IInfoCompte;
import Interface.IInfoJoueur;
import Interface.IListeDeCartes;
import Interface.IPartie;
import Joueur.CoordonneesBancaires;
import ListeDeCartes.GestListeDeCartes;

public class GestJoueurBouchon implements IInfoJoueur, IInfoCompte {

	private String idJoueur;
	private Integer nb_joyaux;
	private Integer rang;
	private Integer nb_pack;
	private String motDePasse;
	private CoordonneesBancaires coordonneesBancaires;
	private ArrayList<IListeDeCartes> decks;
	private ArrayList<IPartie> historique;
	private Boolean isConnected;
	private IListeDeCartes collection;
	
	
	public GestJoueurBouchon() {
		idJoueur = "Bob";
		nb_joyaux = 37;
		rang = 35;
		nb_pack = 5;
		motDePasse = "MonSuperMotDePasse";
		isConnected = false;
		collection = new GestListeDeCartes();
	}

	@Override
	public Boolean estConnecte(String idJoueur, String mdp) {
		return true;
	}

	@Override
	public Boolean acheterEmplacementDeckPack(String idJoueur, Boolean isPack) {
		return true;
	}

	@Override
	public Boolean enregistrerCB(String idJoueur, String nom, Integer numero,
			Date dateExpiration, String cvv) {
		return true;
	}

	@Override
	public Boolean enregistrerDonnees(String idJoueur, String motDePasse) {
		return true;
	}

	@Override
	public String getCoordonneesBancaires(String idJoueur) {
		return null;
	}

	@Override
	public Boolean seConnecter(String idJoueur, String pass) {
		if (idJoueur.equals(this.idJoueur) && pass.equals(this.motDePasse)) {
			isConnected = true;
			return true;
		}
		return false;
	}
	
	@Override
	public Boolean seDeconnecter(String idJoueur) {
		if (isConnected) {
			isConnected = false;
			return true;
		}
		return false;
	}

	@Override
	public Boolean disponiblePseudo(String pseudo) {
		return true;
	}

	@Override
	public ArrayList<IListeDeCartes> listerDeckJoueur(String idJoueur) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public int majSoldejoyaux(String idJoueur, String nomCarte) {
		return 0;
	}

	@Override
	public ArrayList<Integer> destructionCarte(String idJoueur, String nomCarte) {
		return new ArrayList<Integer>(Arrays.asList(39, 1));
	}

	@Override
	public void donnerPack(String id) {
		// TODO Module de remplacement de méthode auto-généré
		
	}

	@Override
	public Boolean VerificationAttributionPack(String id) {
		return true;
	}

	@Override
	public Boolean verifierSoldeJoyaux(String idJoueur, String nomCarte) {
		return true;
	}

	@Override
	public Integer acheterCarte(String idJoueur, String nomCarte) {
		collection.ajouterCarte(nomCarte);
		return 17;
	}

	@Override
	public Integer getRang(String idJoueur) {
		return 35;
	}

	@Override
	public IListeDeCartes getCollection(String idJoueur) {
		return collection;
	}

	@Override
	public Boolean actualiserRang(String idJoueur, Boolean aGagne) {
		return true;
	}

	@Override
	public int getNumberOfPacks(String idJoueur) {
		return 0;
	}

	@Override
	public ArrayList<String> ouvrirPack(String idJoueur) {
		return new ArrayList<String>(Arrays.asList("","","","",""));
	}

	@Override
	public int getNb_joyaux(String idJoueur) {
		return nb_joyaux;
	}
}
