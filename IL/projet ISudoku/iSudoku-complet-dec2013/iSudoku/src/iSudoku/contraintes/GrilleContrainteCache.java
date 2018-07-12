package iSudoku.contraintes;

import iSudoku.itf.IGrille;

import java.util.Set;

public class GrilleContrainteCache extends GrilleContrainte {
	private Set<Integer>[] sugg;

	public GrilleContrainteCache(IGrille grille) {
		super(grille);
		clearSuggs();
	}

	@SuppressWarnings("unchecked")
	private void clearSuggs() {
		sugg = new Set[81];
	}

	@Override
	public void setCellValue(int line, int col, int value) {
		clearSuggs();
		super.setCellValue(line, col, value);
	}

	@Override
	public Set<Integer> getSuggestions(int lig, int col) {
		if (sugg[lig * 9 + col] == null) {
			sugg[lig * 9 + col] = super.getSuggestions(lig, col);
		}
		return sugg[lig * 9 + col];
	}

}
