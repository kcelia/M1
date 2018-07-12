/**
 * 
 */
package Carte;

/** 
 * <!-- begin-UML-doc -->
 * <!-- end-UML-doc -->
 * @author 3407485
 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
 */
public class Carte {
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private String nomCarte;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private Integer valeurAttaque;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private Integer valeurDefense;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private String description_effets;
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private RareteCarte rareteCarte;
	
	public Carte(String nomCarte, Integer valeurAttaque, Integer valeurDefense, String description_effets, RareteCarte rareteCarte){
		this.nomCarte = nomCarte;
		this.valeurAttaque = valeurAttaque;
		this.valeurDefense = valeurDefense;
		this.description_effets = description_effets;
		this.rareteCarte = rareteCarte;
	}
	
	public String getNomCarte() {
		return nomCarte;
	}
	
	public Integer getValeurAttaque() {
		return valeurAttaque;
	}
	
	public Integer getValeurDefense() {
		return valeurDefense;
	}
	
	public String getDescription_effets() {
		return description_effets;
	}
	
	public RareteCarte getRareteCarte() {
		return rareteCarte;
	}
}