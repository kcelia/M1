/**
 * 
 */
package factory;

import Bouchons.GestJoueurBouchon;
import Bouchons.PaiementBouchon;
import Bouchons.CarteBouchon;
import Carte.GestCarte;
import Interface.IInfoCompte;
import Interface.ICarte;
import Interface.IPaiement;
import Interface.IMoteurJeu;
import Interface.IInfoJoueur;
import Interface.IListeDeCartes;
import Joueur.GestJoueur;

/** 
 * <!-- begin-UML-doc -->
 * <!-- end-UML-doc -->
 * @author 3407485
 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
 */
public class ComposantFactory {

	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @return
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public static IInfoCompte createCInfoCompte() {
		// begin-user-code
		// TODO Module de remplacement de méthode auto-généré
		return null;
		// end-user-code
	}

	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @return
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public static IInfoCompte createCInfoCompteBouchon(IInfoJoueur iInfoJoueur, IPaiement iPaiement) {
		// begin-user-code
		return new GestJoueurBouchon();
		// end-user-code
	}

	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @return
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public static ICarte createCCarte() {
		// begin-user-code
		// TODO Module de remplacement de méthode auto-généré
		return new GestCarte();
		// end-user-code
	}
	
	public static ICarte createCCarteBouchon() {
		return new CarteBouchon();
	}

	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @return
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public static IPaiement createCPaiement() {
		// begin-user-code
		return null;
		// end-user-code
	}
	
	public static IPaiement createCPaiementBouchon() {
		// begin-user-code
		return new PaiementBouchon();
		// end-user-code
	}


	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @return
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public static IMoteurJeu createCMoteurJeu() {
		// begin-user-code
		// TODO Module de remplacement de méthode auto-généré
		return null;
		// end-user-code
	}

	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @param ip
	 * @param ic
	 * @return
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public static IInfoJoueur createCInfoJoueur(IPaiement ip, ICarte ic) {
		// begin-user-code
		return new GestJoueur();
		// end-user-code
	}

	
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @param ip
	 * @param ic
	 * @return
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public static IInfoJoueur createCInfoJoueurBouchon(IPaiement ip, ICarte ic) {
		// begin-user-code
		return new GestJoueurBouchon();
		// end-user-code
	}

	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @return
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public static IListeDeCartes createCListeDeCarte() {
		// begin-user-code
		// TODO Module de remplacement de méthode auto-généré
		return null;
		// end-user-code
	}

	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public static void createNominal() {
		// begin-user-code
		// TODO Module de remplacement de méthode auto-généré

		// end-user-code
	}

	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @param ic
	 * @param ij
	 * @param icarte
	 * @param ip
	 * @param im
	 * @param ilc
	 * @return
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public static Object createIHM(IInfoCompte ic, IInfoJoueur ij,
			ICarte icarte, IPaiement ip, IMoteurJeu im, IListeDeCartes ilc) {
		// begin-user-code
		// TODO Module de remplacement de méthode auto-généré
		return null;
		// end-user-code
	}

	public static IInfoCompte createInfoCompte() {
		return null;
	}
}