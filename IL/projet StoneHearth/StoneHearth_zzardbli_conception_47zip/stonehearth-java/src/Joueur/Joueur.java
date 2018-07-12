/**
 * 
 */
package Joueur;

import java.util.ArrayList;
import java.util.Set;

import Interface.IListeDeCartes;
import Interface.IPartie;

/** 
 * <!-- begin-UML-doc -->
 * <!-- end-UML-doc -->
 * @author 3407485
 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
 */
public class Joueur {
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private String idJoueur;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private Integer nb_joyaux;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private Integer rang;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private Integer nb_pack;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private String motDePasse;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private CoordonneesBancaires coordonneesBancaires;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private ArrayList<IListeDeCartes> decks;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private ArrayList<IPartie> historique;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private Boolean isConnected;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private IListeDeCartes collection;
	
	public String getIdJoueur() {
		return idJoueur;
	}
	
	public void setIdJoueur(String idJoueur) {
		this.idJoueur = idJoueur;
	}
	
	public Integer getNb_joyaux() {
		return nb_joyaux;
	}
	public void setNb_joyaux(Integer nb_joyaux) {
		this.nb_joyaux = nb_joyaux;
	}
	
	public Integer getRang() {
		return rang;
	}
	
	public void setRang(Integer rang) {
		this.rang = rang;
	}
	
	public Integer getNb_pack() {
		return nb_pack;
	}
	
	public void setNb_pack(Integer nb_pack) {
		this.nb_pack = nb_pack;
	}
	
	public String getMotDePasse() {
		return motDePasse;
	}
	
	public void setMotDePasse(String motDePasse) {
		this.motDePasse = motDePasse;
	}
	
	public CoordonneesBancaires getCoordonneesBancaires() {
		return coordonneesBancaires;
	}
	
	public void setCoordonneesBancaires(CoordonneesBancaires coordonneesBancaires) {
		this.coordonneesBancaires = coordonneesBancaires;
	}
	
	public ArrayList<IListeDeCartes> getDecks() {
		return decks;
	}
	
	public void setDecks(ArrayList<IListeDeCartes> decks) {
		this.decks = decks;
	}
	
	public ArrayList<IPartie> getHistorique() {
		return historique;
	}
	
	public void setHistorique(ArrayList<IPartie> historique) {
		this.historique = historique;
	}
	
	public Boolean getIsConnected() {
		return isConnected;
	}
	
	public void setIsConnected(Boolean isConnected) {
		this.isConnected = isConnected;
	}
	
	public IListeDeCartes getCollection() {
		return collection;
	}
	
	public void setCollection(IListeDeCartes collection) {
		this.collection = collection;
	}

}