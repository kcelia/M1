package iSudoku.contraintes;

import iSudoku.itf.IGrille;

public abstract class GrilleDecorator implements IGrille {
	private IGrille grille;

	public GrilleDecorator(IGrille grille) {
		this.grille = grille;
	}

	@Override
	public void setCellValue(int line, int col, int value) {
		grille.setCellValue(line, col, value);
	}

	@Override
	public int getCellValue(int line, int col) {
		return grille.getCellValue(line, col);
	}

	@Override
	public boolean isFixed(int line, int col) {
		return grille.isFixed(line, col);
	}

	@Override
	public void setFixed(int line, int col, boolean isFixed) {
		grille.setFixed(line, col, isFixed);
	}

}
