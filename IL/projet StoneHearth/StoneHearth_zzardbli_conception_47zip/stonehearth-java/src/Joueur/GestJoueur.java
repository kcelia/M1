/**
 * 
 */
package Joueur;

import Interface.IInfoJoueur;
import Interface.IInfoCompte;
import Interface.IListeDeCartes;

import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.Set;

import Interface.ICarte;
import Interface.IPaiement;

/** 
 * <!-- begin-UML-doc -->
 * <!-- end-UML-doc -->
 * @author 3407485
 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
 */
public class GestJoueur implements IInfoJoueur, IInfoCompte {

	@Override
	public Boolean estConnecte(String idJoueur, String mdp) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public Boolean acheterEmplacementDeckPack(String idJoueur, Boolean isPack) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public Boolean enregistrerCB(String idJoueur, String nom, Integer numero,
			Date dateExpiration, String cvv) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public Boolean enregistrerDonnees(String idJoueur, String motDePasse) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public String getCoordonneesBancaires(String idJoueur) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public Boolean seConnecter(String idJoueur, String pass) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}
	
	public Boolean seDeconnecter(String idJoueur) {
		return null;
	}

	@Override
	public Boolean disponiblePseudo(String pseudo) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public ArrayList<IListeDeCartes> listerDeckJoueur(String idJoueur) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public int majSoldejoyaux(String idJoueur, String nomCarte) {
		// TODO Module de remplacement de méthode auto-généré
		return 0;
	}

	@Override
	public ArrayList<Integer> destructionCarte(String idJoueur, String nomCarte) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public void donnerPack(String id) {
		// TODO Module de remplacement de méthode auto-généré
		
	}

	@Override
	public Boolean VerificationAttributionPack(String id) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public Boolean verifierSoldeJoyaux(String idJoueur, String nomCarte) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public Integer acheterCarte(String idJoueur, String nomCarte) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public Integer getRang(String idJoueur) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public IListeDeCartes getCollection(String idJoueur) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public Boolean actualiserRang(String idJoueur, Boolean aGagne) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public int getNumberOfPacks(String idJoueur) {
		// TODO Module de remplacement de méthode auto-généré
		return 0;
	}

	@Override
	public ArrayList<String> ouvrirPack(String idJoueur) {
		// TODO Module de remplacement de méthode auto-généré
		return null;
	}

	@Override
	public int getNb_joyaux(String idJoueur) {
		// TODO Module de remplacement de méthode auto-généré
		return 0;
	}

}