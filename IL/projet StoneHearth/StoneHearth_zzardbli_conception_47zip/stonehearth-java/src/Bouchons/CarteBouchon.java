package Bouchons;

import java.util.ArrayList;
import java.util.Arrays;

import Carte.Carte;
import Carte.GestCarte;
import Carte.RareteCarte;
import Interface.ICarte;

// le prof propose un truc tout simple 
/* 
 *public class CarteBOuchon implements ICarte  '
 * public CarteBouchon(){ }
 * 
 *
 */

public class CarteBouchon implements ICarte {


	private GestCarte gest;
	
	public CarteBouchon(){
		gest = new GestCarte(new ArrayList<String>(Arrays.asList("Voleuse solitaire", "Chat", "Robert le chevalier", "Requin avec un laser sur la tête", "Chien", "Homme des tavernes")), 
				new ArrayList<Integer>(Arrays.asList(30, 15, 40, 50, 20, 20)), 
				new ArrayList<Integer>(Arrays.asList(20, 15, 40, 5, 10, 20)), 
				new ArrayList<String>(Arrays.asList("Une voleuse vagabonde voyageant de ville en ville, volant pour survivre. Méfiez-vous de sa dague tranchante.",
						"Un chat très mignon.",
						"Un grand chevalier.",
						"Espèce en voie de disparition.",
						"Wouf wouf!",
						"N'a pas encore vu l'addition.")),
				new ArrayList<RareteCarte>(Arrays.asList(RareteCarte.commune, RareteCarte.commune, RareteCarte.légendaire, RareteCarte.rare, RareteCarte.commune, RareteCarte.basique)));
	}

	public ArrayList<Carte> infosCarte(ArrayList<String> nomCartes) {
		return gest.infosCarte(nomCartes);
	}
	
	public Carte infosCarte(String nomCarte) {
		return gest.infosCarte(nomCarte);
	}

	@Override
	public ArrayList<String> listerCartes() {
		return gest.listerCartes();
	}

	@Override
	public ArrayList<RareteCarte> rareteCarte(ArrayList<String> nomCartes) {
		return gest.rareteCarte(nomCartes);
	}

	public RareteCarte rareteCarte(String nomCarte) {
		return gest.rareteCarte(nomCarte);
	}
	@Override
	public ArrayList<Integer> getPrixVente(ArrayList<String> nomCartes) {
		return gest.getPrixVente(nomCartes);
	}

	@Override
	public Integer getPrixAchat(String nomCarte) {
		return gest.getPrixAchat(nomCarte);
	}

	@Override
	public Integer getPrixVente(String nomCarte) {
		return gest.getPrixVente(nomCarte);
	}

	@Override
	public ArrayList<Integer> getPrixAchat(ArrayList<String> nomCartes) {
		return gest.getPrixVente(nomCartes);
	}
	
	public ArrayList<String> générerPack(){
		return new ArrayList<String>(gest.listerCartes().subList(0, 5));
		
	}
}
