/**
 * 
 */
package Partie;

import Interface.IPartie;
import java.util.Set;
import Interface.IInfoJoueur;
import Interface.IMoteurJeu;
import Interface.IListeDeCartes;

/** 
 * <!-- begin-UML-doc -->
 * <!-- end-UML-doc -->
 * @author 3407485
 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
 */
public class GestPartie implements IPartie {
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private Set<Partie> partie;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private IInfoJoueur[] iInfoJoueur = null;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private IMoteurJeu iMoteurJeu;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private IListeDeCartes[] decks = null;

	/** 
	 * (non-Javadoc)
	 * @see IPartie#TransmettreJoueurMoteur(String id1, String id2, String id1deck, String id2deck)
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public Boolean TransmettreJoueurMoteur(String id1, String id2,
			String id1deck, String id2deck) {
		// begin-user-code
		// TODO Module de remplacement de méthode auto-généré
		return null;
		// end-user-code
	}

	/** 
	 * (non-Javadoc)
	 * @see IPartie#choisirDeck(String idJoueur, String idDeck)
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public Boolean choisirDeck(String idJoueur, String idDeck) {
		// begin-user-code
		// TODO Module de remplacement de méthode auto-généré
		return null;
		// end-user-code
	}

	/** 
	 * (non-Javadoc)
	 * @see IPartie#TrouverAdversaire(String id, Integer rang)
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public String[] TrouverAdversaire(String id, Integer rang) {
		// begin-user-code
		// TODO Module de remplacement de méthode auto-généré
		return null;
		// end-user-code
	}
}