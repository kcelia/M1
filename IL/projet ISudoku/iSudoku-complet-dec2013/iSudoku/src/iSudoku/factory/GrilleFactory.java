package iSudoku.factory;

import externe.recoImage.RecoFactory;
import iSudoku.contraintes.GrilleContrainteCache;
import iSudoku.grille.Grille;
import iSudoku.itf.IGrille;
import iSudoku.itf.IGrilleContrainte;
import iSudoku.itf.IGrilleLoader;
import iSudoku.load.file.FileLoader;
import iSudoku.load.image.ImageLoader;

public class GrilleFactory {

	/**
	 * A factory operation to create empty Igrille objects.
	 * 
	 * @return A newly created empty IGrille, all cells empty, no initial values
	 *         set to fixed.
	 */
	public static IGrille createNewEmptyGrille() {
		return new Grille();
	}


	/**
	 * Décore une grille avec un solver de contraintes.
	 * 
	 * @param une
	 *            grille
	 * @return une grille avec des contraintes
	 */
	public static IGrilleContrainte getContraintes(IGrille grille) {
		return new GrilleContrainteCache(grille);
	}

	public static IGrilleLoader createFileLoader() {
		return new FileLoader();
	}


	public static IGrilleLoader createImageLoader() {
		return new ImageLoader(RecoFactory.createRecoImage());
	}
}
