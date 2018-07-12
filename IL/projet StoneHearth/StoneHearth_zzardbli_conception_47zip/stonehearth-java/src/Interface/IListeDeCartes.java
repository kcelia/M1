/**
 * 
 */
package Interface;

import java.util.ArrayList;

/** 
 * <!-- begin-UML-doc -->
 * <!-- end-UML-doc -->
 * @author 3407485
 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
 */
public interface IListeDeCartes {
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @param idJoueur
	 * @param liste
	 * @return
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */

	//	public Set<String> listerCartesListe(String idJoueur, String liste);
	
	public ArrayList<String> listerCartesListe();
	
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @param idJoueur
	 * @param deck
	 * @return
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
//	public Boolean verificationDeckEmplacementVide(String idJoueur, String deck);
	public Boolean verificationDeckEmplacementVide();
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @param idJoueur
	 * @param nomCarte
	 * @param liste
	 * @return
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public Boolean ajouterCarteListe(ArrayList<String> nomsCarte);
//	public Set<String> ajouterCarteListe(String idJoueur, String nomCarte,
//			String liste);

	public Boolean ajouterCarte(String nomCarte);
}