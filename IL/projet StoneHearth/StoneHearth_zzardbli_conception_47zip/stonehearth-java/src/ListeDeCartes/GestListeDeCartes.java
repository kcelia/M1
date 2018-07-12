/**
 * 
 */
package ListeDeCartes;

import Interface.IListeDeCartes;

import java.util.ArrayList;

/** 
 * <!-- begin-UML-doc -->
 * <!-- end-UML-doc -->
 * @author 3407485
 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
 */
public class GestListeDeCartes implements IListeDeCartes {
	
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private ArrayList<String> cartes;
	
	
	public GestListeDeCartes() {
		cartes = new ArrayList<String>();
	}

	/** 
	 * (non-Javadoc)
	 * @see IListeDeCartes#listerCartesListe(String idJoueur, String liste)
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public ArrayList<String> listerCartesListe() {
		return new ArrayList<String>(cartes);
	}

	/** 
	 * (non-Javadoc)
	 * @see IListeDeCartes#verificationDeckEmplacementVide(String idJoueur, String deck)
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public Boolean verificationDeckEmplacementVide() {
		return cartes.size() < 30;
	}

	/** 
	 * (non-Javadoc)
	 * @see IListeDeCartes#ajouterCarteListe(String idJoueur, String nomCarte, String liste)
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public Boolean ajouterCarteListe(ArrayList<String> liste) {
		if (cartes.addAll(liste)) return true;
		return false;
	}

	public Boolean ajouterCarte(String carte) {
		if (cartes.add(carte)) return true;
		return false;
	}
}