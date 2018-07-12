/**
 * 
 */
package Carte;

import Interface.ICarte;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/** 
 * <!-- begin-UML-doc -->
 * <!-- end-UML-doc -->
 * @author 3407485
 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
 */
public class GestCarte implements ICarte {
	/** 
	 * <!-- begin-UML-doc -->
	 * <!-- end-UML-doc -->
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	private HashMap<String, Carte> cartes;
	
	public GestCarte() {
		cartes = new HashMap<String, Carte>();
	}
	
	public GestCarte(ArrayList<String> noms, ArrayList<Integer> valeursAttaque, ArrayList<Integer> valeursDefense, 
			ArrayList<String> descriptions, ArrayList<RareteCarte> raretesCarte) {
		cartes = new HashMap<String, Carte>();
		for (int i=0;i<noms.size(); i++) {
			cartes.put(noms.get(i), new Carte(noms.get(i), valeursAttaque.get(i), valeursDefense.get(i), descriptions.get(i), raretesCarte.get(i)));
		}
	}
	
	/** 
	 * (non-Javadoc)
	 * @see ICarte#infosCarte(String nomCarte)
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public ArrayList<Carte> infosCarte(ArrayList<String> nomCartes) {
		ArrayList<Carte> res = new ArrayList<>();
		for (String nomCarte: nomCartes){
			res.add(cartes.get(nomCarte));
		}
		return res;
	}

	public Carte infosCarte(String nomCarte) {
		return cartes.get(nomCarte);
	}
	/** 
	 * (non-Javadoc)
	 * @see ICarte#listerCartes()
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public ArrayList<String> listerCartes() {
		return new ArrayList<String>(cartes.keySet());
	}

	/** 
	 * (non-Javadoc)
	 * @see ICarte#rareteCarte(String nomCarte)
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public ArrayList<RareteCarte> rareteCarte(ArrayList<String> nomCartes) {
		ArrayList<RareteCarte> res = new ArrayList<>();
		for (String nomCarte: nomCartes){
			res.add(cartes.get(nomCarte).getRareteCarte());
		}
		return res;
	}
	@Override
	public RareteCarte rareteCarte(String nomCarte) {
		return cartes.get(nomCarte).getRareteCarte();
	}
	/** 
	 * (non-Javadoc)
	 * @see ICarte#getPrixVente(String nomCarte)
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public ArrayList<Integer> getPrixVente(ArrayList<String> nomCartes) {
		ArrayList<Integer> res = new ArrayList<>();
		for (String nomCarte: nomCartes){
			RareteCarte rarete = cartes.get(nomCarte).getRareteCarte();
			if (rarete == RareteCarte.commune) res.add(2);
			else if (rarete == RareteCarte.rare) res.add(5);
			else if (rarete == RareteCarte.légendaire) res.add(20);
		}
		return res;
	}

	public Integer getPrixVente(String nomCarte) {
		RareteCarte rarete = cartes.get(nomCarte).getRareteCarte();
		if (rarete == RareteCarte.commune) return 2;
		else if (rarete == RareteCarte.rare) return 5;
		else if (rarete == RareteCarte.légendaire) return 20;
		else if (rarete == RareteCarte.basique) return 0;
		else return 0; // non atteint
	}

	/** 
	 * (non-Javadoc)
	 * @see ICarte#getPrixAchat(String nomCarte)
	 * @generated "UML vers Java (com.ibm.xtools.transform.uml2.java5.internal.UML2JavaTransform)"
	 */
	public ArrayList<Integer> getPrixAchat(ArrayList<String> nomCartes) {
		ArrayList<Integer> res = new ArrayList<>();
		for (String nomCarte: nomCartes){
			RareteCarte rarete = cartes.get(nomCarte).getRareteCarte();
			if (rarete == RareteCarte.commune) res.add(20);
			else if (rarete == RareteCarte.rare) res.add(50);
			else if (rarete == RareteCarte.légendaire) res.add(200);
		}
		return res;
	}	
	public Integer getPrixAchat(String nomCarte) {
		RareteCarte rarete = cartes.get(nomCarte).getRareteCarte();
		if (rarete == RareteCarte.commune) return 20;
		if (rarete == RareteCarte.rare) return 50;
		if (rarete == RareteCarte.légendaire) return 200;
		return null;
	}
	
	public ArrayList<String> générerPack(){
		//non implémenté
		return null;
	}

}